# Rust Coder – Local Demo Overview

## Summary
This fork adds a local, two-command workflow to port Python/C++ repositories to Rust using Claude Code. It ships slash commands, minimal scripts, and a planning structure so users can run the flow without manual setup.

## Video demo
- Link: <ADD_YOUR_VIDEO_LINK_HERE>

## What’s included
- Slash commands (type “/” in Claude):
  - /rust:port — end-to-end porting flow (plan → implement per item → fmt/clippy/test → commit confirmations)
  - /rust:setup — ensure rustup, rustfmt, clippy
  - /rust:fmt — format Rust sources
  - /rust:clippy — lint (deny warnings)
  - /rust:test — run tests
- Scripts (lightweight, reproducible actions):
  - scripts/rustcoder/ensure_toolchain.sh
  - scripts/rustcoder/clone_repo.sh
  - scripts/rustcoder/test_and_lint.sh
  - scripts/rustcoder/scan_repo.py
  - scripts/rustcoder/plan_breakdown.py
  - scripts/rustcoder/implement_item.py
- Planning directories:
  - plans/ (overview.md will be generated)
  - plans/items/ (per-item plan markdowns)

## How to run (local)
1) Install CLI (once):
   ```
   npm i -g @anthropic-ai/claude-code
   ```
2) From the repo root:
   ```
   claude
   ```
   - Press “/” and select “/rust:port”
   - Provide the source repository URL when asked
   - Approve actions when prompted

## Porting flow (high-level)
1) Clone source repo into ./source_repo/
2) Generate planning docs:
   - plans/overview.md (purpose, architecture, endpoints, external services, deps)
   - plans/items/*.md (one per endpoint/integration/feature with DoD/checklist)
3) Review and approve plans
4) Implement items one by one inside ./rust_project/
   - Create/update Cargo project if missing
   - Add minimal tests
   - Run fmt, clippy (-D warnings), test
   - Confirm commit per item

## Directories used
- Source clone: ./source_repo
- Rust project: ./rust_project
- Plans: ./plans and ./plans/items

## Notes
- All commands and scripts are intentionally minimal to keep the demo focused.
- You remain in control: the agent asks before executing commands or writing files.

