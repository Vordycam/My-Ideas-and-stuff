import os


def test_files_exist():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    assert os.path.exists(os.path.join(root, 'index.html'))
    assert os.path.exists(os.path.join(root, 'assets', 'styles.css'))


def test_index_references_styles():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    with open(os.path.join(root, 'index.html'), 'r', encoding='utf-8') as f:
        html = f.read()
    assert 'assets/styles.css' in html
