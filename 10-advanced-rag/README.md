# 10 Advanced RAG

> Track: **RESEARCH TOPICS** | [Back to repository root](../README.md)

Control-flow research patterns: systems that decide whether, when and how many times to retrieve.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Self-RAG](01-self-rag/) | Retrieve-on-demand with self-critique tokens for relevance, support and usefulness. | `not started` |
| 02 | [Corrective RAG (CRAG)](02-corrective-rag-crag/) | Grading retrieved documents and falling back (e.g. to web search) when they are insufficient. | `not started` |
| 03 | [Adaptive RAG](03-adaptive-rag/) | Routing queries by complexity: no retrieval, single-step, or multi-step. | `not started` |
| 04 | [Iterative RAG](04-iterative-rag/) | Multi-round retrieve-generate loops with a stopping condition. | `not started` |
| 05 | [FLARE](05-flare/) | Forward-looking active retrieval triggered by low-confidence generated tokens. | `not started` |
| 06 | [Retrieval Routing](06-retrieval-routing/) | Choosing between several indexes/sources per query, including 'do not retrieve'. | `not started` |
| 07 | [Corrective Retrieval](07-corrective-retrieval/) | Detecting bad retrievals at runtime and repairing them (re-query, expand, fall back). | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 10-advanced-rag <next-number>-<topic-slug> "Topic Title"
```
