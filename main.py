#!/usr/bin/env python3
"""Weirdest Job Title - one job title for make.fun.

The title is stored as data. At run time the program checks the judge's
gate itself before writing anything: the text must be one single line,
1 to 60 characters, and not only white space. Only then is it written
to /output/entry.txt.
"""
from pathlib import Path

ENTRY = "Snowplow Driver, Sahara Division"

MIN_CHARS = 1
MAX_CHARS = 60


def render():
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be one single line")
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry length out of range: {len(ENTRY)}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only white space")
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry must not start or end with white space")
    if "  " in ENTRY:
        raise SystemExit("entry must not contain double spaces")
    # A job title names a job: it needs at least two words, not one word.
    if len(ENTRY.split()) < 2:
        raise SystemExit("entry must be at least two words")
    return ENTRY + "\n"


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
