# Resources - Why RAG

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| RAG: why, what and how (LangChain playlist, video 1 of 2) | Course video | *TODO - paste the video URL* | Primary source: the three situations where prompting an LLM's parametric knowledge fails. |

## Best explanation I found

Framing the three problems as symptoms of **one** cause - the model cannot see
the information it needs at generation time - rather than as three unrelated
limitations. That reduction is what makes a single fix (RAG) plausible.

The private-data example that stuck: a student watching a two-hour lecture asks
ChatGPT about a specific point in it. Obvious once stated, and it makes
"private data" concrete instead of abstract.

## Explanations that did NOT help

Discussions of hallucination that treat it as a bug to be patched. It follows
directly from optimising for the next likely token; nothing in that objective
rewards truth. Treating it as a defect rather than a property leads to expecting
fixes that cannot exist.

<!-- Add sources here as I find them. -->
