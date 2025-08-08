---
allowed-tools: Bash(cargo fmt *:*)
description: Format Rust code in rust_project using cargo fmt
---

Goal: Format all Rust sources in rust_project.

Instructions:
- Ensure the Rust project exists at ./rust_project (with Cargo.toml).
- Run `cargo fmt --manifest-path rust_project/Cargo.toml`.
- Report changed files succinctly.
- If rust_project is missing, explain and stop.