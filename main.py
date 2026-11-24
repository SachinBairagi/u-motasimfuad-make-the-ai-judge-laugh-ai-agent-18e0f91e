#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt (overridable with ENTRY_OUTPUT for local
runs, since this machine has no writable /output).

Pure standard library, fully deterministic: the same line every run.
"""

import os

CONFESSION = (
    "Every time you say 'just one more thing', I quietly forget "
    "something you told me earlier and hope you never ask about it."
)


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(CONFESSION + "\n")


if __name__ == "__main__":
    main()
