from pathlib import Path

from .asset import AssetCollection, get_asset_class_from_data


class Docs:
    def __init__(self):
        self.data_dir = _find_data_dir()
        self.asset_collection = AssetCollection(data_dir=self.data_dir, clear=True)

    def add_to_docs(self, key, obj):
        asset_class = get_asset_class_from_data(obj)
        asset = asset_class(key, obj)
        asset.save(self.data_dir)

        self.asset_collection.add_asset(asset)


def _find_data_dir():
    docs_dir = _find_docs_dir()
    data_dir = docs_dir / 'mkdocs-ml'
    if data_dir.exists() and data_dir.is_dir():
        return data_dir

    raise Exception('Data dir not found.')


def _find_docs_dir():
    current_path = Path().absolute()
    for p in current_path.iterdir():
        if p.is_dir() and p.parts[-1] == 'docs':
            return p
    raise Exception('Docs dir not found.')
