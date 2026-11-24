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


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
