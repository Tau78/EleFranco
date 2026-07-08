#!/usr/bin/env python3
"""Genera EleFranco-Disegna.pdf — solo pagine line art da colorare (A4)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).parent
OUT_PDF = ROOT / "EleFranco-Disegna.pdf"


def disegna_image_paths(episodes: list[dict]) -> list[Path]:
    sys.path.insert(0, str(ROOT))
    from build_book import book_reading_order

    paths: list[Path] = []
    for ep in book_reading_order(episodes):
        num = ep["num"]
        for ext in ("jpeg", "jpg", "png"):
            candidate = ROOT / "Disegna" / f"{num:02d}.{ext}"
            if candidate.is_file():
                paths.append(candidate)
                break
    return paths


def build_pdf(image_paths: list[Path], out_path: Path) -> None:
    try:
        import img2pdf
    except ImportError as exc:
        raise SystemExit(
            "Serve il pacchetto img2pdf. Installa con:\n"
            "  python3 -m pip install img2pdf\n"
            f"({exc})"
        ) from exc

    if not image_paths:
        raise SystemExit("Nessuna immagine in Disegna/ — impossibile creare il PDF.")

    a4 = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout = img2pdf.get_layout_fun(a4)

    pdf_bytes = img2pdf.convert(
        [str(p) for p in image_paths],
        layout_fun=layout,
    )
    out_path.write_bytes(pdf_bytes)


def main() -> None:
    sys.path.insert(0, str(ROOT))
    from build_book import load_all_episodes

    _, episodes = load_all_episodes()
    paths = disegna_image_paths(episodes)
    build_pdf(paths, OUT_PDF)
    print(f"Scritto: {OUT_PDF} ({len(paths)} pagine)")


if __name__ == "__main__":
    main()
