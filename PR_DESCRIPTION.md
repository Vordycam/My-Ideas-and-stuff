PR title: refactor(ui): extract assets, modularize JS, add checks and tests

Summary:
- Move inline CSS/JS to organized assets.
- Modularize JS into ES modules: `feed.js`, `toast.js`, `ui.js` and `main.js` as the entry.
- Add lightweight sanity & accessibility checks and a small browser test harness.

Why:
- Improves editor/tooling behavior (files recognized as CSS/JS)
- Easier to maintain and extend UI behavior
- Adds quick checks and tests to reduce regressions

How to validate locally:
1. Run sanity checks:
   - python tools/check_html.py
   - python tools/a11y_check.py
2. Run browser tests:
   - python -m http.server 8000
   - open http://localhost:8000/tests/index.html

Notes:
- This PR does not change behavior beyond small accessibility improvements.
- Git is required to create the branch/commit; use `tools/apply_patch_locally.ps1` if you prefer a helper.
