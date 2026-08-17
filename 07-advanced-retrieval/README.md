# 07 Advanced Retrieval

> Track: **ADVANCED TOPICS** | [Back to repository root](../README.md)

Lexical, dense and hybrid retrieval, plus the index structures and rerankers that make them fast and accurate.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [TF-IDF](01-tf-idf/) | Term weighting from scratch: term frequency, inverse document frequency, and the vector space model. | `not started` |
| 02 | [BM25](02-bm25/) | The Okapi BM25 scoring function implemented by hand, then via rank_bm25; the role of k1 and b. | `studied` |
| 03 | [Sparse vs Dense Retrieval](03-sparse-vs-dense/) | Where lexical matching wins (rare terms, IDs, exact phrases) and where dense wins (paraphrase, intent). | `studied` |
| 04 | [Hybrid Search](04-hybrid-search/) | Combining sparse and dense results; score normalisation and weighted fusion. | `studied` |
| 05 | [Reciprocal Rank Fusion](05-reciprocal-rank-fusion/) | Rank-based fusion that avoids score normalisation entirely; implementing RRF from the formula. | `studied` |
| 06 | [Approximate Nearest Neighbour](06-ann/) | The recall/latency trade-off: why exact search stops being viable and what 'approximate' costs you. | `not started` |
| 07 | [HNSW](07-hnsw/) | Hierarchical navigable small world graphs: layers, M, ef_construction, ef_search - and what each does to recall. | `not started` |
| 08 | [IVF (Inverted File Index)](08-ivf/) | Clustering vectors into cells and probing a subset; nlist/nprobe and their effect on recall. | `not started` |
| 09 | [Product Quantization](09-product-quantization/) | Compressing vectors into subspace codes: memory savings vs accuracy loss. | `not started` |
| 10 | [Cross-Encoder Reranking](10-cross-encoder-reranking/) | Joint query-document encoding: why it is more accurate than bi-encoders and why it cannot scale to the whole corpus. | `studied` |
| 11 | [ColBERT](11-colbert/) | Token-level embeddings with MaxSim scoring; storage cost vs retrieval quality. | `not started` |
| 12 | [Late Interaction](12-late-interaction/) | The general idea behind ColBERT-style models compared to early interaction (cross-encoders) and no interaction (bi-encoders). | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 07-advanced-retrieval <next-number>-<topic-slug> "Topic Title"
```
