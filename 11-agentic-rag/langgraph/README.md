#  LangGraph Implementations

> Track: **RESEARCH TOPICS** | [Back to repository root](../../README.md)

Graph-based implementations of the agentic patterns above. Kept separate so the concept and the framework do not get confused with each other.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [LangGraph Basics](01-langgraph-basics/) | State, nodes, edges, conditional edges and checkpointing - the minimum needed to build a RAG graph. | `not started` |
| 02 | [RAG as a Graph](02-rag-graph/) | Rebuilding a linear RAG pipeline as an explicit graph, then adding a grading branch. | `not started` |
| 03 | [Self-Corrective RAG Graph](03-self-corrective-graph/) | CRAG/Self-RAG style loops with cycles, retry limits and fallbacks. | `not started` |
| 04 | [Human in the Loop](04-human-in-the-loop/) | Interrupts, approval steps and state inspection during a retrieval run. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 11-agentic-rag/langgraph <next-number>-<topic-slug> "Topic Title"
```
