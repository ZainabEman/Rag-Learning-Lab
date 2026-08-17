# Small-to-Big Retrieval

> Status: `studied` (self-study, outside the course) | Section: [Context Engineering](../README.md)

## What is it?

The general pattern behind parent-document retrieval: **match on a small unit,
expand to a larger one before generation.**

## Why it matters

Retrieval precision and context sufficiency want opposite chunk sizes. Splitting
the two decisions — one unit for matching, another for reading — removes the
compromise.

## How it works

Three common variants:

| Variant | Match on | Return |
| --- | --- | --- |
| **Sentence window** | One sentence | That sentence ± N neighbours |
| **Parent document** | Small child chunk | Its larger parent |
| **Summary index** | A generated summary | The full underlying document |

## Simple example

Sentence-window with a window of 1:

```
matched sentence : "Rollback requires the --force flag."
returned context : "Deploys are atomic by default.
                    Rollback requires the --force flag.
                    Without it the CLI refuses to overwrite a newer release."
```

The matched sentence alone would have been useless.

## Remember

- Decouples the **matching unit** from the **reading unit** — that is the whole
  idea.
- Expansion multiplies tokens; budget for it.
- Deduplicate after expanding — neighbouring matches produce overlapping windows.
- Sentence-window suits dense prose; parent-document suits structured docs.

## Related

- [07-parent-document-retrieval](../07-parent-document-retrieval/) · [09-hierarchical-retrieval](../09-hierarchical-retrieval/)
