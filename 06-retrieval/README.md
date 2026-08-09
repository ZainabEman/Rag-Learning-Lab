# 06 Retrieval

> Track: **COURSE CONTENT** | [Back to repository root](../README.md)

Turning a query into a set of context chunks that are actually worth putting in the prompt.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Semantic Retrieval](01-semantic-retrieval/) | The baseline retriever end to end: embed query, search, return chunks with scores and sources. | `not started` |
| 02 | [MMR (Maximal Marginal Relevance)](02-mmr/) | Trading relevance against diversity to stop the top-k being five copies of the same paragraph. | `not started` |
| 03 | [Contextual Compression](03-contextual-compression/) | Filtering or shortening retrieved chunks against the query before they reach the prompt. | `not started` |
| 04 | [Reranking Basics](04-reranking-basics/) | Why a second-stage scorer beats first-stage similarity, and the retrieve-many/rerank-few pattern. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 06-retrieval <next-number>-<topic-slug> "Topic Title"
```
