# 02 Document Processing

> Track: **COURSE CONTENT** | [Back to repository root](../README.md)

Getting raw sources into clean, structured text with usable metadata. Garbage in, garbage retrieved.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Document Loading](01-document-loading/) | Loading PDF, HTML, DOCX, Markdown, CSV and plain text into a common document representation. | `studied` |
| 02 | [Document Parsing](02-document-parsing/) | Extracting structure - headings, sections, tables, code blocks - not just a flat string of characters. | `not started` |
| 03 | [Metadata](03-metadata/) | What metadata to attach at ingestion (source, page, section, timestamp, permissions) and how it is used later for filtering and citation. | `overview only` |
| 04 | [Document Cleaning](04-document-cleaning/) | Removing headers/footers, boilerplate, broken whitespace and artifacts; measuring what cleaning does to retrieval quality. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 02-document-processing <next-number>-<topic-slug> "Topic Title"
```
