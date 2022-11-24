import json
from pathlib import Path

import pandas as pd
from matplotlib.figure import Figure


class MatplotlibAsset:
    def __init__(self, key, data: Figure):
        self.key = key
        self.fig = data

    def save(self, data_dir: Path):
        self.file_path = (data_dir / self.generate_filename()).resolve().absolute()
        self.fig.savefig(self.file_path)

    def get_info_for_markdown(self):
        return {
            'class': self.__class__.__name__,
            'args': {
                'image_path': str(self.file_path),
            },
        }

    def generate_filename(self):
        return f'{self.key}.png'

    @staticmethod
    def get_markdown(image_path, docs_dir: Path):
        return f'![]({Path(image_path).relative_to(docs_dir)})'


class TextAsset:
    def __init__(self, key, data: str):
        self.filename = self.generate_filename(key)
        self.data = data

    def save(self, data_dir: Path):
        with open(data_dir / self.filename, 'wt') as f:
            f.write(self.data)

    @staticmethod
    def generate_filename(key):
        return f'{key}.txt'


class TableAsset:
    def __init__(self, key, data: pd.DataFrame):
        self.filename = self.generate_filename(key)
        self.data = data

    @staticmethod
    def generate_filename(key):
        return f'{key}.txt'

    def save(self, data_dir: Path):
        self.data.to_markdown(data_dir / self.filename)


def get_asset_class_from_data(data):
    if isinstance(data, str):
        return TextAsset
    elif isinstance(data, pd.DataFrame):
        return TableAsset
    elif isinstance(data, Figure):
        return MatplotlibAsset


ASSETS_COLLECTION_FILE_NAME = 'assets_info.json'


class AssetCollection:
    def __init__(self, data_dir: Path, clear=False) -> None:
        self.filepath = self.get_filepath(data_dir)
        if clear:
            self.create_file()

    @staticmethod
    def get_filepath(data_dir: Path) -> Path:
        return data_dir / ASSETS_COLLECTION_FILE_NAME

    def create_file(self):
        with open(self.filepath, 'wt') as f:
            json.dump({}, f)

    def add_asset(self, asset):
        with open(self.filepath, 'rt') as f:
            collection_dict = json.load(f)

        collection_dict[asset.key] = asset.get_info_for_markdown()

        with open(self.filepath, 'wt') as f:
            json.dump(collection_dict, f)

    def get_asset_info(self, key: str):
        with open(self.filepath, 'rt') as f:
            collection_dict = json.load(f)
            asset_info = collection_dict[key]
        return asset_info
