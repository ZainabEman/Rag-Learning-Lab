# 05 Vector Search

> Track: **COURSE CONTENT** | [Back to repository root](../README.md)

Storing vectors and finding nearest neighbours at speed.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Vector Databases](01-vector-databases/) | What a vector store adds over a numpy array: persistence, filtering, indexing, updates, scaling. | `not started` |
| 02 | [Similarity Search](02-similarity-search/) | Brute-force search from scratch, then the same query through Chroma/FAISS; verifying the results match. | `not started` |
| 03 | [Top-K](03-top-k/) | How k affects recall, precision, prompt size and cost; finding a sensible default for a corpus. | `not started` |
| 04 | [Metadata Filtering](04-metadata-filtering/) | Pre-filter vs post-filter, and how filtering interacts with approximate indexes. | `not started` |
| 05 | [Vector Indexing](05-vector-indexing/) | Flat vs approximate indexes: what an index build actually does and what it costs. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 05-vector-search <next-number>-<topic-slug> "Topic Title"
```
