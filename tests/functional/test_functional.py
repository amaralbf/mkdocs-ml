from pathlib import Path

import matplotlib.pyplot as plt

from mkdocs_ml.asset import AssetCollection, MatplotlibAsset
from mkdocs_ml.markdown import MarkdownCompleter


def test_plot_image(tmp_path: Path):
    docs_dir = tmp_path / 'docs'
    data_dir = docs_dir / 'data_dir'

    data_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    KEY = 'plot'

    asset = MatplotlibAsset(key=KEY, data=fig)
    asset.save(data_dir=data_dir)

    markdown = f'''
    # plot

    {{ml:{KEY}}}
    '''
    asset_collection = AssetCollection(data_dir=data_dir, clear=True)
    asset_collection.add_asset(asset)

    completer = MarkdownCompleter(docs_dir=docs_dir, data_dir=data_dir)
    processed_markdown = completer.complete_markdown(markdown)

    expected = f'''
    # plot

    ![]({Path(asset.file_path).relative_to(docs_dir)})
    '''
    assert processed_markdown == expected
