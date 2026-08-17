# Context Deduplication

> Status: `studied` (self-study, outside the course) | Section: [Context Engineering](../README.md)

## What is it?

Removing near-duplicate chunks from the retrieved set before building the prompt.

## Why it matters

Corpora contain repeated content — chunk overlap, copies across documents,
boilerplate, versioned pages. Retrieval happily returns the same fact five
times, spending the context budget on one idea and crowding out the others.

## How it works

1. Retrieve more than needed (k=20 for a target of 5).
2. Compare chunks pairwise — exact hash, or embedding similarity above a
   threshold (~0.95), or text overlap.
3. Keep the highest-ranked of each duplicate group.

## Simple example

```
retrieved:
  1. "Arctic glaciers are melting rapidly due to rising temperatures."
  2. "Glaciers in the Arctic are melting at an alarming rate."   ← duplicate of 1
  3. "Deforestation accelerates biodiversity loss."

after dedup: 1, 3  → and slot 2 can be refilled with genuinely new content
```

## Remember

- **Chunk overlap is a built-in duplicate generator** — adjacent chunks share
  text by design.
- Threshold choice matters: too aggressive and you drop genuinely distinct
  chunks that are merely similar.
- [MMR](../../06-retrieval/02-mmr/) prevents duplicates *during* retrieval;
  dedup removes them *after*. They solve the same problem at different stages.
- Always retrieve extra so removals can be backfilled.

## Related

- [06-retrieval/02-mmr](../../06-retrieval/02-mmr/) · [03-chunking/04-chunk-overlap](../../03-chunking/04-chunk-overlap/)
