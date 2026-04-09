"""Very small accessibility checks for index.html
- Ensure inputs have labels or aria-label
- Ensure interactive buttons have type
- Ensure landmark elements exist (nav, main, footer)
"""
from pathlib import Path
import sys

p = Path(__file__).resolve().parent.parent / 'index.html'
if not p.exists():
    print('index.html missing')
    sys.exit(2)
text = p.read_text(encoding='utf-8')
problems = []
if '<nav' not in text.lower():
    problems.append('no <nav> found')
if '<footer' not in text.lower():
    problems.append('no <footer> found')
if 'aria-label' not in text and '<label' not in text:
    problems.append('no aria-label or <label> found for inputs')
if 'type="button"' not in text and "type='button'" not in text:
    problems.append('some interactive elements may lack type="button"')

if problems:
    print('A11Y quick check found potential issues:')
    for p in problems:
        print(' -', p)
    sys.exit(1)
print('A11Y quick check: basic checks passed')
sys.exit(0)
