# Semantic Similarity

> Status: `studied` (self-study, outside the course) | Section: [Embeddings](../README.md)

## What is it?

Measuring how close two pieces of text are **in meaning**, by comparing their
embedding vectors — not by comparing their words.

## Why it matters

It is the operation every semantic search and RAG retrieval step ultimately
performs. "Similar" here means *near in vector space*, which is what lets a
query match a passage that shares no vocabulary with it.

## How it works

1. Embed both texts with the **same** model.
2. Compute a similarity metric between the two vectors (usually cosine).
3. Higher score = closer in meaning.

## Simple example

```
"How do I reset my password?"
"Steps to change your login credentials"     -> high similarity, 0 shared keywords

"The bank raised interest rates"
"I sat on the river bank"                    -> low similarity, 1 shared keyword
```

## Remember

- Similarity is **relative, not absolute**. A score of 0.8 means nothing on its
  own — only the ranking between candidates matters.
- Embeddings capture topic and paraphrase well; they handle **negation, numbers
  and named entities poorly**. "not profitable" sits close to "profitable".
- Query and documents must come from the same embedding model.
- Semantic similarity ≠ relevance. Two texts can be near in vector space and
  still not answer one another.

## Related

- [03-cosine-similarity](../03-cosine-similarity/) · [01-what-are-embeddings](../01-what-are-embeddings/)
- [05-vector-search/02-similarity-search](../../05-vector-search/02-similarity-search/)
