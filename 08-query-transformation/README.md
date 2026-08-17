# 08 Query Transformation

> Track: **ADVANCED TOPICS** | [Back to repository root](../README.md)

Fixing retrieval on the input side: the user's question is often not a good search query.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Query Rewriting](01-query-rewriting/) | Rewriting vague or under-specified questions into retrieval-friendly queries. | `studied` |
| 02 | [Query Expansion](02-query-expansion/) | Adding synonyms, entities and related terms to improve lexical and dense recall. | `studied` |
| 03 | [Multi-Query Retrieval](03-multi-query-retrieval/) | Generating several query variants and merging their result sets. | `studied` |
| 04 | [Query Decomposition](04-query-decomposition/) | Breaking a compound question into independently answerable sub-queries. | `studied` |
| 05 | [RAG Fusion](05-rag-fusion/) | Multi-query generation combined with reciprocal rank fusion. | `not started` |
| 06 | [HyDE (Hypothetical Document Embeddings)](06-hyde/) | Embedding a generated hypothetical answer instead of the raw question; when this helps and when it hurts. | `studied` |
| 07 | [Step-Back Prompting](07-step-back-prompting/) | Asking a more general question first to retrieve the background a specific question depends on. | `studied` |
| 08 | [Sub-Question Retrieval](08-sub-question-retrieval/) | Running retrieval per sub-question and synthesising a single grounded answer. | `not started` |
| 09 | [Conversational Query Rewriting](09-conversational-query-rewriting/) | Resolving pronouns and implicit context in follow-up turns into standalone queries. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 08-query-transformation <next-number>-<topic-slug> "Topic Title"
```
