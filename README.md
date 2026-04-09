AEGIS — cleaned UI and assets

What I changed

- Extracted inline CSS into `assets/styles.css`.
- Extracted inline JS into `assets/app.js`.
- Updated `index.html` to reference the extracted assets.
- Left `Aegis` as a redirect to `index.html` to preserve history.

How to preview

Open `index.html` in your browser. On Windows you can run:

```powershell
start 'index.html'
```

If you prefer a local static server (recommended to avoid some cross-origin font issues), run in PowerShell:

```powershell
# if you have Python 3 installed
python -m http.server 8000; start 'http://localhost:8000/index.html'
```

Next steps (optional)

- Split more JS into modules and add a simple bundler if you plan to extend behavior.
- Add unit tests for JS functions and small smoke tests.
- Run an HTML/CSS/Accessibility validator.
