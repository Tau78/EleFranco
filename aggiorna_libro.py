#!/usr/bin/env python3
"""
Valida episodi + prompt immagini e rigenera il libro EleFranco.

Uso:
  python3 aggiorna_libro.py              # valida e rigenera tutto
  python3 aggiorna_libro.py --check      # solo validazione
  python3 aggiorna_libro.py --nuovo 23 "🦊 Titolo del capitolo"

Dopo --nuovo: completa testo in episodes_extra.py e prompt in episode_prompts_en.py,
poi rilancia senza flag.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
EPISODES_EXTRA = ROOT / "episodes_extra.py"
PROMPTS_EN = ROOT / "episode_prompts_en.py"
BUILD = ROOT / "build_book.py"

PROMPT_KEYS = ("setting", "footwear", "a", "b", "c", "d")
EPISODE_FIELDS = (
    "title",
    "missione",
    "incontro",
    "aiuto",
    "morale",
    "colpo",
    "finale_schema",
    "racconto",
)


def load_episodes() -> list[dict]:
    sys.path.insert(0, str(ROOT))
    from build_book import load_all_episodes

    _, episodes = load_all_episodes()
    return episodes


def load_prompt_nums() -> set[int]:
    sys.path.insert(0, str(ROOT))
    from episode_prompts_en import EPISODES

    return set(EPISODES.keys())


def validate() -> list[str]:
    sys.path.insert(0, str(ROOT))
    from episode_prompts_en import EPISODES

    errors: list[str] = []
    episodes = load_episodes()
    nums = [e["num"] for e in episodes]

    if len(nums) != len(set(nums)):
        errors.append("Numeri episodio duplicati nella lista completa.")

    for ep in episodes:
        n = ep["num"]
        for field in EPISODE_FIELDS:
            if not str(ep.get(field, "")).strip():
                src = "episodes_extra.py" if n >= 22 else "PDF / build_book"
                errors.append(f"Episodio {n}: campo «{field}» vuoto ({src}).")

        if n not in EPISODES:
            errors.append(f"Episodio {n}: manca blocco prompt in episode_prompts_en.py.")
            continue

        prompts = EPISODES[n]
        for key in PROMPT_KEYS:
            val = prompts.get(key, "")
            if not val or "TODO" in val.upper():
                errors.append(f"Episodio {n}: prompt «{key}» mancante o con TODO.")

    return errors


def scaffold_episode(num: int, title: str) -> None:
    episodes = load_episodes()
    if any(e["num"] == num for e in episodes):
        raise SystemExit(f"Episodio {num} esiste già.")

    extra_text = EPISODES_EXTRA.read_text(encoding="utf-8")
    if f'"num": {num}' in extra_text or f'"num": {num},' in extra_text:
        raise SystemExit(f"Episodio {num} già presente in episodes_extra.py.")

    prompts_text = PROMPTS_EN.read_text(encoding="utf-8")
    if re.search(rf"^\s*{num}:\s*\{{", prompts_text, re.MULTILINE):
        raise SystemExit(f"Episodio {num} già presente in episode_prompts_en.py.")

    safe_title = title.replace('"', '\\"')
    episode_block = f'''
    {{
        "num": {num},
        "title": "{safe_title}",
        "missione": "TODO — La Missione",
        "incontro": "TODO — L'Incontro",
        "aiuto": "TODO — L'Aiuto e l'Imprevisto",
        "morale": "TODO — La Morale 🌟",
        "colpo": "TODO — Il Colpo di Scena Finale",
        "finale_schema": "TODO — Il Finale: OH... OH... OH...",
        "racconto": """C'era una volta un Elefante di nome Franco, che gli amici chiamavano ... EleFranco. Di cognome faceva Franchini.

TODO — racconto completo (canone EleFranco).""",
    }},
'''
    extra_text = extra_text.rstrip()
    if extra_text.endswith("]"):
        extra_text = extra_text[:-1].rstrip() + "," + episode_block + "\n]\n"
    else:
        raise SystemExit("Formato episodes_extra.py non riconosciuto.")
    EPISODES_EXTRA.write_text(extra_text, encoding="utf-8")

    prompt_block = f'''
    {num}: {{
        "setting": "FrancaVilla — TODO describe village variant",
        "footwear": "giant boots — TODO",
        "a": f"{{{{BASE}}}}, {{{{STYLE}}}}, TODO episode {num} cover scene",
        "b": f"{{{{BASE}}}}, {{{{STYLE}}}}, TODO incontro scene",
        "c": f"{{{{BASE}}}}, {{{{STYLE}}}}, TODO aiuto e imprevisto",
        "d": f"{{{{BASE}}}}, {{{{STYLE}}}}, TODO colpo di scena finale",
    }},
'''
    prompts_text = prompts_text.rstrip()
    if prompts_text.endswith("}"):
        prompts_text = prompts_text[:-1].rstrip() + "," + prompt_block + "}\n"
    else:
        raise SystemExit("Formato episode_prompts_en.py non riconosciuto.")
    PROMPTS_EN.write_text(prompts_text, encoding="utf-8")

    print(f"Scaffold episodio {num} creato:")
    print(f"  - {EPISODES_EXTRA}")
    print(f"  - {PROMPTS_EN}")
    print("Completa testo e prompt (sostituisci TODO), poi: python3 aggiorna_libro.py")


def rebuild() -> None:
    subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggiorna il libro EleFranco (valida + build)")
    parser.add_argument("--check", action="store_true", help="Solo validazione, senza build")
    parser.add_argument(
        "--nuovo",
        nargs=2,
        metavar=("NUM", "TITOLO"),
        help='Scaffold nuovo capitolo, es. --nuovo 23 "🦊 Titolo"',
    )
    args = parser.parse_args()

    if args.nuovo:
        scaffold_episode(int(args.nuovo[0]), args.nuovo[1])
        print("\nValidazione (attesi TODO):")
        for err in validate():
            print(f"  ⚠ {err}")
        return

    errors = validate()
    if errors:
        print("Validazione fallita:")
        for err in errors:
            print(f"  ✗ {err}")
        sys.exit(1)

    count = len(load_episodes())
    print(f"Validazione OK — {count} episodi, prompt completi.")

    if args.check:
        return

    rebuild()
    print("Libro rigenerato: index.html, capitoli/, prompt-immagini.md")


if __name__ == "__main__":
    main()
