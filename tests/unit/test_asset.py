from pathlib import Path

import matplotlib.pyplot as plt
import pytest

from mkdocs_ml.asset import MatplotlibAsset


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
