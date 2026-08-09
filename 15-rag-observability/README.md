# 15 RAG Observability

> Track: **PRODUCTION TOPICS** | [Back to repository root](../README.md)

Seeing what a running RAG system actually did: what was retrieved, what was prompted, what it cost.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Tracing](01-tracing/) | Spans across the whole pipeline and what to record at each stage. | `not started` |
| 02 | [Retrieval Traces](02-retrieval-traces/) | Logging queries, scores, chosen chunks and filters for post-hoc analysis. | `not started` |
| 03 | [Prompt Traces](03-prompt-traces/) | Capturing the exact final prompt, not the template. | `not started` |
| 04 | [Token Usage](04-token-usage/) | Measuring where the tokens go across ingestion, retrieval and generation. | `not started` |
| 05 | [Latency](05-latency/) | Breaking end-to-end latency down per stage to find the real bottleneck. | `not started` |
| 06 | [Cost Tracking](06-cost-tracking/) | Per-query cost attribution across embedding, reranking and generation. | `not started` |
| 07 | [Failed Retrieval Analysis](07-failed-retrieval-analysis/) | Triaging bad answers into retrieval, ranking, context or generation failures. | `not started` |
| 08 | [Production Evaluation](08-production-evaluation/) | Sampling and scoring live traffic without a labelled set. | `not started` |
| 09 | [Regression Monitoring](09-regression-monitoring/) | Alerting on drift in retrieval quality, latency and cost. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 15-rag-observability <next-number>-<topic-slug> "Topic Title"
```
