# 03 Chunking

> Track: **COURSE CONTENT** | [Back to repository root](../README.md)

Splitting documents into retrievable units. The single highest-leverage knob in a basic RAG system.

## Why chunking exists

> Seeded from the RAG architecture lesson (indexing step 2). The dedicated
> text-splitters material has not been studied yet.

A loaded document is split into smaller, semantically meaningful pieces for two
**independent** reasons — either one alone would force chunking:

1. **Context length.** There is a hard limit on how many tokens an LLM will
   accept in a prompt. A two-hour lecture transcript or a 300-page book cannot
   be sent whole.
2. **Retrieval quality.** Semantic search degrades on large documents. One
   embedding for a long, multi-topic document is an average of everything in it,
   so it matches every topic weakly and none precisely.

The requirement that follows: chunks must break on **meaning**, not at arbitrary
offsets. Ideally one chunk covers one topic — a cut through the middle of an
explanation produces two chunks that each answer nothing.

Splitters named so far: `RecursiveCharacterTextSplitter` (the common default),
`SemanticChunker`, and format-aware splitters for HTML and Markdown.

Note that this is *not* the same as the per-page or per-row split a document
loader produces — that is the source's natural unit, not a semantic decision.
See [02-document-processing/01-document-loading](../02-document-processing/01-document-loading/).

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
