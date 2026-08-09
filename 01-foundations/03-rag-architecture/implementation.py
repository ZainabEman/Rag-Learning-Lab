"""
RAG Architecture - the four stages, implemented from scratch
Section: Foundations

Goal
----
Make the four stages of a RAG pipeline visible by building all of them with
nothing but the standard library: indexing, retrieval, augmentation, generation.

Why from scratch first
----------------------
Every framework collapses this pipeline into about five lines. That is
convenient once you know what is underneath, and useless before. This file has
no framework in it, so every step is inspectable.

Honest limitation, stated up front
----------------------------------
The "embedding model" here is a bag-of-words vector, NOT a real embedding.
It matches on shared words, so it captures lexical overlap and not meaning.
A real embedding model would match "optimisation step" to a passage that says
"we minimise the loss by stepping downhill" - this will not. That gap is
exactly what section 04-embeddings is about, and running this file is the
cheapest way to feel why dense embeddings were needed.

Stage 4 (generation) assembles the real prompt and stops there. Calling an LLM
is one API call away, but faking it would teach nothing.

Run:
    python implementation.py
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Configuration - the only block experiments should need to change
# ---------------------------------------------------------------------------

CHUNK_SIZE_WORDS = 40      # how many words per chunk
CHUNK_OVERLAP_WORDS = 10   # how many words repeat between neighbouring chunks
TOP_K = 2                  # how many chunks become the context

QUERY = "how do we perform the optimization step in gradient descent?"

# A stand-in for a source document: segments of a lecture transcript.
# Small enough to reason about by hand, which is the point.
SOURCE_DOCUMENT = """
Ordinary least squares gives a closed form solution for linear regression.
You compute the coefficients directly by solving the normal equation, which
means no iteration is required at all. This is exact but it needs a matrix
inversion, so it becomes impractical when the number of features is large.

Multiple linear regression extends simple linear regression to several input
features. Each feature receives its own coefficient, and the prediction is the
weighted sum of the features plus an intercept term. The interpretation of each
coefficient changes because it is now conditional on the other features.

Gradient descent is an iterative optimisation algorithm. We start from random
coefficients and repeatedly move them in the direction that reduces the loss.
The optimisation step itself is simple: compute the gradient of the loss with
respect to each coefficient, multiply it by the learning rate, and subtract the
result from the current coefficient value.

Choosing the learning rate for gradient descent is the practical difficulty.
If the learning rate is too large the optimisation step overshoots the minimum
and the loss oscillates or diverges. If it is too small the algorithm converges
correctly but takes far too many iterations to be useful.
"""

PROMPT_TEMPLATE = """You are a helpful assistant.
Answer the question ONLY from the provided context.
If the context is insufficient, just say you don't know.

Context:
{context}

Question:
{question}
"""


# ===========================================================================
# STAGE 1 - INDEXING (offline: runs once per document, not per query)
# ===========================================================================

@dataclass
class Chunk:
    """One retrievable unit: the text, its vector, and where it came from."""

    text: str
    metadata: dict
    vector: Counter = field(default_factory=Counter)


def tokenize(text: str) -> list[str]:
    """Lowercase and split into word tokens. Shared by chunks and queries."""
    return re.findall(r"[a-z]+", text.lower())


def chunk_text(text: str, size: int, overlap: int) -> list[str]:
    """
    Indexing step 2 - split a long document into smaller units.

    Fixed-size word windows with overlap. This is the crude baseline: it splits
    on word counts, not on meaning, so it will happily cut an explanation in
    half. Overlap exists to soften exactly that.
    """
    words = text.split()
    step = size - overlap
    if step <= 0:
        raise ValueError("overlap must be smaller than chunk size")

    chunks = []
    for start in range(0, len(words), step):
        window = words[start:start + size]
        if not window:
            break
        chunks.append(" ".join(window))
        if start + size >= len(words):
            break        # the window already reached the end
    return chunks


def embed(text: str) -> Counter:
    """
    Indexing step 3 - turn text into a vector.

    A real embedding model outputs a fixed-length dense vector from a neural
    network. This returns a sparse term-frequency vector instead. The pipeline
    around it is identical either way, which is the point of the exercise:
    swapping this one function for a sentence-transformer changes nothing else.
    """
    return Counter(tokenize(text))


def build_index(document: str) -> list[Chunk]:
    """Indexing steps 1-4: ingest, chunk, embed, store."""
    # Step 1 - ingestion. Normally a document loader reads from a file, an
    # S3 bucket or a URL. Here the text is already in memory.
    raw = document.strip()

    # Step 2 - chunking.
    pieces = chunk_text(raw, CHUNK_SIZE_WORDS, CHUNK_OVERLAP_WORDS)

    # Steps 3 and 4 - embed each chunk and store vector + text + metadata
    # together. Storing the text is not optional: an embedding cannot be
    # reversed, and it is the text that eventually goes into the prompt.
    return [
        Chunk(
            text=piece,
            metadata={"source": "linear_regression_lecture", "chunk_id": i},
            vector=embed(piece),
        )
        for i, piece in enumerate(pieces)
    ]


# ===========================================================================
# STAGE 2 - RETRIEVAL (online: runs on every query)
# ===========================================================================

def cosine_similarity(a: Counter, b: Counter) -> float:
    """
    cos(u, v) = (u . v) / (||u|| * ||v||)

    Written out rather than imported so the ranking step is not a black box.
    Only shared keys contribute to the dot product; the norms use all keys.
    """
    shared = set(a) & set(b)
    dot = sum(a[token] * b[token] for token in shared)

    norm_a = math.sqrt(sum(count ** 2 for count in a.values()))
    norm_b = math.sqrt(sum(count ** 2 for count in b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def retrieve(query: str, index: list[Chunk], k: int) -> list[tuple[float, Chunk]]:
    """
    The four things a retriever does.

    Returns (score, chunk) pairs, best first.
    """
    # 1. Embed the query with the SAME function used for the chunks.
    #    Different model on either side = incomparable vectors = noise.
    query_vector = embed(query)

    # 2. Search: score the query against every stored vector.
    #    This is brute force. Approximate indexes (HNSW, IVF) exist because
    #    this does not scale - see section 07.
    scored = [(cosine_similarity(query_vector, chunk.vector), chunk)
              for chunk in index]

    # 3. Rank.
    scored.sort(key=lambda pair: pair[0], reverse=True)

    # 4. Take the top k. Note that this ALWAYS returns k results, however bad
    #    the best match is - similarity search has no concept of "no answer".
    return scored[:k]


# ===========================================================================
# STAGE 3 - AUGMENTATION
# ===========================================================================

def augment(query: str, retrieved: list[tuple[float, Chunk]]) -> str:
    """Combine the query and the retrieved context into the final prompt."""
    context = "\n\n".join(
        f"[chunk {chunk.metadata['chunk_id']}] {chunk.text}"
        for _score, chunk in retrieved
    )
    return PROMPT_TEMPLATE.format(context=context, question=query)


# ===========================================================================
# STAGE 4 - GENERATION
# ===========================================================================

def generate(prompt: str) -> str:
    """
    Where the LLM call goes.

    Deliberately not implemented: an LLM call here would add an API key, a
    dependency and a bill, and would demonstrate nothing that the printed
    prompt does not already show. Everything that makes RAG work has already
    happened by this point.

    TODO: wire this to a real model once the LangChain model component is
    revisited, then compare the answer with and without the context block.
    """
    raise NotImplementedError(
        "Generation is left unimplemented on purpose - inspect the prompt above."
    )


# ---------------------------------------------------------------------------
# Example usage + output inspection
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 72)
    print("STAGE 1 - INDEXING")
    print("=" * 72)
    index = build_index(SOURCE_DOCUMENT)
    print(f"chunk size={CHUNK_SIZE_WORDS} words, overlap={CHUNK_OVERLAP_WORDS}")
    print(f"produced {len(index)} chunks\n")
    for chunk in index:
        preview = chunk.text[:64].replace("\n", " ")
        print(f"  chunk {chunk.metadata['chunk_id']}: {preview}...")

    print()
    print("=" * 72)
    print("STAGE 2 - RETRIEVAL")
    print("=" * 72)
    print(f"query: {QUERY}\n")

    # Score EVERY chunk, not just the winners. Seeing the losing scores is
    # what makes retrieval quality legible.
    query_vector = embed(QUERY)
    print("  similarity of the query against every chunk:")
    for chunk in index:
        score = cosine_similarity(query_vector, chunk.vector)
        bar = "#" * int(score * 60)
        print(f"    chunk {chunk.metadata['chunk_id']}: {score:.4f} {bar}")

    retrieved = retrieve(QUERY, index, TOP_K)
    print(f"\n  top-{TOP_K} selected: "
          f"{[c.metadata['chunk_id'] for _s, c in retrieved]}")

    print()
    print("=" * 72)
    print("STAGE 3 - AUGMENTATION")
    print("=" * 72)
    prompt = augment(QUERY, retrieved)
    print(prompt)

    print("=" * 72)
    print("STAGE 4 - GENERATION")
    print("=" * 72)
    print("The prompt above is what an LLM would receive.")
    print("Compare it with the query alone - that difference IS retrieval-augmented")
    print("generation. Everything else is engineering around those extra lines.")

    # Two things worth noticing in the output above:
    #
    # 1. Chunk 3 starts mid-sentence ("conditional on the other features")
    #    because fixed-size chunking cuts on word counts, not meaning. The
    #    retrieved context therefore carries a fragment of an unrelated
    #    paragraph. That is the failure mode section 03-chunking exists to fix.
    #
    # 2. The query says "optimization" and the document says "optimisation".
    #    Those are different tokens, so they contributed NOTHING to the score -
    #    retrieval only succeeded because "gradient", "descent" and "step"
    #    happened to be shared. A dense embedding model would treat the two
    #    spellings as near-identical. This is the concrete argument for
    #    section 04-embeddings.
    #
    # TODO for the experiment file:
    #   - vary CHUNK_SIZE_WORDS and watch which chunks win
    #   - vary TOP_K and watch the prompt grow
    #   - ask a paraphrased query that shares no words with the answer chunk,
    #     and watch bag-of-words retrieval fail where a real embedding would not


if __name__ == "__main__":
    main()
