#  LangSmith Examples

> Track: **PRODUCTION TOPICS** | [Back to repository root](../../README.md)

Concrete tracing/eval setups using LangSmith. Separated from the concepts so the ideas stay portable.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [LangSmith Setup](01-langsmith-setup/) | Environment variables, projects and getting a first trace to appear. Never commit the API key. | `not started` |
| 02 | [Tracing a RAG Pipeline](02-tracing-a-rag-pipeline/) | Annotating retrieval and generation steps so a trace is readable. | `not started` |
| 03 | [Datasets and Experiments](03-datasets-and-experiments/) | Running an evaluation dataset and comparing two pipeline versions. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 15-rag-observability/langsmith <next-number>-<topic-slug> "Topic Title"
```
