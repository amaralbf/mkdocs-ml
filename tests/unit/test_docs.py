from mkdocs_ml.asset import ASSETS_COLLECTION_FILE_NAME
from mkdocs_ml.docs import Docs


def test_docs_object_creation(project):
    docs = Docs()
    assert docs.data_dir == project.data_dir


def test_asset_collection_file_is_created_upon_docs_object_creation(project):
    docs = Docs()
    data_dir = docs.data_dir

    data = list(data_dir.iterdir())

    assert len(data) == 1
    assert data[0].parts[-1] == str(ASSETS_COLLECTION_FILE_NAME)
