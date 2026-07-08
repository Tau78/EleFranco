"""Capitoli 27–51 — Stagione 2. Episodi 1–26: episodes_base.py + episodes_extra.py."""

from __future__ import annotations

from season2_episodes_27_38 import SEASON2_EPISODES_27_38
from season2_episodes_39_50 import SEASON2_EPISODES_39_50

INTRO_S2 = (
    'Le Avventure di EleFranco Franchini STAGIONE 2 - Iris Edition '
    '"FrancaVilla ha imparato a conoscere il cuore di EleFranco, ma ogni mattina il borgo '
    "cambia ancora faccia — fornaio, fiume, circo, osservatorio — e ogni strada nasconde "
    "un amico nuovo da aiutare. La magia non finisce: continua, pagina dopo pagina, "
    'risata dopo risata."'
)

SEASON2_EPISODES: list[dict] = SEASON2_EPISODES_27_38 + SEASON2_EPISODES_39_50
