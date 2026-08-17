# Metadata Filtering

> Status: `studied` | Section: [Vector Search](../README.md)

## What is it?

Restricting a vector-store search to documents whose metadata matches a
condition - so the semantic search only ever considers a subset.

## Why is it used?

Some constraints are exact, not semantic. "Only players from Chennai Super
Kings", "only documents from 2024", "only files this user is allowed to see".
Embeddings are the wrong tool for those; metadata is the right one.

## How it works

Metadata is attached when the document is created and stored next to the vector.
At query time a filter is applied against that metadata.

## Simple example

```python
store.similarity_search(
    query="",
    filter={"team": "Chennai Super Kings"},
)
```

With five cricket-player documents, this returns exactly the two whose metadata
says Chennai Super Kings - MS Dhoni and Ravindra Jadeja. Note the query can be
empty when the filter alone is doing the work.

## Important points

- Metadata must be set **at ingestion**. Adding it later means re-indexing.
- This is the mechanism behind access control in a real system - permissions
  live in metadata, not in the prompt.

## Related

- [01-vector-databases](../01-vector-databases/)
- [02-document-processing/03-metadata](../../02-document-processing/03-metadata/) - where metadata comes from
