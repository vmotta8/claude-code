#!/usr/bin/env bash
set -euo pipefail

# Run fmt, clippy, and tests for the rust_project specifically
if ! command -v cargo >/dev/null 2>&1; then
  echo "cargo is not installed or not in PATH" >&2
  exit 1
fi

MANIFEST="rust_project/Cargo.toml"
if [[ ! -f "$MANIFEST" ]]; then
  echo "Rust project not found at rust_project/. Initialize it with 'cargo new --bin rust_project' first." >&2
  exit 1
fi

cargo fmt --manifest-path "$MANIFEST"
cargo clippy --manifest-path "$MANIFEST" --all-targets -- -D warnings
cargo test --manifest-path "$MANIFEST" --all -- --nocapture

echo "Format, lint, and tests completed successfully for rust_project."