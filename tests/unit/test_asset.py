from pathlib import Path

import matplotlib.pyplot as plt

from mkdocs_ml.asset import MatplotlibAsset, TextAsset

# import pytest


def test_plot_png_creation(tmp_path: Path):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    KEY = 'plot'

    asset = MatplotlibAsset(key=KEY, data=fig)
    asset.save(data_dir=tmp_path)

    files = list(tmp_path.iterdir())

    assert len(files) == 1
    assert KEY in str(files[0])
    assert str(files[0]).endswith('.png')


def test_text_file_creation_from_string(tmp_path: Path):
    TEXT = 'Text to add to the docs.'
    KEY = 'text'

    asset = TextAsset(key=KEY, data=TEXT)
    asset.save(data_dir=tmp_path)

    files = list(tmp_path.iterdir())

    assert len(files) == 1

    filename = str(files[0])
    assert KEY in filename and filename.endswith('.txt')

    with open(tmp_path / filename, 'rt') as f:
        assert f.read() == TEXT
