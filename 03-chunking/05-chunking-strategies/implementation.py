"""
Chunking Strategies - the same text through different splitting rules
Section: Chunking

Goal
----
Run the three non-semantic strategies side by side and show the claim that
matters: strategies 2 and 3 are the SAME algorithm with different separator
lists.

  1. Length-based            CharacterTextSplitter(separator="")
  2. Text-structure-based    RecursiveCharacterTextSplitter()
  3. Document-structure      RecursiveCharacterTextSplitter.from_language(...)

Not implemented here: strategy 4 (semantic). SemanticChunker needs an
embedding model, and embeddings belong to section 04 which has not been
studied yet. Adding it now would mean writing code I do not understand.

Run:
    python implementation.py
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CHUNK_SIZE = 200
CHUNK_OVERLAP = 0

PROSE = (
    "Space exploration has led to incredible scientific discoveries. "
    "From landing on the Moon to exploring Mars, humanity keeps pushing.\n\n"
    "These missions expanded our knowledge of the universe. They also "
    "produced technology that benefits everyday life on Earth."
)

# Top-level functions with NO blank lines between them. The blank-line choice
# is deliberate: if the functions were separated by blank lines, the generic
# "\n\n" separator would find the same boundaries as "\ndef " and the two
# strategies would produce identical output - which would prove nothing.
PYTHON_CODE = '''\
def load(path):
    return open(path).read()
def chunk(text, size):
    return [text[i:i+size] for i in range(0, len(text), size)]
def embed(chunks):
    return [hash(c) for c in chunks]
'''

CODE_CHUNK_SIZE = 100

MARKDOWN_DOC = """\
# RAG Learning Lab

A repository for learning retrieval-augmented generation.

## Features

- Notes written by hand
- Runnable implementations

## Getting started

Install the requirements and start with the foundations section.
"""


# ===========================================================================
# Strategy runners
# ===========================================================================

def show(title: str, chunks: list[str]) -> None:
    print(f"\n  {title}")
    print(f"    -> {len(chunks)} chunks")
    for i, chunk in enumerate(chunks):
        preview = chunk.replace("\n", "\\n")
        if len(preview) > 62:
            preview = preview[:62] + "..."
        print(f"       [{i}] ({len(chunk):>3}) {preview}")


def main() -> None:
    try:
        from langchain_text_splitters import (
            CharacterTextSplitter,
            Language,
            RecursiveCharacterTextSplitter,
        )
    except ImportError:
        print("langchain-text-splitters is not installed.")
        print("Install with:  pip install langchain-text-splitters\n")
        print("This file compares splitter classes, so there is nothing")
        print("meaningful to run without them. The from-scratch versions of")
        print("strategies 1 and 2 live in ../01-fixed-size-chunking/ and")
        print("../02-recursive-chunking/ and need no installs.")
        return

    # -- Same prose, strategies 1 and 2 ------------------------------------
    print("=" * 72)
    print("PROSE - strategy 1 vs strategy 2")
    print("=" * 72)

    show(
        "1. Length-based (CharacterTextSplitter, separator='')",
        CharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, separator=""
        ).split_text(PROSE),
    )

    show(
        "2. Text-structure-based (RecursiveCharacterTextSplitter)",
        RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        ).split_text(PROSE),
    )
    print("\n    Strategy 2 lands on paragraph boundaries; strategy 1 lands")
    print("    wherever the counter ran out.")

    # -- Code: generic vs language-aware -----------------------------------
    print()
    print("=" * 72)
    print("PYTHON CODE - strategy 2 vs strategy 3")
    print("=" * 72)

    print(f"\n  (chunk_size = {CODE_CHUNK_SIZE} for this comparison)")

    show(
        "2. Generic recursive (paragraph/line/word separators)",
        RecursiveCharacterTextSplitter(
            chunk_size=CODE_CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        ).split_text(PYTHON_CODE),
    )
    print("       ^ note chunk 0: it ends with 'def chunk(text, size):' -")
    print("         a function signature severed from its body.")

    show(
        "3. from_language(Language.PYTHON)",
        RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON,
            chunk_size=CODE_CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        ).split_text(PYTHON_CODE),
    )
    print("       ^ one whole function per chunk.")

    # The proof that strategy 3 is not a new algorithm: only the list differs.
    print("\n  Why they differ - the separator lists:")
    generic = ["\n\n", "\n", " ", ""]
    python_seps = RecursiveCharacterTextSplitter.get_separators_for_language(
        Language.PYTHON
    )
    print(f"    generic : {generic}")
    print(f"    python  : {python_seps}")
    print("    Same class, same recursion, same merge step. Only the list of")
    print("    separators changed - and the Python list ENDS with the generic")
    print("    one, so ordinary text splitting takes over below 'class'/'def'.")

    print("\n  Limitation found while testing this:")
    print("    The Python separators are '\\nclass ', '\\ndef ' and '\\n\\tdef '.")
    print("    They match TOP-LEVEL definitions and tab-indented ones - but NOT")
    print("    space-indented methods inside a class. For an ordinary")
    print("    4-space-indented class body, none of them fire and the splitter")
    print("    falls straight through to the generic separators, giving output")
    print("    identical to strategy 2. Verified at every chunk size tried.")

    # -- Markdown ----------------------------------------------------------
    print()
    print("=" * 72)
    print("MARKDOWN - strategy 3")
    print("=" * 72)

    show(
        "3. from_language(Language.MARKDOWN)",
        RecursiveCharacterTextSplitter.from_language(
            language=Language.MARKDOWN,
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        ).split_text(MARKDOWN_DOC),
    )
    md_seps = RecursiveCharacterTextSplitter.get_separators_for_language(
        Language.MARKDOWN
    )
    print(f"\n    markdown separators: {md_seps}")
    print("    The first entry is a heading regex, so headings are preferred")
    print("    split points - which is why the sections come out whole.")

    print(f"\n    Language enum has {len(list(Language))} members: "
          f"{', '.join(m.value for m in list(Language)[:8])}, ...")

    # -- Strategy 4 --------------------------------------------------------
    print()
    print("=" * 72)
    print("STRATEGY 4 - SEMANTIC (not implemented here)")
    print("=" * 72)
    print("""
  SemanticChunker splits where the MEANING changes rather than where the
  structure does. It embeds each sentence, measures cosine similarity between
  consecutive sentences, and puts a breakpoint where similarity drops sharply.

  It is not implemented in this file for two reasons:
    - it requires an embedding model, which is section 04 and not yet studied
    - it lives in langchain_experimental, not the main library

  For reference, the shape of the call is:

      from langchain_experimental.text_splitter import SemanticChunker
      splitter = SemanticChunker(
          embeddings,
          breakpoint_threshold_type="standard_deviation",  # or percentile,
          breakpoint_threshold_amount=1,                   # interquartile, gradient
      )

  Come back and implement it after ../../04-embeddings/.
""")


if __name__ == "__main__":
    main()
