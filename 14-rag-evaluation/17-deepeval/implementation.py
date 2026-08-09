"""
DeepEval
Section: RAG Evaluation

Goal
----
Test-style evaluation and assertions in a pytest workflow.

Approach (see the repository README for why it is done in this order)
--------------------------------------------------------------------
1. From scratch / minimal  -> make the mechanics visible
2. Library implementation  -> what production code would actually use
3. Comparison              -> same result? same cost? what was hidden?

Status: NOT STARTED. Written while studying this topic - not before.
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
# TODO: add imports as the implementation grows. Keep the from-scratch part
# dependency-free (stdlib + numpy) so the mechanics stay readable.


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
# Every tunable value lives here so experiments only ever change this block.
# TODO: e.g. MODEL_NAME, CHUNK_SIZE, CHUNK_OVERLAP, TOP_K, DATA_PATH


# ---------------------------------------------------------------------------
# 1. From scratch / minimal implementation
# ---------------------------------------------------------------------------
# TODO: implement the concept directly. Comment the *why*, not the syntax.


# ---------------------------------------------------------------------------
# 2. Library implementation
# ---------------------------------------------------------------------------
# TODO: the same idea using the library I would reach for in real work.
# Only add a framework here if it genuinely earns its place.


# ---------------------------------------------------------------------------
# 3. Comparison
# ---------------------------------------------------------------------------
# TODO: do (1) and (2) agree? Where do they differ, and why?
# What is the abstraction doing that I did not have to write?


# ---------------------------------------------------------------------------
# Example usage
# ---------------------------------------------------------------------------
def main() -> None:
    """Smallest example that demonstrates the concept end to end."""
    raise NotImplementedError("TODO: implement while studying DeepEval.")


# ---------------------------------------------------------------------------
# Output inspection
# ---------------------------------------------------------------------------
# TODO: print the intermediate values, not just the final answer -
# shapes, scores, ranks, retrieved chunk text. This is where understanding
# actually happens.


if __name__ == "__main__":
    main()
