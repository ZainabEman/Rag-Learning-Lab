# Experiments

Experiments that compare **more than one topic**. Anything that belongs to a
single concept lives in that concept's own folder instead.

Rules I am holding myself to:

- Write the hypothesis **before** running the experiment.
- Change one variable at a time; hold everything else constant.
- Small, reproducible datasets with a fixed seed - not big corpora.
- Record the result even when it contradicts the hypothesis, especially then.
- A result without the config that produced it is worthless.

## Layout

```
experiments/<nn>-<name>/
├── README.md        question, setup, results table, conclusion
├── experiment.py    the runnable comparison
├── data/            small inputs (large files stay untracked)
└── results/         raw output of each run
```

## Index

| # | Experiment | Question | Status |
| --- | --- | --- | --- |
| 01 | [Chunking Comparison](01-chunking-comparison/) | Does chunk size / strategy change retrieval quality on a fixed corpus and query set? | `not started` |
| 02 | [Embedding Model Comparison](02-embedding-model-comparison/) | Is a larger or hosted embedding model actually better here, and is it worth the cost and latency? | `not started` |
| 03 | [BM25 vs Vector Search](03-bm25-vs-vector/) | Which query types does lexical retrieval win, and which does dense retrieval win? | `not started` |
| 04 | [Hybrid vs Dense](04-hybrid-vs-dense/) | Does hybrid search beat dense-only, and by how much, on the same evaluation set? | `not started` |
| 05 | [Reranking Impact](05-reranking-impact/) | How much does a cross-encoder reranker improve top-k quality, and what does it cost in latency? | `not started` |
| 06 | [Query Rewriting Impact](06-query-rewriting-impact/) | Does rewriting the query before retrieval measurably improve recall? | `not started` |
| 07 | [HyDE vs Standard Retrieval](07-hyde-vs-standard-retrieval/) | When does embedding a hypothetical answer beat embedding the question? | `not started` |
| 08 | [Contextual Retrieval](08-contextual-retrieval/) | Does prepending chunk context before embedding reduce retrieval failures? | `not started` |
| 09 | [RAG Architecture Comparison](09-rag-architecture-comparison/) | Naive vs advanced vs modular pipeline on the same task: quality, latency and cost. | `not started` |
| 10 | [Agentic vs Standard RAG](10-agentic-vs-standard-rag/) | Does an agentic loop beat a single-pass pipeline enough to justify the extra calls? | `not started` |
