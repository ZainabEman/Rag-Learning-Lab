# Vector Databases

> Status: `studied` | Section: [Vector Search](../README.md)

## What is it?

A system built to **store vectors and retrieve them by similarity**.

Once text is embedded, the query-time question becomes "which stored vector is
closest to this one?" Relational databases (MySQL, Oracle) cannot answer that -
they can store the numbers, but they have no notion of similarity between rows.
That gap is the reason a separate kind of store exists.

## Why is it used?

The motivating example: a movie catalogue site that wants a recommender.

| Approach | How it works | Why it fails |
| --- | --- | --- |
| Keyword matching | Compare director, actor, genre, release year | *My Name Is Khan* -> *Kabhi Alvida Naa Kehna* scores high (same director, same lead actor, similar era) but the stories are unrelated. And *Taare Zameen Par* / *A Beautiful Mind* are genuinely similar in theme yet share **no** keywords, so they can never be matched. |
| Plot embeddings | Embed each movie's plot, compare vectors | Compares what the film is actually *about* |

Switching to embeddings then creates three new engineering problems, and a
vector store is the thing that solves all three:

1. **Generating** embeddings for a large catalogue.
2. **Storing** them somewhere that understands similarity.
3. **Searching** them fast - comparing one query against a million vectors
   one-by-one is far too slow.

## How it works

Four core features:

| Feature | What it gives you |
| --- | --- |
| **Storage** | Vectors + their metadata, either in memory (fast, lost on exit) or on disk (persistent) |
| **Similarity search** | Compare a query vector against stored vectors, return the closest |
| **Indexing** | Data structures that make that search fast instead of linear - see [05-vector-indexing](../05-vector-indexing/) |
| **CRUD** | Add, read, update and delete vectors, like any database |

## Vector store vs vector database

These terms get used interchangeably, but there is a real distinction:

```
vector store  +  database-like features  =  vector database
```

- **Vector store** - a lightweight library that stores vectors and does
  similarity search. Good for prototyping. Example: **FAISS** (from Meta).
- **Vector database** - all of that, plus distributed architecture, backup and
  restore, ACID-style guarantees, concurrency control, authentication.
  Examples: **Milvus, Qdrant, Weaviate, Pinecone**.

Every vector database is a vector store; the reverse is not true.

**Chroma** sits between the two - lightweight enough for local development, but
with some database features. It stores data as a SQLite file on disk.

Chroma's hierarchy: `tenant -> database -> collection -> document`.
A *collection* is the equivalent of a table; a *document* holds an embedding
plus its metadata.

## Simple example

LangChain wraps every vector store behind the **same method signatures**, so
swapping FAISS for Pinecone later means changing the constructor, not the code
around it.

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="my_chroma_db",
    collection_name="sample",
)

store.add_documents(docs)              # returns auto-generated ids
store.get(include=["embeddings", "documents", "metadatas"])
store.update_document(document_id=some_id, document=new_doc)
store.delete(ids=[some_id])
```

## Important points

- Store the **metadata alongside the vector** - it is what makes filtering and
  citation possible later.
- In-memory vs on-disk is a real choice: in-memory disappears when the process
  exits.
- Each added document gets a unique id (auto-generated, or supply your own).
  Updates and deletes work through that id.
- The common LangChain interface (`from_documents`, `add_documents`,
  `similarity_search`) is the reason vector stores are swappable.

## Related

- [02-similarity-search](../02-similarity-search/) · [04-metadata-filtering](../04-metadata-filtering/) · [05-vector-indexing](../05-vector-indexing/)
- [06-retrieval/01-semantic-retrieval](../../06-retrieval/01-semantic-retrieval/)

## Questions I still have

- When is Chroma no longer enough, in practice?
- How much does index choice matter compared to embedding-model choice?
