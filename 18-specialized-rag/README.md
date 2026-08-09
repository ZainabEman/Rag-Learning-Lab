# 18 Specialized RAG

> Track: **PRODUCTION TOPICS** | [Back to repository root](../README.md)

RAG variants where the retrieval target is not a pile of documents.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [SQL RAG](01-sql-rag/) | Schema retrieval, text-to-SQL, execution and grounding answers in query results. | `not started` |
| 02 | [API RAG](02-api-rag/) | Retrieving over API specs and calling endpoints as the retrieval step. | `not started` |
| 03 | [Web RAG](03-web-rag/) | Live search, fetching, extraction and freshness/trust handling. | `not started` |
| 04 | [Code RAG](04-code-rag/) | Repository-aware chunking by symbol, plus dependency and call-graph context. | `not started` |
| 05 | [Knowledge Base RAG](05-knowledge-base-rag/) | Internal docs/wikis: permissions, staleness and duplicate content. | `not started` |
| 06 | [Research RAG](06-research-rag/) | Papers: sections, citations, figures and multi-document synthesis. | `not started` |
| 07 | [Conversational RAG](07-conversational-rag/) | History-aware retrieval, memory and topic switching across turns. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 18-specialized-rag <next-number>-<topic-slug> "Topic Title"
```
