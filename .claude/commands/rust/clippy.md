---
allowed-tools: Bash(cargo clippy *:*)
description: Lint Rust code with clippy (deny warnings)
---

Goal: Lint the workspace with strict clippy settings.

Instructions:
- Run `cargo clippy --all-targets -- -D warnings`.
- Summarize key diagnostics. Suggest fixes if common lints are triggered.
- If the workspace is not initialized yet, explain and stop.