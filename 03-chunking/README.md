# 03 Chunking

> Track: **COURSE CONTENT** | [Back to repository root](../README.md)

Splitting documents into retrievable units. The single highest-leverage knob in a basic RAG system.

## Why chunking exists

**Text splitting** is the process of breaking large text — articles, PDFs, HTML
pages, books — into smaller, manageable pieces an LLM can handle effectively.
The code that performs it is a **text splitter**.

Three independent reasons force it; any one of them alone would be enough:

**1. Model limits.** Both LLMs and embedding models cap how much input they
accept at once. If a model's context length is 50,000 tokens and the PDF runs to
100,000 words, it cannot be sent whole — the request simply fails.

**2. Better results on every downstream task.**

| Task | What happens on one large text | What happens on chunks |
| --- | --- | --- |
| Embedding | One vector has to compress the meaning of the whole text, so it represents nothing precisely | Each chunk gets its own vector that captures *its* meaning |
| Semantic search | Matches are vague — the query matches "the document" rather than a passage | Search is far more precise |
| Summarisation | LLMs drift off-topic on long inputs, and sometimes hallucinate content that is not in the document | Summaries stay grounded |

The embedding case is the clearest. Take a text where paragraph 1 is about CSK,
paragraph 2 about Mumbai Indians and paragraph 3 about RCB. Embed all three
together and the single vector is an average of three teams — close to nothing.
Embed them separately and each vector actually represents one team.

**3. Computational efficiency.** Smaller pieces need less memory to process and
can be handled in parallel.

The requirement that follows: chunks should break on **meaning**, not at
arbitrary offsets. A cut through the middle of an explanation produces two
chunks that each answer nothing.

> Chunking is *not* the same as the per-page or per-row split a document loader
> produces — that is the source's natural unit, not a deliberate decision. See
> [02-document-processing/01-document-loading](../02-document-processing/01-document-loading/).

## The four splitting strategies

| Strategy | Splits on | Topic |
| --- | --- | --- |
| Length-based | A character or token count | [01-fixed-size-chunking](01-fixed-size-chunking/) |
| Text-structure-based | Paragraphs → lines → words → characters | [02-recursive-chunking](02-recursive-chunking/) |
| Document-structure-based | Format constructs (`class`, `def`, Markdown headings) | [05-chunking-strategies](05-chunking-strategies/) |
| Semantic-meaning-based | Where the meaning changes, measured with embeddings | [05-chunking-strategies](05-chunking-strategies/) |

Two parameters cut across all of them: [chunk size](03-chunk-size/) and
[chunk overlap](04-chunk-overlap/).

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Fixed-Size Chunking](01-fixed-size-chunking/) | Character and token based splitting; why it is the baseline and where it breaks semantic units. | `studied` |
| 02 | [Recursive Chunking](02-recursive-chunking/) | Splitting on a hierarchy of separators so paragraphs and sentences survive where possible. | `studied` |
| 03 | [Chunk Size](03-chunk-size/) | The trade-off between retrieval precision (small chunks) and context sufficiency (large chunks). | `studied` |
| 04 | [Chunk Overlap](04-chunk-overlap/) | Why overlap exists, what it costs in storage and duplication, and how much is actually useful. | `studied` |
| 05 | [Chunking Strategies](05-chunking-strategies/) | Semantic, structure-aware, sentence-window and document-specific strategies compared on the same corpus. | `studied` |

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
