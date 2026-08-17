# Semantic Retrieval

> Status: `studied` | Section: [Retrieval](../README.md)

## What is it?

A **retriever** is a component that takes a user query and returns relevant
`Document` objects from a data source.

```
query (string)  ->  [ retriever ]  ->  list[Document]
```

Think of it as a search engine sitting in front of your data.

## Why is it used?

A vector store can already do `similarity_search`, so why wrap it?

Two reasons:

1. **Retrievers are runnables.** They have `.invoke()`, so they plug directly
   into LCEL chains alongside prompts and models.
2. **A vector store only knows one search strategy.** Retrievers let you swap in
   smarter strategies - MMR, multi-query, compression - without changing the
   store.

For plain similarity search the two are equivalent. The value shows up when the
strategy changes.

## How it works

Retrievers are categorised two ways:

**By data source**

| Retriever | Source |
| --- | --- |
| `WikipediaRetriever` | The Wikipedia API |
| `VectorStoreRetriever` | A vector store (the most common) |
| `ArxivRetriever` | Research papers on arXiv |

**By search strategy**

| Retriever | Strategy |
| --- | --- |
| Vector store retriever | Plain semantic similarity |
| [MMR](../02-mmr/) | Relevant **and** diverse |
| [Multi-query](../../08-query-transformation/03-multi-query-retrieval/) | Generate several queries from one |
| [Contextual compression](../03-contextual-compression/) | Trim retrieved text to what matters |

## Simple example

```python
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke("What is Chroma used for?")
```

`WikipediaRetriever` works the same way:

```python
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang="en")
docs = retriever.invoke("geopolitical history of India and Pakistan")
```

## Important points

- Input is always a query string; output is always `list[Document]`.
- **A retriever is not a document loader.** `WikipediaRetriever` does not fetch
  all of Wikipedia - it searches and decides which articles are relevant. The
  intelligence in between is what makes it a retriever.
- `WikipediaRetriever` matches on **keywords** internally, not semantics.
- Retrievers are runnables, so `.invoke()` works and they compose into chains.
- LangChain ships 20-30+ retrievers. Learn the interface, then look up the one a
  project needs.

## Why so many retrievers exist

A simple RAG system often retrieves poorly. The usual way to improve it is to
swap the retriever for a more advanced one. "Advanced RAG" is, in large part,
this list of retrievers.

## Related

- [02-mmr](../02-mmr/) · [03-contextual-compression](../03-contextual-compression/)
- [05-vector-search/01-vector-databases](../../05-vector-search/01-vector-databases/)
