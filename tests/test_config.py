import pytest
from src.config.settings import Settings


def test_settings():
    settings = Settings()
    assert settings is not None
    assert settings.project_config is not None
    assert settings.paths is not None
    assert settings.plot_config is not None
    assert settings.logger_config is not None
    # assert Settings().parameters is not None
