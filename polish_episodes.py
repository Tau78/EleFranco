#!/usr/bin/env python3
"""Rifinitura racconti episodes_base.py — stile ep. 20–21."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent
TARGET = ROOT / "episodes_base.py"

RISATA_BY_NUM: dict[int, str] = {
    1: "EleFranco alzò la proboscide al cielo e scoppiò nella sua famosa risata",
    2: "Felice, EleFranco partì con la sua conosciutissima risata",
    3: "EleFranco si sedette felice e si lanciò nella sua contagiosa risata",
    4: "EleFranco alzò la proboscide e fece ridere tutti con la sua famosa risata",
    5: "EleFranco si indossò fiero la mantella e tutta FrancaVilla sentì la famosa risata",
    6: "Felice, l'elefante tornò a casa e inondò tutti con la sua famosa risata",
    7: "EleFranco partì felice sulla sua bici, esordendo con la sua famosa risata",
    8: "EleFranco alzò la proboscide e fece sorridere tutti con la sua famosa risata",
    9: "EleFranco alzò la proboscide e tutti si girarono a sentire la famosa risata",
    10: "EleFranco alzò la proboscide e travolse tutti con la sua famosa risata",
    11: "EleFranco alzò la proboscide e tutti lo seguirono nella sua famosa risata",
    12: "EleFranco inserì la proboscide all'insù e rallegrò tutti con la sua famosa risata",
    13: "EleFranco alzò la proboscide e partì con la sua famosa risata",
    14: "EleFranco guardò lo spettacolo e scoppiò nella sua famosa risata",
    15: "EleFranco alzò la proboscide e si lanciò nella sua contagiosa risata",
    16: "EleFranco si sbloccò dalla gioia e partì con la sua conosciutissima risata",
    17: "EleFranco si sedette felice e scoppiò nella sua famosa risata",
    18: "EleFranco alzò la proboscide e inondò tutti con la sua famosa risata",
    19: "EleFranco si ripulì il ciuffo e scoppiò nella sua famosa risata",
    20: "EleFranco si riprese, guardò la sua nuova amica e lanciò la sua famosa risata",
    21: "Felice, l'elefante si mise comodo e lanciò la sua famosa risata",
}

BREAK_BEFORE = (
    r" (?=Un mattino,|Quella mattina|Quel giorno|Era un pomeriggio|Era tutto coperto|"
    r"Era il giorno|Scoprì che|Voleva |Aveva scritto|La lampadina|Un giorno notò|"
    r"La staccionata|Quella mattina doveva|Era uscito il fumetto|"
    r"Si infilò i suoi stivali giganti, prese|"
    r"Mentre |Arrivato |Passando |Lungo la |Lungo il |Vicino |Sotto |Nel bosco|Presso |"
    r"Davanti |In ospedale|Fu a metà|Lassù,|Lalla stava|Si sporse |Pino cercava|"
    r"EleFranco si fermò|EleFranco rimase|EleFranco guardò la|Si stava |Stava quasi|"
    r"Stava per |Stava proprio|Allora |Scosse |Deciso |In un attimo|Corse alla|"
    r"Entrò nel|Si inginocchiò|Afferrò|Prese la|Fece salire|Sollevò|Recuperò|"
    r"L'elefante|Purtroppo|Mentro si|Incredibilmente|Proprio allora|Proprio in quel|"
    r"Con un colpo|Ma proprio|Ma a forza|Ma continuò|Ma il |Ma vedendo|Felice,|"
    r"La missione|Tutto era|Lettera spedita|Lo zucchero|La merenda|EleFranco guardò lo|"
    r"EleFranco si ripulì|EleFranco si sedette|EleFranco partì|EleFranco tornò|"
    r"EleFranco si riprese|EleFranco guardò il|EleFranco guardò la sua|"
    r"EleFranco non ci|Otto |Guarda le casette|Ho un mal di|Uniamo lo zucchero|"
    r"Si stava lasciando|In un attimo passò|In quel momento, gli scoiattoli)"
)

BROKEN_EMOJI = re.compile(r"\\U000f[0-9a-fA-F]{4,5}|\U000f0a54|\U000f0d58|\U000f0d1b|\U000f0b49")


def clean_schema(value: str) -> str:
    value = BROKEN_EMOJI.sub("", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.replace(": è Ciccio", ": c'era Ciccio")
    value = value.replace("rompono le unghie", "rompevano le unghie")
    value = value.replace("buco strettissimo", "buco strettissimo")  # ok
    value = value.replace("enorme orecchie", "enormi orecchie")
    value = value.replace("seu corno", "suo corno")
    value = value.replace("STRECH!", "SCRACK!")
    return value


def apply_mechanical(text: str) -> str:
    text = text.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"THUMP THUMP THUMP \.", "THUMP THUMP THUMP", text)
    text = re.sub(r'["""]FOCUS!["""] \.', '"FOCUS!"', text)
    text = re.sub(r'["""]FOCUS!["""]', '"FOCUS!"', text)
    text = text.replace(" la diga fue salvata", " la diga fu salvata")
    text = text.replace("seu peso", "suo peso")
    text = text.replace("seu corno", "suo corno")
    text = text.replace("strettissimo e profonda", "strettissima e profonda")
    text = text.replace("EleFranco si ferma e pensò", "EleFranco si fermò e pensò")
    text = text.replace("enorme occhiaie", "enormi occhiaie")
    text = text.replace("enorme orecchie", "enormi orecchie")
    text = text.replace(": è Ciccio", ": c'era Ciccio")
    text = text.replace("che gli rompono le unghie", "che gli rompeva le unghie")
    text = re.sub(r" Seconda Parte:.*$", "", text)
    text = re.sub(r" Terza Parte:.*$", "", text)
    text = re.sub(r" Quarta Parte:.*$", "", text)
    text = text.replace("But nel secchiello", "Ma nel secchiello")
    text = text.replace("triste ed invisibile", "triste e invisibile")
    text = text.replace(" ( STRECH! )", " (SCRACK!)")
    text = text.replace("STRECH!", "SCRACK!")
    text = text.replace("SBLING!", "SLING!")
    text = text.replace("curano il crampo e rilassano", "curarono il crampo e rilassarono")
    text = re.sub(r"\b(incontra)\b", "incontrò", text)
    text = re.sub(r"\b(tossisce)\b", "tossiva", text)
    return text


def merge_orphan_breaks(text: str) -> str:
    text = re.sub(r"Il suo amico\n\nFred", "Il suo amico Fred", text)
    text = re.sub(r"\.([A-ZÉÈ])", r". \1", text)
    return text


def add_paragraphs(text: str) -> str:
    if "\n\n" in text:
        return merge_orphan_breaks(text)
    text = re.sub(BREAK_BEFORE, "\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return merge_orphan_breaks(text.strip())


def fix_risata(text: str, closing: str) -> str:
    text = re.sub(r"\s*\n\n\s*", "\n\n", text.strip())
    if not text.endswith("OH... OH... OH..."):
        return text
    text = re.sub(
        r"(?:EleFranco|Felice, (?:l'elefante|EleFranco)) [^:\n]+: OH\.\.\. OH\.\.\. OH\.\.\.\s*$",
        f"{closing}: OH... OH... OH...",
        text,
    )
    return text


def polish_episode(ep: dict) -> None:
    for key in ("missione", "incontro", "aiuto", "morale", "colpo", "finale_schema"):
        ep[key] = clean_schema(str(ep[key]))
    racconto = apply_mechanical(str(ep["racconto"]))
    if ep["num"] not in (20, 21):
        racconto = add_paragraphs(racconto)
    else:
        racconto = merge_orphan_breaks(racconto)
    closing = RISATA_BY_NUM.get(ep["num"], "EleFranco scoppiò nella sua famosa risata")
    racconto = fix_risata(racconto, closing)
    ep["racconto"] = racconto


def py_string(value: str, *, multiline: bool = False) -> str:
    if multiline or "\n" in value:
        escaped = value.replace("\\", "\\\\").replace('"""', '\\"""')
        return f'"""{escaped}"""'
    return repr(value)


def format_episode(ep: dict) -> str:
    lines = [f'    {{"num": {ep["num"]},', f'        "title": {py_string(ep["title"])},']
    for key in ("missione", "incontro", "aiuto", "morale", "colpo", "finale_schema"):
        lines.append(f'        "{key}": {py_string(ep[key])},')
    lines.append(f'        "racconto": {py_string(ep["racconto"], multiline=True)},')
    lines.append("    },")
    return "\n".join(lines)


def main() -> None:
    ns: dict = {}
    exec(TARGET.read_text(encoding="utf-8"), ns)
    episodes = ns["BASE_EPISODES"]
    intro = ns["INTRO"]

    for ep in episodes:
        if ep["num"] <= 21:
            polish_episode(ep)

    body = [
        '"""Episodi 1–21 — sorgente testi editabile. Modifica qui e rigenera con aggiorna_libro.py."""',
        "",
        "from __future__ import annotations",
        "",
        f"INTRO = {py_string(intro)}",
        "",
        "BASE_EPISODES: list[dict] = [",
    ]
    for ep in episodes:
        body.append(format_episode(ep))
    body.append("]")
    body.append("")

    TARGET.write_text("\n".join(body), encoding="utf-8")
    compile(TARGET.read_text(encoding="utf-8"), str(TARGET), "exec")
    print(f"Rifiniti {len(episodes)} episodi in {TARGET}")


if __name__ == "__main__":
    main()
