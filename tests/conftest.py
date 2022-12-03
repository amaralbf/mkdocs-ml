from collections import namedtuple
from pathlib import Path

from pytest_cases import fixture

Project = namedtuple('Project', ['project_dir', 'docs_dir', 'data_dir'])


@fixture
def project(tmp_path: Path, monkeypatch):
    project_dir = tmp_path / 'project'
    project_dir.mkdir()

    docs_dir = project_dir / 'docs'
    docs_dir.mkdir()

    data_dir = docs_dir / 'mkdocs-ml'
    data_dir.mkdir()

    monkeypatch.chdir(project_dir)

    return Project(project_dir, docs_dir, data_dir)
