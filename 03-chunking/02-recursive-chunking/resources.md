# Resources - Recursive Chunking

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| Text Splitters (LangChain playlist, video 3) | Course video | *TODO - paste the video URL* | Primary source: the separator hierarchy and the hand-traced worked example at chunk sizes 10, 25 and 50. |
| Text splitter integrations | Docs | https://docs.langchain.com/oss/python/integrations/splitters | Confirms `RecursiveCharacterTextSplitter` as the recommended default: "a solid balance between keeping context intact and managing chunk size". |
| ChunkViz | Tool | https://chunkviz.up.railway.app/ | Shows the split level changing as chunk size grows. |

> LangChain moved its documentation to `docs.langchain.com` and its API
> reference to `reference.langchain.com` during 2025-2026. Older links under
> `python.langchain.com` now redirect. Everything below was checked against
> `langchain_text_splitters` **1.1.2** directly, which is the authority when the
> docs and the installed package disagree.

## Best explanation I found

The hand-traced example. Following one short text through paragraph -> line ->
word splitting and then back up through the merge step is what turned this from
"a splitter that works better" into an algorithm I could re-implement. Writing
it from scratch and getting byte-identical output to the library confirmed it.

## Explanations that did NOT help

Descriptions that stop at "it tries separators in order". They leave out the
merge step, which is half the algorithm - without it, a small chunk size would
return one word per chunk and the outputs make no sense.

<!-- Add sources here as I find them. -->
