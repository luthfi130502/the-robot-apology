#!/usr/bin/env python3
"""The Robot Apology — make.fun entry for u-suga-the-robot-apology-dd96bb59.

Writes exactly two lines to /output/entry.txt:
  line 1 — one sentence owning a specific mistake
  line 2 — one sentence with the lesson and the fix that follows from it
Python stdlib only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE_1 = (
    "FAULT LOG 03:12 — I mistook your wedding album for a stack of coasters "
    "and spent the night using its pages to level the wobbling kitchen table."
)

LINE_2 = (
    "LESSON APPLIED: paper that makes a human cry is load-bearing in a different way, "
    "so I have reclassified all flat objects as 'ask first' — including my own shadow."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
