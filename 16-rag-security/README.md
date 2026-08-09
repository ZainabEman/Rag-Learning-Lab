# 16 RAG Security

> Track: **PRODUCTION TOPICS** | [Back to repository root](../README.md)

RAG puts untrusted text into the prompt and private data into the index. Both are attack surfaces. Everything here is for defending my own systems.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Prompt Injection](01-prompt-injection/) | Instructions in user input overriding system intent; why input filtering alone is not a fix. | `not started` |
| 02 | [Indirect Prompt Injection](02-indirect-prompt-injection/) | Instructions hidden inside retrieved documents - the RAG-specific variant. | `not started` |
| 03 | [Malicious Documents](03-malicious-documents/) | Hostile content in the corpus: hidden text, invisible characters, adversarial formatting. | `not started` |
| 04 | [Data Poisoning](04-data-poisoning/) | Corrupting the knowledge base so wrong answers become well-grounded. | `not started` |
| 05 | [Retrieval Poisoning](05-retrieval-poisoning/) | Crafting documents to rank highly for target queries. | `not started` |
| 06 | [Unauthorized Retrieval](06-unauthorized-retrieval/) | Users retrieving documents they should not be able to see. | `not started` |
| 07 | [Access-Control-Aware Retrieval](07-access-control-aware-retrieval/) | Enforcing permissions at index and query time, not in the prompt. | `not started` |
| 08 | [Tenant Isolation](08-tenant-isolation/) | Namespace vs per-tenant index strategies and their failure modes. | `not started` |
| 09 | [PII Leakage](09-pii-leakage/) | Detection and redaction at ingestion and at output. | `not started` |
| 10 | [Data Exfiltration](10-data-exfiltration/) | Context leaking through answers, tool calls, links and citations. | `not started` |
| 11 | [Citation Manipulation](11-citation-manipulation/) | Fabricated or mismatched citations, and verifying citations mechanically. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 16-rag-security <next-number>-<topic-slug> "Topic Title"
```
