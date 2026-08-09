# 11 Agentic RAG

> Track: **RESEARCH TOPICS** | [Back to repository root](../README.md)

Retrieval as a tool an agent plans with, reflects on and repeats - rather than a fixed pipeline stage.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Agentic Retrieval](01-agentic-retrieval/) | The shift from a fixed pipeline to an agent that decides what to retrieve next. | `not started` |
| 02 | [Query Planning](02-query-planning/) | Producing an explicit retrieval plan before executing any search. | `not started` |
| 03 | [Iterative Retrieval](03-iterative-retrieval/) | Search, read, refine loops with budgets and termination criteria. | `not started` |
| 04 | [Tool-Based Retrieval](04-tool-based-retrieval/) | Exposing multiple retrievers (vector, SQL, web, API) as tools and letting the model choose. | `not started` |
| 05 | [Document Navigation](05-document-navigation/) | Agents that traverse structure - table of contents, sections, links - instead of flat top-k. | `not started` |
| 06 | [Reflection](06-reflection/) | Self-evaluation of retrieved evidence and drafted answers before responding. | `not started` |
| 07 | [Agent State](07-agent-state/) | What must be tracked across steps: query history, seen documents, evidence, budget. | `not started` |
| 08 | [Agent Memory](08-agent-memory/) | Short-term vs long-term memory and how memory interacts with retrieval. | `not started` |
| 09 | [Multi-Agent RAG](09-multi-agent-rag/) | Splitting planner, retriever, critic and writer roles; where coordination cost exceeds the benefit. | `not started` |
| 10 | [Agentic RAG Evaluation](10-agentic-rag-evaluation/) | Evaluating trajectories, not just final answers: step count, tool choice, redundant retrievals, cost. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 11-agentic-rag <next-number>-<topic-slug> "Topic Title"
```
