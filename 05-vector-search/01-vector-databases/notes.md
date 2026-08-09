# Vector Databases

> Status: `overview only` — seeded from the RAG architecture lesson, where the
> vector store appears as step 4 of indexing. The dedicated vector-store lesson
> has not been studied yet.
>
> Section: [Vector Search](../README.md)

## What is it?

The storage layer of the external knowledge base. It holds, for every chunk,
three things together:

| Stored | Why it must be there |
| --- | --- |
| The **embedding vector** | What the similarity search runs against |
| The **original chunk text** | What eventually goes into the prompt |
| The **metadata** | Citation, filtering, debugging |

Storing the text alongside the vector is not an optimisation — it is required.
An embedding cannot be reversed back into its text, so a store of vectors alone
would be able to tell you *which* chunk matched and nothing about what it said.

## Why does it exist?

Once every chunk is a vector, the query-time question becomes "which of these
vectors is nearest to the query vector?" — and that has to be answered fast,
repeatedly, over a corpus that can be very large. A vector store is the
component that makes that lookup practical, and it is what turns a pile of
embeddings into a searchable knowledge base.

Options named so far:

| Type | Examples |
| --- | --- |
| Local / embedded | FAISS, Chroma |
| Cloud / managed | Pinecone, Weaviate, Milvus, Qdrant |

Local stores are the right choice for learning and for privacy-sensitive work —
nothing leaves the machine. What managed stores add (scaling, replication,
operational concerns) is [10-vector-db-scaling](../../17-production-rag/10-vector-db-scaling/).

## Problem it solves

TODO

## How it works

<!-- Step by step. If I cannot write the steps, I have not understood it yet. -->

TODO

## Architecture

<!-- Diagram or ASCII sketch of where this sits in a RAG pipeline. -->

TODO

## Important concepts

TODO

## Mathematical intuition

<!-- The formula, what each symbol means, and why the formula has that shape.
     Skip only if there genuinely is no maths involved. -->

TODO

## Implementation details

<!-- Gotchas found while writing implementation.py. -->

TODO

## What I initially misunderstood

<!-- Be specific and honest. This section is the most valuable one later. -->

TODO

## What I learned

TODO

## Limitations

TODO

## When should I use it?

TODO

## When should I NOT use it?

TODO

## Related concepts

<!-- Relative links to other topic folders in this repo. -->

TODO

## Questions I still have

- TODO
