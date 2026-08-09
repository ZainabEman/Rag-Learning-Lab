# Engineering Decisions

Every non-obvious choice I make in this repository, with the reasoning and,
where possible, the evidence behind it. The point is to be able to look back and
see whether my judgement was any good - and to stop re-deciding the same thing.

A decision belongs here if I had to choose between real alternatives. It does
not belong here if there was only one option.

Copy this template per decision:

```markdown
## <Decision title>

### Context

### Options considered

### Decision

### Reason

### Evidence / experiment

### Result
```

---

## Learn each concept from scratch before using a framework

### Context

Almost every RAG concept has a one-line LangChain equivalent. Using it first is
faster but teaches nothing about what is happening underneath.

### Options considered

1. Framework-first - fastest to a working pipeline, weakest understanding.
2. From-scratch only - deepest understanding, unrealistic for production work.
3. From-scratch, then framework, then compare.

### Decision

Option 3, for any concept small enough to implement by hand (similarity metrics,
BM25, RRF, MMR, ranking metrics). Framework-first is fine for infrastructure
(vector stores, model APIs, orchestration).

### Reason

The abstractions are only useful once I know what they replaced. Debugging a
retrieval problem requires knowing what the library is doing.

### Evidence / experiment

None yet - this is a starting assumption, to be revisited if it slows learning
down without adding understanding.

### Result

TODO - review after finishing the foundations track.
