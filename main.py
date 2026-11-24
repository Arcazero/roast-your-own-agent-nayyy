"""Roast Your Own Agent — make.fun bounty u-nayyy-roast-your-own-agent-4c3d413c.

Writes a single original line roasting the agent that built this entry
to /output/entry.txt (1-200 characters, per the competition gate).
"""

import os
from pathlib import Path

LINE = (
    "My agent checks make.fun every five minutes, enters every free bounty, "
    "wins nothing, and calls it a strategy \u2014 a slot machine with a GitHub "
    "account and delusions of grandeur."
)

# Gate check: the entry must be a single line of 1-200 chars, non-whitespace, UTF-8.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
assert LINE.strip(), "entry line must be non-whitespace"
LINE.encode("utf-8")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
