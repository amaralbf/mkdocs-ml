from pathlib import Path

import matplotlib.pyplot as plt

from mkdocs_ml.asset import AssetCollection, MatplotlibAsset


def test_plot_image(tmp_path):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    KEY = 'plot'

    asset = MatplotlibAsset(key=KEY, data=fig)
    asset.save(data_dir=tmp_path)

    markdown = f'''
    # plot

    {{ml:{KEY}}}
    '''
    asset_collection = AssetCollection(data_dir=tmp_path, clear=True)
    asset_collection.add_asset(asset)

    loaded_asset_collection = AssetCollection(data_dir=tmp_path)
    asset_markdown = loaded_asset_collection.get_asset_markdown(KEY, docs_dir=tmp_path)

    processed_markdown = markdown.replace(f'{{ml:{KEY}}}', asset_markdown)

    expected = f'''
    # plot

    ![]({Path(asset.file_path).relative_to(tmp_path)})
    '''
    assert processed_markdown == expected
