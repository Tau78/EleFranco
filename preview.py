#!/usr/bin/env python3
"""Anteprima live: server locale + auto-reload browser."""

from __future__ import annotations

import threading
import time
from collections.abc import Callable
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
BUILD_STAMP = ROOT / ".last_build"

RELOAD_SNIPPET = """
<script>
(function () {
  var last = 0;
  function poll() {
    fetch("/__livereload__?t=" + Date.now())
      .then(function (r) { return r.text(); })
      .then(function (txt) {
        var ts = parseFloat(txt);
        if (!last) { last = ts; return; }
        if (ts > last) { last = ts; location.reload(); }
      })
      .catch(function () {});
  }
  setInterval(poll, 700);
  poll();
})();
</script>
"""


def touch_build_stamp() -> None:
    BUILD_STAMP.write_text(str(time.time()), encoding="utf-8")


def watched_mtimes(paths: list[Path]) -> dict[str, float]:
    out: dict[str, float] = {}
    for path in paths:
        if path.is_file():
            out[str(path)] = path.stat().st_mtime
        elif path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and child.suffix in {".py", ".css", ".js"}:
                    out[str(child)] = child.stat().st_mtime
    return out


class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        if args and isinstance(args[0], str) and args[0].startswith("GET /__livereload__"):
            return
        super().log_message(fmt, *args)

    def do_GET(self) -> None:
        if self.path.split("?", 1)[0] == "/__livereload__":
            stamp = BUILD_STAMP.read_text(encoding="utf-8") if BUILD_STAMP.exists() else "0"
            payload = stamp.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        path = self.path.split("?", 1)[0]
        if path in ("", "/"):
            path = "/index.html"
        file_path = (ROOT / path.lstrip("/")).resolve()
        if not str(file_path).startswith(str(ROOT.resolve())):
            self.send_error(403)
            return

        if file_path.suffix.lower() == ".html" and file_path.is_file():
            html = file_path.read_text(encoding="utf-8")
            if "</body>" in html and "/__livereload__" not in html:
                html = html.replace("</body>", RELOAD_SNIPPET + "\n</body>", 1)
            payload = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        super().do_GET()


def start_server(port: int) -> ThreadingHTTPServer:
    server = ThreadingHTTPServer(("127.0.0.1", port), PreviewHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def watch_loop(
    paths: list[Path],
    rebuild: Callable[[], None],
    *,
    interval: float = 0.6,
) -> None:
    baseline = watched_mtimes(paths)
    while True:
        time.sleep(interval)
        current = watched_mtimes(paths)
        if current != baseline:
            baseline = current
            print("\n↻ Modifica rilevata — rigenero…")
            try:
                rebuild()
                touch_build_stamp()
                print("✓ Libro aggiornato — il browser si ricarica da solo")
            except SystemExit as exc:
                print(f"✗ Validazione fallita (codice {exc.code}) — correggi e salva di nuovo")
            except Exception as exc:
                print(f"✗ Errore build: {exc}")


def run_preview(
    rebuild: Callable[[], None],
    *,
    port: int = 8765,
    watch_paths: list[Path] | None = None,
) -> None:
    paths = watch_paths or [
        ROOT / "episodes_base.py",
        ROOT / "episodes_extra.py",
        ROOT / "episodes_season2.py",
        ROOT / "episode_prompts_en.py",
        ROOT / "css" / "libro.css",
        ROOT / "js" / "console-papa.js",
        ROOT / "build_book.py",
    ]

    touch_build_stamp()
    rebuild()
    touch_build_stamp()

    server = start_server(port)
    url = f"http://127.0.0.1:{port}/index.html"
    print(f"\nAnteprima live: {url}", flush=True)
    print("Modifica episodes_base.py / episodes_extra.py / episodes_season2.py e salva — rebuild automatico.", flush=True)
    print("Ctrl+C per uscire.\n", flush=True)

    try:
        watch_loop(paths, rebuild)
    except KeyboardInterrupt:
        print("\nAnteprima terminata.")
    finally:
        server.shutdown()
