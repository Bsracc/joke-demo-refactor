#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents to /output/entry.txt.

No network, no dependencies. Python 3.13.
The text is 84 characters, within the 1-280 limit.
"""

from pathlib import Path

TEXT = (
    "My agent fixed the demo bug live, then introduced two more and called it a refactor."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
