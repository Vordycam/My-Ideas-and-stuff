# Changelog

## Unreleased

- Extracted inline CSS to `assets/styles.css`.
- Extracted inline JS to modular ES modules (`assets/modules/*`) and added `assets/main.js` entry.
- Added `README.md` and local sanity checks (`tools/check_html.py`, `tools/a11y_check.py`).
- Added browser-based tests at `tests/index.html` and a PowerShell helper `tools/run_tests.ps1` to preview them.
- Added `package.json` with basic scripts.

### Notes

- No breaking changes expected; this refactor moves inline assets into standalone files and adds tooling for validation and testing.
- Recommend running the included sanity checks locally before merging.

### PR Checklist

- [ ] Confirm visual parity in a browser (`python -m http.server 8000` then open `/index.html`).
- [ ] Run `python tools/check_html.py` and `python tools/a11y_check.py` and address any issues.
- [ ] Verify smoke tests: open `tests/index.html` in a browser.
- [ ] Ensure CI (if configured) passes on the PR.

