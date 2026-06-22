#!/usr/bin/env python3
"""Genera il libro EleFranco: capitoli separati + index.html unificato."""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

from episode_prompts_en import EPISODES, NEGATIVE_PROMPT, SECTION_PROMPTS
from episodes_base import BASE_EPISODES, INTRO
from episodes_extra import EXTRA_EPISODES

ROOT = Path(__file__).parent
CAPITOLI_DIR = ROOT / "capitoli"
SEZIONI_DIR = ROOT / "sezioni"
CSS_DIR = ROOT / "css"
INDEX_HTML = ROOT / "index.html"
OUT_PROMPTS = ROOT / "prompt-immagini.md"
LEGACY_HTML = ROOT / "elefranco-libro.html"
IMMAGINI_DIR = ROOT / "Immagini"


def load_all_episodes() -> tuple[str, list[dict]]:
    episodes = list(BASE_EPISODES) + list(EXTRA_EPISODES)
    episodes.sort(key=lambda e: e["num"])
    return INTRO, episodes


def format_story(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()

    ell = "⟦ELL⟧"
    ris = "⟦RIS⟧"
    foc = "⟦FOCUS⟧"
    thu = "⟦THUMP⟧"

    text = re.sub(r"OH\.\.\.\s*OH\.\.\.\s*OH\.\.\.?", ris, text, flags=re.IGNORECASE)
    text = text.replace("...", ell)
    text = re.sub(r'["""\u201c]FOCUS!["""\u201d]\s*\.?', foc, text)
    text = re.sub(r'(?<![\w])"FOCUS!"\s*\.?', foc, text)
    text = re.sub(r"\bTHUMP\s+THUMP\s+THUMP\b\s*\.?", thu, text, flags=re.IGNORECASE)

    text = html.escape(text)
    text = text.replace(foc, '<strong>"FOCUS!"</strong>')
    text = text.replace(thu, "<em>THUMP THUMP THUMP</em>")
    text = text.replace(ell, "...")

    sentences = re.split(r"(?<=[.!?»])\s+(?=[«\"A-ZÉÈ])", text)
    sentences = [s.strip() for s in sentences if s.strip()]

    paragraphs: list[str] = []
    buf: list[str] = []
    for sentence in sentences:
        buf.append(sentence)
        if len(buf) >= 4:
            paragraphs.append(" ".join(buf))
            buf = []
    if buf:
        paragraphs.append(" ".join(buf))

    def finalize(part: str) -> str:
        part = part.replace(ris, '<span class="risata">OH... OH... OH...</span>')
        if ris not in part and "OH... OH... OH..." in part and "risata" not in part.lower():
            part = re.sub(
                r"OH\.\.\.\s*OH\.\.\.\s*OH\.\.\.?\s*$",
                '<span class="risata">OH... OH... OH...</span>',
                part,
                flags=re.IGNORECASE,
            )
        return part

    return "".join(f"<p>{finalize(p)}</p>" for p in paragraphs if p.strip())


def schema_block(ep: dict) -> str:
    fields = [
        ("La Missione", ep["missione"]),
        ("L'Incontro", ep["incontro"]),
        ("L'Aiuto e l'Imprevisto", ep["aiuto"]),
        ("La Morale", ep["morale"]),
        ("Il Colpo di Scena Finale", ep["colpo"]),
        ("Il Finale", ep["finale_schema"]),
    ]
    rows = "\n".join(
        f'    <div class="schema-row"><span class="schema-label">{html.escape(label)}:</span> '
        f"<span>{html.escape(value)}</span></div>"
        for label, value in fields
    )
    return f'  <div class="schema">\n{rows}\n  </div>'


def _disegna_image_src(ep_num: int, asset_prefix: str) -> str | None:
    for ext in ("jpeg", "jpg", "png"):
        rel = f"{asset_prefix}Disegna/{ep_num:02d}.{ext}"
        if (ROOT / rel.removeprefix(asset_prefix)).exists():
            return rel
    return None


def image_block(ep: dict, asset_prefix: str) -> str:
    src = _disegna_image_src(ep["num"], asset_prefix)
    if src:
        return (
            f'  <img class="episode-image" src="{html.escape(src)}" '
            f'alt="Illustrazione episodio {ep["num"]}">\n'
        )
    return (
        f'  <div class="image-placeholder" data-prompt="episodio-{ep["num"]}">\n'
        f'    <span>🖼 Illustrazione Episodio {ep["num"]}</span>\n'
        f"  </div>\n"
    )


def episode_fragment(ep: dict, asset_prefix: str = "") -> str:
    return f"""<div class="episode" id="episodio-{ep['num']}">
  <h2 class="episode-title">Episodio {ep['num']}: {html.escape(ep['title'])}</h2>
{image_block(ep, asset_prefix)}{schema_block(ep)}
  <h3 class="racconto-title">Il Racconto Completo</h3>
  <div class="racconto">
{format_story(ep['racconto'])}
  </div>
</div>"""


def chapter_nav(ep: dict, episodes: list[dict], *, from_index: bool) -> str:
    nums = [e["num"] for e in episodes]
    idx = nums.index(ep["num"])
    prev_link = ""
    next_link = ""
    if idx > 0:
        n = nums[idx - 1]
        if from_index:
            prev_link = f'<a href="#episodio-{n}">← Ep. {n}</a>'
        else:
            prev_link = f'<a href="capitolo_{n:02d}.html">← Ep. {n}</a>'
    if idx < len(nums) - 1:
        n = nums[idx + 1]
        if from_index:
            next_link = f'<a href="#episodio-{n}">Ep. {n} →</a>'
        else:
            next_link = f'<a href="capitolo_{n:02d}.html">Ep. {n} →</a>'
    index_href = "../index.html" if not from_index else "#indice"
    return f"""<nav class="chapter-nav" aria-label="Navigazione capitolo">
  <span>{prev_link or " "}</span>
  <a class="nav-index" href="{index_href}">📖 Indice</a>
  <span>{next_link or " "}</span>
</nav>"""


def html_shell(title: str, css_href: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{html.escape(css_href)}">
</head>
<body>
{body}
</body>
</html>
"""


def cover_fragment(asset_prefix: str = "", cover_num: int = 1) -> str:
    cover_id = {1: "cover", 2: "cover2", 3: "cover3", 4: "cover4"}[cover_num]
    alt = {
        1: "Copertina — Le Avventure di EleFranco Franchini",
        2: "Seconda di copertina",
        3: "Terza di copertina",
        4: "Quarta di copertina",
    }[cover_num]
    return f"""<div class="cover-page page-full" id="{cover_id}">
  <img src="{asset_prefix}Immagini/00-cover-{cover_num}.jpeg" alt="{html.escape(alt)}">
</div>"""


def intro_fragment(intro_clean: str, asset_prefix: str = "") -> str:
    return f"""<div class="intro-page" id="introduzione">
  <h1>Le Avventure di EleFranco Franchini</h1>
  <p class="dedication">Iris Edition — Stagione 1</p>
  <div class="quote">{html.escape(intro_clean)}</div>
  <p class="dedication">Per Iris, con tutto l'amore del mondo 🐘💛</p>
</div>"""


def sezione_intro_fragment(section_file: str, section_id: str, alt: str, asset_prefix: str = "") -> str:
    return f"""<div class="section-intro page-full" id="{section_id}">
  <img src="{asset_prefix}Immagini/{section_file}" alt="{html.escape(alt)}">
</div>"""


def parte_01_fragment(asset_prefix: str = "") -> str:
    return sezione_intro_fragment(
        "sezione-01-missioni.jpeg",
        "parte-01",
        "Prima Parte — Missioni Quotidiane",
        asset_prefix,
    )


def parte_02_fragment(asset_prefix: str = "") -> str:
    return sezione_intro_fragment(
        "sezione-02-intoppi.jpeg",
        "parte-02",
        "Seconda Parte — Intoppi e Soluzioni",
        asset_prefix,
    )


def parte_03_fragment(asset_prefix: str = "") -> str:
    return sezione_intro_fragment(
        "sezione-03-nuoviamici.jpeg",
        "parte-03",
        "Terza Parte — Nuovi Amici",
        asset_prefix,
    )


def colora_cover_fragment(asset_prefix: str = "") -> str:
    return sezione_intro_fragment(
        "sezione-colora.jpeg",
        "colora",
        "Colora con EleFranco",
        asset_prefix,
    )


def colora_fragment(episodes: list[dict], asset_prefix: str = "") -> str:
    ep_by_num = {e["num"]: e for e in episodes}
    coloring_pages = sorted(
        p for p in (ROOT / "Disegna").glob("*.*") if p.suffix.lower() in {".jpeg", ".jpg", ".png"}
    )
    pages_html = ""
    for path in coloring_pages:
        num_match = re.match(r"(\d+)", path.stem)
        num = int(num_match.group(1)) if num_match else None
        if num and num in ep_by_num:
            alt = html.escape(f"Colora — Episodio {num}: {ep_by_num[num]['title']}")
        elif num:
            alt = html.escape(f"Colora — Episodio {num}")
        else:
            alt = html.escape(f"Colora — {path.stem}")
        pages_html += f"""  <div class="coloring-page page-full" id="colora-capitolo-{num or path.stem}">
    <img src="{asset_prefix}Disegna/{path.name}" alt="{alt}">
  </div>
"""
    return f"""<div class="coloring-section" id="colora-pagine">
{pages_html}</div>"""


def toc_fragment(episodes: list[dict], *, link_prefix: str, use_anchors: bool) -> str:
    items: list[str] = []
    for ep in episodes:
        n = ep["num"]
        label = f"Episodio {n}: {html.escape(ep['title'])}"
        if use_anchors:
            href = f"#episodio-{n}"
        else:
            href = f"{link_prefix}capitolo_{n:02d}.html"
        items.append(f'    <li><a href="{href}">{label}</a></li>')
        if n == 4:
            items.append('    <li class="toc-part">Seconda Parte: Intoppi e Soluzioni 🛠</li>')
        if n == 21:
            items.append('    <li class="toc-part">Terza Parte: Nuovi Amici 🌱</li>')

    list_html = "\n".join(items)
    return f"""<div class="toc" id="indice">
  <h2>📚 Indice delle Avventure</h2>
  <ul class="toc-list">
{list_html}
    <li class="toc-part"><a href="#colora">🎨 Colora con EleFranco</a></li>
  </ul>
</div>"""


def build_index(intro_clean: str, episodes: list[dict]) -> str:
    body_parts = [
        cover_fragment(cover_num=1),
        cover_fragment(cover_num=2),
        intro_fragment(intro_clean),
        toc_fragment(episodes, link_prefix="", use_anchors=True),
        parte_01_fragment(),
    ]
    first_extra = min(e["num"] for e in EXTRA_EPISODES) if EXTRA_EPISODES else None
    for ep in episodes:
        if ep["num"] == 5:
            body_parts.append(parte_02_fragment())
        if first_extra is not None and ep["num"] == first_extra:
            body_parts.append(parte_03_fragment())
        body_parts.append(episode_fragment(ep))
    body_parts.append(colora_cover_fragment())
    body_parts.append(colora_fragment(episodes))
    body_parts.append(cover_fragment(cover_num=3))
    body_parts.append(cover_fragment(cover_num=4))

    return html_shell(
        "Le Avventure di EleFranco Franchini — Iris Edition",
        "css/libro.css",
        "\n\n".join(body_parts),
    )


def build_chapter_file(ep: dict, episodes: list[dict]) -> str:
    nav = chapter_nav(ep, episodes, from_index=False)
    content = episode_fragment(ep, asset_prefix="../")
    title = f"Episodio {ep['num']}: {ep['title']} — EleFranco"
    return html_shell(title, "../css/libro.css", f"{nav}\n\n{content}")


def build_prompts(episodes: list[dict]) -> str:
    lines = [
        "# Prompt immagini — Le Avventure di EleFranco",
        "",
        "> Formato Iris Edition — prompt in **inglese**, 4 scene per episodio (A–D).",
        "> Stile Story: acquerello morbido + flat colors. Disegna: line art separata in `Disegna/`.",
        "> **NO TEXT** nelle immagini. Formato **A4 portrait** (~3:4).",
        "",
        "---",
        "",
        "## Cover libro",
        "",
        SECTION_PROMPTS["cover"],
        "",
        f"**Negative prompt:** `{NEGATIVE_PROMPT}`",
        "",
        "---",
        "",
        "## Sezioni macro",
        "",
        "### Prima Parte — Missioni Quotidiane 🏡",
        "",
        SECTION_PROMPTS["parte_1"],
        "",
        f"**Negative prompt:** `{NEGATIVE_PROMPT}`",
        "",
        "### Seconda Parte — Intoppi e Soluzioni 🛠",
        "",
        SECTION_PROMPTS["parte_2"],
        "",
        f"**Negative prompt:** `{NEGATIVE_PROMPT}`",
        "",
        "### Terza Parte — Nuovi Amici 🌱",
        "",
        SECTION_PROMPTS["parte_3"],
        "",
        f"**Negative prompt:** `{NEGATIVE_PROMPT}`",
        "",
        "### Sezione Disegna — slide intro (story)",
        "",
        SECTION_PROMPTS["disegna_slide"],
        "",
        f"**Negative prompt:** `{NEGATIVE_PROMPT}`",
        "",
        "### Sezione Disegna (line art)",
        "",
        SECTION_PROMPTS["disegna"],
        "",
        "**Negative prompt:** `color fill, shading, grayscale photo, text, letters, watermark`",
        "",
        "---",
        "",
        "## Episodi",
        "",
    ]

    for ep in episodes:
        n = ep["num"]
        prompts = EPISODES.get(n)
        lines.append(f"### Episodio {n}: {ep['title']}")
        lines.append("")
        lines.append(f"*FrancaVilla:* {prompts['setting'] if prompts else '—'}")
        lines.append(f"*Calzature:* {prompts['footwear'] if prompts else 'giant boots'}")
        lines.append("")
        if prompts:
            lines.extend(
                [
                    "#### A — Episode cover",
                    "",
                    prompts["a"],
                    "",
                    "#### B — L'Incontro",
                    "",
                    prompts["b"],
                    "",
                    "#### C — L'Aiuto e l'Imprevisto",
                    "",
                    prompts["c"],
                    "",
                    "#### D — Il Colpo di Scena Finale",
                    "",
                    prompts["d"],
                    "",
                    f"**Negative prompt:** `{NEGATIVE_PROMPT}`",
                    "",
                    "---",
                    "",
                ]
            )
        else:
            lines.extend(
                [
                    f"*Prompt non ancora definiti — compilare in `episode_prompts_en.py`*",
                    "",
                    "---",
                    "",
                ]
            )

    lines.extend(
        [
            "## Note Colora",
            "",
            "22 pagine line art in `Disegna/` (01–22), una per episodio.",
            "Copertina sezione: `Immagini/sezione-colora.jpeg`.",
            "Intro sezioni: `Immagini/sezione-01-missioni.jpeg`, `sezione-02-intoppi.jpeg`, `sezione-03-nuoviamici.jpeg`.",
            "Copertine libro: `Immagini/00-cover-1.jpeg` … `00-cover-4.jpeg`.",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    intro, episodes = load_all_episodes()

    intro_clean = re.sub(r"\s+", " ", intro).strip()
    intro_clean = re.sub(r"Prima Parte:.*", "", intro_clean).strip()

    CAPITOLI_DIR.mkdir(exist_ok=True)
    SEZIONI_DIR.mkdir(exist_ok=True)

    # Sezioni riutilizzabili (fragment HTML)
    (SEZIONI_DIR / "cover.html").write_text(cover_fragment(cover_num=1), encoding="utf-8")
    (SEZIONI_DIR / "cover2.html").write_text(cover_fragment(cover_num=2), encoding="utf-8")
    (SEZIONI_DIR / "cover3.html").write_text(cover_fragment(cover_num=3), encoding="utf-8")
    (SEZIONI_DIR / "cover4.html").write_text(cover_fragment(cover_num=4), encoding="utf-8")
    (SEZIONI_DIR / "introduzione.html").write_text(intro_fragment(intro_clean), encoding="utf-8")
    (SEZIONI_DIR / "parte_01.html").write_text(parte_01_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "parte_02.html").write_text(parte_02_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "parte_03.html").write_text(parte_03_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "colora_cover.html").write_text(colora_cover_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "colora.html").write_text(colora_fragment(episodes), encoding="utf-8")

    # Capitoli singoli
    for ep in episodes:
        path = CAPITOLI_DIR / f"capitolo_{ep['num']:02d}.html"
        path.write_text(build_chapter_file(ep, episodes), encoding="utf-8")

    # Index unificato
    index_content = build_index(intro_clean, episodes)
    INDEX_HTML.write_text(index_content, encoding="utf-8")
    shutil.copy(INDEX_HTML, LEGACY_HTML)

    OUT_PROMPTS.write_text(build_prompts(episodes), encoding="utf-8")

    print(f"Scritto: {INDEX_HTML}")
    print(f"Scritti: {len(episodes)} file in {CAPITOLI_DIR}/")
    print(f"Scritte: sezioni in {SEZIONI_DIR}/")
    print(f"CSS: {CSS_DIR / 'libro.css'}")
    print(f"Copia legacy: {LEGACY_HTML}")


if __name__ == "__main__":
    main()
