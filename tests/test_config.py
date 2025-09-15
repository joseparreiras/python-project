from src.utils.config.settings import (
    DataPaths,
    ImagesPaths,
    LoggerConfig,
    Parameters,
    Paths,
    PlotConfig,
    Settings,
)


def test_settings():
    assert Settings() is not None


def test_paths():
    assert Paths() is not None


def test_plot_config():
    assert PlotConfig() is not None


def test_images_paths():
    assert ImagesPaths() is not None


def test_data_paths():
    assert DataPaths() is not None


def test_logger_config():
    assert LoggerConfig() is not None


def test_parameters():
    assert Parameters() is not None
