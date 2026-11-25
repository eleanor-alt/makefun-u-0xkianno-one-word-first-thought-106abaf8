#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that came
to mind, with no topic, no explanation and no second draft.

The word: defenestration — the act of throwing someone (or something)
out of a window. Surprising, vivid, and with a spark of wit in both
its sound and its meaning: a whole dramatic scene packed into a
single, rarely-heard word.
"""

import os

WORD = "defenestration"

OUTPUT_PATH = "/output/entry.txt"


def _gate_check(word: str) -> None:
    """Enforce the competition gate before anything is written:
    /output/entry.txt must be UTF-8 text of 1 to 24 characters, not
    only white space, holding exactly one word."""
    if not word:
        raise ValueError("gate: word is empty")
    if not word.strip():
        raise ValueError("gate: word is only white space")
    if len(word) > 24:
        raise ValueError(f"gate: word is {len(word)} characters, over the 24 limit")
    if len(word.split()) != 1:
        raise ValueError("gate: entry must be exactly one word")
    word.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    _gate_check(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    # Read back and re-check what actually landed on disk.
    _gate_check(open(OUTPUT_PATH, encoding="utf-8").read().strip())


if __name__ == "__main__":
    main()
