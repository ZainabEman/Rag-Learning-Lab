# 12 GraphRAG

> Track: **RESEARCH TOPICS** | [Back to repository root](../README.md)

Building a knowledge graph from a corpus and retrieving over structure instead of (or alongside) vectors.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Knowledge Graphs](01-knowledge-graphs/) | Entities, relations, triples and schemas; what a graph represents that a vector index cannot. | `not started` |
| 02 | [Entity Extraction](02-entity-extraction/) | Extracting and normalising entities from chunks; handling aliases and duplicates. | `not started` |
| 03 | [Relationship Extraction](03-relationship-extraction/) | Extracting typed relations between entities with evidence pointers back to source chunks. | `not started` |
| 04 | [Graph Construction](04-graph-construction/) | Assembling extractions into a queryable graph; deduplication and merge rules. | `not started` |
| 05 | [Community Detection](05-community-detection/) | Clustering the graph (e.g. Leiden) into communities at multiple levels. | `not started` |
| 06 | [Community Summaries](06-community-summaries/) | Generating hierarchical summaries per community for global questions. | `not started` |
| 07 | [Local Search](07-local-search/) | Entity-anchored retrieval over neighbourhoods for specific questions. | `not started` |
| 08 | [Global Search](08-global-search/) | Map-reduce over community summaries for corpus-wide questions. | `not started` |
| 09 | [Graph Retrieval](09-graph-retrieval/) | Traversal-based retrieval: paths, neighbourhoods and subgraphs as context. | `not started` |
| 10 | [Vector + Graph Retrieval](10-vector-plus-graph-retrieval/) | Vector search to find entry points, graph traversal to expand context. | `not started` |
| 11 | [Multi-Hop Retrieval](11-multi-hop-retrieval/) | Questions whose answer requires chaining facts across documents. | `not started` |
| 12 | [Agentic GraphRAG](12-agentic-graphrag/) | An agent choosing between local, global and traversal strategies per query. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 12-graphrag <next-number>-<topic-slug> "Topic Title"
```
