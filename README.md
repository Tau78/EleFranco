# Le Avventure di EleFranco Franchini — Iris Edition

Libro serale per Iris, generato da `episodes_*.py` e `build_book.py`.

## Leggere il libro (telefono / tablet)

**Non usare** il link `raw.githubusercontent.com` — mostra il codice HTML, non il libro.

Apri nel browser:

**https://tau78.github.io/EleFranco/elefranco-lettura.html**

Versione ottimizzata per la lettura serale (senza console di modifica, testo più grande su mobile).

- Indice con tutti gli episodi
- Scorri o tocca un episodio nell’indice
- Leggi ad alta voce la sezione **«Il Racconto Completo»**

## Sviluppo

```bash
python3 aggiorna_libro.py          # valida e rigenera tutto
python3 aggiorna_libro.py --watch  # anteprima locale
```

File generati: `index.html`, `elefranco-libro.html`, `elefranco-lettura.html`, `capitoli/`, `sezioni/`.
