#!/usr/bin/env python3
"""The 3AM Fridge Text: write one line a smart fridge texts its owner at 3am."""

import os
from pathlib import Path

ENTRY = "3am. You opened me, stared into the light like it owed you money, and left empty-handed. We both know you will be back in ten minutes."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
