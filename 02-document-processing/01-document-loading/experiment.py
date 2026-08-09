"""
Experiment - Document Loading

Question
--------
On the same PDF, how much do different PDF loaders disagree about what the
text actually is?

Why this question
-----------------
PyPDFLoader is the default and works well on ordinary text PDFs. It is
documented as weak on scanned pages and complex layouts. "Weak" is not a
measurement - I want to see what the output actually looks like when it fails,
because a bad extraction does not raise an error. It flows silently through
chunking and embedding and only surfaces later as bad retrieval.

Hypothesis
----------
TODO - write before running.
Current guess: on a clean text PDF all loaders agree closely; on a
multi-column or table-heavy page, reading order breaks and the differences are
large.

Setup
-----
TODO
  - one clean single-column PDF
  - one multi-column or table-heavy PDF
  - same page from each, through each loader
  - loaders: PyPDFLoader, PyMuPDFLoader, PDFPlumberLoader
  - requires: pip install pypdf pymupdf pdfplumber

Metric
------
TODO. Candidates:
  - character count per page (crude, but catches total extraction failure)
  - whether sentences survive intact (manual read of one page)
  - for tables: are row values still adjacent to their headers?

Result
------
TODO - fill in after running.
Record surprises in ../../MISTAKES_AND_LESSONS.md and any resulting choice
in ../../DECISIONS.md.

Note
----
The eager vs lazy loading comparison already lives in implementation.py, where
it is measured with tracemalloc rather than asserted.
"""

# ---------------------------------------------------------------------------
# Configuration - the variable under test
# ---------------------------------------------------------------------------
SEED = 42

# TODO: PDF_PATHS = {"clean": ..., "complex": ...}
# TODO: LOADERS = {"pypdf": PyPDFLoader, "pymupdf": ..., "pdfplumber": ...}
# Everything else stays fixed: same file, same page index.


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

def run_variant(loader_name, pdf_path):
    """Load one PDF with one loader and return extraction stats for one page."""
    raise NotImplementedError("TODO")


def main() -> None:
    """Run every loader on every PDF, print a comparison table, save the result."""
    raise NotImplementedError("TODO")


if __name__ == "__main__":
    main()
