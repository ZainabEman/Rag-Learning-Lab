"""
Vector Databases - a minimal vector store, built from scratch
Section: Vector Search

Goal
----
Show that a vector store is not magic. Its four features - storage, similarity
search, indexing and CRUD - fit in about 80 lines of plain Python.

Once this is clear, the LangChain/Chroma API stops looking like a new thing to
learn and starts looking like the same operations with a nicer interface.

The "embedding" here is a bag-of-words vector so the file runs with zero
installs. A real store uses a neural embedding model - see ../../04-embeddings/.

Run:
    python implementation.py
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PLAYERS = [
    ("Virat Kohli is one of the most successful and consistent batsmen in IPL history.",
     {"team": "Royal Challengers Bangalore"}),
    ("Rohit Sharma is the most successful captain in IPL history.",
     {"team": "Mumbai Indians"}),
    ("MS Dhoni is a wicket-keeper batsman known for his calm captaincy.",
     {"team": "Chennai Super Kings"}),
    ("Jasprit Bumrah is a fast bowler famous for his yorkers in death overs.",
     {"team": "Mumbai Indians"}),
    ("Ravindra Jadeja is an all-rounder who bats, bowls spin and fields brilliantly.",
     {"team": "Chennai Super Kings"}),
]


# ===========================================================================
# The store
# ===========================================================================

@dataclass
class Record:
    """One stored item: id, text, its vector, and its metadata."""

    id: str
    text: str
    metadata: dict
    vector: Counter = field(default_factory=Counter)


def embed(text: str) -> Counter:
    """Stand-in for an embedding model. Real stores call a neural model here."""
    return Counter(re.findall(r"[a-z]+", text.lower()))


def cosine(a: Counter, b: Counter) -> float:
    shared = set(a) & set(b)
    dot = sum(a[t] * b[t] for t in shared)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


class MiniVectorStore:
    """The four core features of any vector store."""

    def __init__(self) -> None:
        self._records: dict[str, Record] = {}
        self._next = 0

    # -- feature 1: storage (+ CRUD, feature 4) -----------------------------
    def add_documents(self, docs: list[tuple[str, dict]]) -> list[str]:
        """Store text + metadata, embedding it on the way in. Returns new ids."""
        ids = []
        for text, metadata in docs:
            doc_id = f"doc-{self._next}"
            self._next += 1
            self._records[doc_id] = Record(doc_id, text, metadata, embed(text))
            ids.append(doc_id)
        return ids

    def get(self) -> list[Record]:
        return list(self._records.values())

    def update_document(self, doc_id: str, text: str, metadata: dict) -> None:
        # Note the re-embed: changing the text MUST change the vector.
        self._records[doc_id] = Record(doc_id, text, metadata, embed(text))

    def delete(self, ids: list[str]) -> None:
        for doc_id in ids:
            self._records.pop(doc_id, None)

    # -- feature 2: similarity search --------------------------------------
    def similarity_search_with_score(
        self, query: str, k: int = 2, filter: dict | None = None
    ) -> list[tuple[Record, float]]:
        """
        Embed the query, score against every record, return the best k.

        `filter` restricts the search by metadata BEFORE scoring - the exact
        constraints that embeddings are the wrong tool for.
        """
        candidates = [
            r for r in self._records.values()
            if not filter or all(r.metadata.get(key) == val for key, val in filter.items())
        ]

        if not query:                      # filter-only search
            return [(r, 0.0) for r in candidates][:k]

        qv = embed(query)
        scored = [(r, cosine(qv, r.vector)) for r in candidates]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return scored[:k]


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------

def main() -> None:
    store = MiniVectorStore()

    print("=" * 70)
    print("STORAGE + CRUD")
    print("=" * 70)
    ids = store.add_documents(PLAYERS)
    print(f"added {len(ids)} documents, auto-generated ids: {ids}")

    print("\n" + "=" * 70)
    print("SIMILARITY SEARCH")
    print("=" * 70)
    query = "Among these, who is a bowler?"
    print(f"query: {query!r}\n")
    for k in (1, 2):
        print(f"  k={k}:")
        for record, score in store.similarity_search_with_score(query, k=k):
            print(f"    {score:.3f}  {record.text[:58]}...")

    print("\n  Note: with a real embedding model, 'all-rounder' would score high")
    print("  for a bowling query because it MEANS batting + bowling. Bag-of-words")
    print("  only catches it if the word overlaps - the limit of this stand-in.")

    print("\n" + "=" * 70)
    print("METADATA FILTERING")
    print("=" * 70)
    print("  filter={'team': 'Chennai Super Kings'}, empty query\n")
    for record, _ in store.similarity_search_with_score("", k=5,
                                                        filter={"team": "Chennai Super Kings"}):
        print(f"    {record.text[:58]}...")

    print("\n" + "=" * 70)
    print("UPDATE + DELETE")
    print("=" * 70)
    kohli_id = ids[0]
    store.update_document(
        kohli_id,
        "Virat Kohli, former captain of RCB, is known for aggressive leadership.",
        {"team": "Royal Challengers Bangalore"},
    )
    print(f"  updated {kohli_id}: {store.get()[0].text[:58]}...")

    store.delete([kohli_id])
    print(f"  deleted {kohli_id} -> {len(store.get())} documents remain")

    print("\n" + "=" * 70)
    print("THE SAME THING IN LANGCHAIN")
    print("=" * 70)
    print("""
    from langchain_chroma import Chroma
    from langchain_openai import OpenAIEmbeddings

    store = Chroma(embedding_function=OpenAIEmbeddings(),
                   persist_directory="my_chroma_db",
                   collection_name="sample")

    store.add_documents(docs)
    store.similarity_search(query="who is a bowler?", k=2)
    store.similarity_search_with_score(query="...", k=2)
    store.get(include=["embeddings", "documents", "metadatas"])
    store.update_document(document_id=doc_id, document=new_doc)
    store.delete(ids=[doc_id])

    Same operations. What Chroma adds: a real embedding model, persistence to
    disk (SQLite), collections, and an index so search does not stay O(n).
""")


if __name__ == "__main__":
    main()
