# Reciprocal Rank Fusion (RRF)

> Status: `studied` (self-study, outside the course) | Section: [Advanced Retrieval](../README.md)

## What is it?

An algorithm for merging several ranked lists into one, using **only the
positions** of the documents — never their scores.

```
RRF(d) = Σ  1 / (k + rank_i(d))          k is usually 60
        lists i containing d
```

## Why it matters

It solves the central problem of hybrid search: BM25 scores and cosine
similarities live on incomparable scales, so adding or averaging them is
meaningless. Ranks are always comparable.

## How it works

Each list votes for a document with weight `1/(k + rank)`. Rank 1 contributes
the most, and the contribution decays quickly. Documents appearing in several
lists accumulate votes and rise to the top.

The constant `k` (default 60) dampens the influence of the very top positions,
so one list cannot dominate outright.

## Simple example

```python
def rrf(rankings, k=60):
    scores = {}
    for ranking in rankings:                      # each is a list of doc ids
        for rank, doc in enumerate(ranking, start=1):
            scores[doc] = scores.get(doc, 0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)

bm25  = ["A", "B", "C"]
dense = ["D", "A", "E"]
rrf([bm25, dense])        # -> A first: it is the only doc in BOTH lists
```

## Remember

- **No score normalisation needed** — that is the whole point.
- Works for any number of lists: hybrid search, multi-query, multiple retrievers.
- `k=60` is the standard default from the original paper; rarely worth tuning.
- It rewards **consensus**. A document ranked mid-table by everyone can beat one
  ranked first by a single list.
- It cannot rescue a document that no list retrieved.

## Related

- [04-hybrid-search](../04-hybrid-search/) · [08-query-transformation/05-rag-fusion](../../08-query-transformation/05-rag-fusion/)
