"""Ordine di lettura e ripartizione parti — Stagione 1.

Modifica qui per spostare capitoli tra le parti o cambiare l'ordine di lettura
(senza rinumerare gli episodi: Disegna/NN.jpeg resta legato al num).
"""

from __future__ import annotations

SEASON1_LAST = 25

SEASON1_PARTS: list[dict] = [
    {
        "slug": "parte-01",
        "toc_label": "Prima Parte: Missioni Quotidiane 🏡",
        "fragment": "parte_01",
        "episodes": [1, 2, 3, 4, 5, 6, 7, 8],
    },
    {
        "slug": "parte-02",
        "toc_label": "Seconda Parte: Intoppi e Soluzioni 🛠",
        "fragment": "parte_02",
        "episodes": [9, 10, 11, 12, 13, 14, 15, 16, 17],
    },
    {
        "slug": "parte-03",
        "toc_label": "Terza Parte: Nuovi Amici 🌱",
        "fragment": "parte_03",
        # Iris (23) chiude la stagione — dedica Iris Edition
        "episodes": [18, 19, 20, 21, 22, 24, 25, 23],
    },
]

SEASON1_END_TOC = "Fine Stagione 1 🌟"


def season1_reading_order() -> list[int]:
    return [n for part in SEASON1_PARTS for n in part["episodes"]]


def validate_season1_parts(season1_nums: set[int]) -> list[str]:
    errors: list[str] = []
    ordered = season1_reading_order()
    expected = set(range(1, SEASON1_LAST + 1))

    if season1_nums != expected:
        missing = expected - season1_nums
        extra = season1_nums - expected
        if missing:
            errors.append(f"Stagione 1 incompleta: mancano episodi {sorted(missing)}.")
        if extra:
            errors.append(f"Episodi fuori range S1: {sorted(extra)}.")

    if len(ordered) != len(set(ordered)):
        dupes = sorted({n for n in ordered if ordered.count(n) > 1})
        errors.append(f"Episodio duplicato in book_structure.py: {dupes}.")

    if set(ordered) != expected and season1_nums == expected:
        errors.append("book_structure.py non contiene tutti gli episodi 1–25 esattamente una volta.")

    for part in SEASON1_PARTS:
        if not part["episodes"]:
            errors.append(f"Parte {part['slug']} senza episodi.")

    return errors
