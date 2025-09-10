"""setup_logger.py

This module contains the function to setup the logger. It uses the :class:`src.config.settings.LoggerConfig` class from :mod:`src.config.settings` for the parameters.
"""

from logging import (
    getLogger,
    Logger,
    FileHandler,
    StreamHandler,
)
from logging import Formatter
from src.config.settings import LoggerConfig


def setup_logger() -> Logger:
    logger = getLogger(LoggerConfig.NAME)
    logger.setLevel(LoggerConfig.LEVEL)

    # Ensure logs directory exists
    LoggerConfig.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    formatter = Formatter(LoggerConfig.FORMAT, LoggerConfig.DATEFMT)

    file_handler = FileHandler(LoggerConfig.LOG_FILE, mode="w")
    file_handler.setLevel(LoggerConfig.FILE_LEVEL)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = StreamHandler()
    console_handler.setLevel(LoggerConfig.CONSOLE_LEVEL)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
