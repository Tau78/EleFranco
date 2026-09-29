#!/usr/bin/env bash
# Copia solo ciò che serve a GitHub Pages (niente sorgenti Python / IDE / cache).
# Uso: bash scripts/prepare-pages-site.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/_site"
rm -rf "$OUT"
mkdir -p "$OUT"

copy_tree() {
  local src="$1"
  if [[ -e "$ROOT/$src" ]]; then
    mkdir -p "$(dirname "$OUT/$src")"
    cp -R "$ROOT/$src" "$OUT/$src"
  fi
}

# Static site
for f in index.html elefranco-lettura.html elefranco-libro.html colora-app.html .nojekyll EleFranco-Disegna.pdf; do
  [[ -e "$ROOT/$f" ]] && cp "$ROOT/$f" "$OUT/$f"
done
copy_tree css
copy_tree js
copy_tree capitoli
copy_tree sezioni
copy_tree Disegna
copy_tree Immagini

# README breve per chi apre la root su Pages (opzionale)
[[ -f "$ROOT/README.md" ]] && cp "$ROOT/README.md" "$OUT/README.md"

du -sh "$OUT" "$OUT"/* 2>/dev/null | sort -hr | head -20
echo "Prepared $OUT"
