---
allowed-tools: Bash(cargo test *:*)
description: Run Rust tests with verbose output
---

Goal: Execute all tests and show concise results.

Instructions:
- Run `cargo test --all -- --nocapture`.
- Summarize passed/failed tests and any panics.
- If the workspace is not initialized yet, explain and stop.