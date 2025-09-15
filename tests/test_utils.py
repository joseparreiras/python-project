import tempfile

import pandas as pd
import pytest

from src.utils.logger import setup_logger
from src.utils.plots import setup_plots
from src.utils.tables import read_table, write_table


@pytest.fixture(scope="session")
def dummy_data():
    return pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 2, 3, 4, 5]})


@pytest.fixture(scope="session")
def temp_file():
    return tempfile.NamedTemporaryFile(suffix=".parquet")


def test_logger():
    assert setup_logger() is not None


def test_plots():
    assert setup_plots() is None


def test_write_table(dummy_data, temp_file):
    try:
        write_table(dummy_data, temp_file.name)
    except Exception as e:
        pytest.fail(f"Error writing table: {e}")


def test_read_table(dummy_data, temp_file):
    data = read_table(temp_file.name)
    assert data.equals(dummy_data)
