# Lost in the Middle

> Status: `studied` (self-study, outside the course) | Section: [Context Engineering](../README.md)

## What is it?

The empirical finding that LLMs use information at the **start and end** of a
long context far more reliably than information in the **middle**.

Accuracy plotted against the position of the relevant fact forms a **U-shape**.

## Why it matters

It breaks the intuitive assumption that a bigger context window is strictly
better. Stuffing 50 chunks into a prompt can perform *worse* than carefully
choosing 5, because the answer may land in the dead zone.

## How it works

```
answer accuracy
   high │ *                           *
        │   *                      *
        │       *      *       *
   low  │            (middle)
        └───────────────────────────────
         first    position of fact    last
```

Attributed to positional attention patterns learned during training —
recency and primacy both get reinforced.

## Simple example

Same 20 documents, same question. Put the answer-bearing document at position 1
or 20 → the model answers correctly. Put it at position 10 → accuracy drops
sharply, sometimes below what the model achieves with *no* context at all.

## Remember

- **More context is not automatically better.** Precision beats volume.
- Directly motivates [reranking](../../06-retrieval/04-reranking-basics/),
  [compression](../02-context-compression/) and
  [ordering](../04-context-ordering/).
- The effect is weaker in newer long-context models but has not disappeared.
- Practical rule: if a chunk is not worth putting near an edge, consider not
  including it.

## Related

- [04-context-ordering](../04-context-ordering/) · [06-token-budgeting](../06-token-budgeting/)
- Paper: [PAPERS.md](../../PAPERS.md) (arXiv:2307.03172)
