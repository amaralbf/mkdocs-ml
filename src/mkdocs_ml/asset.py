from pathlib import Path

from matplotlib.figure import Figure


class MatplotlibAsset:
    def __init__(self, key, data: Figure):
        self.filename = self.generate_filename(key)
        self.fig = data

    def save(self, data_dir: Path):
        self.fig.savefig(data_dir / self.filename)

    @staticmethod
    def generate_filename(key):
        return f'{key}.png'


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
