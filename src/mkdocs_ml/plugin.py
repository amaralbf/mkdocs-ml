from pathlib import Path
from typing import Literal, Optional, Tuple

# from mkdocs.config import config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin, Config

from mkdocs_ml.markdown import MarkdownCompleter

MKDOCS_ML_DIRNAME = 'mkdocs-ml-data'


class Plugin(BasePlugin):
    config_scheme: Tuple = tuple()

    def on_startup(
        self, *, command: Literal['build', 'gh-deploy', 'serve'], dirty: bool
    ) -> None:
        pass

    def on_config(self, config: MkDocsConfig) -> Optional[Config]:
        self.docs_dir = Path(config['docs_dir'])
        self.data_dir = self.docs_dir / MKDOCS_ML_DIRNAME
        return config

    def on_pre_build(self, *, config: MkDocsConfig) -> None:
        self.data_dir.mkdir(exist_ok=True)

    # def on_pre_page(self, page, *, config, files):
    #     print(f'{page=}')
    #     print(f'{config=}')
    #     print(f'{files=}')
    #     return page

    # def on_page_read_source(self, *, page, config):
    #     print(f'{page=}')
    #     print(f'{config=}')

    def on_page_markdown(self, markdown: str, *, page, config, files):
        completer = MarkdownCompleter(docs_dir=self.docs_dir, data_dir=self.data_dir)
        processed_markdown = completer.complete_markdown(markdown)

        return processed_markdown
