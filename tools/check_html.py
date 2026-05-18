#!/usr/bin/env python3
"""Simple sanity checks for index.html (no external deps).
Checks for presence of doctype, stylesheet link, and app script reference.
Exits with 0 on success, 1 on failure.
"""
import sys
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'index.html'
if not p.exists():
    print('ERROR: index.html not found at', p)
    sys.exit(1)
text = p.read_text(encoding='utf-8').lower()
errors = []
if '<!doctype html' not in text:
    errors.append('missing doctype')
if 'link rel="stylesheet" href="./assets/styles.css"' not in text:
    errors.append('missing stylesheet link to ./assets/styles.css')
# Accept either the legacy app.js or the new ES module main.js
if ('<script src="./assets/app.js"></script>' not in text) and ('<script type="module" src="./assets/main.js"></script>' not in text) and ('<script src="./assets/main.js"></script>' not in text):
    errors.append('missing script src to ./assets/app.js or ./assets/main.js')
if '<meta charset' not in text:
    errors.append('missing meta charset')

if errors:
    print('HTML sanity check FAILED:')
    for e in errors:
        print(' -', e)
    sys.exit(1)
print('HTML sanity check passed: index.html looks good (basic checks)')
sys.exit(0)
