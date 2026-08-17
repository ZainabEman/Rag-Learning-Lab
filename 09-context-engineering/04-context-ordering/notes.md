# Context Ordering

> Status: `studied` (self-study, outside the course) | Section: [Context Engineering](../README.md)

## What is it?

Deciding **where in the prompt** each retrieved chunk goes.

## Why it matters

Models do not attend uniformly across a long prompt. The same chunks, reordered,
produce different answers — so ordering is a free quality lever that costs no
extra tokens or calls.

## How it works

Because of the [lost-in-the-middle](../05-lost-in-the-middle/) effect, the
standard trick is **"reordering"**: put the most relevant chunks at the
beginning *and* the end, and bury the weakest in the middle.

```
relevance rank:  1  2  3  4  5
prompt order  :  1  3  5  4  2
                 ^           ^
                 strongest at both edges
```

## Simple example

```python
def reorder(docs):                 # docs sorted best-first
    head, tail = [], []
    for i, d in enumerate(docs):
        (head if i % 2 == 0 else tail).append(d)
    return head + tail[::-1]       # best at both ends, worst in the middle
```

## Remember

- Costs nothing — no extra tokens, no extra calls. Pure reordering.
- Matters more the longer the context; negligible with 3 short chunks.
- Some pipelines instead put the best chunk **last**, nearest the question.
  Which wins is model-specific — test it.
- Keep chunks from the same source adjacent so the model can follow continuity.

## Related

- [05-lost-in-the-middle](../05-lost-in-the-middle/) · [06-token-budgeting](../06-token-budgeting/)
