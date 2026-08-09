# RAG Learning Lab

A working repository for learning Retrieval-Augmented Generation properly:
theory in my own words, an implementation of every concept, and a small
experiment wherever a claim can actually be measured.

This is a learning journey in progress, not a tutorial and not a finished
framework. Most folders are currently empty scaffolding - that is intentional.
Files get filled in as I study each topic, and nothing here is written ahead of
the learning.

---

## Contents

- [What this repository is](#what-this-repository-is)
- [Why I am learning RAG](#why-i-am-learning-rag)
- [Learning philosophy](#learning-philosophy)
- [How the repository is organized](#how-the-repository-is-organized)
- [Roadmap](#roadmap)
- [Current progress](#current-progress)
- [Experiments](#experiments)
- [Technologies](#technologies)
- [Resources](#resources)
- [Getting started](#getting-started)

---

## What this repository is

A structured lab where each RAG concept gets one self-contained folder
containing:

```
<nn>-<topic>/
├── README.md          what the topic is and its status
├── notes.md           my understanding, written in my own words
├── implementation.py  from-scratch version, library version, comparison
├── experiment.py|md   the small test that checks the claim
└── resources.md       what I actually studied
```

Theory and code stay next to each other on purpose. Reading about MMR and
implementing MMR are different kinds of understanding, and I want both in the
same place.

## Why I am learning RAG

Retrieval is the part of an LLM system that determines whether the answer can
be correct at all. A model cannot reason over context it never received. Most
of the difficulty in a real RAG system is not the model - it is chunking,
retrieval quality, ranking, context construction and evaluation. Those are
engineering problems, and they are learnable by measurement.

## Learning philosophy

1. **Build it before importing it.** Cosine similarity, BM25, RRF and nDCG are
   short functions. Writing them once makes the library version legible.
2. **Then use the real tool.** After the from-scratch version, do it the way
   production code would, and compare the two.
3. **Measure instead of assuming.** "Semantic chunking is better" is a
   hypothesis. It goes in `experiments/` with a metric attached.
4. **Write it down in my own words.** Copied notes are not understanding.
5. **Keep the failures.** Wrong assumptions and failed experiments are recorded
   in [MISTAKES_AND_LESSONS.md](MISTAKES_AND_LESSONS.md), not deleted.
6. **No filler.** A file exists because it has a purpose.

## How the repository is organized

| Folder | Track | Purpose |
| --- | --- | --- |
| [`01-foundations/`](01-foundations/) | Course Content | What RAG is, why it exists, and how the pieces fit together before any code. |
| [`02-document-processing/`](02-document-processing/) | Course Content | Getting raw sources into clean, structured text with usable metadata. Garbage in, garbage retrieved. |
| [`03-chunking/`](03-chunking/) | Course Content | Splitting documents into retrievable units. The single highest-leverage knob in a basic RAG system. |
| [`04-embeddings/`](04-embeddings/) | Course Content | Turning text into vectors, and understanding what 'similar' actually means in that space. |
| [`05-vector-search/`](05-vector-search/) | Course Content | Storing vectors and finding nearest neighbours at speed. |
| [`06-retrieval/`](06-retrieval/) | Course Content | Turning a query into a set of context chunks that are actually worth putting in the prompt. |
| [`07-advanced-retrieval/`](07-advanced-retrieval/) | Advanced Topics | Lexical, dense and hybrid retrieval, plus the index structures and rerankers that make them fast and accurate. |
| [`08-query-transformation/`](08-query-transformation/) | Advanced Topics | Fixing retrieval on the input side: the user's question is often not a good search query. |
| [`09-context-engineering/`](09-context-engineering/) | Advanced Topics | What actually reaches the model: how much, in what order, and with what surrounding information. |
| [`10-advanced-rag/`](10-advanced-rag/) | Research Topics | Control-flow research patterns: systems that decide whether, when and how many times to retrieve. |
| [`11-agentic-rag/`](11-agentic-rag/) | Research Topics | Retrieval as a tool an agent plans with, reflects on and repeats - rather than a fixed pipeline stage. |
| [`12-graphrag/`](12-graphrag/) | Research Topics | Building a knowledge graph from a corpus and retrieving over structure instead of (or alongside) vectors. |
| [`13-multimodal-rag/`](13-multimodal-rag/) | Advanced Topics | Retrieval over documents that are not plain text: images, layout, tables, charts, audio and video. |
| [`14-rag-evaluation/`](14-rag-evaluation/) | Production Topics | Measuring whether a change actually improved anything. Without this, every other section is guesswork. |
| [`15-rag-observability/`](15-rag-observability/) | Production Topics | Seeing what a running RAG system actually did: what was retrieved, what was prompted, what it cost. |
| [`16-rag-security/`](16-rag-security/) | Production Topics | RAG puts untrusted text into the prompt and private data into the index. Both are attack surfaces. Everything here is for defending my own systems. |
| [`17-production-rag/`](17-production-rag/) | Production Topics | Everything between a working notebook and a system that stays fast, cheap and correct under real traffic. |
| [`18-specialized-rag/`](18-specialized-rag/) | Production Topics | RAG variants where the retrieval target is not a pile of documents. |
| [`experiments/`](experiments/) | - | Cross-topic experiments that compare several concepts |
| [`_templates/`](_templates/) | - | The topic template + a script to add new topics |

Root documents:

| File | Purpose |
| --- | --- |
| [ROADMAP.md](ROADMAP.md) | Full learning progression, split by track |
| [PROGRESS.md](PROGRESS.md) | Per-topic checklist: studied / implemented / experimented / documented |
| [LEARNING_LOG.md](LEARNING_LOG.md) | Chronological log of what I did each session |
| [DECISIONS.md](DECISIONS.md) | Engineering decisions and the evidence behind them |
| [MISTAKES_AND_LESSONS.md](MISTAKES_AND_LESSONS.md) | Misunderstandings, failed experiments, lessons |
| [RESOURCES.md](RESOURCES.md) | Courses, docs, videos, blogs, tools |
| [PAPERS.md](PAPERS.md) | Reading list with status and notes |

Numbering shows the intended order. It is a suggested path, not a hard
dependency chain.

## Roadmap

Four tracks, kept deliberately separate - see [ROADMAP.md](ROADMAP.md):

1. **Course content** (`01`-`06`) - the fundamentals I am studying now.
2. **Advanced topics** (`07`-`09`, `13`) - retrieval, query and context techniques.
3. **Research topics** (`10`-`12`) - paper-driven patterns: Self-RAG, CRAG, GraphRAG, agentic RAG.
4. **Production topics** (`14`-`18`) - evaluation, observability, security, scaling, specialized RAG.

## Current progress

Just started. Structure created; topics not yet filled in.
Live status: [PROGRESS.md](PROGRESS.md).

## Experiments

Comparisons that span multiple topics live in [experiments/](experiments/) -
chunking strategies, embedding models, BM25 vs vector, reranking impact, and so
on. Each has a stated question, a fixed setup, a metric, and recorded results.

## Technologies

Python is the implementation language. Libraries are used where they earn their
place, not by default:

- **Core** - numpy, pandas for the from-scratch implementations
- **Frameworks** - LangChain, LangGraph (agentic/graph-based flows)
- **Models** - Hugging Face, sentence-transformers, PyTorch
- **Vector stores** - ChromaDB, FAISS
- **Evaluation** - RAGAS, DeepEval
- **Observability** - LangSmith

See [requirements.txt](requirements.txt).

## Getting started

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate    # macOS / Linux

pip install -r requirements.txt

copy .env.example .env         # then fill in the keys that are actually needed
```

`.env` is git-ignored and must never be committed.

---

*If something in here is wrong, it is wrong because I have not learned it yet -
corrections in the notes are part of the record.*
