# MMR (Maximal Marginal Relevance)

> Status: `studied` | Section: [Retrieval](../README.md)

## What is it?

A retrieval strategy that picks results which are relevant to the query **and
different from each other**.

## Why is it used?

Plain similarity search returns the top-k most similar documents - and those are
often near-duplicates of one another.

Example. A store holds five documents about climate change. Query: *"what are
the adverse effects of climate change?"* Plain similarity returns:

| # | Document | Problem |
| --- | --- | --- |
| 1 | Glaciers melting in the Arctic | fine |
| 2 | Arctic glaciers melting at an alarming rate | **says the same thing as #1** |
| 3 | Deforestation | fine |

Two of the three results carry the same information. Asking for 3 documents and
getting 2 distinct facts is wasted budget.

What you actually want: glaciers, wildfires, coastal flooding - three different
perspectives.

## How it works

MMR builds the result set greedily:

1. Pick the **most relevant** document first.
2. For each next pick, choose a document that is relevant **but dissimilar to
   what has already been picked**.
3. Repeat until `k` documents are selected.

## Simple example

```python
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.5},
)
```

`lambda_mult` runs from 0 to 1 and controls the balance:

| Value | Behaviour |
| --- | --- |
| `1.0` | Pure relevance - behaves exactly like normal similarity search |
| `0.5` | Balanced (a reasonable default) |
| `0.0` | Maximum diversity |

## Important points

- MMR does not make results *more relevant* - it makes the set *less redundant*.
- The trade-off is direct: pushing diversity up means accepting slightly less
  relevant documents.
- Useful whenever the corpus contains many documents saying similar things.

## Related

- [01-semantic-retrieval](../01-semantic-retrieval/)
- [09-context-engineering/03-context-deduplication](../../09-context-engineering/03-context-deduplication/) - the same problem, later in the pipeline
