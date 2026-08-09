# Roadmap

The complete learning progression, split into four tracks that are deliberately
**not** mixed together. Course fundamentals, established advanced techniques,
research patterns and production concerns are different kinds of knowledge and
are learned at different times.

Order within a track is a suggestion, not a dependency chain - except that
**Evaluation (14)** should be started early, because without it there is no way
to tell whether anything in tracks 2 and 3 actually helped.

## Tracks at a glance

| Track | Sections | When |
| --- | --- | --- |
| Course content | 01 - 06 | Now |
| Advanced topics | 07 - 09, 13 | After a working baseline pipeline exists |
| Research topics | 10 - 12 | After evaluation is in place |
| Production topics | 14 - 18 | 14 early, the rest alongside real projects |

## Personal milestones

- [ ] **M1** - A working end-to-end RAG pipeline I wrote myself (sections 01-06).
- [ ] **M2** - An evaluation set + baseline metrics I can compare against (section 14).
- [ ] **M3** - One measured improvement over the baseline, with the experiment recorded.
- [ ] **M4** - A hybrid + reranked retriever (section 07) beating the dense baseline.
- [ ] **M5** - An agentic RAG flow in LangGraph (section 11).
- [ ] **M6** - A GraphRAG prototype on a small corpus (section 12).
- [ ] **M7** - A pipeline with tracing, cost tracking and regression tests (15, 14).

---

## COURSE CONTENT

The RAG course I am currently working through. These are the fundamentals -
everything else assumes them. Goal: be able to build a working RAG pipeline
end to end and explain every stage of it.

### 01 - [Foundations](01-foundations/)

What RAG is, why it exists, and how the pieces fit together before any code.

- **What is RAG** - Define retrieval-augmented generation precisely: retrieve, augment, generate - and what each stage is responsible for.
- **Why RAG** - The failure modes RAG addresses: stale knowledge, hallucination, private data, citation requirements, cost of retraining.
- **RAG Architecture** - The two pipelines - offline ingestion (load, chunk, embed, index) and online query (embed, retrieve, rerank, prompt, generate).
- **RAG vs Fine-tuning** - When to add knowledge at inference time vs bake behaviour into weights, and when both are used together.

### 02 - [Document Processing](02-document-processing/)

Getting raw sources into clean, structured text with usable metadata. Garbage in, garbage retrieved.

- **Document Loading** - Loading PDF, HTML, DOCX, Markdown, CSV and plain text into a common document representation.
- **Document Parsing** - Extracting structure - headings, sections, tables, code blocks - not just a flat string of characters.
- **Metadata** - What metadata to attach at ingestion (source, page, section, timestamp, permissions) and how it is used later for filtering and citation.
- **Document Cleaning** - Removing headers/footers, boilerplate, broken whitespace and artifacts; measuring what cleaning does to retrieval quality.

### 03 - [Chunking](03-chunking/)

Splitting documents into retrievable units. The single highest-leverage knob in a basic RAG system.

- **Fixed-Size Chunking** - Character and token based splitting; why it is the baseline and where it breaks semantic units.
- **Recursive Chunking** - Splitting on a hierarchy of separators so paragraphs and sentences survive where possible.
- **Chunk Size** - The trade-off between retrieval precision (small chunks) and context sufficiency (large chunks).
- **Chunk Overlap** - Why overlap exists, what it costs in storage and duplication, and how much is actually useful.
- **Chunking Strategies** - Semantic, structure-aware, sentence-window and document-specific strategies compared on the same corpus.

### 04 - [Embeddings](04-embeddings/)

Turning text into vectors, and understanding what 'similar' actually means in that space.

- **What Are Embeddings** - Vectors as learned representations: dimensionality, what the axes do and do not mean, and how they are trained.
- **Semantic Similarity** - What embedding similarity captures (topic, paraphrase) and what it misses (negation, numbers, entities).
- **Cosine Similarity** - Cosine, dot product and Euclidean distance from scratch with numpy; why normalisation matters.
- **Embedding Models** - Comparing local sentence-transformers vs hosted APIs on dimension, cost, latency, context length and domain fit.
- **Embedding Experiments** - Probing embedding behaviour: negation, synonyms, numbers, code, multilingual text, chunk length effects.

### 05 - [Vector Search](05-vector-search/)

Storing vectors and finding nearest neighbours at speed.

- **Vector Databases** - What a vector store adds over a numpy array: persistence, filtering, indexing, updates, scaling.
- **Similarity Search** - Brute-force search from scratch, then the same query through Chroma/FAISS; verifying the results match.
- **Top-K** - How k affects recall, precision, prompt size and cost; finding a sensible default for a corpus.
- **Metadata Filtering** - Pre-filter vs post-filter, and how filtering interacts with approximate indexes.
- **Vector Indexing** - Flat vs approximate indexes: what an index build actually does and what it costs.

### 06 - [Retrieval](06-retrieval/)

Turning a query into a set of context chunks that are actually worth putting in the prompt.

- **Semantic Retrieval** - The baseline retriever end to end: embed query, search, return chunks with scores and sources.
- **MMR (Maximal Marginal Relevance)** - Trading relevance against diversity to stop the top-k being five copies of the same paragraph.
- **Contextual Compression** - Filtering or shortening retrieved chunks against the query before they reach the prompt.
- **Reranking Basics** - Why a second-stage scorer beats first-stage similarity, and the retrieve-many/rerank-few pattern.

---

## ADVANCED TOPICS

Techniques that improve a working pipeline. These are well-established in
practice, not experimental. Goal: know which technique fixes which failure mode,
and be able to show the improvement with a measurement.

### 07 - [Advanced Retrieval](07-advanced-retrieval/)

Lexical, dense and hybrid retrieval, plus the index structures and rerankers that make them fast and accurate.

- **TF-IDF** - Term weighting from scratch: term frequency, inverse document frequency, and the vector space model.
- **BM25** - The Okapi BM25 scoring function implemented by hand, then via rank_bm25; the role of k1 and b.
- **Sparse vs Dense Retrieval** - Where lexical matching wins (rare terms, IDs, exact phrases) and where dense wins (paraphrase, intent).
- **Hybrid Search** - Combining sparse and dense results; score normalisation and weighted fusion.
- **Reciprocal Rank Fusion** - Rank-based fusion that avoids score normalisation entirely; implementing RRF from the formula.
- **Approximate Nearest Neighbour** - The recall/latency trade-off: why exact search stops being viable and what 'approximate' costs you.
- **HNSW** - Hierarchical navigable small world graphs: layers, M, ef_construction, ef_search - and what each does to recall.
- **IVF (Inverted File Index)** - Clustering vectors into cells and probing a subset; nlist/nprobe and their effect on recall.
- **Product Quantization** - Compressing vectors into subspace codes: memory savings vs accuracy loss.
- **Cross-Encoder Reranking** - Joint query-document encoding: why it is more accurate than bi-encoders and why it cannot scale to the whole corpus.
- **ColBERT** - Token-level embeddings with MaxSim scoring; storage cost vs retrieval quality.
- **Late Interaction** - The general idea behind ColBERT-style models compared to early interaction (cross-encoders) and no interaction (bi-encoders).

### 08 - [Query Transformation](08-query-transformation/)

Fixing retrieval on the input side: the user's question is often not a good search query.

- **Query Rewriting** - Rewriting vague or under-specified questions into retrieval-friendly queries.
- **Query Expansion** - Adding synonyms, entities and related terms to improve lexical and dense recall.
- **Multi-Query Retrieval** - Generating several query variants and merging their result sets.
- **Query Decomposition** - Breaking a compound question into independently answerable sub-queries.
- **RAG Fusion** - Multi-query generation combined with reciprocal rank fusion.
- **HyDE (Hypothetical Document Embeddings)** - Embedding a generated hypothetical answer instead of the raw question; when this helps and when it hurts.
- **Step-Back Prompting** - Asking a more general question first to retrieve the background a specific question depends on.
- **Sub-Question Retrieval** - Running retrieval per sub-question and synthesising a single grounded answer.
- **Conversational Query Rewriting** - Resolving pronouns and implicit context in follow-up turns into standalone queries.

### 09 - [Context Engineering](09-context-engineering/)

What actually reaches the model: how much, in what order, and with what surrounding information.

- **Contextual Retrieval** - Prepending chunk-level context (document/section summary) before embedding to fix orphaned chunks.
- **Context Compression** - Extractive and abstractive compression of retrieved context under a token budget.
- **Context Deduplication** - Detecting near-duplicate chunks so the budget is not spent on the same sentence three times.
- **Context Ordering** - How placement of the relevant chunk in the prompt changes answer quality.
- **Lost in the Middle** - Reproducing the positional-attention effect on a small controlled set.
- **Token Budgeting** - Allocating a fixed context window across system prompt, history, retrieved context and answer.
- **Parent Document Retrieval** - Indexing small chunks for precision but returning the parent block for context.
- **Small-to-Big Retrieval** - Sentence-window and expanding-window retrieval variants.
- **Hierarchical Retrieval** - Summary-level retrieval that routes down to detail-level chunks.

### 13 - [Multimodal RAG](13-multimodal-rag/)

Retrieval over documents that are not plain text: images, layout, tables, charts, audio and video.

- **Image Retrieval** - Retrieving images by text query and images by image.
- **Image Embeddings** - How image vectors are produced and how they relate to text vectors.
- **CLIP** - Contrastive image-text pretraining and the shared embedding space it produces.
- **Vision-Language Models** - Using a VLM to describe or answer over retrieved pages instead of parsing them to text first.
- **PDF Layout Understanding** - Reading order, columns, figures and captions; why naive text extraction destroys meaning.
- **OCR** - Scanned and image-only documents; quality, errors and their downstream effect on retrieval.
- **Tables** - Extracting, representing and retrieving tabular data so numbers survive chunking.
- **Charts** - Getting answerable information out of figures - description, data extraction, or page-image retrieval.
- **Multimodal Embeddings** - Unified vs separate index designs for mixed-modality corpora.
- **Video RAG** - Segmentation, transcripts, keyframes and timestamped citation.
- **Audio RAG** - Transcription, diarisation and chunking of spoken content.

---

## RESEARCH TOPICS

Paper-driven patterns. These change the control flow of RAG rather than tuning a
stage of it. Goal: read the paper, implement a minimal version, and understand
the cost, not just the idea.

### 10 - [Advanced RAG](10-advanced-rag/)

Control-flow research patterns: systems that decide whether, when and how many times to retrieve.

- **Self-RAG** - Retrieve-on-demand with self-critique tokens for relevance, support and usefulness.
- **Corrective RAG (CRAG)** - Grading retrieved documents and falling back (e.g. to web search) when they are insufficient.
- **Adaptive RAG** - Routing queries by complexity: no retrieval, single-step, or multi-step.
- **Iterative RAG** - Multi-round retrieve-generate loops with a stopping condition.
- **FLARE** - Forward-looking active retrieval triggered by low-confidence generated tokens.
- **Retrieval Routing** - Choosing between several indexes/sources per query, including 'do not retrieve'.
- **Corrective Retrieval** - Detecting bad retrievals at runtime and repairing them (re-query, expand, fall back).

### 11 - [Agentic RAG](11-agentic-rag/)

Retrieval as a tool an agent plans with, reflects on and repeats - rather than a fixed pipeline stage.

- **Agentic Retrieval** - The shift from a fixed pipeline to an agent that decides what to retrieve next.
- **Query Planning** - Producing an explicit retrieval plan before executing any search.
- **Iterative Retrieval** - Search, read, refine loops with budgets and termination criteria.
- **Tool-Based Retrieval** - Exposing multiple retrievers (vector, SQL, web, API) as tools and letting the model choose.
- **Document Navigation** - Agents that traverse structure - table of contents, sections, links - instead of flat top-k.
- **Reflection** - Self-evaluation of retrieved evidence and drafted answers before responding.
- **Agent State** - What must be tracked across steps: query history, seen documents, evidence, budget.
- **Agent Memory** - Short-term vs long-term memory and how memory interacts with retrieval.
- **Multi-Agent RAG** - Splitting planner, retriever, critic and writer roles; where coordination cost exceeds the benefit.
- **Agentic RAG Evaluation** - Evaluating trajectories, not just final answers: step count, tool choice, redundant retrievals, cost.

*[LangGraph Implementations](11-agentic-rag/langgraph/)*
- **LangGraph Basics** - State, nodes, edges, conditional edges and checkpointing - the minimum needed to build a RAG graph.
- **RAG as a Graph** - Rebuilding a linear RAG pipeline as an explicit graph, then adding a grading branch.
- **Self-Corrective RAG Graph** - CRAG/Self-RAG style loops with cycles, retry limits and fallbacks.
- **Human in the Loop** - Interrupts, approval steps and state inspection during a retrieval run.

### 12 - [GraphRAG](12-graphrag/)

Building a knowledge graph from a corpus and retrieving over structure instead of (or alongside) vectors.

- **Knowledge Graphs** - Entities, relations, triples and schemas; what a graph represents that a vector index cannot.
- **Entity Extraction** - Extracting and normalising entities from chunks; handling aliases and duplicates.
- **Relationship Extraction** - Extracting typed relations between entities with evidence pointers back to source chunks.
- **Graph Construction** - Assembling extractions into a queryable graph; deduplication and merge rules.
- **Community Detection** - Clustering the graph (e.g. Leiden) into communities at multiple levels.
- **Community Summaries** - Generating hierarchical summaries per community for global questions.
- **Local Search** - Entity-anchored retrieval over neighbourhoods for specific questions.
- **Global Search** - Map-reduce over community summaries for corpus-wide questions.
- **Graph Retrieval** - Traversal-based retrieval: paths, neighbourhoods and subgraphs as context.
- **Vector + Graph Retrieval** - Vector search to find entry points, graph traversal to expand context.
- **Multi-Hop Retrieval** - Questions whose answer requires chaining facts across documents.
- **Agentic GraphRAG** - An agent choosing between local, global and traversal strategies per query.

---

## PRODUCTION TOPICS

What separates a demo from a system: measurement, visibility, safety and scale.
Evaluation comes first here - without it, every other change is guesswork.

### 14 - [RAG Evaluation](14-rag-evaluation/)

Measuring whether a change actually improved anything. Without this, every other section is guesswork.

- **Evaluation Fundamentals** - Separating retrieval quality from generation quality; offline vs online; what a good test set looks like.
- **Retrieval Evaluation** - Building a labelled query/relevant-document set and scoring a retriever against it.
- **Recall@K** - Implementing recall@k from the definition and reading it correctly.
- **Precision@K** - Implementing precision@k and understanding its tension with recall.
- **Hit Rate** - The simplest 'did we get anything useful' metric and its blind spots.
- **MRR (Mean Reciprocal Rank)** - Rank-sensitive scoring when there is one correct answer.
- **nDCG** - Graded relevance with positional discounting, implemented from the formula.
- **Context Precision** - How much of the retrieved context was actually relevant.
- **Context Recall** - How much of the needed evidence was retrieved at all.
- **Context Relevance** - Judging query-context relevance and where judges disagree with humans.
- **Faithfulness** - Whether every claim in the answer is supported by the retrieved context.
- **Answer Relevance** - Whether the answer addresses the question asked.
- **Groundedness** - Claim-level attribution to source spans.
- **Citation Correctness** - Do the citations point at text that supports the claim.
- **LLM-as-a-Judge** - Designing judge prompts, calibrating them against human labels, and their biases.
- **RAGAS** - Running the RAGAS metric suite on my own pipeline and interpreting the output.
- **DeepEval** - Test-style evaluation and assertions in a pytest workflow.
- **Evaluation Datasets** - Building small golden sets by hand and generating synthetic ones; keeping them honest.
- **Regression Testing** - Locking in a baseline so a 'small improvement' cannot silently break retrieval.

### 15 - [RAG Observability](15-rag-observability/)

Seeing what a running RAG system actually did: what was retrieved, what was prompted, what it cost.

- **Tracing** - Spans across the whole pipeline and what to record at each stage.
- **Retrieval Traces** - Logging queries, scores, chosen chunks and filters for post-hoc analysis.
- **Prompt Traces** - Capturing the exact final prompt, not the template.
- **Token Usage** - Measuring where the tokens go across ingestion, retrieval and generation.
- **Latency** - Breaking end-to-end latency down per stage to find the real bottleneck.
- **Cost Tracking** - Per-query cost attribution across embedding, reranking and generation.
- **Failed Retrieval Analysis** - Triaging bad answers into retrieval, ranking, context or generation failures.
- **Production Evaluation** - Sampling and scoring live traffic without a labelled set.
- **Regression Monitoring** - Alerting on drift in retrieval quality, latency and cost.

*[LangSmith Examples](15-rag-observability/langsmith/)*
- **LangSmith Setup** - Environment variables, projects and getting a first trace to appear. Never commit the API key.
- **Tracing a RAG Pipeline** - Annotating retrieval and generation steps so a trace is readable.
- **Datasets and Experiments** - Running an evaluation dataset and comparing two pipeline versions.

### 16 - [RAG Security](16-rag-security/)

RAG puts untrusted text into the prompt and private data into the index. Both are attack surfaces. Everything here is for defending my own systems.

- **Prompt Injection** - Instructions in user input overriding system intent; why input filtering alone is not a fix.
- **Indirect Prompt Injection** - Instructions hidden inside retrieved documents - the RAG-specific variant.
- **Malicious Documents** - Hostile content in the corpus: hidden text, invisible characters, adversarial formatting.
- **Data Poisoning** - Corrupting the knowledge base so wrong answers become well-grounded.
- **Retrieval Poisoning** - Crafting documents to rank highly for target queries.
- **Unauthorized Retrieval** - Users retrieving documents they should not be able to see.
- **Access-Control-Aware Retrieval** - Enforcing permissions at index and query time, not in the prompt.
- **Tenant Isolation** - Namespace vs per-tenant index strategies and their failure modes.
- **PII Leakage** - Detection and redaction at ingestion and at output.
- **Data Exfiltration** - Context leaking through answers, tool calls, links and citations.
- **Citation Manipulation** - Fabricated or mismatched citations, and verifying citations mechanically.

### 17 - [Production RAG](17-production-rag/)

Everything between a working notebook and a system that stays fast, cheap and correct under real traffic.

- **Async Retrieval** - Non-blocking I/O across embedding, search and generation calls.
- **Parallel Retrieval** - Fanning out to multiple retrievers concurrently and merging results.
- **Caching** - What is safe to cache in a RAG pipeline and for how long.
- **Semantic Caching** - Serving near-duplicate queries from cache, and the risk of wrong hits.
- **Embedding Caching** - Content-hash keyed embedding reuse across re-ingestion runs.
- **Batch Ingestion** - Throughput, batching, rate limits and resumability for large corpora.
- **Incremental Indexing** - Adding new documents without rebuilding the whole index.
- **Document Updates** - Detecting changes and re-embedding only what changed.
- **Document Deletion** - Hard vs soft deletes and keeping deleted content out of results.
- **Vector DB Scaling** - Sharding, replication, memory footprint and index build time.
- **Latency Optimization** - Measuring first, then cutting the stage that actually dominates.
- **Cost Optimization** - Model choice, chunk sizes, top-k, reranking depth and caching as cost levers.
- **Retries** - Idempotency, backoff and not amplifying an outage.
- **Timeouts** - Per-stage deadlines and returning a degraded answer instead of hanging.
- **Fallbacks** - Graceful degradation when the index, reranker or model is unavailable.
- **Rate Limiting** - Client-side throttling and queueing against provider limits.
- **Multi-Tenancy** - Data separation, noisy neighbours and per-tenant configuration.
- **Authentication** - Identifying the caller before any retrieval happens.
- **Authorization** - Turning identity into a retrieval filter that cannot be prompted around.

### 18 - [Specialized RAG](18-specialized-rag/)

RAG variants where the retrieval target is not a pile of documents.

- **SQL RAG** - Schema retrieval, text-to-SQL, execution and grounding answers in query results.
- **API RAG** - Retrieving over API specs and calling endpoints as the retrieval step.
- **Web RAG** - Live search, fetching, extraction and freshness/trust handling.
- **Code RAG** - Repository-aware chunking by symbol, plus dependency and call-graph context.
- **Knowledge Base RAG** - Internal docs/wikis: permissions, staleness and duplicate content.
- **Research RAG** - Papers: sections, citations, figures and multi-document synthesis.
- **Conversational RAG** - History-aware retrieval, memory and topic switching across turns.
