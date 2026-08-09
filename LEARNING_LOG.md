# Learning Log

Chronological record of what I actually did, newest entry at the top.
One entry per study session. Short is fine - honest is the point.

Copy this template for each entry:

```markdown
## YYYY-MM-DD - Topic

### Learned

### Implemented

### Experimented

### Surprised me

### Still unclear

### Next step
```

---

## 2026-08-10 - RAG theory + document loaders

Wrote up the first two videos of the course from my notebook notes and the
transcripts.

### Learned

- **Parametric knowledge** — an LLM stores everything it knows in its weights,
  frozen at the end of pre-training. Prompting is the only way to access it.
- The **three failure modes** of that setup: private data, knowledge cutoff,
  hallucination. All three are the same underlying problem — the model cannot
  see the information it needs at generation time.
- **Fine-tuning** as the older fix: SFT, continued pre-training, RLHF,
  LoRA/QLoRA; the four-step SFT process; and why it fails for knowledge that
  changes (retrain on every update, and removing knowledge is far harder than
  adding it).
- **In-context learning** as an emergent property that appeared at GPT-3 scale,
  and that RAG is the same delivery channel carrying facts instead of examples.
- The **four stages**: indexing (ingest → chunk → embed → store), retrieval,
  augmentation, generation.
- **Document loaders**: the `Document` object (`page_content` + `metadata`),
  that every loader returns a *list*, per-loader splitting policies (file /
  page / row / URL), `DirectoryLoader` with `glob` + `loader_cls`, and
  `load()` vs `lazy_load()`.

### Implemented

- [01-foundations/03-rag-architecture/implementation.py](01-foundations/03-rag-architecture/implementation.py)
  — all four stages from scratch, standard library only, with a bag-of-words
  vector standing in for a real embedding model.
- [02-document-processing/01-document-loading/implementation.py](02-document-processing/01-document-loading/implementation.py)
  — a `Document` dataclass and three loaders written by hand, then the
  LangChain equivalents, plus a measured `load()` vs `lazy_load()` comparison.

### Experimented

- Ran the from-scratch pipeline on a synthetic lecture transcript. It correctly
  retrieved the two gradient-descent chunks and skipped the OLS and multiple
  regression ones — the same example used in the video.
- Measured eager vs lazy loading over 20,000 CSV rows: **8297 KB vs 44 KB**
  peak memory (~187×). Same documents, same work.

### Surprised me

- The query said "optimi**z**ation" and the document said "optimi**s**ation".
  Bag-of-words scored those as completely unrelated tokens — retrieval only
  worked because "gradient", "descent" and "step" happened to overlap. That is
  the argument for dense embeddings, and I hit it by accident rather than
  reading it.
- Fixed-size chunking visibly cut mid-sentence: chunk 3 begins "conditional on
  the other features", a fragment of the *previous* paragraph, and it still won
  the retrieval. Context can be relevant and malformed at the same time.
- My first lazy-loading demo showed no memory saving at all, because the
  generator wrapped an *eager* reader. Laziness has to go all the way down to
  the read or it is decoration.

### Still unclear

- What decides `k` (how many chunks) in practice?
- Where reranking sits — inside retrieval, or as a fifth stage?
- If retrieved context contradicts the model's parametric knowledge, which wins?
- How to detect a bad load (empty or garbled text) before it poisons the index.

### Next step

- Read the GPT-3 paper (at minimum the abstract) — see [PAPERS.md](PAPERS.md).
- Paste the actual course URLs into [RESOURCES.md](RESOURCES.md); they are
  currently TODO placeholders.
- Next video: text splitters → fills in [03-chunking](03-chunking/).

---

## YYYY-MM-DD - Repository setup

### Learned

- (nothing technical yet - set up the lab structure)

### Implemented

- Created the RAG Learning Lab structure: 18 sections, topic template, experiments folder.

### Experimented

- n/a

### Surprised me

- n/a

### Still unclear

- n/a

### Next step

- Start `01-foundations/01-what-is-rag/` - write notes.md before writing any code.
