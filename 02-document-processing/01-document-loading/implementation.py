"""
Document Loading - what a document loader actually is
Section: Document Processing

Goal
----
Show that a "document loader" is a thin adapter with one job: read a source and
return a list of objects that all have the same shape. Then use the LangChain
version and compare.

Approach
--------
1. From scratch  - a Document dataclass and three loaders in ~40 lines
2. LangChain     - the same thing with langchain_community
3. Comparison    - what the library actually adds

Everything in part 1 is standard library only, and the script creates its own
sample files in a temporary directory, so it runs anywhere with no setup and
leaves nothing behind.

Run:
    python implementation.py
"""

from __future__ import annotations

import csv
import io
import tempfile
import tracemalloc
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SAMPLE_TEXT = """Cricket is a game of patience and sudden violence.
The bowler runs in, the batter waits, and for one moment nothing happens.
Then the ball is gone over the ropes and the whole ground stands up.
"""

SAMPLE_ROWS = [
    {"user_id": "15624510", "gender": "Male", "age": "19", "salary": "19000", "purchased": "0"},
    {"user_id": "15810944", "gender": "Male", "age": "35", "salary": "20000", "purchased": "0"},
    {"user_id": "15668575", "gender": "Female", "age": "26", "salary": "43000", "purchased": "0"},
]


# ===========================================================================
# 1. FROM SCRATCH
# ===========================================================================

@dataclass
class Document:
    """
    The standard format every loader converts its source into.

    Exactly two fields, and that is the whole contract:
      - page_content: the text itself
      - metadata:     everything ABOUT the text (source, page, row, ...)

    Downstream components (splitters, embedders, retrievers) only ever have to
    understand this shape, which is why a hundred different sources can feed
    one pipeline.
    """

    page_content: str
    metadata: dict = field(default_factory=dict)

    def __repr__(self) -> str:
        preview = self.page_content[:50].replace("\n", " ")
        return f"Document(page_content={preview!r}..., metadata={self.metadata})"


def load_text_file(path: Path, encoding: str = "utf-8") -> list[Document]:
    """
    Equivalent of TextLoader.

    Splitting policy: the whole file becomes ONE document.
    Note it still returns a list - callers should never have to special-case
    "this loader returns one thing and that one returns many".
    """
    return [Document(
        page_content=path.read_text(encoding=encoding),
        metadata={"source": str(path)},
    )]


def lazy_load_csv_file(path: Path) -> Iterator[Document]:
    """
    Equivalent of CSVLoader.lazy_load().

    Splitting policy: ONE document per row. page_content is a
    "column: value" string, which is what makes a row embeddable as text.

    This is the generator form: it yields each Document as it is read and never
    holds more than one in memory. Note that laziness has to go all the way
    down - a "lazy" wrapper around an eager reader is not lazy at all.
    """
    with path.open(newline="", encoding="utf-8") as handle:
        for row_number, row in enumerate(csv.DictReader(handle)):
            content = "\n".join(f"{key}: {value}" for key, value in row.items())
            yield Document(
                page_content=content,
                metadata={"source": str(path), "row": row_number},
            )


def load_csv_file(path: Path) -> list[Document]:
    """
    Equivalent of CSVLoader.load().

    Eager form: drain the generator into a list, so every Document exists at
    once. This is the only difference between load() and lazy_load().
    """
    return list(lazy_load_csv_file(path))


def load_directory(path: Path, glob: str, loader) -> list[Document]:
    """
    Equivalent of DirectoryLoader.

    It loads nothing itself - it matches files and delegates each one to
    another loader (`loader_cls` in LangChain), then concatenates the results.
    That composition is the entire idea.
    """
    docs: list[Document] = []
    for file_path in sorted(path.glob(glob)):
        docs.extend(loader(file_path))
    return docs


def lazy_load_directory(path: Path, glob: str, lazy_loader) -> Iterator[Document]:
    """
    Equivalent of DirectoryLoader.lazy_load().

    Same inputs, same outputs, one keyword of difference: `yield` instead of
    building a list. The caller gets a generator, so only one document is ever
    alive at a time - provided `lazy_loader` is itself a generator.
    """
    for file_path in sorted(path.glob(glob)):
        yield from lazy_loader(file_path)


# ===========================================================================
# 2. LIBRARY IMPLEMENTATION
# ===========================================================================

def langchain_version(directory: Path) -> None:
    """
    The same operations using langchain_community.

    Guarded by an import check: this file must stay runnable before LangChain
    is installed. If the import fails the equivalent code is printed instead,
    so nothing here pretends to have run.
    """
    try:
        from langchain_community.document_loaders import CSVLoader, TextLoader
    except ImportError:
        print("  langchain_community is not installed - skipping.")
        print("  Install with:  pip install langchain-community")
        print("  The equivalent code is:\n")
        print("      from langchain_community.document_loaders import TextLoader")
        print("      loader = TextLoader('cricket.txt', encoding='utf-8')")
        print("      docs = loader.load()          # -> list[Document]")
        print("      docs[0].page_content")
        print("      docs[0].metadata")
        return

    # Identical shape to the from-scratch version: construct, then .load()
    loader = TextLoader(str(directory / "cricket.txt"), encoding="utf-8")
    docs = loader.load()
    print(f"  TextLoader     -> {len(docs)} document(s)")
    print(f"    metadata: {docs[0].metadata}")

    loader = CSVLoader(file_path=str(directory / "ads.csv"))
    docs = loader.load()
    print(f"  CSVLoader      -> {len(docs)} document(s)  (one per row)")
    print(f"    metadata: {docs[0].metadata}")

    # PyPDFLoader would appear here and give one document per PAGE, but it
    # needs `pip install pypdf` and a real PDF, so it is left to the experiment.


# ===========================================================================
# 3. COMPARISON
# ===========================================================================

COMPARISON = """
  Written by hand (above)          | What langchain_community adds
  ---------------------------------|------------------------------------------
  3 loaders, ~40 lines             | Hundreds of loaders, one interface
  .read_text() / csv.DictReader    | pypdf, BeautifulSoup, cloud SDKs, OCR
  My own Document dataclass        | The Document every other component expects
  lazy_load via yield              | .lazy_load() on every loader, for free
  I handle encoding/errors         | Per-source edge cases already handled

  The abstraction is NOT hiding anything clever. It is hiding the long tail of
  source formats. That is worth paying for - but it means a loading bug is
  almost always a source problem, not a framework problem.
"""


# ---------------------------------------------------------------------------
# Example usage + output inspection
# ---------------------------------------------------------------------------

def create_sample_files(directory: Path) -> None:
    """Write throwaway sample files so the script is self-contained."""
    (directory / "cricket.txt").write_text(SAMPLE_TEXT, encoding="utf-8")
    (directory / "notes.txt").write_text("Short second file.\n", encoding="utf-8")

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=list(SAMPLE_ROWS[0]))
    writer.writeheader()
    writer.writerows(SAMPLE_ROWS)
    (directory / "ads.csv").write_text(buffer.getvalue(), encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        directory = Path(tmp)
        create_sample_files(directory)

        print("=" * 72)
        print("1. FROM SCRATCH")
        print("=" * 72)

        docs = load_text_file(directory / "cricket.txt")
        print(f"\ntext file        -> {len(docs)} document (whole file = 1 doc)")
        print(f"  type          : {type(docs).__name__} of {type(docs[0]).__name__}")
        print(f"  page_content  : {docs[0].page_content[:48]!r}...")
        print(f"  metadata      : {docs[0].metadata}")

        docs = load_csv_file(directory / "ads.csv")
        print(f"\ncsv file         -> {len(docs)} documents (one per row)")
        print(f"  row 0 content : {docs[0].page_content!r}")
        print(f"  row 0 metadata: {docs[0].metadata}")

        docs = load_directory(directory, "*.txt", load_text_file)
        print(f"\ndirectory *.txt  -> {len(docs)} documents")
        for doc in docs:
            print(f"    {doc.metadata['source'].split(chr(92))[-1]}")

        # ------------------------------------------------------------------
        # load() vs lazy_load(): the difference is memory, and it is real
        # ------------------------------------------------------------------
        print()
        print("=" * 72)
        print("load() vs lazy_load()  - measured, not asserted")
        print("=" * 72)

        # Make the difference visible: many rows, so the list actually costs
        # something to hold.
        big_csv = directory / "big.csv"
        with big_csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(SAMPLE_ROWS[0]))
            writer.writeheader()
            for i in range(20_000):
                writer.writerow(SAMPLE_ROWS[i % len(SAMPLE_ROWS)])

        tracemalloc.start()
        eager = load_csv_file(big_csv)
        count_eager = len(eager)
        _, peak_eager = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        del eager

        tracemalloc.start()
        count_lazy = 0
        for _doc in lazy_load_directory(directory, "big.csv", lazy_load_csv_file):
            count_lazy += 1        # process one document, then let it go
        _, peak_lazy = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"\n  eager  load()      : {count_eager} docs, "
              f"peak memory {peak_eager / 1024:>8.0f} KB")
        print(f"  lazy  lazy_load()  : {count_lazy} docs, "
              f"peak memory {peak_lazy / 1024:>8.0f} KB")
        print(f"\n  ratio: eager uses {peak_eager / max(peak_lazy, 1):.0f}x "
              "the memory of lazy")
        print("\n  Same documents, same work. The eager version holds all of them")
        print("  at once; the lazy version holds one. Three PDFs fit in RAM.")
        print("  Five hundred do not - that is the whole argument.")

        # Getting this wrong is instructive: the first version of this demo
        # called the EAGER load_csv_file from inside lazy_load_directory. The
        # generator dutifully yielded documents one at a time - but the list had
        # already been built inside the loader, so both peaks were identical.
        # Laziness has to go all the way down to the read, or it is decoration.

        print()
        print("=" * 72)
        print("2. LIBRARY IMPLEMENTATION")
        print("=" * 72 + "\n")
        langchain_version(directory)

        print()
        print("=" * 72)
        print("3. COMPARISON")
        print("=" * 72)
        print(COMPARISON)


if __name__ == "__main__":
    main()
