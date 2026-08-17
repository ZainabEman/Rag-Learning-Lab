"""
BM25 - lexical ranking from the formula
Section: Advanced Retrieval

    score(q, d) = sum over terms t in q of
                    IDF(t) * ( tf * (k1 + 1) ) / ( tf + k1 * (1 - b + b * |d|/avgdl) )

Three ideas in one formula: term frequency with saturation, inverse document
frequency, and length normalisation.

Stdlib only. Run:
    python implementation.py
"""

from __future__ import annotations

import math
import re
from collections import Counter

K1 = 1.5      # TF saturation: higher = repeated terms keep counting
B = 0.75      # length normalisation: 0 = ignore length, 1 = full normalisation

CORPUS = [
    "the cat sat on the mat",
    "error code 502 means bad gateway from the upstream server",
    "dogs are loyal animals and make good pets",
    "a 502 error usually indicates the server is unreachable",
    "the mat was bought for the cat last week",
]


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


class BM25:
    def __init__(self, corpus: list[str], k1: float = K1, b: float = B):
        self.k1, self.b = k1, b
        self.docs = [tokenize(d) for d in corpus]
        self.raw = corpus
        self.avgdl = sum(len(d) for d in self.docs) / len(self.docs)
        self.tf = [Counter(d) for d in self.docs]

        # document frequency: in how many documents does each term appear?
        self.df: Counter = Counter()
        for doc in self.docs:
            for term in set(doc):
                self.df[term] += 1

    def idf(self, term: str) -> float:
        """Rare terms are worth more. Common terms ('the') approach zero."""
        n = len(self.docs)
        return math.log(1 + (n - self.df[term] + 0.5) / (self.df[term] + 0.5))

    def score(self, query: str, i: int) -> float:
        total = 0.0
        dl = len(self.docs[i])
        for term in tokenize(query):
            if term not in self.tf[i]:
                continue
            tf = self.tf[i][term]
            num = tf * (self.k1 + 1)
            den = tf + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
            total += self.idf(term) * num / den
        return total

    def search(self, query: str, k: int = 3):
        scored = [(self.score(query, i), self.raw[i]) for i in range(len(self.docs))]
        scored.sort(reverse=True, key=lambda p: p[0])
        return scored[:k]


def main() -> None:
    bm25 = BM25(CORPUS)

    query = "502 error"
    print(f"query: {query!r}\n")
    for score, doc in bm25.search(query):
        print(f"  {score:.3f}  {doc}")

    print("\n  Both '502' documents rank top. A dense retriever often fumbles")
    print("  bare identifiers like '502' - this is exactly BM25's strength.\n")

    # IDF: why "the" contributes nothing
    print("IDF by term (higher = rarer = more informative):")
    for term in ("the", "server", "502", "dogs"):
        print(f"  {term:<8} df={bm25.df[term]}  idf={bm25.idf(term):.3f}")

    # TF saturation: the point that separates BM25 from naive TF-IDF
    print("\nTF saturation - what one term contributes as it repeats:")
    dl, avgdl = 10, bm25.avgdl
    for tf in (1, 2, 5, 10, 50):
        num = tf * (K1 + 1)
        den = tf + K1 * (1 - B + B * dl / avgdl)
        print(f"  tf={tf:>2}: {num / den:.3f}")
    print("  -> 50 occurrences are worth barely more than 10. Keyword stuffing")
    print("     does not work, which is precisely why BM25 replaced raw TF-IDF.")


if __name__ == "__main__":
    main()
