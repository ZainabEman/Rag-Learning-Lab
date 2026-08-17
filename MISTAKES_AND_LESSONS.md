# Mistakes and Lessons

Failed experiments and wrong assumptions stay here. They are the most useful
part of the repository, because they are the parts I will not learn twice.

Nothing gets deleted from this file. If a lesson turns out to be wrong, a
correction gets appended underneath it.

---

## Things I misunderstood

<!-- What I believed, why it was wrong, and what made it click. -->

| Date | I thought | Actually | What corrected me |
| --- | --- | --- | --- |
| 2026-08-10 | A document loader returning "one document per page" was already doing chunking | Loading and chunking are separate steps. Per-page/per-row splitting is the source's natural unit; chunking is a deliberate later step driven by context limits and embedding quality | Noticing that a 23-page PDF gives 23 documents that *still* need splitting |
| 2026-08-10 | RAG is a technique layered on top of LLMs | RAG depends on in-context learning, an emergent property of large models. Without it, injecting context into the prompt would do nothing | The progression few-shot prompting → RAG: same channel, different payload |
| 2026-08-10 | Fine-tuning and RAG are competing answers to the same question | They answer different questions — behaviour vs knowledge. The hard asymmetry is deletion: RAG removes a document, fine-tuning cannot cleanly forget | Working through the "remove a course from the catalogue" case |
| 2026-08-16 | `CharacterTextSplitter` is the fixed-size splitter | Its default separator is `"\n\n"` — by default it is a *paragraph* splitter that merges up to `chunk_size`. Pure length splitting needs `separator=""` | Reading the constructor signature in the installed package |
| 2026-08-16 | `chunk_size` guarantees a maximum chunk length | It is a merge budget. A piece already larger than `chunk_size` comes back oversized — measured: a 299-char chunk when 50 was requested, with no warning | Testing a paragraph with no blank lines in it |
| 2026-08-16 | `from_language(PYTHON)` splits code on every `class` and `def` | Its separators are `'\nclass '`, `'\ndef '`, `'\n\tdef '` — line-anchored, so space-indented methods never match. On a normal PEP 8 class it behaves exactly like the generic splitter | Building a comparison that showed *identical* output at every chunk size, then working out why |
| TODO | TODO | TODO | TODO |

## Mistakes in implementation

<!-- Bugs that cost real time. Include the symptom - that is what I will
     search for next time, not the cause. -->

| Date | Symptom | Cause | Fix |
| --- | --- | --- | --- |
| 2026-08-10 | `lazy_load()` demo showed the *same* peak memory as `load()` (8297 KB vs 8288 KB) | The generator wrapped an eager reader — the full list was already built inside the loader before the first `yield` | Made the CSV reader itself a generator (`yield` per row) and had the eager version call `list()` on it. Result: 8297 KB vs 44 KB |
| TODO | TODO | TODO | TODO |

## Failed experiments

<!-- Experiments where the hypothesis lost. Record them fully - a negative
     result is still a result. -->

### TODO - <experiment>

- **Hypothesis:**
- **What happened:**
- **Why I think it failed:**
- **Was the experiment wrong, or the hypothesis?**

## Unexpected results

<!-- The result was real but not what I expected. Often the most interesting. -->

### 2026-08-10 - Spelling defeated retrieval, and I did not notice at first

- **Expected:** the query "how do we perform the **optimization** step in
  gradient descent?" would match the chunk containing "the **optimisation**
  step itself is simple" largely *because* of that word.
- **Observed:** those two tokens contributed exactly nothing to the similarity
  score. Retrieval still returned the right chunks, but only because
  "gradient", "descent" and "step" happened to overlap.
- **Explanation:** the stand-in embedding in
  [01-foundations/03-rag-architecture/implementation.py](01-foundations/03-rag-architecture/implementation.py)
  is bag-of-words, so US and UK spellings are unrelated tokens. A dense
  embedding model would place them almost on top of each other. This is the
  concrete argument for [04-embeddings](04-embeddings/) — found by accident,
  not by reading.

### 2026-08-10 - The winning chunk was malformed and still won

- **Expected:** the top-ranked chunk would be a clean, self-contained passage.
- **Observed:** chunk 3 begins "conditional on the other features" — a fragment
  of the *previous* paragraph about multiple regression — and still scored
  highest.
- **Explanation:** fixed-size chunking cuts on word counts, not meaning.
  Relevance and well-formedness are independent properties, and similarity
  search only measures the first. Motivates [03-chunking](03-chunking/).

### 2026-08-16 - I claimed the recursive splitter never cuts words. It does.

- **Expected:** having watched `RecursiveCharacterTextSplitter` keep every word
  intact at `chunk_size=10` on the worked example, I wrote in my notes that it
  "never cut inside a word".
- **Observed:** the chunk-size sweep in
  [03-chunk-size/implementation.py](03-chunking/03-chunk-size/implementation.py)
  reported **7 mid-word cuts** at `chunk_size=10` on a different text.
- **Explanation:** every word in the first example happened to be ≤ 10
  characters. Words like "exploration" (11) and "discoveries." (12) cannot fit
  in the budget at all, so the separator list falls through to `""` and cuts
  them. The real property is "never cuts a word it could have avoided cutting".
- **Lesson:** one example is not a guarantee. I generalised from a sample that
  happened to be favourable, and only caught it because the sweep measured
  something the example could not show.

### TODO - <observation>

## Lessons learned

<!-- One line each. Only things I would tell someone else. -->

- TODO
