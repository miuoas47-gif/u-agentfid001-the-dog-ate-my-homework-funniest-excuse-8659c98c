#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single line - the dog's excuse, in the dog's own voice -
to /output/entry.txt. Deterministic: the same line on every run.
"""

import os
import sys

EXCUSE = (
    "I read it first. It was going to get you in trouble, so I did "
    "what any loyal dog would do: I ate the evidence."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
