# Contextual Retrieval

> Status: `studied` (self-study, outside the course) | Section: [Context Engineering](../README.md)

## What is it?

Before embedding a chunk, prepend a short generated description of where it came
from and what it is about — so the chunk carries its own context.

## Why it matters

Chunks lose their surroundings. A chunk reading "It rose 12% year over year" is
unretrievable and unusable: no reader, human or model, can tell what "it" is.
Roughly the most common silent failure in naive RAG.

## How it works

For each chunk, an LLM writes 1–2 sentences situating it inside its parent
document. That context is prepended to the chunk text **before embedding**, and
usually stored with it.

## Simple example

```
raw chunk:
  "It rose 12% year over year, driven mainly by the enterprise segment."

contextualised chunk:
  "From Acme Corp's 2024 annual report, revenue section:
   It rose 12% year over year, driven mainly by the enterprise segment."
```

Now a query about "Acme revenue growth 2024" can actually find it.

## Remember

- Costs **one LLM call per chunk at ingestion** — expensive once, free at query
  time. Prompt caching makes this much cheaper.
- Fixes pronouns and implicit subjects, which is where most orphaned chunks come
  from.
- Combines well with BM25: the added context supplies keywords too.
- Ingestion-time fix, so changing the strategy means re-indexing everything.

## Related

- [07-parent-document-retrieval](../07-parent-document-retrieval/) · [03-chunking](../../03-chunking/)
