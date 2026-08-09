# Resources - RAG Architecture

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| RAG: why, what and how (LangChain playlist, video 1 of 2) | Course video | *TODO - paste the video URL* | Primary source: indexing / retrieval / augmentation / generation, and the four sub-steps of indexing. |
| LangChain document loaders | Docs | https://python.langchain.com/docs/integrations/document_loaders/ | Indexing step 1 in practice. |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Paper | https://arxiv.org/abs/2005.11401 | The architecture's origin. Not yet read. |

## Best explanation I found

Splitting the pipeline into **offline** and **online** halves. Indexing is paid
once; retrieval, augmentation and generation are paid per query. Almost every
confusion about "where does X happen" resolves once that line is drawn.

The retrieval example was the other useful one: a two-hour lecture transcript,
a question about gradient descent, and the job being to return the two relevant
passages rather than the whole transcript.

## Explanations that did NOT help

Architecture diagrams that show a single linear flow from documents to answer.
They hide the fact that the left half runs at a completely different time from
the right half, which is the most important structural fact about RAG.

<!-- Add sources here as I find them. -->
