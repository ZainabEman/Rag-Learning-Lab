# Sparse vs Dense Retrieval

> Status: `studied` (self-study, outside the course) | Section: [Advanced Retrieval](../README.md)

## What is it?

The two families of retrieval:

| | **Sparse** | **Dense** |
| --- | --- | --- |
| Vector | One dimension per vocabulary word, mostly zeros | Few hundred/thousand dims, all non-zero |
| Built by | Counting (TF-IDF, BM25) | A neural embedding model |
| Matches on | Exact terms | Meaning |

## Why it matters

They fail in *opposite* ways. Knowing which failure you are looking at tells you
which fix to apply — and explains why combining them works so well.

## How it works

- **Sparse**: an inverted index maps each term to the documents containing it.
  Scoring is term overlap, weighted by rarity and length.
- **Dense**: both query and documents become vectors; retrieval is
  nearest-neighbour search in that space.

## Simple example

```
query: "how to fix error 502"
  sparse  ✅ finds the doc containing literally "502"
  dense   ❌ may drift to general "server problems" content

query: "my subscription auto-renewed and I want my money back"
  sparse  ❌ no keyword overlap with "refund policy"
  dense   ✅ matches on meaning
```

## Remember

- **Sparse wins** on rare terms, IDs, codes, names, exact phrases.
- **Dense wins** on paraphrase, synonyms, intent, natural questions.
- Dense retrieval needs a model and an index build; sparse needs neither.
- Dense quality is bounded by the embedding model's domain knowledge — a
  general model on medical or legal text underperforms badly.
- The practical answer is usually not to choose: see
  [04-hybrid-search](../04-hybrid-search/).

## Related

- [02-bm25](../02-bm25/) · [04-hybrid-search](../04-hybrid-search/)
