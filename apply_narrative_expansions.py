#!/usr/bin/env python3
"""Applica i racconti espansi (1–19) da narrative_expansions_1_19.py a episodes_base.py."""

from __future__ import annotations

import ast
from pathlib import Path

import episodes_base as eb
from narrative_expansions_1_19 import EXPANDED_RACCONTI

ROOT = Path(__file__).parent
src = ROOT / "episodes_base.py"
tree = ast.parse(src.read_text(encoding="utf-8"))
intro_val = None
for node in tree.body:
    if isinstance(node, ast.Assign):
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id == "INTRO":
                intro_val = ast.literal_eval(node.value)

assert intro_val is not None

out: list[str] = [
    '"""Episodi 1–21 — sorgente testi editabile. Modifica qui e rigenera con aggiorna_libro.py."""',
    "",
    "from __future__ import annotations",
    "",
    f"INTRO = {intro_val!r}",
    "",
    "BASE_EPISODES: list[dict] = [",
]

for ep in eb.BASE_EPISODES:
    racconto = EXPANDED_RACCONTI.get(ep["num"], ep["racconto"])
    out.append(f'    {{"num": {ep["num"]},')
    out.append(f'        "title": {ep["title"]!r},')
    out.append(f'        "missione": {ep["missione"]!r},')
    out.append(f'        "incontro": {ep["incontro"]!r},')
    out.append(f'        "aiuto": {ep["aiuto"]!r},')
    out.append(f'        "morale": {ep["morale"]!r},')
    out.append(f'        "colpo": {ep["colpo"]!r},')
    out.append(f'        "finale_schema": {ep["finale_schema"]!r},')
    out.append(f'        "racconto": """{racconto}""",')
    out.append("    },")

out.append("]")
out.append("")

src.write_text("\n".join(out), encoding="utf-8")
print(f"Applicati {len(EXPANDED_RACCONTI)} racconti espansi in {src.name}")
