"""Persistenza revisioni lettura → file nel workspace per Cursor."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent
REVISIONI_JSON = ROOT / "revisioni.json"
REVISIONI_MD = ROOT / "Revisioni.md"
REVISIONI_INBOX = ROOT / ".cursor-revisioni-inbox.md"


def _now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def load_store() -> dict[str, Any]:
    if not REVISIONI_JSON.exists():
        return {"version": 1, "updatedAt": None, "episodes": {}}
    try:
        data = json.loads(REVISIONI_JSON.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"version": 1, "updatedAt": None, "episodes": {}}
    data.setdefault("version", 1)
    data.setdefault("episodes", {})
    return data


def _episode_sort_key(key: str) -> tuple[int, str]:
    try:
        return (0, f"{int(key):09d}")
    except ValueError:
        return (1, key)


def _normalize_mark(mark: dict[str, Any], *, status: str | None = None) -> dict[str, Any]:
    out = {
        "id": str(mark.get("id", "")),
        "text": str(mark.get("text", "")).strip(),
        "note": str(mark.get("note", "")).strip(),
        "start": int(mark.get("start", 0) or 0),
        "end": int(mark.get("end", 0) or 0),
        "createdAt": mark.get("createdAt") or _now_iso(),
        "status": status or mark.get("status") or "pending",
        "action": str(mark.get("action") or "segna"),
        "target": str(mark.get("target") or "racconto"),
    }
    if mark.get("field"):
        out["field"] = str(mark["field"]).strip()
    if "replacement" in mark:
        replacement = mark.get("replacement")
        out["replacement"] = "" if replacement is None else str(replacement)
    return out


def merge_sync_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Unisce evidenziazioni dal browser con lo store locale."""
    existing = load_store()
    incoming_eps = payload.get("episodes") or {}
    titles = payload.get("titles") or {}
    merged_eps: dict[str, Any] = {}

    for ep_key, marks in incoming_eps.items():
        key = str(ep_key)
        old_entry = existing.get("episodes", {}).get(key, {})
        old_by_id = {
            m.get("id"): m for m in old_entry.get("marks", []) if m.get("id")
        }
        normalized: list[dict[str, Any]] = []
        for raw in marks or []:
            mid = str(raw.get("id", ""))
            prev = old_by_id.get(mid)
            status = prev.get("status") if prev and prev.get("status") == "applied" else "pending"
            normalized.append(_normalize_mark(raw, status=status))
        normalized.sort(key=lambda m: (m.get("start", 0), m.get("createdAt", "")))
        merged_eps[key] = {
            "title": titles.get(key) or old_entry.get("title") or f"Episodio {key}",
            "marks": normalized,
        }

    pending = sum(
        1
        for ep in merged_eps.values()
        for m in ep.get("marks", [])
        if m.get("status") == "pending"
    )

    store = {
        "version": 1,
        "updatedAt": payload.get("syncedAt") or _now_iso(),
        "pendingCount": pending,
        "episodes": merged_eps,
    }
    write_store(store)
    return store


def write_store(store: dict[str, Any]) -> None:
    REVISIONI_JSON.write_text(
        json.dumps(store, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    REVISIONI_MD.write_text(render_markdown(store), encoding="utf-8")
    REVISIONI_INBOX.write_text(render_inbox(store), encoding="utf-8")


def render_markdown(store: dict[str, Any]) -> str:
    lines = [
        "# Revisioni lettura EleFranco",
        "",
        f"_Aggiornato: {store.get('updatedAt') or '—'} · "
        f"{store.get('pendingCount', 0)} in attesa_",
        "",
        "> File generato automaticamente dall'iPad (modalità Revisione).",
        "> In Cursor: scrivi **applica revisioni** oppure @Revisioni.md",
        "",
    ]
    episodes = store.get("episodes") or {}
    keys = sorted(episodes.keys(), key=_episode_sort_key)

    if not keys:
        lines.append("_Nessuna evidenziazione._\n")
        return "\n".join(lines)

    for key in keys:
        ep = episodes[key]
        title = ep.get("title") or f"Episodio {key}"
        lines.append(f"## {title}")
        lines.append("")
        marks = ep.get("marks") or []
        if not marks:
            lines.append("_Nessuna evidenziazione._")
            lines.append("")
            continue
        for i, mark in enumerate(marks, 1):
            status = mark.get("status", "pending")
            badge = " ✅" if status == "applied" else ""
            text = " ".join(str(mark.get("text", "")).split())
            action = mark.get("action") or "segna"
            line = f"{i}. «{text}»"
            if "replacement" in mark:
                new = " ".join(str(mark.get("replacement", "")).split())
                line += f" → «{new}»"
            line += f"  [{action}]{badge}"
            lines.append(line)
            if mark.get("target") and mark.get("target") != "racconto":
                field = mark.get("field")
                extra = f"{mark['target']}" + (f" / {field}" if field else "")
                lines.append(f"   - Dove: {extra}")
            if mark.get("note"):
                lines.append(f"   - Nota: {mark['note']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_inbox(store: dict[str, Any]) -> str:
    pending = store.get("pendingCount", 0)
    if pending <= 0:
        return (
            "# Inbox revisioni\n\n"
            "_Nessuna revisione in attesa._\n"
        )
    lines = [
        "# Inbox revisioni — azione richiesta",
        "",
        f"**{pending}** passaggi da rivedere (lettura ad alta voce / test).",
        "",
        "Applica le modifiche nei file `episodes_*.py` rispettando il canone EleFranco.",
        "Dettaglio completo in `Revisioni.md` e `revisioni.json`.",
        "",
        "## Prompt suggerito per Cursor",
        "",
        "```",
        "Applica le revisioni pendenti in revisioni.json / Revisioni.md:",
        "- se un mark ha replacement, usa ESATTAMENTE quel testo (vuoto = cancella)",
        "- se ha solo text + note, riscrivi tu il passaggio",
        "- rispetta le note dell'autore e elefranco-canone",
        "- poi python3 aggiorna_libro.py e python3 statistiche_libro.py",
        "- marca le revisioni come applied in revisioni.json",
        "```",
        "",
    ]
    return "\n".join(lines)


def pending_count(store: dict[str, Any] | None = None) -> int:
    data = store or load_store()
    return int(data.get("pendingCount", 0))
