"""setup_logger.py

This module contains the function to setup the logger. It uses the :class:`src.config.settings.LoggerConfig` class from :mod:`src.config.settings` for the parameters.
"""

from inspect import currentframe, getfile
from logging import FileHandler, Formatter, Logger, StreamHandler, getLogger
from pathlib import Path

from .config.settings import LoggerConfig


def get_script_name() -> str:
    """
    Get the name of the script.
    """
    frame = currentframe()
    try:
        filename = getfile(frame.f_back)
        return Path(filename).stem
    finally:
        del frame


def setup_logger(name: str | None = None) -> Logger:
    """
    Setup the logger using the :class:`src.utils.config.settings.LoggerConfig` parameters.

    Args:
        name: The name of the logger. If None, the name of the script is used.

    Returns:
        The logger.
    """
    if name is None:
        name = get_script_name()
    cfg = LoggerConfig()

    logger = getLogger(name)
    logger.setLevel(level=cfg.LEVEL)
    # Ensure logs directory exists
    cfg.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    formatter = Formatter(fmt=cfg.FORMAT, datefmt=cfg.DATEFMT)

    if cfg.FILE_LEVEL is not None:
        file_handler = FileHandler(cfg.LOG_FILE, mode="w")
        file_handler.setLevel(level=cfg.FILE_LEVEL)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if cfg.CONSOLE_LEVEL is not None:
        console_handler = StreamHandler()
        console_handler.setLevel(level=cfg.CONSOLE_LEVEL)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
