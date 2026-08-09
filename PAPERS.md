# Papers

Reading list. Status legend:

- `[ ] To read` - on the list
- `[~] Reading` - in progress
- `[x] Read` - read and summarised in the relevant topic's `notes.md`
- `[C] Implemented` - a minimal version exists in this repository

> The links below were added from memory when the repository was created.
> **Verify each link before relying on it**, and delete anything that does not
> resolve - a wrong citation is worse than no citation.

| Paper | Year | Topic | Link | Status | My notes |
| --- | --- | --- | --- | --- | --- |
| Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al.) | 2020 | The original RAG paper | https://arxiv.org/abs/2005.11401 | `[ ] To read` | [01-foundations](01-foundations/01-what-is-rag/notes.md) |
| Dense Passage Retrieval for Open-Domain QA (Karpukhin et al.) | 2020 | Dense retrieval | https://arxiv.org/abs/2004.04906 | `[ ] To read` | [07-advanced-retrieval](07-advanced-retrieval/03-sparse-vs-dense/notes.md) |
| ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction | 2020 | Late interaction | https://arxiv.org/abs/2004.12832 | `[ ] To read` | [07-advanced-retrieval](07-advanced-retrieval/11-colbert/notes.md) |
| ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction | 2021 | Late interaction | https://arxiv.org/abs/2112.01488 | `[ ] To read` | [07-advanced-retrieval](07-advanced-retrieval/11-colbert/notes.md) |
| Efficient and Robust ANN Search using HNSW Graphs (Malkov & Yashunin) | 2016 | ANN indexing | https://arxiv.org/abs/1603.09320 | `[ ] To read` | [07-advanced-retrieval](07-advanced-retrieval/07-hnsw/notes.md) |
| Precise Zero-Shot Dense Retrieval without Relevance Labels (HyDE) | 2022 | Query transformation | https://arxiv.org/abs/2212.10496 | `[ ] To read` | [08-query-transformation](08-query-transformation/06-hyde/notes.md) |
| Take a Step Back: Evoking Reasoning via Abstraction | 2023 | Query transformation | https://arxiv.org/abs/2310.06117 | `[ ] To read` | [08-query-transformation](08-query-transformation/07-step-back-prompting/notes.md) |
| Lost in the Middle: How Language Models Use Long Contexts | 2023 | Context engineering | https://arxiv.org/abs/2307.03172 | `[ ] To read` | [09-context-engineering](09-context-engineering/05-lost-in-the-middle/notes.md) |
| Active Retrieval Augmented Generation (FLARE) | 2023 | Advanced RAG | https://arxiv.org/abs/2305.06983 | `[ ] To read` | [10-advanced-rag](10-advanced-rag/05-flare/notes.md) |
| Self-RAG: Learning to Retrieve, Generate and Critique through Self-Reflection | 2023 | Advanced RAG | https://arxiv.org/abs/2310.11511 | `[ ] To read` | [10-advanced-rag](10-advanced-rag/01-self-rag/notes.md) |
| Corrective Retrieval Augmented Generation (CRAG) | 2024 | Advanced RAG | https://arxiv.org/abs/2401.15884 | `[ ] To read` | [10-advanced-rag](10-advanced-rag/02-corrective-rag-crag/notes.md) |
| Adaptive-RAG: Learning to Adapt Retrieval-Augmented LLMs through Question Complexity | 2024 | Advanced RAG | https://arxiv.org/abs/2403.14403 | `[ ] To read` | [10-advanced-rag](10-advanced-rag/03-adaptive-rag/notes.md) |
| From Local to Global: A Graph RAG Approach to Query-Focused Summarization | 2024 | GraphRAG | https://arxiv.org/abs/2404.16130 | `[ ] To read` | [12-graphrag](12-graphrag/01-knowledge-graphs/notes.md) |
| Learning Transferable Visual Models From Natural Language Supervision (CLIP) | 2021 | Multimodal | https://arxiv.org/abs/2103.00020 | `[ ] To read` | [13-multimodal-rag](13-multimodal-rag/03-clip/notes.md) |
| RAGAS: Automated Evaluation of Retrieval Augmented Generation | 2023 | Evaluation | https://arxiv.org/abs/2309.15217 | `[ ] To read` | [14-rag-evaluation](14-rag-evaluation/16-ragas/notes.md) |
| Retrieval-Augmented Generation for Large Language Models: A Survey | 2023 | Survey / orientation | https://arxiv.org/abs/2312.10997 | `[ ] To read` | - |

## Reading notes

Full notes live in the relevant topic's `notes.md`. This file only tracks
**status** and where the notes are.

### Template for a paper I have read

```markdown
### <Paper title>

- **Problem:**
- **Key idea:**
- **How it works:**
- **Results claimed:**
- **What I am sceptical about:**
- **Is it worth implementing here?**
```
