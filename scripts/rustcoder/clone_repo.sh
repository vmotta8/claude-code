#!/usr/bin/env bash
set -euo pipefail

SRC_URL=${1:-}
DEST_DIR=${2:-source_repo}

if [[ -z "${SRC_URL}" ]]; then
  echo "Usage: $0 <source_repo_url> [dest_dir]" >&2
  exit 1
fi

if [[ -d "${DEST_DIR}" ]]; then
  echo "Destination ${DEST_DIR} exists. Pulling latest..."
  git -C "${DEST_DIR}" pull --rebase --autostash || true
else
  echo "Cloning ${SRC_URL} into ${DEST_DIR}..."
  git clone --depth 1 "${SRC_URL}" "${DEST_DIR}"
fi

echo "Repository ready at ${DEST_DIR}"