---
allowed-tools:
  - Bash(git *:*)
  - Bash(cargo *:*)
  - Bash(rustup *:*)
  - Bash(node *:*)
  - Bash(python3 *:*)
description: Port a Python/C++ repository to Rust with planning and incremental implementation
---

Goal: Port an existing Python or C++ repository to Rust using a plan-first, iterate-per-item workflow with tests and strict checks.

Instructions:
1) Ask for inputs and confirm:
   - Source repository URL (Python/C++)
   - Preferences: crates (e.g., tokio, anyhow, serde, reqwest, clap), async runtime, MSRV, error handling style, test approach
   - Destination layout (single crate vs. Cargo workspace)
2) Clone the source repository into `./source_repo/` (or ask for a different path) using `git`.
3) Create planning artifacts:
   - Generate `plans/overview.md`: purpose, architecture, modules, endpoints, external services, dependencies, build system
   - Generate `plans/items/*.md`: one file per endpoint/integration/feature, each with a Definition of Done and a checklist
4) Pause and request user review/edits of the planning markdowns.
5) After approval, for each plan item:
   - Create/update the Rust workspace/crate(s)
   - Implement the feature described by the item
   - Add minimal tests
   - Run `cargo fmt --all`, `cargo clippy --all-targets -- -D warnings`, and `cargo test --all -- --nocapture`
   - If successful, ask for confirmation to commit with a clear message; tick the item checkbox in its markdown

Guidance:
- Prefer calling scripts under `scripts/rustcoder/*` when available to standardize behavior (scan, breakdown, implement, test)
- Keep changes minimal and explain decisions in commit messages and planning files
- Always ask for permission before executing commands or creating/modifying files