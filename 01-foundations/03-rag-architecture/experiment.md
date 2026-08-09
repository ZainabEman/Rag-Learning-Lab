# Experiment - RAG Architecture

The runnable version lives in
[implementation.py](implementation.py) — it builds the whole pipeline, so
"the experiment" here is what running it revealed and what to vary next.

## Question

Does a four-stage RAG pipeline actually select the right context, and what does
it get wrong when it does not?

## What I compared

Ran the from-scratch pipeline on a synthetic linear-regression lecture
transcript (4 paragraphs → 7 chunks of 40 words with 10 words of overlap),
querying *"how do we perform the optimization step in gradient descent?"* and
printing the similarity of **every** chunk, not just the winners.

## Observations

| Chunk | Topic | Score |
| --- | --- | --- |
| 0 | OLS / normal equation | 0.0913 |
| 1 | Matrix inversion cost | 0.0845 |
| 2 | Multiple linear regression | 0.2539 |
| **3** | **Gradient descent intro + optimisation step** | **0.4297** |
| **4** | **The optimisation step in detail** | **0.3627** |
| 5 | Learning rate | 0.3227 |
| 6 | Learning rate too small | 0.0707 |

Retrieval selected chunks 3 and 4 — the correct ones, and the same result the
course example describes.

Three things the numbers made visible that prose did not:

1. **The scores are close.** Chunk 5 (0.3227) is nearly as high as chunk 4
   (0.3627) despite being about learning rate selection rather than the
   optimisation step. A slightly different query would reorder them. Retrieval
   is a ranking over near-ties, not a clean separation.
2. **Similarity search always returns k results.** Even chunk 6, at 0.07, is
   "retrievable" — nothing in the mechanism can say "no chunk answers this".
3. **The winning chunk was malformed.** Chunk 3 opens with "conditional on the
   other features", a fragment of the previous paragraph.

## Conclusion

The architecture works, and its two weakest joints are visible in a 200-line
implementation: chunk boundaries are arbitrary, and lexical matching is
brittle. Both have dedicated sections later ([03-chunking](../../03-chunking/),
[04-embeddings](../../04-embeddings/)), and now I know *why* those sections
exist rather than being told.

## What would make this measurable?

Currently there is one query and no ground truth, so "correct" is my judgement.
To turn this into a real experiment I would need:

- a set of queries with the relevant chunk labelled for each
- a metric (recall@k, MRR) — [14-rag-evaluation](../../14-rag-evaluation/)
- then vary one thing at a time:
  - `CHUNK_SIZE_WORDS` and `CHUNK_OVERLAP_WORDS` → which chunks win?
  - `TOP_K` → how much noise enters the prompt?
  - bag-of-words vs a real embedding model → how much does spelling and
    paraphrase robustness improve?

The last one is the experiment worth running first, and it belongs in
[experiments/02-embedding-model-comparison](../../experiments/02-embedding-model-comparison/).
