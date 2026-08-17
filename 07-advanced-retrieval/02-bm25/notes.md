# BM25

> Status: `studied` (self-study, outside the course) | Section: [Advanced Retrieval](../README.md)

## What is it?

The standard **lexical** (keyword) ranking function. Scores a document by how
often the query's terms appear in it, adjusted for term rarity and document
length.

## Why it matters

Dense embeddings are bad at exact matches — product codes, error numbers, names,
rare technical terms. BM25 is excellent at exactly those, which is why it is
still used in 2026 and why hybrid search exists.

## How it works

For each query term, BM25 combines three signals:

| Signal | Effect |
| --- | --- |
| **Term frequency (TF)** | More occurrences → higher score, but with *saturation* — the 10th occurrence adds far less than the 2nd |
| **Inverse document frequency (IDF)** | Rare terms across the corpus count for more |
| **Length normalisation** | Long documents don't win just by being long |

Two knobs: `k1` controls TF saturation (typ. 1.2–2.0), `b` controls length
normalisation (typ. 0.75).

## Simple example

```python
from rank_bm25 import BM25Okapi

corpus = [
    "the cat sat on the mat".split(),
    "error code 502 means bad gateway".split(),
    "dogs are loyal animals".split(),
]
bm25 = BM25Okapi(corpus)
bm25.get_scores("error code 502".split())   # doc 2 scores far above the rest
```

A dense retriever often struggles with "502" — BM25 nails it.

## Remember

- **TF saturation is the key idea** over naive TF-IDF: repeating a word 50 times
  does not make a document 50× more relevant.
- BM25 cannot match paraphrases. "car" never matches "automobile".
- It needs no training, no embeddings and no GPU — it is fast and cheap.
- Still a strong baseline; many "advanced" systems fail to beat BM25 alone.

## Related

- [01-tf-idf](../01-tf-idf/) · [03-sparse-vs-dense](../03-sparse-vs-dense/) · [04-hybrid-search](../04-hybrid-search/)
