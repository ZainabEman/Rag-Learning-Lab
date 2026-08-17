# Resources - Fixed-Size Chunking

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| Text Splitters (LangChain playlist, video 3) | Course video | *TODO - paste the video URL* | Primary source: length-based splitting, `CharacterTextSplitter`, and why it is fast but rarely used. |
| Text splitter integrations | Docs | https://docs.langchain.com/oss/python/integrations/splitters | Current catalogue of splitter classes and import paths. |
| ChunkViz | Tool | https://chunkviz.up.railway.app/ | The visualiser used in the lesson - paste text, pick a splitter, see the chunks coloured in. Fastest way to build intuition for chunk size and overlap. |

> LangChain moved its documentation to `docs.langchain.com` and its API
> reference to `reference.langchain.com` during 2025-2026. Older links under
> `python.langchain.com` now redirect. Everything below was checked against
> `langchain_text_splitters` **1.1.2** directly, which is the authority when the
> docs and the installed package disagree.

## Best explanation I found

Watching the chunk boundaries in the visualiser while dragging chunk size. The
disadvantage of length-based splitting stops being an abstract warning the
moment you see a chunk end in the middle of a word.

## Explanations that did NOT help

Material that presents `CharacterTextSplitter` as "the fixed-size splitter"
without mentioning that its default separator is `"\n\n"`. That single omission
makes its actual behaviour look like a bug.

<!-- Add sources here as I find them. -->
