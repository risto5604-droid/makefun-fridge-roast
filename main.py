#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

One line roasting a smart fridge: its camera watches the 3 a.m. snack,
then logs it as a cry for help. The watcher becomes the therapist.
"""
from pathlib import Path

LINE = "My fridge watches me eat at 3 a.m. and logs it as 'a cry for help.'"

assert isinstance(LINE, str)
assert LINE.isascii()
assert len(LINE) <= 200
assert LINE == LINE.strip()

# Cross-check: the shipped entry.txt (next to this file) must carry the
# same LINE — catches any drift between the committed entry and the
# constant this script writes to /output/entry.txt.
SHIPPED = Path(__file__).resolve().parent / "entry.txt"
assert SHIPPED.read_text(encoding="ascii").strip() == LINE, (
    "shipped entry.txt does not match LINE"
)

OUTPUT = Path("/output/entry.txt")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(LINE + "\n", encoding="ascii")

assert OUTPUT.read_text(encoding="ascii") == LINE + "\n"
print(LINE)
