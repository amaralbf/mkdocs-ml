import re
from importlib import import_module
from pathlib import Path

from .asset import AssetCollection


class MarkdownCompleter:
    PATTERN = r'\{ml:([^}]+)\}'

    def __init__(self, docs_dir: Path, data_dir: Path) -> None:
        self.docs_dir = docs_dir
        self.data_dir = data_dir

    def complete_markdown(self, markdown: str):
        asset_collection = AssetCollection(data_dir=self.data_dir)

        processed_markdown = markdown
        for match in re.finditer(self.PATTERN, markdown):
            key = match.group(1)

            asset_info = asset_collection.get_asset_info(key)
            asset_module = import_module('mkdocs_ml.asset')
            asset_class = getattr(asset_module, asset_info['class'])
            asset_markdown = asset_class.get_markdown(
                **asset_info['args'], docs_dir=self.docs_dir
            )

            processed_markdown = processed_markdown.replace(
                f'{{ml:{key}}}', asset_markdown
            )

        return processed_markdown
