#!/usr/bin/env bash
set -euo pipefail

# Ensure rustup is installed
if ! command -v rustup >/dev/null 2>&1; then
  echo "rustup is not installed. Please install rustup first: https://rustup.rs"
  exit 1
fi

# Update toolchain and ensure components
rustup show >/dev/null
rustup component add rustfmt clippy || true

# Show versions
rustc --version
cargo --version

echo "Rust toolchain verified."