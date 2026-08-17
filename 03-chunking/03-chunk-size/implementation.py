"""
Chunk Size - what the number actually controls
Section: Chunking

Goal
----
Show that chunk_size does two things at once:
  1. the obvious one - it sets how many chunks you get
  2. the useful one - it selects WHICH structural level the split lands on

A sweep across chunk sizes on one fixed text makes both visible at a glance.

No embeddings or retrieval here - this is string processing only. Part 1 runs
on the standard library; part 2 needs langchain-text-splitters and is skipped
with an explanation if it is missing.

Run:
    python implementation.py
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Configuration - the variable under test is CHUNK_SIZES, everything else fixed
# ---------------------------------------------------------------------------

CHUNK_SIZES = [10, 25, 50, 100, 200, 400]
CHUNK_OVERLAP = 0

TEXT = (
    "Space exploration has led to incredible scientific discoveries.\n"
    "From landing on the Moon to exploring Mars, humanity keeps pushing.\n\n"
    "These missions expanded our knowledge of the universe.\n"
    "They also produced technology that benefits everyday life on Earth."
)


# ===========================================================================
# Helpers
# ===========================================================================

def classify_level(chunks: list[str]) -> str:
    """
    Infer which structural unit the splitter settled on.

    Crude but honest: look at what the chunks contain rather than guessing
    from chunk_size.
    """
    if len(chunks) == 1:
        return "whole text (one chunk)"
    if any("\n\n" in c for c in chunks):
        return "multi-paragraph"
    if any("\n" in c for c in chunks):
        return "paragraph"
    # No newlines inside any chunk: either full lines, or fragments of them.
    lines = {line.strip() for line in TEXT.replace("\n\n", "\n").split("\n")}
    if all(c.strip() in lines for c in chunks):
        return "line / sentence"
    return "word"


def cuts_mid_word(chunks: list[str], source: str) -> int:
    """Count chunks whose end falls inside a word in the source text."""
    count = 0
    cursor = 0
    for chunk in chunks[:-1]:
        idx = source.find(chunk.strip(), cursor)
        if idx == -1:
            continue
        end = idx + len(chunk.strip())
        cursor = idx
        # A clean break has whitespace (or end of text) on both sides of the cut
        if end < len(source) and not source[end].isspace() and not source[end - 1].isspace():
            count += 1
    return count


# ===========================================================================
# The sweep
# ===========================================================================

def sweep_recursive() -> None:
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
    except ImportError:
        print("  langchain-text-splitters is not installed - skipping.")
        print("  Install with:  pip install langchain-text-splitters")
        return

    print(f"  text length = {len(TEXT)} chars\n")
    header = f"  {'chunk_size':>10} | {'chunks':>6} | {'longest':>7} | {'mid-word cuts':>13} | split level"
    print(header)
    print("  " + "-" * (len(header) - 2))

    for size in CHUNK_SIZES:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap=CHUNK_OVERLAP,
        )
        chunks = splitter.split_text(TEXT)
        longest = max(len(c) for c in chunks)
        print(f"  {size:>10} | {len(chunks):>6} | {longest:>7} | "
              f"{cuts_mid_word(chunks, TEXT):>13} | {classify_level(chunks)}")


def sweep_fixed_size() -> None:
    """
    The same sweep with pure length splitting, for contrast.

    Written from scratch so this part needs no install.
    """
    print(f"\n  pure length splitting (no structure awareness):\n")
    header = f"  {'chunk_size':>10} | {'chunks':>6} | {'mid-word cuts':>13}"
    print(header)
    print("  " + "-" * (len(header) - 2))

    for size in CHUNK_SIZES:
        chunks = [TEXT[i:i + size] for i in range(0, len(TEXT), size)]
        print(f"  {size:>10} | {len(chunks):>6} | "
              f"{cuts_mid_word(chunks, TEXT):>13}")


def main() -> None:
    print("=" * 72)
    print("CHUNK SIZE SWEEP - RecursiveCharacterTextSplitter")
    print("=" * 72 + "\n")
    sweep_recursive()

    print()
    print("=" * 72)
    print("SAME SWEEP - fixed-size splitting")
    print("=" * 72)
    sweep_fixed_size()

    print()
    print("=" * 72)
    print("WHAT TO READ OFF THIS")
    print("=" * 72)
    print("""
  1. Chunk count falls roughly as 1/chunk_size. That part is arithmetic.

  2. The 'split level' column is the part worth remembering: the same text
     splits at word level, then line level, then paragraph level, purely
     because the budget grew. Choosing chunk_size is really choosing which
     unit of text a chunk should represent.

  3. The mid-word column is the difference between the two strategies. The
     recursive splitter keeps it at zero by dropping a structural level
     instead of cutting; fixed-size splitting cannot.

  Neither table says which chunk_size is BEST. That needs a retrieval metric
  and a labelled query set - see ../../14-rag-evaluation/.
""")

    # TODO for the experiment file:
    #   - run this sweep over a real document instead of a 4-line sample
    #   - once embeddings exist, plot retrieval quality against chunk_size


if __name__ == "__main__":
    main()
