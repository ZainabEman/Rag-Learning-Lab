# Cross-Encoder Reranking

> Status: `studied` (self-study, outside the course) | Section: [Advanced Retrieval](../README.md)

## What is it?

Reranking with a model that reads the **query and document together** in one
forward pass and outputs a single relevance score.

## Why it matters

It is substantially more accurate than vector similarity, because the model can
attend across both texts at once instead of comparing two summaries produced in
isolation.

## How it works

| | **Bi-encoder** (normal retrieval) | **Cross-encoder** (reranking) |
| --- | --- | --- |
| Input | Query and doc encoded separately | Query + doc encoded **together** |
| Output | Two vectors, compared by cosine | One relevance score |
| Precompute | Documents embedded in advance | Nothing — must run per pair |
| Cost | O(1) per query after indexing | **One model call per candidate** |
| Accuracy | Good | Better |

That cost line is why cross-encoders cannot search a corpus: scoring 1M
documents means 1M forward passes. They only ever rerank a shortlist.

## Simple example

```python
from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
pairs = [(query, doc.page_content) for doc in candidates]
scores = model.predict(pairs)
top = [d for _, d in sorted(zip(scores, candidates), reverse=True)][:5]
```

## Remember

- Cross-encoders **rerank, never retrieve**. Always pair with a fast first stage.
- Typical shape: retrieve 50 → rerank → keep 5.
- Latency is the real constraint; batch the pairs.
- Hosted rerank APIs (e.g. Cohere Rerank) do the same job without self-hosting.
- ColBERT sits in between — token-level vectors, precomputable, cheaper than a
  full cross-encoder.

## Related

- [06-retrieval/04-reranking-basics](../../06-retrieval/04-reranking-basics/) · [11-colbert](../11-colbert/)
