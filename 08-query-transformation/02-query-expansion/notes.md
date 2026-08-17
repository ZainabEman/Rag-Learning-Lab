# Query Expansion

> Status: `studied` (self-study, outside the course) | Section: [Query Transformation](../README.md)

## What is it?

Adding extra terms — synonyms, related concepts, spelled-out acronyms — to the
query so it matches more of the relevant documents.

## Why it matters

Vocabulary mismatch is a core retrieval failure: the user says "car", the
document says "vehicle". Expansion widens the net, which mainly helps **recall**.

## How it works

Two flavours:

- **Lexical** — append synonyms and morphological variants. Helps sparse
  retrieval most.
- **LLM-based** — ask a model for related terms or an expanded phrasing.

## Simple example

```
original : "EV range"
expanded : "EV range electric vehicle battery range miles per charge autonomy"
```

For BM25 this is a large gain; for dense retrieval a modest one, since
embeddings already handle some synonymy.

## Remember

- Expansion raises recall and can **lower precision** — extra terms drag in
  loosely related documents.
- **Query drift** is the main risk: expand too aggressively and the query stops
  meaning what the user asked.
- Helps sparse retrieval far more than dense.
- Expansion adds terms; [rewriting](../01-query-rewriting/) replaces the query;
  [multi-query](../03-multi-query-retrieval/) issues several.

## Related

- [01-query-rewriting](../01-query-rewriting/) · [07-advanced-retrieval/02-bm25](../../07-advanced-retrieval/02-bm25/)
