# What Are Embeddings

> Status: `studied` — originally seeded from the RAG architecture lesson, then
> filled in from self-study.
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

## How it works

A neural model (usually a transformer encoder) reads the text and outputs a
fixed-length vector — typically 384, 768 or 1536 dimensions. Training pushes
texts with similar meaning close together and dissimilar ones apart, so
*position* in the space encodes meaning.

Individual dimensions are **not** interpretable. There is no "sentiment axis";
only relative distances mean anything.

## Simple example

```
embed("How do I reset my password?")  -> [0.021, -0.118, 0.334, ... ]  (1536 floats)
embed("Steps to change your login")   -> [0.019, -0.101, 0.341, ... ]  ← nearby
embed("Best pizza in Naples")         -> [-0.44,  0.203, -0.02, ... ]  ← far away
```

## Remember

- **Fixed length regardless of input size.** A sentence and a page both become
  the same-sized vector — which is why long chunks embed poorly: more meaning
  compressed into the same space.
- Dimensions are meaningless individually; only distances matter.
- Same model on both sides, always. Changing the model = re-embedding everything.
- Embeddings are **not reversible** — you cannot recover text from a vector,
  which is why the chunk text is stored alongside it.
- Weak on negation, numbers and exact identifiers. That is what
  [BM25](../../07-advanced-retrieval/02-bm25/) is for.

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
