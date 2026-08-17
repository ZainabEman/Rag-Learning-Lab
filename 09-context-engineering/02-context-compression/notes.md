# Context Compression

> Status: `studied` (self-study, outside the course) | Section: [Context Engineering](../README.md)

## What is it?

Shrinking retrieved context before it reaches the prompt, keeping only what is
relevant to the query.

## Why it matters

Retrieved chunks are padded with irrelevant text. That padding costs tokens,
costs money, adds latency, and measurably degrades answer quality by diluting
the signal.

## How it works

| Approach | Method | Trade-off |
| --- | --- | --- |
| **Extractive** | Keep only the relevant sentences | Fast, cheap, safe — nothing invented |
| **Abstractive** | LLM rewrites/summarises the chunk | Higher compression, risks losing detail |
| **Filtering** | Drop whole chunks below a relevance threshold | Cheapest; coarse |

## Simple example

```
retrieved (180 tokens):
  "The Grand Canyon is a famous natural site. Photosynthesis is how plants
   convert light into energy. Many tourists visit every year..."

query: "what is photosynthesis?"

compressed (12 tokens):
  "Photosynthesis is how plants convert light into energy."
```

## Remember

- Compression happens **after** retrieval — it cannot recover a missed document.
- Abstractive compression can drop the one number the user needed. Prefer
  extractive when facts matter.
- The LLM-based version costs a call per document; weigh that against the tokens
  saved.
- Better chunking reduces how much compression you need in the first place.

## Related

- [06-retrieval/03-contextual-compression](../../06-retrieval/03-contextual-compression/) — the LangChain implementation
- [06-token-budgeting](../06-token-budgeting/)
