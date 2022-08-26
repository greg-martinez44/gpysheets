from pathlib import Path
import pytest
from gpysheets import Connection


def test_connection_import_is_successful():
    assert(True)


def test_path_to_creds_file_is_correct():
    connection = Connection()
    expected_path = str(Path(
        Path(__file__).parent.parent.absolute(), "resources", "credentials.json"))
    actual_path = connection.cred_file_path()
    assert(expected_path == actual_path)


def test_connection_returns_service():
    connection = Connection()
    service = connection.get_service()
    assert(service.spreadsheets())
