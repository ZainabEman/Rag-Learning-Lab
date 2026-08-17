# Resources - Chunk Size

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| Text Splitters (LangChain playlist, video 3) | Course video | *TODO - paste the video URL* | Primary source: chunk size as the parameter that selects the structural split level. |
| ChunkViz | Tool | https://chunkviz.up.railway.app/ | Sweeping chunk size on a Markdown document and watching 64 meaningless chunks collapse to the 4 real sections. |

> LangChain moved its documentation to `docs.langchain.com` and its API
> reference to `reference.langchain.com` during 2025-2026. Older links under
> `python.langchain.com` now redirect. Everything below was checked against
> `langchain_text_splitters` **1.1.2** directly, which is the authority when the
> docs and the installed package disagree.

## Best explanation I found

Nothing textual - the sweep did it. Seeing the same text split at word, then
sentence, then paragraph level purely because the budget grew reframed the
parameter from "how big" to "which unit".

## Explanations that did NOT help

Blog posts recommending a specific chunk size as a universal default. The right
value depends on the corpus and on what the retriever gets asked, and no source
that skips measurement can know either.

<!-- Add sources here as I find them. -->
