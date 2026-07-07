#!/usr/bin/env python3
"""Genera il libro EleFranco: capitoli separati + index.html unificato."""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

from book_structure import (
    SEASON1_END_TOC,
    SEASON1_LAST,
    SEASON1_PARTS,
    season1_reading_order,
)
from episode_color_hints import COLOR_HINT_PREFIX, COLOR_HINTS
from episode_prompts_en import EPISODES, NEGATIVE_PROMPT, SECTION_PROMPTS
from episodes_base import BASE_EPISODES, INTRO
from episodes_extra import EXTRA_EPISODES
from episodes_season2 import INTRO_S2, SEASON2_EPISODES

ROOT = Path(__file__).parent
CAPITOLI_DIR = ROOT / "capitoli"
SEZIONI_DIR = ROOT / "sezioni"
CSS_DIR = ROOT / "css"
INDEX_HTML = ROOT / "index.html"
OUT_PROMPTS = ROOT / "prompt-immagini.md"
LEGACY_HTML = ROOT / "elefranco-libro.html"
READER_HTML = ROOT / "elefranco-lettura.html"
IMMAGINI_DIR = ROOT / "Immagini"


def load_all_episodes() -> tuple[str, list[dict]]:
    episodes = list(BASE_EPISODES) + list(EXTRA_EPISODES) + list(SEASON2_EPISODES)
    episodes.sort(key=lambda e: e["num"])
    return INTRO, episodes


def book_reading_order(episodes: list[dict]) -> list[dict]:
    """Ordine di lettura nel libro (S1 per parti, S2 per num)."""
    by_num = {e["num"]: e for e in episodes}
    s1 = [by_num[n] for n in season1_reading_order()]
    s2 = sorted((e for e in episodes if e["num"] > SEASON1_LAST), key=lambda e: e["num"])
    return s1 + s2


MORAL_EXPLICIT_MARKER = "la morale di quella giornata"


def moral_explicit_sentence(morale: str) -> str:
    return f"EleFranco capì allora la morale di quella giornata: {morale.strip()}"


def format_story(text: str, *, morale: str | None = None) -> str:
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

    def split_paragraph_at_risata(paragraph: str) -> tuple[str, str | None]:
        sentences = re.split(r"(?<=[.!?»])\s+(?=[«\"A-ZÉÈ(])", paragraph)
        for i, sentence in enumerate(sentences):
            if ris in sentence:
                before = " ".join(sentences[:i]).strip()
                risata = " ".join(sentences[i:]).strip()
                return before, risata or None
        return paragraph, None

    paragraphs_html = [f"<p>{finalize(p)}</p>" for p in paragraphs if p.strip()]

    already_explicit = MORAL_EXPLICIT_MARKER in text.lower()
    if morale and morale.strip() and not already_explicit:
        moral_html = (
            f'<p class="morale-esplicita">{html.escape(moral_explicit_sentence(morale))}</p>'
        )
        risata_idx = next(
            (i for i in range(len(paragraphs) - 1, -1, -1) if ris in paragraphs[i]),
            None,
        )
        if risata_idx is not None:
            before_risata, risata_part = split_paragraph_at_risata(paragraphs[risata_idx])
            chunks: list[str] = paragraphs_html[:risata_idx]
            if before_risata:
                chunks.append(f"<p>{finalize(before_risata)}</p>")
            chunks.append(moral_html)
            if risata_part:
                chunks.append(f"<p>{finalize(risata_part)}</p>")
            chunks.extend(paragraphs_html[risata_idx + 1 :])
            return "".join(chunks)
        paragraphs_html.append(moral_html)

    return "".join(paragraphs_html)


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
        f'      <div class="schema-row"><span class="schema-label console-editable">'
        f"{html.escape(label)}:</span> "
        f'<span class="schema-value console-editable">{html.escape(value)}</span></div>'
        for label, value in fields
    )
    return f'    <div class="schema">\n{rows}\n    </div>'


def _disegna_image_src(ep_num: int, asset_prefix: str) -> str | None:
    for ext in ("jpeg", "jpg", "png"):
        rel = f"{asset_prefix}Disegna/{ep_num:02d}.{ext}"
        if (ROOT / rel.removeprefix(asset_prefix)).exists():
            return rel
    return None


def color_hint_caption(ep_num: int, *, indent: str = "  ") -> str:
    hint = COLOR_HINTS.get(ep_num, "").strip()
    if not hint:
        return ""
    text = f"{COLOR_HINT_PREFIX}{hint}."
    return (
        f'{indent}<p class="color-hint console-editable" data-color-hint="{ep_num}">'
        f"{html.escape(text)}</p>"
    )


def image_block(ep: dict, asset_prefix: str, *, indent: str = "  ") -> str:
    src = _disegna_image_src(ep["num"], asset_prefix)
    caption = color_hint_caption(ep["num"], indent=f"{indent}    ")
    if src:
        return (
            f'{indent}<div class="episode-image-row">\n'
            f'{indent}  <img class="episode-image console-editable-image" '
            f'src="{html.escape(src)}" alt="Illustrazione episodio {ep["num"]}">\n'
            f"{caption}\n"
            f"{indent}</div>"
        )
    return (
        f'{indent}<div class="image-placeholder console-editable-image" '
        f'data-prompt="episodio-{ep["num"]}">\n'
        f'{indent}  <span class="console-editable">🖼 Illustrazione Episodio {ep["num"]}</span>\n'
        f"{indent}</div>"
    )


def episode_fragment(ep: dict, asset_prefix: str = "") -> str:
    n = ep["num"]
    img = image_block(ep, asset_prefix, indent="      ")
    return f"""<div class="episode" id="episodio-{n}" data-episode="{n}">
  <div class="episode-console-bar" hidden>
    <button type="button" class="btn-save-chapter" data-episode="{n}">Salva capitolo</button>
    <button type="button" class="btn-reset-chapter" data-episode="{n}">Ripristina</button>
  </div>
  <div class="episode-layout">
    <div class="console-block" data-block="title">
      <h2 class="episode-title console-editable">Episodio {n}: {html.escape(ep['title'])}</h2>
    </div>
    <div class="console-block" data-block="image">
{img}
    </div>
    <div class="console-block" data-block="schema">
{schema_block(ep)}
    </div>
    <div class="console-block" data-block="racconto-title">
      <h3 class="racconto-title console-editable">Il Racconto Completo</h3>
    </div>
    <div class="console-block" data-block="story">
      <div class="racconto story-text console-editable">
{format_story(ep['racconto'], morale=ep.get('morale'))}
      </div>
    </div>
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
    prev_span = prev_link or " "
    next_span = next_link or " "
    if prev_link:
        prev_span = prev_link.replace("<a ", '<a class="console-editable" ', 1)
    if next_link:
        next_span = next_link.replace("<a ", '<a class="console-editable" ', 1)
    return f"""<nav class="chapter-nav console-section" aria-label="Navigazione capitolo" data-console-section="chapter-nav">
  <div class="console-section-bar" hidden>
    <button type="button" class="btn-save-section" data-section="chapter-nav">Salva navigazione</button>
    <button type="button" class="btn-reset-section" data-section="chapter-nav">Ripristina</button>
  </div>
  <span>{prev_span}</span>
  <a class="nav-index console-editable" href="{index_href}">📖 Indice</a>
  <span>{next_span}</span>
</nav>"""


def html_shell(
    title: str,
    css_href: str,
    body: str,
    *,
    enable_console: bool = True,
    reader_mode: bool = False,
) -> str:
    asset_prefix = "../" if css_href.startswith("../") else ""
    console_block = ""
    if enable_console:
        console_block = f"""
<button type="button" id="console-papa-toggle" class="console-papa-toggle" aria-pressed="false" title="Console di lavoro papà">Console Papà</button>
<script src="{asset_prefix}js/console-papa.js" defer></script>"""
    body_class = ' class="reader-mode"' if reader_mode else ""
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{html.escape(css_href)}">
</head>
<body{body_class}>
{body}{console_block}
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
    return f"""<div class="cover-page page-full console-section" id="{cover_id}" data-console-section="{cover_id}">
  <div class="console-section-bar" hidden>
    <button type="button" class="btn-save-section" data-section="{cover_id}">Salva sezione</button>
    <button type="button" class="btn-reset-section" data-section="{cover_id}">Ripristina</button>
  </div>
  <img class="console-editable-image" src="{asset_prefix}Immagini/00-cover-{cover_num}.jpeg" alt="{html.escape(alt)}">
</div>"""


def intro_fragment(intro_clean: str, asset_prefix: str = "", *, season: int = 1) -> str:
    dedication = f"Iris Edition — Stagione {season}"
    return f"""<div class="intro-page console-section" id="{'introduzione-s2' if season == 2 else 'introduzione'}" data-console-section="{'introduzione-s2' if season == 2 else 'introduzione'}">
  <div class="console-section-bar" hidden>
    <button type="button" class="btn-save-section" data-section="{'introduzione-s2' if season == 2 else 'introduzione'}">Salva sezione</button>
    <button type="button" class="btn-reset-section" data-section="{'introduzione-s2' if season == 2 else 'introduzione'}">Ripristina</button>
  </div>
  <h1 class="console-editable">Le Avventure di EleFranco Franchini</h1>
  <p class="dedication console-editable">{dedication}</p>
  <div class="quote console-editable">{html.escape(intro_clean)}</div>
  <p class="dedication console-editable">Per Iris, con tutto l'amore del mondo 🐘💛</p>
</div>"""


def sezione_intro_fragment(section_file: str, section_id: str, alt: str, asset_prefix: str = "") -> str:
    return f"""<div class="section-intro page-full console-section" id="{section_id}" data-console-section="{section_id}">
  <div class="console-section-bar" hidden>
    <button type="button" class="btn-save-section" data-section="{section_id}">Salva sezione</button>
    <button type="button" class="btn-reset-section" data-section="{section_id}">Ripristina</button>
  </div>
  <img class="console-editable-image" src="{asset_prefix}Immagini/{section_file}" alt="{html.escape(alt)}">
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


def parte_04_fragment(asset_prefix: str = "") -> str:
    return sezione_intro_fragment(
        "sezione-04-vicini.jpeg",
        "parte-04",
        "Quarta Parte — Vicini Nuovi (Stagione 2)",
        asset_prefix,
    )


def parte_05_fragment(asset_prefix: str = "") -> str:
    return sezione_intro_fragment(
        "sezione-05-colori.jpeg",
        "parte-05",
        "Quinta Parte — Colori e Suoni (Stagione 2)",
        asset_prefix,
    )


def parte_06_fragment(asset_prefix: str = "") -> str:
    return sezione_intro_fragment(
        "sezione-06-famiglia.jpeg",
        "parte-06",
        "Sesta Parte — La Grande Famiglia (Stagione 2)",
        asset_prefix,
    )


PARTE_FRAGMENTS = {
    "parte_01": parte_01_fragment,
    "parte_02": parte_02_fragment,
    "parte_03": parte_03_fragment,
    "parte_04": parte_04_fragment,
    "parte_05": parte_05_fragment,
    "parte_06": parte_06_fragment,
}


def colora_cover_fragment(asset_prefix: str = "") -> str:
    return f"""<div class="section-intro page-full console-section" id="colora" data-console-section="colora">
  <div class="console-section-bar" hidden>
    <button type="button" class="btn-save-section" data-section="colora">Salva sezione</button>
    <button type="button" class="btn-reset-section" data-section="colora">Ripristina</button>
  </div>
  <img class="console-editable-image" src="{asset_prefix}Immagini/sezione-colora.jpeg" alt="Colora con EleFranco">
</div>"""


def colora_fragment(episodes: list[dict], asset_prefix: str = "") -> str:
    ep_by_num = {e["num"]: e for e in episodes}
    pages_html = ""
    for ep in book_reading_order(episodes):
        num = ep["num"]
        src = _disegna_image_src(num, asset_prefix)
        if not src:
            continue
        img_file = Path(src.removeprefix(asset_prefix)).name
        alt = html.escape(f"Colora — Episodio {num}: {ep_by_num[num]['title']}")
        page_id = f"colora-capitolo-{num}"
        pages_html += f"""  <div class="coloring-page page-full console-section" id="{page_id}" data-console-section="{page_id}">
    <div class="console-section-bar" hidden>
      <button type="button" class="btn-save-section" data-section="{page_id}">Salva sezione</button>
      <button type="button" class="btn-reset-section" data-section="{page_id}">Ripristina</button>
    </div>
    <img class="console-editable-image" src="{asset_prefix}Disegna/{img_file}" alt="{alt}">
  </div>
"""
    return f"""<div class="coloring-section" id="colora-pagine">
{pages_html}</div>"""


def toc_fragment(episodes: list[dict], *, link_prefix: str, use_anchors: bool) -> str:
    by_num = {e["num"]: e for e in episodes}
    items: list[str] = []

    for part_idx, part in enumerate(SEASON1_PARTS):
        if part_idx > 0:
            items.append(f'    <li class="toc-part console-editable">{part["toc_label"]}</li>')
        for num in part["episodes"]:
            ep = by_num[num]
            label = f"Episodio {num}: {html.escape(ep['title'])}"
            href = f"#episodio-{num}" if use_anchors else f"{link_prefix}capitolo_{num:02d}.html"
            items.append(f'    <li><a class="console-editable" href="{href}">{label}</a></li>')

    items.append(f'    <li class="toc-part console-editable">{SEASON1_END_TOC}</li>')

    first_s2 = min(e["num"] for e in SEASON2_EPISODES) if SEASON2_EPISODES else None
    for ep in sorted((e for e in episodes if e["num"] > SEASON1_LAST), key=lambda e: e["num"]):
        n = ep["num"]
        if first_s2 is not None and n == first_s2:
            items.append(
                '    <li class="toc-part console-editable">Stagione 2 — Nuove Avventure 🌅</li>'
            )
        if n == 35:
            items.append('    <li class="toc-part console-editable">Quinta Parte: Colori e Suoni 🎨</li>')
        if n == 43:
            items.append('    <li class="toc-part console-editable">Sesta Parte: La Grande Famiglia 🎉</li>')
        label = f"Episodio {n}: {html.escape(ep['title'])}"
        href = f"#episodio-{n}" if use_anchors else f"{link_prefix}capitolo_{n:02d}.html"
        items.append(f'    <li><a class="console-editable" href="{href}">{label}</a></li>')

    list_html = "\n".join(items)
    return f"""<div class="toc console-section" id="indice" data-console-section="indice">
  <div class="console-section-bar" hidden>
    <button type="button" class="btn-save-section" data-section="indice">Salva sezione</button>
    <button type="button" class="btn-reset-section" data-section="indice">Ripristina</button>
  </div>
  <h2 class="console-editable">📚 Indice delle Avventure</h2>
  <ul class="toc-list">
{list_html}
    <li class="toc-part"><a class="console-editable" href="#colora">🎨 Colora con EleFranco</a></li>
  </ul>
</div>"""


def build_index(
    intro_clean: str,
    episodes: list[dict],
    *,
    enable_console: bool = True,
    reader_mode: bool = False,
) -> str:
    by_num = {e["num"]: e for e in episodes}
    body_parts = [
        cover_fragment(cover_num=1),
        cover_fragment(cover_num=2),
        intro_fragment(intro_clean),
        toc_fragment(episodes, link_prefix="", use_anchors=True),
    ]

    for part in SEASON1_PARTS:
        body_parts.append(PARTE_FRAGMENTS[part["fragment"]]())
        for num in part["episodes"]:
            body_parts.append(episode_fragment(by_num[num]))

    first_s2 = min(e["num"] for e in SEASON2_EPISODES) if SEASON2_EPISODES else None
    for ep in sorted((e for e in episodes if e["num"] > SEASON1_LAST), key=lambda e: e["num"]):
        if first_s2 is not None and ep["num"] == first_s2:
            body_parts.append(intro_fragment(INTRO_S2, season=2))
            body_parts.append(parte_04_fragment())
        if ep["num"] == 35:
            body_parts.append(parte_05_fragment())
        if ep["num"] == 43:
            body_parts.append(parte_06_fragment())
        body_parts.append(episode_fragment(ep))

    body_parts.append(colora_cover_fragment())
    body_parts.append(colora_fragment(episodes))
    body_parts.append(cover_fragment(cover_num=3))
    body_parts.append(cover_fragment(cover_num=4))

    return html_shell(
        "Le Avventure di EleFranco Franchini — Iris Edition",
        "css/libro.css",
        "\n\n".join(body_parts),
        enable_console=enable_console,
        reader_mode=reader_mode,
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
    intro_s2_clean = re.sub(r"\s+", " ", INTRO_S2).strip()
    (SEZIONI_DIR / "introduzione_s2.html").write_text(
        intro_fragment(intro_s2_clean, season=2), encoding="utf-8"
    )
    (SEZIONI_DIR / "parte_01.html").write_text(parte_01_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "parte_02.html").write_text(parte_02_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "parte_03.html").write_text(parte_03_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "parte_04.html").write_text(parte_04_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "parte_05.html").write_text(parte_05_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "parte_06.html").write_text(parte_06_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "colora_cover.html").write_text(colora_cover_fragment(), encoding="utf-8")
    (SEZIONI_DIR / "colora.html").write_text(colora_fragment(episodes), encoding="utf-8")

    # Capitoli singoli (navigazione in ordine di lettura)
    reading_order = book_reading_order(episodes)
    for ep in episodes:
        path = CAPITOLI_DIR / f"capitolo_{ep['num']:02d}.html"
        path.write_text(build_chapter_file(ep, reading_order), encoding="utf-8")

    # Index unificato (+ versione lettura senza console)
    index_content = build_index(intro_clean, episodes)
    INDEX_HTML.write_text(index_content, encoding="utf-8")
    shutil.copy(INDEX_HTML, LEGACY_HTML)
    reader_content = build_index(
        intro_clean,
        episodes,
        enable_console=False,
        reader_mode=True,
    )
    READER_HTML.write_text(reader_content, encoding="utf-8")

    OUT_PROMPTS.write_text(build_prompts(episodes), encoding="utf-8")

    print(f"Scritto: {INDEX_HTML}")
    print(f"Scritti: {len(episodes)} file in {CAPITOLI_DIR}/")
    print(f"Scritte: sezioni in {SEZIONI_DIR}/")
    print(f"CSS: {CSS_DIR / 'libro.css'}")
    print(f"Copia legacy: {LEGACY_HTML}")
    print(f"Lettura mobile: {READER_HTML}")


if __name__ == "__main__":
    main()
