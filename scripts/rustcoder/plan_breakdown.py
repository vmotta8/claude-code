#!/usr/bin/env python3
import os
import sys
from pathlib import Path

"""
Minimal plan breakdown: reads plans/overview.md and emits placeholder items under plans/items/
The agent will refine these per the conversation.
"""

ITEM_TITLES = [
    "api_endpoints",
    "external_integrations",
    "core_logic",
    "config_and_cli",
    "data_models",
    "error_handling",
    "testing_setup",
]


def main():
    plans_dir = Path("plans")
    items_dir = plans_dir / "items"
    overview = plans_dir / "overview.md"

    if not overview.exists():
        print("Missing plans/overview.md", file=sys.stderr)
        sys.exit(1)

    items_dir.mkdir(parents=True, exist_ok=True)

    for name in ITEM_TITLES:
        p = items_dir / f"{name}.md"
        if not p.exists():
            p.write_text(
                f"""# Plan Item: {name}

Definition of Done:
- Implement the functionality described for {name}
- Add minimal tests
- Pass cargo fmt, clippy (-D warnings), and test

Tasks:
- [ ] Outline the Rust modules and crates involved
- [ ] Implement core code
- [ ] Write tests
- [ ] Update planning docs with notes/decisions
""",
                encoding="utf-8",
            )
            print(f"Created {p}")
        else:
            print(f"Exists {p}")


if __name__ == "__main__":
    main()
