"""settings.py

This module contains the configuration for the project. It uses the :class:`BaseSettings` class from :mod:`pydantic_settings` for the parameters.
"""

from pydantic_settings import BaseSettings
from pydantic import (
    BaseModel,
    Field,
    DirectoryPath,
    PositiveInt,
    PositiveFloat,
    FilePath,
)
from pathlib import Path
from typing import Annotated, ClassVar, Literal

LowerCaseStr = Annotated[str, Field(pattern=r"^[a-z]+$")]
UpperCaseStr = Annotated[str, Field(pattern=r"^[A-Z]+$")]

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class ProjectConfig(BaseSettings):
    """
    Project name.
    """

    NAME: ClassVar[str] = Path(__file__).parent.parent.parent.name


class Paths(BaseSettings):
    """
    Project paths.
    """

    PROJECT_ROOT: ClassVar[DirectoryPath] = Path(__file__).parent.parent.parent
    PACKAGE_ROOT: ClassVar[DirectoryPath] = Path(__file__).parent.parent
    IMAGES_PATH: ClassVar[DirectoryPath] = Path(PROJECT_ROOT, "images")
    DATA_PATH: ClassVar[DirectoryPath] = Path(PROJECT_ROOT, "data")
    INPUT_PATH: ClassVar[DirectoryPath] = Path(DATA_PATH, "raw")
    OUTPUT_PATH: ClassVar[DirectoryPath] = Path(DATA_PATH, "out")
    LOGS_PATH: ClassVar[DirectoryPath] = Path(PROJECT_ROOT, "logs")
    SCRIPTS_PATH: ClassVar[DirectoryPath] = Path(PROJECT_ROOT, "scripts")
    SRC_PATH: ClassVar[DirectoryPath] = Path(PROJECT_ROOT, "src")
    TESTS_PATH: ClassVar[DirectoryPath] = Path(PROJECT_ROOT, "tests")


class PlotConfig(BaseSettings):
    """
    Plot configuration for :mod:`matplotlib` and :mod:`seaborn`.
    """

    # Figure parameters
    FIGSIZE: ClassVar[tuple[PositiveInt, PositiveInt]] = (16, 10)
    DPI: ClassVar[PositiveInt] = 600
    # Savefig parameters
    FORMAT: ClassVar[LowerCaseStr] = "pdf"
    BBOX: ClassVar[str] = "tight"
    DIRECTORY: ClassVar[Path] = Path(Paths().IMAGES_PATH, FORMAT)
    # Seaborn style
    CONTEXT: ClassVar[Literal["paper", "notebook", "talk", "poster"]] = "paper"
    STYLE: ClassVar[Literal["white", "dark", "whitegrid", "darkgrid", "ticks"]] = (
        "whitegrid"
    )
    PALETTE: ClassVar[str] = "colorblind"
    FONT: ClassVar[str] = "sans-serif"
    FONT_SCALE: ClassVar[PositiveFloat] = 1.0
    FONTSIZE: ClassVar[PositiveInt] = 14


class LoggerConfig(BaseSettings):
    """
    Logger configuration for the project using :mod:`logging`.
    """

    NAME: ClassVar[str] = ProjectConfig().NAME
    LEVEL: ClassVar[LogLevel] = "INFO"
    FORMAT: ClassVar[str] = (
        "%(asctime)s - %(name)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s"
    )
    DATEFMT: ClassVar[str] = "%Y-%m-%d %H:%M:%S"
    HANDLERS: ClassVar[list[str]] = ["console", "file"]
    CONSOLE_LEVEL: ClassVar[LogLevel] = "INFO"
    FILE_LEVEL: ClassVar[LogLevel] = "INFO"
    LOG_FILE: ClassVar[FilePath] = Path(Paths().LOGS_PATH, f"{NAME}.log")


class Parameters(BaseModel):
    """
    Parameters for the project.
    """

    pass


class Settings(BaseSettings):
    """
    Settings for the project.
    """

    project_config: ProjectConfig = ProjectConfig()
    paths: Paths = Paths()
    parameters: Parameters = Parameters()
    plot_config: PlotConfig = PlotConfig()
    logger_config: LoggerConfig = LoggerConfig()
