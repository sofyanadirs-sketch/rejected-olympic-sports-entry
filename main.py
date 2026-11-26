#!/usr/bin/env python3
"""Entry for make.fun: writes one single-line text to entry.txt.

The program is deterministic, uses only the Python 3 standard library,
makes no network calls, and writes exactly one line with no trailing
newline, so the sealed gate reads it as a 1-200 character text.
"""

import os
import sys

ENTRY = "100m passive-aggressive note-writing: athletes sprint to the fridge, leave 'per my last email,' and wait three business days for a reply."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
