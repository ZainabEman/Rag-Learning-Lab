# Resources - Vector Databases

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| Vector Stores (LangChain playlist, video 4) | Course video | *TODO - paste the video URL* | Primary source: the movie-recommender motivation, the four features, and vector store vs vector database. |
| LangChain vector store integrations | Docs | https://docs.langchain.com/oss/python/integrations/vectorstores | Current import paths - Chroma is now `from langchain_chroma import Chroma`. |
| Chroma docs | Docs | https://docs.trychroma.com/ | Collections, persistence, metadata filtering. |
| FAISS wiki | Docs | https://github.com/facebookresearch/faiss/wiki | The lightweight vector *store* referenced as the contrast to full databases. |

## Best explanation I found

The two failure cases of keyword matching. *My Name Is Khan* vs *Kabhi Alvida
Naa Kehna* (same keywords, unrelated stories) and *Taare Zameen Par* vs *A
Beautiful Mind* (no shared keywords, genuinely similar) make the argument for
embeddings far better than any definition.
