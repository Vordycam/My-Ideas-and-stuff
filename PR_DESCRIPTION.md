Refactor: extract assets and modularize JS

This PR refactors the project's single-file UI into a cleaned, maintainable layout
with extracted assets and basic validation helpers.

What changed
- Extracted inline CSS into `assets/styles.css`.
- Extracted inline JS into modules under `assets/modules/` and entry `assets/main.js`.
- Added a cleaned `index.html` referencing the extracted assets.
- Added lightweight checks and smoke tests under `tools/` and `tests/`.
- Kept the original `Aegis` file as a redirect to preserve history.

Files of interest
- `assets/styles.css`, `assets/main.js`, `assets/modules/*`
- `index.html`
- `tools/check_html.py`, `tools/a11y_check.py`, `tests/index.html`
- Patch for review: `tidy/assets-extract-changes.patch`

Preview
- Run a local static server and open: `http://localhost:8000/index.html`

Notes
- Intent: improve maintainability and accessibility; avoid behavioral regressions.
- Follow-up suggestions: split JS further, add unit tests, wire a CI check for HTML/a11y.

PR Checklist

- [ ] Confirm visual parity in a browser (`python -m http.server 8000` then open `/index.html`).
- [ ] Run `python tools/check_html.py` and `python tools/a11y_check.py` and address any issues.
- [ ] Verify smoke tests: open `tests/index.html` in a browser.
- [ ] Ensure CI (if configured) passes on the PR.

