#!/usr/bin/env python3
"""Genera Statistiche.md — parole, spazio A4 e tempo di lettura per capitolo."""

from __future__ import annotations

import html
import re
from datetime import date
from pathlib import Path

from build_book import format_story, load_all_episodes
from episode_color_hints import COLOR_HINTS, COLOR_HINT_PREFIX

ROOT = Path(__file__).parent
OUT = ROOT / "Statistiche.md"

PAGE_H_MM = 261
LINE_MM = 11 * 0.352778 * 1.55
CHARS_PER_LINE_BODY = 72
CHARS_PER_LINE_SCHEMA = 62
WPM_READ_ALOUD = 130

FIXED_MM = {
    "title": 14,
    "image_row": 88,
    "schema_box_padding": 8,
    "racconto_title": 10,
    "episode_padding": 6,
}


def count_words(text: str) -> int:
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    text = re.sub(r"[^\w\s'\u2019À-ÿ]+", " ", text)
    return len([w for w in text.split() if w])


def strip_tags(text: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", " ", text))


def wrap_lines(plain: str, chars_per_line: int) -> int:
    plain = re.sub(r"\s+", " ", plain).strip()
    if not plain:
        return 0
    return max(1, (len(plain) + chars_per_line - 1) // chars_per_line)


def chapter_stats(ep: dict) -> dict:
    num = ep["num"]
    racconto_html = format_story(ep["racconto"], morale=ep.get("morale"))
    schema_fields = [
        ("La Missione:", ep["missione"]),
        ("L'Incontro:", ep["incontro"]),
        ("L'Aiuto e l'Imprevisto:", ep["aiuto"]),
        ("La Morale:", ep["morale"]),
        ("Il Colpo di Scena Finale:", ep["colpo"]),
        ("Il Finale:", ep["finale_schema"]),
    ]
    hint = ""
    if num in COLOR_HINTS:
        hint = COLOR_HINT_PREFIX + COLOR_HINTS[num] + "."

    words_racconto = count_words(racconto_html)
    words_schema = count_words(" ".join(f"{a} {b}" for a, b in schema_fields))
    words_hint = count_words(hint)
    words_titolo = count_words(f"Episodio {num}: {ep['title']}")
    total_words = words_titolo + words_schema + words_hint + words_racconto

    schema_lines = sum(wrap_lines(f"{label} {val}", CHARS_PER_LINE_SCHEMA) for label, val in schema_fields)
    racconto_lines = 0
    for match in re.finditer(
        r'<p(?:\s+class="morale-esplicita")?>(.*?)</p>', racconto_html, re.DOTALL
    ):
        tag = match.group(0)
        plain = strip_tags(match.group(1))
        cpl = 66 if "morale-esplicita" in tag else CHARS_PER_LINE_BODY
        racconto_lines += wrap_lines(plain, cpl)
        if "morale-esplicita" in tag:
            racconto_lines += 1.2

    height_mm = (
        FIXED_MM["episode_padding"]
        + FIXED_MM["title"]
        + FIXED_MM["image_row"]
        + FIXED_MM["schema_box_padding"]
        + schema_lines * LINE_MM * 0.98
        + FIXED_MM["racconto_title"]
        + racconto_lines * LINE_MM
    )

    return {
        "num": num,
        "title": ep["title"],
        "words": total_words,
        "words_racconto": words_racconto,
        "mm": height_mm,
        "pages": height_mm / PAGE_H_MM,
        "minutes": total_words / WPM_READ_ALOUD,
    }


def avg(results: list[dict], key: str) -> float:
    return sum(r[key] for r in results) / len(results)


def build_markdown(results: list[dict]) -> str:
    tot_w = sum(r["words"] for r in results)
    tot_p = sum(r["pages"] for r in results)
    tot_m = sum(r["minutes"] for r in results)
    g1 = [r for r in results if r["num"] <= 21]
    g2 = [r for r in results if r["num"] >= 22]

    lines = [
        "# Statistiche — Le Avventure di EleFranco (Iris Edition)",
        "",
        f"> Aggiornato: {date.today().isoformat()} — {len(results)} capitoli",
        "",
        "## Metodologia",
        "",
        "- **Parole:** titolo, schema tecnico, didascalia colore, racconto completo (con morale esplicita in build).",
        "- **Spazio fisico:** stima su formato **A4** (margini 18/16 mm), corpo **11 pt**, `line-height: 1.55`, layout da `css/libro.css`.",
        "- **Lettura:** ~**130 parole/min** — lettura ad alta voce serale per bambini 3–7 anni (con pause e dialoghi).",
        "- Ogni capitolo inizia su **pagina nuova**; se il contenuto supera un foglio, continua sulla pagina successiva.",
        "",
        "## Tabella per capitolo",
        "",
        "| Ep | Titolo | Parole | Racconto | Spazio (A4) | Lettura |",
        "|---:|--------|-------:|---------:|------------:|--------:|",
    ]
    for r in results:
        title = r["title"].replace("|", "\\|")
        lines.append(
            f"| {r['num']} | {title} | {r['words']:,} | {r['words_racconto']:,} | "
            f"~{r['pages']:.1f} pag. ({r['mm']:.0f} mm) | ~{r['minutes']:.0f} min |"
        )

    lines += [
        "",
        "## Totali",
        "",
        "| Metrica | Valore |",
        "|--------|-------:|",
        f"| Parole totali | **{tot_w:,}** |",
        f"| Spazio stampa stimato | **~{tot_p:.1f} pagine A4** |",
        f"| Lettura ad alta voce | **~{tot_m:.0f} min** ({tot_m / 60:.1f} h) |",
        "",
        "## Medie per gruppo",
        "",
        "| Gruppo | Capitoli | Parole (media) | Pagine (media) | Lettura (media) |",
        "|--------|----------|---------------:|---------------:|----------------:|",
        f"| Ep. 1–21 | {len(g1)} | {avg(g1, 'words'):.0f} | {avg(g1, 'pages'):.1f} | {avg(g1, 'minutes'):.1f} min |",
        f"| Ep. 22–25 | {len(g2)} | {avg(g2, 'words'):.0f} | {avg(g2, 'pages'):.1f} | {avg(g2, 'minutes'):.1f} min |",
        "",
        "## Note",
        "",
        "- **Ep. 1–21:** ritmo omogeneo da favola serale (~5–7 min a capitolo).",
        "- **Ep. 22–25:** capitoli più lunghi (~+50% parole rispetto alla media precedente).",
        "- Le stime di spazio possono variare di **±0,2 pagine** in stampa/PDF reale.",
        "",
        "## Rigenerare",
        "",
        "```bash",
        "python3 statistiche_libro.py",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    _, episodes = load_all_episodes()
    results = [chapter_stats(ep) for ep in episodes]
    OUT.write_text(build_markdown(results), encoding="utf-8")
    print(f"Scritto: {OUT}")


if __name__ == "__main__":
    main()
