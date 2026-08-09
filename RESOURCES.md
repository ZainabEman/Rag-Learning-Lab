# Resources

Only resources I have actually used, with a note on **why** each one was worth
the time. This is not a link collection.

The starter entries below are official documentation homepages for the tools
this repository uses. Everything else - courses, videos, blog posts - gets added
by me as I encounter it, so I do not end up with links I never read.

## Courses

| Title | URL | Topic | Why it is useful |
| --- | --- | --- | --- |
| LangChain playlist (the RAG course I am currently taking) | *TODO — paste the playlist URL* | LangChain components → RAG | Main source. Teaches the four RAG components (document loaders, text splitters, vector stores, retrievers) before assembling them into RAG. |
| ↳ *RAG: why, what and how* (theory video) | *TODO — paste the video URL* | Foundations | Parametric knowledge, the three failure modes, fine-tuning, in-context learning, the four RAG stages. Notes in [01-foundations](01-foundations/). |
| ↳ *Document Loaders* | *TODO — paste the video URL* | Document processing | The `Document` object, four core loaders, `DirectoryLoader`, `load()` vs `lazy_load()`. Notes in [02-document-processing/01-document-loading](02-document-processing/01-document-loading/). |

## Documentation

| Title | URL | Topic | Why it is useful |
| --- | --- | --- | --- |
| LangChain docs | https://python.langchain.com/ | Pipelines, retrievers, loaders | Reference for the library-side implementations |
| LangGraph docs | https://langchain-ai.github.io/langgraph/ | Agentic / graph flows | Used for section 11 |
| LangSmith docs | https://docs.smith.langchain.com/ | Tracing, evaluation | Used for section 15 |
| Chroma docs | https://docs.trychroma.com/ | Vector store | Default local vector store here |
| FAISS wiki | https://github.com/facebookresearch/faiss/wiki | ANN indexes | Where HNSW/IVF/PQ behaviour is explained concretely |
| Sentence-Transformers docs | https://www.sbert.net/ | Embeddings, cross-encoders | Local embedding + reranking models |
| Hugging Face docs | https://huggingface.co/docs | Models, datasets | Model hub and inference |
| RAGAS docs | https://docs.ragas.io/ | RAG evaluation | Metric definitions and implementations |
| DeepEval docs | https://deepeval.com/docs/getting-started | Evaluation as tests | pytest-style evaluation |

## Papers

Tracked separately in [PAPERS.md](PAPERS.md).

## Videos

| Title | URL | Topic | Why it is useful |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Blog posts

| Title | URL | Topic | Why it is useful |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Tools

| Title | URL | Topic | Why it is useful |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Libraries

| Library | URL | Topic | Why it is useful |
| --- | --- | --- | --- |
| numpy | https://numpy.org/doc/ | From-scratch implementations | Vector maths without a framework |
| rank_bm25 | https://github.com/dorianbrown/rank_bm25 | Lexical retrieval | Reference BM25 to check my own against |
| PyTorch | https://pytorch.org/docs/stable/index.html | Models | Underneath the embedding/reranking models |
