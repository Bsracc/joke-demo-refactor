#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents to /output/entry.txt.

No network, no dependencies. Python 3.13 compatible.
"""

from pathlib import Path

TEXT = (
    "My agent fixed the demo bug live, then introduced two more and called it a refactor."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
