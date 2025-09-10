from src.utils.logger import setup_logger
from src.utils.plots import setup_plots

def test_logger():
    assert setup_logger() is not None

def test_plots():
    assert setup_plots() is None