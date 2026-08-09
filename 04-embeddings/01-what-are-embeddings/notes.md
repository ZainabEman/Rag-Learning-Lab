# What Are Embeddings

> Status: `overview only` — seeded from the RAG architecture lesson, where
> embeddings appear as step 3 of indexing. The dedicated embeddings lesson has
> not been studied yet, so the sections below "Problem it solves" are still open.
>
> Section: [Embeddings](../README.md)

## What is it?

An embedding is a **dense vector** that represents the semantic meaning of a
piece of unstructured data — here, text. A deep-learning model reads a chunk of
text and outputs a fixed-length list of numbers, positioned so that texts with
similar meanings land near each other in that space.

"Dense" is doing work in that sentence: every dimension carries signal, unlike
sparse representations such as TF-IDF where almost every entry is zero.

## Why does it exist?

In a RAG pipeline, embeddings exist to make search **semantic** rather than
lexical. A user asking *"how do we perform the optimization step in gradient
descent?"* needs to match a passage that may never contain the word
"optimization". Keyword matching cannot do that; vector similarity can.

The chain of reasoning from the architecture is worth keeping in one line:
semantic search happens *between vectors*, so every chunk has to become a vector
before it can be searched. That is why embedding is a mandatory indexing step
rather than an optional improvement.

Two constraints that follow, both learned as architecture rather than as
embedding theory:

- The **same** embedding model must be used for chunks and for queries. Two
  models produce two incompatible spaces, and the similarity between them is
  noise.
- Changing the embedding model means re-embedding the entire corpus. The choice
  is effectively locked in for the lifetime of an index.

Models named so far: OpenAI embeddings (hosted API) and sentence-transformers
(runs locally). Comparing them properly is
[04-embedding-models](../04-embedding-models/).

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
