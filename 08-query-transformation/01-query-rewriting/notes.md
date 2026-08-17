# Query Rewriting

> Status: `studied` (self-study, outside the course) | Section: [Query Transformation](../README.md)

## What is it?

Using an LLM to turn the user's raw question into a better **search query**
before retrieval runs.

## Why it matters

Users write questions; retrieval works best with well-specified statements.
Vague, conversational or typo-ridden input retrieves badly, and no amount of
reranking downstream can fix a bad query.

## How it works

Query → LLM ("rewrite this as a precise search query") → rewritten query →
retriever.

## Simple example

```
user     : "it broke again, same as last time"
rewritten: "recurring application crash after update — troubleshooting steps"

user     : "cheapest way to do this?"
rewritten: "lowest-cost pricing tier options and cost comparison"
```

## Remember

- Costs one LLM call **before** retrieval — pure added latency on every query.
- The rewrite can *lose* information; keep the original as a fallback or
  retrieve with both.
- Especially valuable in chat, where a follow-up like "what about the other
  one?" is meaningless standing alone — see
  [09-conversational-query-rewriting](../09-conversational-query-rewriting/).
- Distinct from [expansion](../02-query-expansion/): rewriting *replaces* the
  query, expansion *adds* to it.

## Related

- [02-query-expansion](../02-query-expansion/) · [03-multi-query-retrieval](../03-multi-query-retrieval/)
