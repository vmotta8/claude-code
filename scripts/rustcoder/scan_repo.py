#!/usr/bin/env python3
import os
import sys
import json
from pathlib import Path

"""
Minimal repo scanner: emits a rough overview markdown at plans/overview.md
- Detects common entry points and build files
- Lists top-level dirs/files (excluding typical noise)
"""

IGNORES = {".git", ".github", ".venv", "venv", "node_modules", "target", ".idea", ".vscode", ".DS_Store"}
BUILD_HINTS = [
    "requirements.txt", "pyproject.toml", "setup.py",
    "CMakeLists.txt", "Makefile", "makefile",
]


def walk_tree(root: Path):
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        parts = rel.parts
        if any(p in IGNORES for p in parts):
            continue
        yield rel


def detect_overview(src: Path) -> str:
    lines = []
    lines.append(f"# Source Repository Overview\n")
    lines.append(f"Path: {src.resolve()}\n")

    # Build hints
    hints = [p for p in BUILD_HINTS if (src / p).exists()]
    if hints:
        lines.append("\n## Build/System Hints\n")
        for h in hints:
            lines.append(f"- {h}")

    # Entry points (simple heuristics)
    entries = []
    if (src / "main.py").exists():
        entries.append("main.py")
    if (src / "src/main.cpp").exists():
        entries.append("src/main.cpp")
    if (src / "app.py").exists():
        entries.append("app.py")
    if entries:
        lines.append("\n## Possible Entry Points\n")
        for e in entries:
            lines.append(f"- {e}")

    # Top-level structure
    lines.append("\n## Top-level Structure (filtered)\n")
    count = 0
    for rel in walk_tree(src):
        lines.append(f"- {rel}")
        count += 1
        if count > 500:
            lines.append("- ... (truncated)")
            break

    lines.append("\n## External Services / Dependencies (to confirm)\n")
    lines.append("- Review code for HTTP clients, DB drivers, cloud SDKs, CLI tools")

    lines.append("\n## Next Steps\n")
    lines.append("- Break down into items (endpoints/integrations/features)")
    return "\n".join(lines) + "\n"


def main():
    src_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "source_repo")
    plans_dir = Path("plans")
    plans_dir.mkdir(parents=True, exist_ok=True)

    if not src_dir.exists():
        print(f"Source directory not found: {src_dir}", file=sys.stderr)
        sys.exit(1)

    overview_md = detect_overview(src_dir)
    (plans_dir / "overview.md").write_text(overview_md, encoding="utf-8")
    print("Wrote plans/overview.md")


if __name__ == "__main__":
    main()
