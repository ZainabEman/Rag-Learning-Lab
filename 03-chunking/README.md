# 03 Chunking

> Track: **COURSE CONTENT** | [Back to repository root](../README.md)

Splitting documents into retrievable units. The single highest-leverage knob in a basic RAG system.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Fixed-Size Chunking](01-fixed-size-chunking/) | Character and token based splitting; why it is the baseline and where it breaks semantic units. | `not started` |
| 02 | [Recursive Chunking](02-recursive-chunking/) | Splitting on a hierarchy of separators so paragraphs and sentences survive where possible. | `not started` |
| 03 | [Chunk Size](03-chunk-size/) | The trade-off between retrieval precision (small chunks) and context sufficiency (large chunks). | `not started` |
| 04 | [Chunk Overlap](04-chunk-overlap/) | Why overlap exists, what it costs in storage and duplication, and how much is actually useful. | `not started` |
| 05 | [Chunking Strategies](05-chunking-strategies/) | Semantic, structure-aware, sentence-window and document-specific strategies compared on the same corpus. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 03-chunking <next-number>-<topic-slug> "Topic Title"
```
