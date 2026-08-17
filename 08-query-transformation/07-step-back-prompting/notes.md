# Step-Back Prompting

> Status: `studied` (self-study, outside the course) | Section: [Query Transformation](../README.md)

## What is it?

Generate a **more general** version of the question, retrieve for that too, and
use both sets of context.

## Why it matters

Very specific questions often need background the corpus states only in general
terms. Retrieving on the specific query alone misses the principle that
actually explains the answer.

## How it works

Query → LLM ("what more general question would help answer this?") → retrieve
for both the original and the step-back question → merge context → answer.

## Simple example

```
specific : "why did our p99 latency spike at 14:32 after the deploy?"
step-back: "what causes latency spikes after a deployment?"

specific retrieval  → the incident log for that timestamp
step-back retrieval → the doc on cold starts and connection-pool warm-up
```

The second one contains the actual explanation.

## Remember

- Use **both** queries — the step-back one alone loses the specifics.
- Works best for "why" and reasoning questions; adds little to simple lookups.
- Related to [decomposition](../04-query-decomposition/), but goes *up* a level
  of abstraction rather than sideways into parts.
- Costs one extra LLM call and one extra retrieval.

## Related

- [04-query-decomposition](../04-query-decomposition/) · [06-hyde](../06-hyde/)
- Paper: [PAPERS.md](../../PAPERS.md) (arXiv:2310.06117)
