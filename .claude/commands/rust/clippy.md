---
allowed-tools: Bash(cargo clippy *:*)
description: Lint rust_project with clippy (deny warnings)
---

Goal: Lint rust_project with strict clippy settings.

Instructions:
- Ensure the Rust project exists at ./rust_project (with Cargo.toml).
- Run `cargo clippy --manifest-path rust_project/Cargo.toml --all-targets -- -D warnings`.
- Summarize key diagnostics. Suggest fixes if common lints are triggered.
- If rust_project is missing, explain and stop.