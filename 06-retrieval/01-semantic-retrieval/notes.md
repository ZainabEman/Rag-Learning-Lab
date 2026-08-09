# Semantic Retrieval

> Status: `overview only` — seeded from the RAG architecture lesson, where
> retrieval is stage 2 of the pipeline. The dedicated retrievers lesson has not
> been studied yet.
>
> Section: [Retrieval](../README.md)

## What is it?

> Retrieval is the real-time process of finding the most relevant pieces of
> information from a pre-built index, based on the user's question.

The useful phrasing: *"of all the knowledge I have, which 3–5 chunks are most
helpful for answering this query?"*

Inside the retriever, four things happen:

| Step | What happens | Detail that matters |
| --- | --- | --- |
| 1 | Embed the query | Must use **exactly** the embedding model that indexed the chunks — same model, same dimension |
| 2 | Search the vector store | Find the vectors closest to the query vector |
| 3 | Rank the candidates | Cosine similarity in the simple case; a reranking model in the advanced case |
| 4 | Fetch the chunk text | The text of the top-ranked chunks *is* the context |

## Why does it exist?

Because the whole corpus cannot go into the prompt. Retrieval is the filter that
turns an arbitrarily large knowledge base into a few hundred tokens of relevant
evidence, and it is the stage that decides the ceiling on answer quality —
stages 3 and 4 can only work with what it hands over.

Concretely: a two-hour lecture transcript is indexed, and the user asks about
the optimisation step in gradient descent. Retrieval's job is to return the two
passages where gradient descent is actually discussed and to leave out the ones
about OLS and multiple linear regression — rather than sending the entire
transcript.

Techniques named as alternatives to plain similarity search, not yet studied:
[MMR](../02-mmr/) and [contextual compression](../03-contextual-compression/).

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
