---
allowed-tools: Bash(rustup *:*), Bash(cargo *:*), Bash(sh *:*), Bash(sudo *:*)
description: Validate and install Rust toolchain (rustup, rustfmt, clippy)
---

Goal: Ensure a working Rust toolchain.

Steps:
- Check if `rustup` is installed. If missing, guide the user to install it for their OS.
- Ensure required components are present:
  - `rustup component add rustfmt clippy`
- Show versions for visibility:
  - `rustc --version`
  - `cargo --version`

Notes:
- Do not modify unrelated files.
- If installation requires elevated privileges, explain why before attempting.