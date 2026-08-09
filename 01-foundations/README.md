# 01 Foundations

> Track: **COURSE CONTENT** | [Back to repository root](../README.md)

What RAG is, why it exists, and how the pieces fit together before any code.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [What is RAG](01-what-is-rag/) | Define retrieval-augmented generation precisely: retrieve, augment, generate - and what each stage is responsible for. | `studied` |
| 02 | [Why RAG](02-why-rag/) | The failure modes RAG addresses: stale knowledge, hallucination, private data, citation requirements, cost of retraining. | `studied` |
| 03 | [RAG Architecture](03-rag-architecture/) | The two pipelines - offline ingestion (load, chunk, embed, index) and online query (embed, retrieve, rerank, prompt, generate). | `studied` |
| 04 | [RAG vs Fine-tuning](04-rag-vs-finetuning/) | When to add knowledge at inference time vs bake behaviour into weights, and when both are used together. | `studied` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 01-foundations <next-number>-<topic-slug> "Topic Title"
```
