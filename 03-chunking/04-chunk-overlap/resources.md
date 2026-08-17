# Resources - Chunk Overlap

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| Text Splitters (LangChain playlist, video 3) | Course video | *TODO - paste the video URL* | Primary source: what overlap is, why it retains context across a cut, and the 10-20% rule of thumb for RAG. |
| ChunkViz | Tool | https://chunkviz.up.railway.app/ | The overlap slider makes the shared band visible directly. |

> LangChain moved its documentation to `docs.langchain.com` and its API
> reference to `reference.langchain.com` during 2025-2026. Older links under
> `python.langchain.com` now redirect. Everything below was checked against
> `langchain_text_splitters` **1.1.2** directly, which is the authority when the
> docs and the installed package disagree.

## Best explanation I found

The framing that overlap is a **patch for a bad cut**, not a feature. It follows
that the better the splitting strategy, the less overlap is needed - which is
not how most material presents it.

## Explanations that did NOT help

Anything giving an overlap number without relating it to chunk size. Overlap
only means something as a percentage, because chunk count depends on
`chunk_size - chunk_overlap`.

<!-- Add sources here as I find them. -->
