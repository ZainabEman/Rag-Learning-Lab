"""
Chunk Overlap - what repeating text between chunks costs and buys
Section: Chunking

Goal
----
Make the overlap trade-off concrete:
  - what "shared band" actually means, character by character
  - how quickly chunk count grows as overlap rises (it is NOT linear)
  - how much duplicated text ends up in the index

No embeddings or retrieval here - this is string processing only.

Run:
    python implementation.py
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CHUNK_SIZE = 100
OVERLAPS = [0, 10, 20, 30, 50, 75, 90]

TEXT = (
    "Gradient descent is an iterative optimisation algorithm. We start from "
    "random coefficients and repeatedly move them in the direction that "
    "reduces the loss. The optimisation step itself is simple: compute the "
    "gradient of the loss with respect to each coefficient, multiply it by "
    "the learning rate, and subtract the result from the current value."
)


# ===========================================================================
# 1. FROM SCRATCH
# ===========================================================================

def split_with_overlap(text: str, chunk_size: int, chunk_overlap: int) -> list[str]:
    """
    Length-based splitting where each chunk starts `chunk_overlap` characters
    before the previous one ended.

    The step between chunk starts is (chunk_size - chunk_overlap), which is the
    whole reason overlap is expensive: it shrinks the denominator.
    """
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    step = chunk_size - chunk_overlap
    chunks = []
    for start in range(0, len(text), step):
        piece = text[start:start + chunk_size]
        if not piece:
            break
        chunks.append(piece)
        if start + chunk_size >= len(text):
            break
    return chunks


def shared_band(a: str, b: str) -> str:
    """The text that consecutive chunks a and b have in common at the seam."""
    longest = ""
    for size in range(1, min(len(a), len(b)) + 1):
        if a[-size:] == b[:size]:
            longest = a[-size:]
    return longest


# ---------------------------------------------------------------------------
# Example usage + output inspection
# ---------------------------------------------------------------------------

def show_the_seam() -> None:
    """Look at one boundary closely, with and without overlap."""
    print("  Without overlap - the seam between chunk 0 and chunk 1:\n")
    none = split_with_overlap(TEXT, CHUNK_SIZE, 0)
    print(f"    chunk 0 ends   : ...{none[0][-40:]!r}")
    print(f"    chunk 1 starts : {none[1][:40]!r}...")
    print("    -> the sentence is cut, and neither chunk contains it whole")

    print("\n  With chunk_overlap=20:\n")
    some = split_with_overlap(TEXT, CHUNK_SIZE, 20)
    print(f"    chunk 0 ends   : ...{some[0][-40:]!r}")
    print(f"    chunk 1 starts : {some[1][:40]!r}...")
    band = shared_band(some[0], some[1])
    print(f"    shared band    : {band!r}  ({len(band)} chars in BOTH chunks)")
    print("    -> the text that was cut now survives intact inside chunk 1")


def sweep() -> None:
    """How overlap affects chunk count and duplication."""
    header = (f"  {'overlap':>7} | {'% of size':>9} | {'step':>5} | "
              f"{'chunks':>6} | {'total chars':>11} | {'duplicated':>10}")
    print(header)
    print("  " + "-" * (len(header) - 2))

    baseline = len(TEXT)
    for overlap in OVERLAPS:
        chunks = split_with_overlap(TEXT, CHUNK_SIZE, overlap)
        stored = sum(len(c) for c in chunks)
        duplicated = stored - baseline
        pct = f"{overlap / CHUNK_SIZE:.0%}"
        print(f"  {overlap:>7} | {pct:>9} | {CHUNK_SIZE - overlap:>5} | "
              f"{len(chunks):>6} | {stored:>11} | {duplicated / baseline:>9.0%}")


def main() -> None:
    print("=" * 72)
    print("1. WHAT OVERLAP DOES AT THE SEAM")
    print("=" * 72 + "\n")
    show_the_seam()

    print()
    print("=" * 72)
    print(f"2. THE COST - text is {len(TEXT)} chars, chunk_size = {CHUNK_SIZE}")
    print("=" * 72 + "\n")
    sweep()

    print()
    print("=" * 72)
    print("3. WHAT TO READ OFF THIS")
    print("=" * 72)
    print("""
  number_of_chunks  ~  len(text) / (chunk_size - chunk_overlap)

  The overlap sits in the DENOMINATOR, so the cost is not linear:

      overlap 10%  ->  ~11% more chunks     cheap
      overlap 20%  ->  ~25% more chunks     the usual upper bound
      overlap 50%  ->  ~100% more chunks    twice the embeddings
      overlap 90%  ->  ~10x more chunks     unusable

  Every extra chunk is another embedding to compute, store and search, which
  is why "set it high to be safe" is the wrong instinct. The 10-20% rule of
  thumb sits exactly where the curve is still flat.

  Note also that overlap only rescues context at ARBITRARY cuts. A recursive
  splitter breaking on paragraph boundaries has far less to rescue - see
  ../02-recursive-chunking/.
""")

    # TODO for the experiment file:
    #   - once embeddings exist, test whether overlap actually improves recall
    #     or just inflates the index


if __name__ == "__main__":
    main()
