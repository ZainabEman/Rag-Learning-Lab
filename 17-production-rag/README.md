# 17 Production RAG

> Track: **PRODUCTION TOPICS** | [Back to repository root](../README.md)

Everything between a working notebook and a system that stays fast, cheap and correct under real traffic.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Async Retrieval](01-async-retrieval/) | Non-blocking I/O across embedding, search and generation calls. | `not started` |
| 02 | [Parallel Retrieval](02-parallel-retrieval/) | Fanning out to multiple retrievers concurrently and merging results. | `not started` |
| 03 | [Caching](03-caching/) | What is safe to cache in a RAG pipeline and for how long. | `not started` |
| 04 | [Semantic Caching](04-semantic-caching/) | Serving near-duplicate queries from cache, and the risk of wrong hits. | `not started` |
| 05 | [Embedding Caching](05-embedding-caching/) | Content-hash keyed embedding reuse across re-ingestion runs. | `not started` |
| 06 | [Batch Ingestion](06-batch-ingestion/) | Throughput, batching, rate limits and resumability for large corpora. | `not started` |
| 07 | [Incremental Indexing](07-incremental-indexing/) | Adding new documents without rebuilding the whole index. | `not started` |
| 08 | [Document Updates](08-document-updates/) | Detecting changes and re-embedding only what changed. | `not started` |
| 09 | [Document Deletion](09-document-deletion/) | Hard vs soft deletes and keeping deleted content out of results. | `not started` |
| 10 | [Vector DB Scaling](10-vector-db-scaling/) | Sharding, replication, memory footprint and index build time. | `not started` |
| 11 | [Latency Optimization](11-latency-optimization/) | Measuring first, then cutting the stage that actually dominates. | `not started` |
| 12 | [Cost Optimization](12-cost-optimization/) | Model choice, chunk sizes, top-k, reranking depth and caching as cost levers. | `not started` |
| 13 | [Retries](13-retries/) | Idempotency, backoff and not amplifying an outage. | `not started` |
| 14 | [Timeouts](14-timeouts/) | Per-stage deadlines and returning a degraded answer instead of hanging. | `not started` |
| 15 | [Fallbacks](15-fallbacks/) | Graceful degradation when the index, reranker or model is unavailable. | `not started` |
| 16 | [Rate Limiting](16-rate-limiting/) | Client-side throttling and queueing against provider limits. | `not started` |
| 17 | [Multi-Tenancy](17-multi-tenancy/) | Data separation, noisy neighbours and per-tenant configuration. | `not started` |
| 18 | [Authentication](18-authentication/) | Identifying the caller before any retrieval happens. | `not started` |
| 19 | [Authorization](19-authorization/) | Turning identity into a retrieval filter that cannot be prompted around. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 17-production-rag <next-number>-<topic-slug> "Topic Title"
```
