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

## 2026-08-18 - Self-studied topics written up

Documented the RAG topics I'd already learned outside the course, so the repo
reflects what I actually know rather than only what the playlist covered.

### Learned

Written up as short reference notes (definition / why / how / example /
key points), not deep dives:

- **Embeddings** — semantic similarity, cosine similarity.
- **Advanced retrieval** — BM25, sparse vs dense, hybrid search, RRF,
  cross-encoder reranking, reranking basics.
- **Query transformation** — rewriting, expansion, decomposition, HyDE,
  step-back.
- **Context engineering** — contextual retrieval, compression, deduplication,
  ordering, lost-in-the-middle, parent-document, small-to-big, hierarchical.

### Implemented

- [BM25](07-advanced-retrieval/02-bm25/implementation.py) — the formula from
  scratch, showing IDF and TF saturation.
- [RRF](07-advanced-retrieval/05-reciprocal-rank-fusion/implementation.py) —
  rank fusion in ~10 lines.

### Ideas that connected things

- **Sparse and dense fail in opposite directions**, which is the entire case for
  hybrid search — and hybrid search needs RRF because BM25 scores and cosine
  scores are not comparable numbers.
- **Lost-in-the-middle is the reason** reranking, compression and ordering all
  exist. They are three answers to one finding.
- **Small-to-big is the general pattern** behind parent-document retrieval,
  sentence-window and summary indexes: match on a small unit, read a large one.
- TF saturation is what separates BM25 from naive TF-IDF — 50 occurrences are
  worth barely more than 10.

### Still unclear

- Whether hybrid search beats dense-only on *my* data — untested.
- Good default for reranking depth (retrieve 20? 50?).

### Next step

- These are notes from reading, not from building. Most are marked studied +
  documented but **not implemented or experimented** — the experiments in
  [experiments/](experiments/) are where they'd get tested.

---

## 2026-08-18 - Vector stores, retrievers, and a working RAG system

Three videos: the last two RAG components, then the end-to-end build.

### Learned

- **Vector stores** — why relational DBs can't do this (no notion of similarity),
  the four features (storage, similarity search, indexing, CRUD), and that
  `vector store + database features = vector database`. FAISS is a store;
  Milvus/Qdrant/Weaviate/Pinecone are databases; Chroma sits in between.
- **Indexing** — cluster the vectors, compare against centroids first, then only
  inside the winning cluster. 1M comparisons becomes ~100k.
- **Retrievers** — query in, `list[Document]` out. They're runnables, so they
  compose into chains. Categorised by data source (Wikipedia, vector store,
  arXiv) or by search strategy (MMR, multi-query, compression).
- **MMR** — relevant *and* diverse, so the top-k isn't three copies of one fact.
  `lambda_mult`: 1.0 = pure relevance, 0.0 = max diversity.
- **Multi-query retriever** — an LLM turns one ambiguous query into several, then
  merges the results.
- **Contextual compression** — an LLM trims each retrieved document down to the
  part that answers the query.
- **End-to-end RAG** — YouTube Chat: transcript → chunks → FAISS → retriever →
  prompt → LLM, wired into one LCEL chain with `RunnableParallel` +
  `RunnablePassthrough` + `RunnableLambda`.

### Implemented

- [05-vector-search/01-vector-databases](05-vector-search/01-vector-databases/implementation.py)
  — a whole vector store from scratch in ~80 lines: storage, similarity search,
  metadata filtering, CRUD.
- [05-vector-search/05-vector-indexing](05-vector-search/05-vector-indexing/implementation.py)
  — cluster index vs brute force, measured.

### Experimented

- Cluster indexing over 10,000 vectors: **9.9× fewer comparisons**, and the
  exact nearest neighbour **100%** of the time.

### Surprised me

- My first indexing test showed only **35% recall**. The cause was my test data:
  uniformly random vectors have no cluster structure, so the index was
  meaningless. Regenerating the vectors with real clustering (which is what
  actual embeddings look like) took recall to 100% at the same speed-up. **An
  index is only as good as the structure in the data** — and a benchmark on
  unrealistic data can badly misjudge one.
- A retriever and `vector_store.similarity_search()` return the *same* result
  for plain search. The retriever only earns its place when the strategy changes
  or it needs to sit in a chain.
- `WikipediaRetriever` matches on keywords internally, not semantics.

### Still unclear

- When does Chroma stop being enough in practice?
- Does MMR measurably improve answers, or just make results look nicer?

### Next step

- Section 04-embeddings is still `overview only` — it is the one gap left in the
  indexing pipeline.
- Try the homework: rebuild the Chroma example with FAISS or Pinecone.

---

## 2026-08-16 - Text splitters

Third video of the course. Wrote up all five chunking topics and verified every
API claim against `langchain_text_splitters` 1.1.2 rather than trusting the
docs, which have just been migrated and are patchy.

### Learned

- **Why splitting exists**: three independent reasons — model input limits,
  better results on every downstream task (embedding, semantic search,
  summarisation), and lower compute/memory.
- **Length-based splitting** (`CharacterTextSplitter`): one counter, no
  judgement. Fast, and cuts mid-word.
- **Chunk overlap**: repeat a band of text between chunks so context survives
  the cut. 10–20% of chunk size is the rule of thumb for RAG.
- **Recursive splitting** (`RecursiveCharacterTextSplitter`): separators
  `["\n\n", "\n", " ", ""]` tried in order, recursing only where a piece is
  still too big, then merging small pieces back up. The default choice.
- **Document-structure splitting**: `from_language(Language.PYTHON)` etc. — the
  *same* algorithm with format-specific separators prepended.
- **Semantic splitting** (`SemanticChunker`, experimental): embed each sentence,
  compare consecutive pairs, break where similarity collapses. Threshold types:
  percentile, standard_deviation, interquartile, gradient.

### Implemented

- [01-fixed-size-chunking](03-chunking/01-fixed-size-chunking/implementation.py)
  — length splitter from scratch, then `CharacterTextSplitter` and its two
  surprises.
- [02-recursive-chunking](03-chunking/02-recursive-chunking/implementation.py)
  — the full recursive algorithm from scratch, including the merge step.
- [03-chunk-size](03-chunking/03-chunk-size/implementation.py) — a size sweep
  showing which structural level each value lands on.
- [04-chunk-overlap](03-chunking/04-chunk-overlap/implementation.py) — the seam,
  and the non-linear cost curve.
- [05-chunking-strategies](03-chunking/05-chunking-strategies/implementation.py)
  — three strategies side by side on prose, Python and Markdown.

### Experimented

- **My from-scratch recursive splitter produces byte-identical output to
  LangChain** at chunk sizes 10, 25 and 50 on the worked example. That is the
  strongest signal yet that I actually understand an algorithm rather than just
  its description.
- Chunk-size sweep: same text splits at word → line → paragraph level purely
  because the budget grew. Mid-word cuts: recursive 7 → 0 → 0; fixed-size
  19 → 8 → 4 → 2 → 1.
- Overlap cost curve: 10% overlap → 9% duplication; 50% → 73%; 90% → 654%.

### Surprised me

- `CharacterTextSplitter`'s **default separator is `"\n\n"`, not `""`**. Out of
  the box it is a paragraph splitter, not a fixed-size one.
- **`chunk_size` is not a hard cap.** A 300-character paragraph with no blank
  lines, split at `chunk_size=50`, came back as one 299-character chunk — with
  no warning at all. Other oversized merges *do* log a warning. The recursive
  splitter never has this problem because its list ends in `""`.
- **`Language.PYTHON` separators don't match indented methods.** They are
  `'\nclass '`, `'\ndef '`, `'\n\tdef '` — so a normal 4-space-indented class
  body gives output *identical* to the generic splitter. `from_language` only
  earns its keep on top-level definitions.
- The video's character counts for the worked example were slightly off (the
  last line is 12 characters, not 11; the paragraphs are 35 and 30, not 34 and
  28). Conclusions unchanged, but I used the measured values.

### Still unclear

- How to choose chunk size by measurement rather than by eyeballing a
  visualiser.
- Whether overlap actually improves retrieval or mostly inflates the index.
- Whether semantic chunking's weakness is the embedding model or the
  sentence-pair method itself.

### Next step

- Next video: vector stores / embeddings → fills in
  [04-embeddings](04-embeddings/) and [05-vector-search](05-vector-search/).
- Come back and implement `SemanticChunker` once embeddings are studied —
  deliberately skipped for now.

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
