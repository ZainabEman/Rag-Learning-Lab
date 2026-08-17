"""
Fixed-Size Chunking - length-based text splitting
Section: Chunking

Goal
----
Split text purely on a character count, from scratch, then compare with
LangChain's CharacterTextSplitter - including the two places where the library
does NOT behave the way "fixed size" suggests.

Approach
--------
1. From scratch  - a length splitter in ~10 lines
2. LangChain     - CharacterTextSplitter, and its separator/overshoot behaviour
3. Comparison    - where the two agree and where they deliberately differ

Part 1 is standard library only, so this file runs with no installs. Part 2 is
skipped with an explanation if langchain-text-splitters is not present.

Run:
    python implementation.py
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CHUNK_SIZE = 100
CHUNK_OVERLAP = 0

TEXT = (
    "Space exploration has led to incredible scientific discoveries. "
    "From landing on the Moon to exploring Mars, humanity continues to push "
    "the boundaries of what's possible beyond our planet.\n\n"
    "These missions have not only expanded our knowledge of the universe but "
    "have also contributed to technological advancements that benefit everyday "
    "life on Earth."
)


# ===========================================================================
# 1. FROM SCRATCH
# ===========================================================================

def split_by_length(text: str, chunk_size: int, chunk_overlap: int = 0) -> list[str]:
    """
    Walk the text and cut every `chunk_size` characters.

    No analysis of the content at all: if the counter runs out mid-word, the
    cut lands mid-word. That is the entire method, and the entire problem.

    `chunk_overlap` makes each chunk start slightly before the previous one
    ended, so the step between starts is (chunk_size - chunk_overlap).
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
            break        # the window already covered the tail
    return chunks


# ===========================================================================
# 2. LIBRARY IMPLEMENTATION
# ===========================================================================

def langchain_version() -> None:
    """
    CharacterTextSplitter, and the two surprises it holds.

    Guarded import so this file stays runnable before the install.
    """
    try:
        from langchain_text_splitters import CharacterTextSplitter
    except ImportError:
        print("  langchain-text-splitters is not installed - skipping.")
        print("  Install with:  pip install langchain-text-splitters")
        print("  The equivalent code is:\n")
        print("      from langchain_text_splitters import CharacterTextSplitter")
        print("      splitter = CharacterTextSplitter(")
        print("          chunk_size=100, chunk_overlap=0, separator='')")
        print("      chunks = splitter.split_text(text)")
        return

    # -- Surprise 1: the default separator is "\n\n", not "" ----------------
    # Out of the box this is a PARAGRAPH splitter that merges paragraphs up to
    # chunk_size. It is not a fixed-size splitter until you tell it to be.
    default = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=0)
    default_chunks = default.split_text(TEXT)
    print(f"  default separator ('\\n\\n'): {len(default_chunks)} chunks, "
          f"lengths {[len(c) for c in default_chunks]}")

    # Pure length behaviour requires separator=""
    pure = CharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=0, separator="")
    pure_chunks = pure.split_text(TEXT)
    print(f"  separator='' (pure length): {len(pure_chunks)} chunks, "
          f"lengths {[len(c) for c in pure_chunks]}")

    # -- Surprise 2: chunk_size is a merge budget, not a hard cap -----------
    # The splitter divides on the separator FIRST, then merges pieces up to
    # chunk_size. A piece that is already larger than chunk_size cannot be
    # shrunk, so it comes back oversized. LangChain logs a WARNING for some of
    # these cases (never an exception) - and for the case below, none at all.
    one_long_paragraph = "word " * 60           # 300 chars, no blank lines
    overshoot = CharacterTextSplitter(chunk_size=50, chunk_overlap=0)
    result = overshoot.split_text(one_long_paragraph)
    print(f"\n  asked for chunk_size=50 on a 300-char paragraph with no '\\n\\n':")
    print(f"    got {len(result)} chunk(s), longest = {max(len(c) for c in result)} chars")
    print("    -> chunk_size exceeded, and this case logs nothing")

    # The recursive splitter does not have this problem: its separator list
    # ends in "", so there is always a level left to fall back to.
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    rec = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0)
    rec_result = rec.split_text(one_long_paragraph)
    print(f"    same input through RecursiveCharacterTextSplitter: "
          f"{len(rec_result)} chunks, longest = {max(len(c) for c in rec_result)}")

    return pure_chunks


# ===========================================================================
# 3. COMPARISON
# ===========================================================================

def compare(mine: list[str], theirs: list[str] | None) -> None:
    if theirs is None:
        print("  (library not installed - nothing to compare)")
        return

    print(f"  from scratch : {len(mine)} chunks, lengths {[len(c) for c in mine]}")
    print(f"  CharacterTextSplitter(separator=''): {len(theirs)} chunks, "
          f"lengths {[len(c) for c in theirs]}")

    if [len(c) for c in mine] == [len(c) for c in theirs]:
        print("  -> identical chunk boundaries")
    else:
        print("  -> boundaries differ: the library strips whitespace at chunk")
        print("     edges (strip_whitespace=True by default), so its chunks can")
        print("     be a few characters shorter than the raw slice.")


# ---------------------------------------------------------------------------
# Example usage + output inspection
# ---------------------------------------------------------------------------

def main() -> None:
    print("=" * 72)
    print("1. FROM SCRATCH")
    print("=" * 72)
    chunks = split_by_length(TEXT, CHUNK_SIZE, CHUNK_OVERLAP)
    print(f"text length = {len(TEXT)} chars, chunk_size = {CHUNK_SIZE}")
    print(f"-> {len(chunks)} chunks (expected ceil({len(TEXT)}/{CHUNK_SIZE}) = "
          f"{-(-len(TEXT) // CHUNK_SIZE)})\n")
    for i, chunk in enumerate(chunks):
        print(f"  [{i}] ({len(chunk):>3} chars) {chunk!r}")

    # Output inspection: where did the cuts actually land?
    print("\n  cut quality - the last 12 chars of each chunk:")
    for i, chunk in enumerate(chunks[:-1]):
        tail = chunk[-12:]
        clean = chunk.endswith((" ", ".", "\n"))
        print(f"    [{i}] ...{tail!r}  {'clean break' if clean else 'CUT MID-WORD'}")

    print()
    print("=" * 72)
    print("2. LIBRARY IMPLEMENTATION")
    print("=" * 72 + "\n")
    library_chunks = langchain_version()

    print()
    print("=" * 72)
    print("3. COMPARISON")
    print("=" * 72)
    compare(chunks, library_chunks)

    print("\n  Takeaway: length-based splitting is one counter and no judgement.")
    print("  It is the fastest strategy and the one most likely to cut an idea")
    print("  in half. See ../02-recursive-chunking/ for the structure-aware fix.")

    # TODO for the experiment file:
    #   - count how many chunks end mid-word at different chunk sizes
    #   - repeat with token-based sizing via CharacterTextSplitter.from_tiktoken_encoder


if __name__ == "__main__":
    main()
