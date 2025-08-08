---
allowed-tools: Bash(cargo test *:*)
description: Run tests for rust_project with verbose output
---

Goal: Execute all tests in rust_project and show concise results.

Instructions:
- Ensure the Rust project exists at ./rust_project (with Cargo.toml).
- Run `cargo test --manifest-path rust_project/Cargo.toml --all -- --nocapture`.
- Summarize passed/failed tests and any panics.
- If rust_project is missing, explain and stop.