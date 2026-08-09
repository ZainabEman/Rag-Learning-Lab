"""
Experiment - Document Cleaning

Question
--------
TODO: the single question this experiment answers.

Hypothesis
----------
TODO: what I expect to happen, written BEFORE running it.

Setup
-----
TODO: dataset, model(s), parameters, and what is held constant.
Keep the dataset small and reproducible - fixed seed, committed inputs.

Metric
------
TODO: how "better" is measured here.

Result
------
TODO: fill in after running.
Record surprises in ../../MISTAKES_AND_LESSONS.md and any resulting choice
in ../../DECISIONS.md.
"""

# ---------------------------------------------------------------------------
# Configuration - the variable(s) under test
# ---------------------------------------------------------------------------
SEED = 42
# TODO: VARIANTS = [...]  # the thing being varied
# TODO: everything else stays fixed


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
# TODO: a handful of documents and queries, small enough to reason about.


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
def run_variant(variant):
    """Run the pipeline for one variant and return its metrics."""
    raise NotImplementedError("TODO")


def main() -> None:
    """Run every variant, print a comparison table, save the result."""
    raise NotImplementedError("TODO")


if __name__ == "__main__":
    main()
