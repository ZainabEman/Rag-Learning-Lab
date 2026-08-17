"""
Reciprocal Rank Fusion - merging ranked lists without comparing scores
Section: Advanced Retrieval

The whole algorithm is one formula:

    RRF(d) = sum over lists  of  1 / (k + rank_of_d_in_that_list)

Stdlib only. Run:
    python implementation.py
"""

from __future__ import annotations

K = 60          # standard constant from the original paper


def rrf(rankings: list[list[str]], k: int = K) -> list[tuple[str, float]]:
    """
    Fuse several ranked lists into one.

    Each list votes for a document with weight 1/(k + rank). Rank 1 contributes
    most; the weight decays quickly. Documents appearing in several lists
    accumulate votes.

    Note what is NOT used: the original relevance scores. Only positions.
    """
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, doc in enumerate(ranking, start=1):
            scores[doc] = scores.get(doc, 0.0) + 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)


def main() -> None:
    # Two retrievers, two very different score scales - which is exactly why
    # adding the scores together would be meaningless.
    bm25 = ["doc_2fa_setup", "doc_password_reset", "doc_login_errors"]
    dense = ["doc_account_recovery", "doc_2fa_setup", "doc_security_faq"]

    print("query: 'reset 2FA on my account'\n")
    print(f"  BM25 (sparse) : {bm25}")
    print(f"  Dense (vector): {dense}\n")

    print("fused:")
    for rank, (doc, score) in enumerate(rrf([bm25, dense]), start=1):
        both = " <- appears in BOTH lists" if doc in bm25 and doc in dense else ""
        print(f"  {rank}. {doc:<24} {score:.5f}{both}")

    print("""
  doc_2fa_setup wins despite being 1st in neither list, because it is the only
  document both retrievers agree on. RRF rewards consensus.

  Why not just add the scores? BM25 might return 14.2 and cosine 0.83. Those
  are not the same kind of number, and their ranges shift per query. Ranks are
  always comparable - that is the entire point of the algorithm.
""")

    # The k constant damps the advantage of the top positions.
    print("effect of k (score gap between rank 1 and rank 3 in one list):")
    for k in (1, 10, 60, 200):
        gap = (1 / (k + 1)) - (1 / (k + 3))
        print(f"  k={k:>3}: {gap:.5f}   {'top-heavy' if k < 30 else 'flatter, more consensus-driven'}")


if __name__ == "__main__":
    main()
