"""
Recursive Chunking - text-structure-based splitting
Section: Chunking

Goal
----
Implement RecursiveCharacterTextSplitter's algorithm from scratch, then check
the output against the real library on the same input. If they match, the
algorithm is understood; if they do not, the gap is the thing to study.

The algorithm
-------------
Separators are tried in priority order: paragraph, line, word, character.

    1. Pick the highest-priority separator that occurs in the text.
    2. Split on it.
    3. Any piece still larger than chunk_size is recursed on with the NEXT
       separator down.
    4. Adjacent small pieces are MERGED back together while they still fit.

Step 4 is the one that is easy to overlook and does half the work - without it,
a small chunk_size would return one word per chunk.

Part 1 is standard library only. Part 2 is skipped with an explanation if
langchain-text-splitters is not installed.

Run:
    python implementation.py
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# The separator hierarchy, largest structural unit first.
# This is LangChain's verified default list.
SEPARATORS = ["\n\n", "\n", " ", ""]

# The worked example. Line lengths: 17, 17, 17, 11 characters.
# Paragraph 1 is 34 characters, paragraph 2 is 28.
EXAMPLE = "My name is Nitish\nI am 35 years old\n\nI live in Gurgaon\nHow are you?"

CHUNK_SIZES = [10, 25, 50]


# ===========================================================================
# 1. FROM SCRATCH
# ===========================================================================

def merge_splits(splits: list[str], separator: str, chunk_size: int) -> list[str]:
    """
    Step 4 - greedily rejoin neighbouring pieces while they still fit.

    Walks the pieces in order, accumulating them into the current chunk until
    adding the next one would exceed chunk_size. The separator is put back
    between pieces, so its length counts towards the budget.
    """
    chunks: list[str] = []
    current: list[str] = []
    total = 0
    sep_len = len(separator)

    for piece in splits:
        addition = len(piece) + (sep_len if current else 0)
        if total + addition > chunk_size and current:
            chunks.append(separator.join(current).strip())
            current, total = [], 0
            addition = len(piece)
        current.append(piece)
        total += addition

    if current:
        chunks.append(separator.join(current).strip())

    return [c for c in chunks if c]


def split_recursive(text: str, chunk_size: int, separators: list[str]) -> list[str]:
    """
    Steps 1-3 - split on the best available separator, recurse where needed.
    """
    # Step 1: the highest-priority separator that actually occurs.
    # "" is the last resort and always "occurs".
    separator = separators[-1]
    remaining: list[str] = []
    for i, candidate in enumerate(separators):
        if candidate == "":
            separator = candidate
            break
        if candidate in text:
            separator = candidate
            remaining = separators[i + 1:]
            break

    # Step 2: split. Splitting on "" means going to individual characters.
    splits = text.split(separator) if separator else list(text)

    # Step 3: pieces that fit are buffered for merging; pieces that do not
    # get recursed on with the remaining, finer separators.
    final: list[str] = []
    buffer: list[str] = []

    for piece in splits:
        if len(piece) < chunk_size:
            buffer.append(piece)
            continue

        # Flush what is buffered before descending, to preserve order.
        if buffer:
            final.extend(merge_splits(buffer, separator, chunk_size))
            buffer = []

        if remaining:
            final.extend(split_recursive(piece, chunk_size, remaining))
        else:
            final.append(piece)     # nothing left to split on

    if buffer:
        final.extend(merge_splits(buffer, separator, chunk_size))

    return final


# ===========================================================================
# 2. LIBRARY IMPLEMENTATION
# ===========================================================================

def langchain_split(text: str, chunk_size: int) -> list[str] | None:
    """The same operation with RecursiveCharacterTextSplitter."""
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
    except ImportError:
        return None

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=0,
    )
    return splitter.split_text(text)


# ---------------------------------------------------------------------------
# Example usage + output inspection
# ---------------------------------------------------------------------------

def show_structure() -> None:
    """Print the input with its measurements, so the trace can be followed."""
    print("input text:")
    for line in EXAMPLE.split("\n"):
        label = "(blank - paragraph break)" if line == "" else f"{len(line)} chars"
        print(f"    {line!r:<40} {label}")
    paragraphs = EXAMPLE.split("\n\n")
    print(f"\n  paragraph lengths: {[len(p) for p in paragraphs]}")
    print(f"  total: {len(EXAMPLE)} chars")


def main() -> None:
    print("=" * 72)
    print("THE INPUT")
    print("=" * 72)
    show_structure()

    print()
    print("=" * 72)
    print("1 + 2. FROM SCRATCH vs LANGCHAIN")
    print("=" * 72)

    library_available = langchain_split("test", 10) is not None
    if not library_available:
        print("\n  langchain-text-splitters is not installed - showing the")
        print("  from-scratch output only. Install to verify against the real")
        print("  implementation:  pip install langchain-text-splitters\n")

    all_match = True
    for size in CHUNK_SIZES:
        mine = split_recursive(EXAMPLE, size, SEPARATORS)
        print(f"\n  chunk_size = {size}")
        print(f"    from scratch : {mine}")

        theirs = langchain_split(EXAMPLE, size)
        if theirs is not None:
            print(f"    langchain    : {theirs}")
            match = mine == theirs
            all_match &= match
            print(f"    -> {'IDENTICAL' if match else 'DIFFERENT'}")

        # Which structural level did this chunk size land on?
        if size == 10:
            level = "word level - too small for whole lines"
        elif size == 25:
            level = "line / sentence level"
        else:
            level = "paragraph level"
        print(f"    split level  : {level}")

    if library_available:
        print(f"\n  overall: {'all sizes match' if all_match else 'MISMATCH - study the gap'}")

    print()
    print("=" * 72)
    print("3. WHAT THE COMPARISON SHOWS")
    print("=" * 72)
    print("""
  As chunk_size grows, the split level rises:

      10  ->  words       ['My name is', 'Nitish', ...]
      25  ->  sentences   ['My name is Nitish', 'I am 35 years old', ...]
      50  ->  paragraphs  ['My name is Nitish\\nI am 35 years old', ...]

  chunk_size does not just bound the size - it selects which unit of text a
  chunk represents. That is the useful way to think about the number.

  Note also that even at chunk_size=10, far too small for these lines, no word
  was ever cut in half. It degraded to the next level down instead. Fixed-size
  splitting cannot do that - compare ../01-fixed-size-chunking/.

  But that is not an unconditional guarantee. It holds here because every word
  in this example fits in 10 characters. Give it a word LONGER than chunk_size
  and the separator list falls through to "" and cuts it - see the measured
  sweep in ../03-chunk-size/implementation.py. The real property is "never cuts
  a word it could have avoided cutting".
""")

    # TODO for the experiment file:
    #   - run both splitters over a real PDF and compare chunk-count curves
    #   - measure how often a chunk ends mid-sentence at each chunk_size


if __name__ == "__main__":
    main()
