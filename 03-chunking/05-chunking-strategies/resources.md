# Resources - Chunking Strategies

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| Text Splitters (LangChain playlist, video 3) | Course video | *TODO - paste the video URL* | Primary source: the four-strategy taxonomy, `from_language`, and semantic chunking with its threshold types. |
| Text splitter integrations | Docs | https://docs.langchain.com/oss/python/integrations/splitters | Current list of splitter classes including the code, Markdown and HTML splitters. |
| ChunkViz | Tool | https://chunkviz.up.railway.app/ | Has per-language modes - useful for seeing Markdown and Python splitting without writing code. |

> LangChain moved its documentation to `docs.langchain.com` and its API
> reference to `reference.langchain.com` during 2025-2026. Older links under
> `python.langchain.com` now redirect. Everything below was checked against
> `langchain_text_splitters` **1.1.2** directly, which is the authority when the
> docs and the installed package disagree.

## Best explanation I found

The realisation that strategy 3 is not a new algorithm. Printing the separator
lists side by side - generic `['\n\n', '\n', ' ', '']` versus Python
`['\nclass ', '\ndef ', '\n\tdef ', '\n\n', '\n', ' ', '']` - shows the language
version is the generic one with format-specific entries prepended.

The motivating example for semantic chunking was the other good one: a single
paragraph covering both agriculture and the IPL. Structurally one paragraph, so
no structural splitter can ever separate them.

## Explanations that did NOT help

Content presenting semantic chunking as the obvious next step. It is
experimental, costs an embedding call per sentence, and on the example tested it
still put a sentence in the wrong chunk.

<!-- Add sources here as I find them. -->
