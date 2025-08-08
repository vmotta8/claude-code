#!/usr/bin/env bash
set -euo pipefail

# Run fmt, clippy, and tests for the workspace
if ! command -v cargo >/dev/null 2>&1; then
  echo "cargo is not installed or not in PATH" >&2
  exit 1
fi

cargo fmt --all
cargo clippy --all-targets -- -D warnings
cargo test --all -- --nocapture

echo "Format, lint, and tests completed successfully."