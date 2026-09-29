#!/usr/bin/env python3
"""Avvia un agente Cursor per applicare le revisioni pendenti (opzionale, richiede API key)."""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent

PROMPT = """Applica le revisioni pendenti del libro EleFranco.

1. Leggi `revisioni.json`, `Revisioni.md` e `.cursor-revisioni-inbox.md`.
2. Per ogni evidenziazione con status `pending`:
   - trova il passaggio nel file sorgente corretto (`episodes_base.py`, `episodes_extra.py`, `episodes_season2.py`, `episodes_speciali.py`)
   - riscrivi il testo rispettando il canone EleFranco e le note dell'autore
3. Esegui `python3 aggiorna_libro.py` e `python3 statistiche_libro.py`.
4. In `revisioni.json` imposta `status: applied` sulle revisioni completate.
5. Rigenera `Revisioni.md` e `.cursor-revisioni-inbox.md` coerenti con lo store.

Non chiedere conferma: procedi con le revisioni pendenti."""


def main() -> int:
    api_key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not api_key:
        print("CURSOR_API_KEY non impostata — salto avvio agente.", file=sys.stderr)
        return 0

    from revisioni_store import load_store, pending_count

    if pending_count(load_store()) <= 0:
        print("Nessuna revisione pendente.")
        return 0

    try:
        from cursor_sdk import Agent, AgentOptions, LocalAgentOptions
    except ImportError:
        print(
            "cursor-sdk non installato. Esegui: pip install cursor-sdk",
            file=sys.stderr,
        )
        return 1

    print("Avvio agente Cursor per revisioni pendenti…")
    result = Agent.prompt(
        PROMPT,
        AgentOptions(
            api_key=api_key,
            model=os.environ.get("CURSOR_REVISIONI_MODEL", "composer-2.5"),
            local=LocalAgentOptions(cwd=str(ROOT)),
        ),
    )
    print(f"Agente terminato: {result.status}")
    if result.result:
        print(result.result[:2000])
    return 0 if result.status == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
