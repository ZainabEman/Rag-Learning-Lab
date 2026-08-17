# Similarity Search

> Status: `studied` | Section: [Vector Search](../README.md)

## What is it?

The core read operation of a vector store: embed the query, compare it against
every stored vector, return the closest `k`.

## Why is it used?

It is how "find me things that mean something similar" gets answered. Keyword
search cannot do it; this can.

## How it works

1. The query string is embedded with the **same model** used for the documents.
2. The store compares the query vector against stored vectors.
3. The top `k` matches come back as `Document` objects.

## Simple example

```python
# k = how many results to return
store.similarity_search(query="Among these, who is a bowler?", k=2)

# same thing, but each result carries its distance score
store.similarity_search_with_score(query="Among these, who is a bowler?", k=2)
```

Given five documents about cricket players, the query *"who is a bowler?"*
returns Jasprit Bumrah first. At `k=2` the second result is Ravindra Jadeja -
his document says "all-rounder", which semantically covers bowling. No keyword
matching would find that.

## Important points

- **The score is a distance, so lower is better.** Closer vector = more similar.
- `k` controls how many results come back, nothing else - it does not make the
  matches better, just longer.
- Similarity search always returns `k` results, however poor the best match is.
  There is no "nothing matched" signal.

## Related

- [01-vector-databases](../01-vector-databases/) · [03-top-k](../03-top-k/)
- [06-retrieval/01-semantic-retrieval](../../06-retrieval/01-semantic-retrieval/) - the same operation wrapped as a retriever
