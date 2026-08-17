# 09 Context Engineering

> Track: **ADVANCED TOPICS** | [Back to repository root](../README.md)

What actually reaches the model: how much, in what order, and with what surrounding information.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Contextual Retrieval](01-contextual-retrieval/) | Prepending chunk-level context (document/section summary) before embedding to fix orphaned chunks. | `studied` |
| 02 | [Context Compression](02-context-compression/) | Extractive and abstractive compression of retrieved context under a token budget. | `studied` |
| 03 | [Context Deduplication](03-context-deduplication/) | Detecting near-duplicate chunks so the budget is not spent on the same sentence three times. | `studied` |
| 04 | [Context Ordering](04-context-ordering/) | How placement of the relevant chunk in the prompt changes answer quality. | `studied` |
| 05 | [Lost in the Middle](05-lost-in-the-middle/) | Reproducing the positional-attention effect on a small controlled set. | `studied` |
| 06 | [Token Budgeting](06-token-budgeting/) | Allocating a fixed context window across system prompt, history, retrieved context and answer. | `not started` |
| 07 | [Parent Document Retrieval](07-parent-document-retrieval/) | Indexing small chunks for precision but returning the parent block for context. | `studied` |
| 08 | [Small-to-Big Retrieval](08-small-to-big-retrieval/) | Sentence-window and expanding-window retrieval variants. | `studied` |
| 09 | [Hierarchical Retrieval](09-hierarchical-retrieval/) | Summary-level retrieval that routes down to detail-level chunks. | `studied` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 09-context-engineering <next-number>-<topic-slug> "Topic Title"
```
