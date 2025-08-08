#!/usr/bin/env python3
import os
import sys
from pathlib import Path

"""
Implement a single plan item. This is a stub that:
- Reads a plan item markdown path
- Prints next actions (to be executed by the agent)
A future version can generate code using an LLM and apply edits automatically.
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: implement_item.py <plans/items/<item>.md>", file=sys.stderr)
        sys.exit(1)

    item_path = Path(sys.argv[1])
    if not item_path.exists():
        print(f"Item file not found: {item_path}", file=sys.stderr)
        sys.exit(1)

    print("Implementing item from:", item_path)
    print("Next actions (to be performed by the agent):")
    print("1) Create/update Cargo workspace and crates as needed")
    print("2) Implement the functionality described in the item")
    print("3) Add minimal tests")
    print("4) Run cargo fmt, clippy (-D warnings), and test")


if __name__ == "__main__":
    main()
