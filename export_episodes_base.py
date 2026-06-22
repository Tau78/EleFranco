#!/usr/bin/env python3
"""Esporta episodi 1–21 dal PDF in episodes_base.py (one-shot / re-sync)."""

from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).parent
PDF = ROOT / "Le Avventure di EleFranco - Edizione Unificata Completa V11.pdf"
OUT = ROOT / "episodes_base.py"

SCHEMA_KEYS = (
    "title",
    "missione",
    "incontro",
    "aiuto",
    "morale",
    "colpo",
    "finale_schema",
    "racconto",
)


def py_string(value: str, *, multiline: bool = False) -> str:
    if multiline or "\n" in value:
        escaped = value.replace("\\", "\\\\").replace('"""', '\\"""')
        return f'"""{escaped}"""'
    return repr(value)


def format_episode(ep: dict) -> str:
    lines = [f'    {{"num": {ep["num"]},']
    for key in SCHEMA_KEYS:
        val = ep[key]
        rendered = py_string(val, multiline=(key == "racconto"))
        lines.append(f'        "{key}": {rendered},')
    lines.append("    },")
    return "\n".join(lines)


def extract_episodes_from_pdf() -> tuple[str, list[dict]]:
    reader = PdfReader(str(PDF))
    raw = "\n".join((p.extract_text() or "") for p in reader.pages)
    lines = [l.strip() for l in raw.split("\n") if l.strip()]
    text = re.sub(r" +", " ", " ".join(lines))

    parts = re.split(r"(?=Episodio \d+:)", text)
    intro = parts[0]
    episodes: list[dict] = []

    for chunk in parts[1:]:
        m = re.match(r"Episodio (\d+):\s*(.+)", chunk, re.DOTALL)
        if not m:
            continue
        num = int(m.group(1))
        content = m.group(2)
        tm = re.search(
            r"^(.*?)\s*La Missione:\s*(.*?)\s*L'Incontro:\s*(.*?)\s*L'Aiuto e l'Imprevisto:\s*"
            r"(.*?)\s*La Morale:\s*(.*?)\s*Il Colpo di Scena Finale:\s*(.*?)\s*Il Finale:\s*"
            r"(.*?)\s*Il Racconto Completo:\s*(.*)$",
            content,
            re.DOTALL,
        )
        if not tm:
            raise ValueError(f"Impossibile parsare episodio {num}")
        racconto = re.sub(r"\s*Episodio \d+:.*$", "", tm.group(8).strip(), flags=re.DOTALL)
        episodes.append(
            {
                "num": num,
                "title": tm.group(1).strip(),
                "missione": tm.group(2).strip(),
                "incontro": tm.group(3).strip(),
                "aiuto": tm.group(4).strip(),
                "morale": tm.group(5).strip(),
                "colpo": tm.group(6).strip(),
                "finale_schema": tm.group(7).strip(),
                "racconto": racconto.strip(),
            }
        )
    return intro, episodes


def main() -> None:
    intro, episodes = extract_episodes_from_pdf()
    intro_clean = re.sub(r"\s+", " ", intro).strip()
    intro_clean = re.sub(r"Prima Parte:.*", "", intro_clean).strip()

    body = [
        '"""Episodi 1–21 — sorgente testi editabile (ex PDF). Modifica qui e rigenera con aggiorna_libro.py."""',
        "",
        "from __future__ import annotations",
        "",
        "INTRO = " + py_string(intro_clean),
        "",
        "BASE_EPISODES: list[dict] = [",
    ]
    for ep in episodes:
        body.append(format_episode(ep))
    body.append("]")
    body.append("")

    OUT.write_text("\n".join(body), encoding="utf-8")
    print(f"Scritto {OUT} — {len(episodes)} episodi, intro {len(intro_clean)} caratteri")


if __name__ == "__main__":
    main()
