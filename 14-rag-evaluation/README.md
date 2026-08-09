# 14 RAG Evaluation

> Track: **PRODUCTION TOPICS** | [Back to repository root](../README.md)

Measuring whether a change actually improved anything. Without this, every other section is guesswork.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Evaluation Fundamentals](01-evaluation-fundamentals/) | Separating retrieval quality from generation quality; offline vs online; what a good test set looks like. | `not started` |
| 02 | [Retrieval Evaluation](02-retrieval-evaluation/) | Building a labelled query/relevant-document set and scoring a retriever against it. | `not started` |
| 03 | [Recall@K](03-recall-at-k/) | Implementing recall@k from the definition and reading it correctly. | `not started` |
| 04 | [Precision@K](04-precision-at-k/) | Implementing precision@k and understanding its tension with recall. | `not started` |
| 05 | [Hit Rate](05-hit-rate/) | The simplest 'did we get anything useful' metric and its blind spots. | `not started` |
| 06 | [MRR (Mean Reciprocal Rank)](06-mrr/) | Rank-sensitive scoring when there is one correct answer. | `not started` |
| 07 | [nDCG](07-ndcg/) | Graded relevance with positional discounting, implemented from the formula. | `not started` |
| 08 | [Context Precision](08-context-precision/) | How much of the retrieved context was actually relevant. | `not started` |
| 09 | [Context Recall](09-context-recall/) | How much of the needed evidence was retrieved at all. | `not started` |
| 10 | [Context Relevance](10-context-relevance/) | Judging query-context relevance and where judges disagree with humans. | `not started` |
| 11 | [Faithfulness](11-faithfulness/) | Whether every claim in the answer is supported by the retrieved context. | `not started` |
| 12 | [Answer Relevance](12-answer-relevance/) | Whether the answer addresses the question asked. | `not started` |
| 13 | [Groundedness](13-groundedness/) | Claim-level attribution to source spans. | `not started` |
| 14 | [Citation Correctness](14-citation-correctness/) | Do the citations point at text that supports the claim. | `not started` |
| 15 | [LLM-as-a-Judge](15-llm-as-a-judge/) | Designing judge prompts, calibrating them against human labels, and their biases. | `not started` |
| 16 | [RAGAS](16-ragas/) | Running the RAGAS metric suite on my own pipeline and interpreting the output. | `not started` |
| 17 | [DeepEval](17-deepeval/) | Test-style evaluation and assertions in a pytest workflow. | `not started` |
| 18 | [Evaluation Datasets](18-evaluation-datasets/) | Building small golden sets by hand and generating synthetic ones; keeping them honest. | `not started` |
| 19 | [Regression Testing](19-regression-testing/) | Locking in a baseline so a 'small improvement' cannot silently break retrieval. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 14-rag-evaluation <next-number>-<topic-slug> "Topic Title"
```
