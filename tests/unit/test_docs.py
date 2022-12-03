from collections import namedtuple
from pathlib import Path

import pytest

from mkdocs_ml.asset import ASSETS_COLLECTION_FILE_NAME
from mkdocs_ml.docs import Docs

Project = namedtuple('Project', ['project_dir', 'docs_dir', 'data_dir'])


@pytest.fixture
def project(tmp_path: Path, monkeypatch):
    project_dir = tmp_path / 'project'
    project_dir.mkdir()

    docs_dir = project_dir / 'docs'
    docs_dir.mkdir()

    data_dir = docs_dir / 'mkdocs-ml'
    data_dir.mkdir()

    monkeypatch.chdir(project_dir)

    return Project(project_dir, docs_dir, data_dir)


def test_docs_object_creation(project: Project):
    docs = Docs()
    assert docs.data_dir == project.data_dir


def test_asset_collection_file_is_created_upon_docs_object_creation(project: Project):
    docs = Docs()
    data_dir = docs.data_dir

    data = list(data_dir.iterdir())

    assert len(data) == 1
    assert data[0].parts[-1] == str(ASSETS_COLLECTION_FILE_NAME)
