# Le Avventure di EleFranco Franchini — Iris Edition

Libro serale per Iris, generato da `episodes_*.py` e `build_book.py`.

## Leggere il libro (telefono / tablet)

### Opzione A — Subito (senza GitHub Pages)

1. Scarica lo zip: **https://github.com/Tau78/EleFranco/archive/refs/heads/main.zip**
2. Aprilo con **File** su iPhone/iPad
3. Tocca **`elefranco-lettura.html`** → «Apri in Safari»

Funziona offline con copertina, illustrazioni e testo grande.

### Opzione B — Link web (dopo attivazione Pages)

**Non usare** `raw.githubusercontent.com` né solo `tau78.github.io` (manca il percorso del progetto).

Link corretto:

**https://tau78.github.io/EleFranco/elefranco-lettura.html**

#### Se vedi ancora 404 — attiva GitHub Pages (una volta sola)

1. Apri **https://github.com/Tau78/EleFranco/settings/pages**
2. In **Build and deployment** → **Source** scegli **GitHub Actions**
3. Vai in **Actions** → workflow «Deploy GitHub Pages» → **Re-run all jobs**

Dopo 1–2 minuti il link sopra funziona.

### Come leggere a Iris

- Tocca un episodio nell’**indice**
- Leggi ad alta voce **«Il Racconto Completo»**
- Episodio speciale: **23 — Iris, la Bambina Gentile** 🌸

## Sviluppo

```bash
python3 aggiorna_libro.py          # valida e rigenera tutto
python3 aggiorna_libro.py --watch  # anteprima locale
```

File generati: `index.html`, `elefranco-libro.html`, `elefranco-lettura.html`, `capitoli/`, `sezioni/`.
