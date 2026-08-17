# HyDE (Hypothetical Document Embeddings)

> Status: `studied` (self-study, outside the course) | Section: [Query Transformation](../README.md)

## What is it?

Ask an LLM to **invent an answer** to the query, then embed that fake answer and
use *it* as the search vector instead of the query.

## Why it matters

Questions and answers look different. A short question and a long explanatory
passage sit in different regions of embedding space even when one answers the
other. A hypothetical answer looks like the documents you are searching for, so
it lands closer to them.

## How it works

```mermaid
flowchart LR
    Q[Query] --> L["LLM: write a passage<br/>that answers this"]
    L --> H["Hypothetical answer<br/>(may be factually wrong)"]
    H --> E[Embed it]
    E --> V[(Vector search)]
    V --> D[Real documents]
```

The generated text does **not** need to be correct. It only needs the right
shape and vocabulary — it is a search probe, and it is discarded afterwards.

## Simple example

```
query : "why is my container OOMKilled?"

hypothetical answer (generated):
  "A container is OOMKilled when it exceeds its memory limit. Kubernetes
   terminates it with exit code 137. Check resource limits and requests..."

→ embed that paragraph → retrieves the real docs on memory limits and exit 137
```

## Remember

- The hypothetical answer being **wrong is fine** — it is never shown to the user.
- Costs one LLM call before retrieval; that is the whole price.
- Helps most on short/vague queries and technical domains; helps least when the
  model knows nothing about the domain and hallucinates off-topic vocabulary.
- Can *hurt* on queries with rare exact terms — the generated text may bury them.

## Related

- [01-query-rewriting](../01-query-rewriting/) · [07-step-back-prompting](../07-step-back-prompting/)
- Paper: [PAPERS.md](../../PAPERS.md) (arXiv:2212.10496)
