# 04 Embeddings

> Track: **COURSE CONTENT** | [Back to repository root](../README.md)

Turning text into vectors, and understanding what 'similar' actually means in that space.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [What Are Embeddings](01-what-are-embeddings/) | Vectors as learned representations: dimensionality, what the axes do and do not mean, and how they are trained. | `studied` |
| 02 | [Semantic Similarity](02-semantic-similarity/) | What embedding similarity captures (topic, paraphrase) and what it misses (negation, numbers, entities). | `studied` |
| 03 | [Cosine Similarity](03-cosine-similarity/) | Cosine, dot product and Euclidean distance from scratch with numpy; why normalisation matters. | `studied` |
| 04 | [Embedding Models](04-embedding-models/) | Comparing local sentence-transformers vs hosted APIs on dimension, cost, latency, context length and domain fit. | `not started` |
| 05 | [Embedding Experiments](05-embedding-experiments/) | Probing embedding behaviour: negation, synonyms, numbers, code, multilingual text, chunk length effects. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 04-embeddings <next-number>-<topic-slug> "Topic Title"
```
