# Resources - What is RAG

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| RAG: why, what and how (LangChain playlist, video 1 of 2) | Course video | *TODO — paste the video URL* | The whole theory: parametric knowledge, the three failure modes, in-context learning, and the four RAG stages. Primary source for this topic. |
| Language Models are Few-Shot Learners (GPT-3) | Paper | https://arxiv.org/abs/2005.14165 | Where in-context learning was first documented. The abstract alone makes the argument: fine-tuning needs 10k–1M labelled rows, humans need a few examples. |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Paper | https://arxiv.org/abs/2005.11401 | The original RAG paper — the name and the architecture come from here. Not yet read. |

## Best explanation I found

The framing that made RAG click was the **progression**, not the definition:
prompting → fine-tuning → in-context learning → RAG. Presented as a definition,
"retrieve then generate" sounds arbitrary. Presented as the last step of a chain
where each technique fixes the previous one's cost, it becomes the obvious move.

The second useful framing: RAG is the marriage of **information retrieval** (an
old, well-studied field) and **text generation** (new). Neither half is novel.

## Explanations that did NOT help

Definitions that start with "RAG combines retrieval with generation to improve
LLM outputs" — technically correct and completely uninformative. They skip the
question of *why the model needed help in the first place*, which is where all
the actual understanding is.

<!-- Add sources here as I find them. -->
