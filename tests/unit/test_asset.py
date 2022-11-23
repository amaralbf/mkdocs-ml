from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import pytest

from mkdocs_ml.asset import (
    MatplotlibAsset,
    TableAsset,
    TextAsset,
    get_asset_class_from_data,
)


@pytest.fixture
def plot_asset():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    KEY = 'plot'

    asset = MatplotlibAsset(key=KEY, data=fig)
    return asset


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
    with open(tmp_path / filename, 'rt') as f:
        assert f.read() == TEXT


def test_table_asset_file_creation_from_dataframe(tmp_path: Path):
    KEY = 'table'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    asset = TableAsset(key=KEY, data=df)
    asset.save(data_dir=tmp_path)

    files = list(tmp_path.iterdir())

    assert len(files) == 1

    filename = str(files[0])
    with open(tmp_path / filename, 'rt') as f:
        assert f.read() == df.to_markdown()


@pytest.mark.parametrize(
    ['data', 'expected_class'],
    [
        ('string', TextAsset),
        (plt.subplots()[0], MatplotlibAsset),
        (pd.DataFrame(), TableAsset),
    ],
)
def test_get_asset_class_from_data(data, expected_class):
    assert get_asset_class_from_data(data) == expected_class
