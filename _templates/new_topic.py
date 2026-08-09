"""
Add a new topic folder to a section, using _templates/topic-template.

Usage:
    python _templates/new_topic.py <section-path> <nn-topic-slug> "Topic Title"

Example:
    python _templates/new_topic.py 07-advanced-retrieval 13-splade "SPLADE"
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "_templates" / "topic-template"


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 1

    section, slug, title = sys.argv[1], sys.argv[2], sys.argv[3]
    section_dir = ROOT / section
    target = section_dir / slug

    if not section_dir.is_dir():
        print(f"Section not found: {section_dir}")
        return 1
    if target.exists():
        print(f"Refusing to overwrite existing folder: {target}")
        return 1

    shutil.copytree(TEMPLATE, target)

    section_title = section_dir.name.split("-", 1)[-1].replace("-", " ").title()
    for path in target.rglob("*"):
        if path.suffix in {".md", ".py"}:
            text = path.read_text(encoding="utf-8")
            text = text.replace("<Topic Title>", title).replace("<Section>", section_title)
            path.write_text(text, encoding="utf-8")

    print(f"Created {target}")
    print("Next: add it to the section README table and to PROGRESS.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
