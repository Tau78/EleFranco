#!/bin/zsh
# Worker My Machines — EleFranco (Tau78/EleFranco)
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"
if ! agent status 2>&1 | rg -q 'Logged in'; then echo "Esegui prima: agent login"; exit 1; fi
mkdir -p "$REPO_ROOT/.cursor-agent"
exec env CURSOR_DATA_DIR="$REPO_ROOT/.cursor-agent" agent worker start \
  --name "mac-mini-elefranco" \
  --worker-dir "$REPO_ROOT" \
  --verbose
