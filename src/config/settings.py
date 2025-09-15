"""settings.py

This module contains the configuration for the project. It uses the :class:`BaseSettings` class from :mod:`pydantic_settings` for the parameters.
"""

from datetime import datetime
from pathlib import Path
from typing import ClassVar, Literal, TypeAlias

from pydantic import (
    BaseModel,
    DirectoryPath,
    FilePath,
    PositiveFloat,
    PositiveInt,
    field_validator,
    model_validator,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

# Type aliases
LogLevel: TypeAlias = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
SnsPlotContext: TypeAlias = Literal["paper", "notebook", "talk", "poster"]
SnsPlotStyle: TypeAlias = Literal["white", "dark", "whitegrid", "darkgrid", "ticks"]
SnsPlotPalette: TypeAlias = Literal[
    "deep", "muted", "pastel", "bright", "dark", "colorblind"
]


def settings_from_env(prefix: str) -> SettingsConfigDict:
    """
    Read the settings from the environment file.

    Args:
        prefix: The prefix of the environment variables.

    Returns:
        The settings from the environment file.
    """
    return SettingsConfigDict(env_file=".env", env_prefix=prefix, extra="ignore")


@classmethod
def validate_file_names(cls, values):
    """Automatically append file extension to all FilePath attributes."""
    # Process each field that might need extension
    try:
        directory_path = cls.model_fields["DIRECTORY"].default
        extension = cls.model_fields["EXTENSION"].default

    except KeyError:
        raise ValueError(f"Class {cls} must have EXTENSION and DIRECTORY attributes")
    for field_name, field_info in cls.model_fields.items():
        if field_name in ["DIRECTORY", "EXTENSION"]:
            continue
        value = field_info.default
        if isinstance(value, str):
            # Create full path with directory and extension
            full_path = Path(directory_path, f"{value}.{extension}")
            values[field_name] = full_path
    return values


class ProjectConfig(BaseModel):
    """
    Project name.
    """

    NAME: ClassVar[str] = Path(__file__).parent.parent.parent.name


class Paths(BaseSettings):
    """
    Project paths.
    """

    PROJECT_ROOT: DirectoryPath
    PACKAGE_ROOT: DirectoryPath
    IMAGES: DirectoryPath
    DATA: DirectoryPath
    INPUT: DirectoryPath
    OUTPUT: DirectoryPath
    LOGS: DirectoryPath
    SCRIPTS: DirectoryPath
    TESTS: DirectoryPath

    model_config = settings_from_env(prefix="PATH_")


class PlotConfig(BaseSettings):
    """
    Plot configuration for :mod:`matplotlib` and :mod:`seaborn`.
    """

    # Figure parameters
    FIGSIZE: str
    DPI: PositiveInt
    FORMAT: str
    BBOX: str
    CONTEXT: SnsPlotContext
    STYLE: SnsPlotStyle
    PALETTE: SnsPlotPalette
    FONT: str
    FONT_SCALE: PositiveFloat
    FONTSIZE: PositiveInt

    model_config = settings_from_env(prefix="PLOT_")

    @field_validator("FIGSIZE", mode="after")
    @classmethod
    def validate_figsize(cls, v):
        if not isinstance(v, str):
            raise ValueError(
                "FIGSIZE must be a string of two positive integers separated by a comma"
            )
        return tuple(map(int, v.split(",")))


class ImagesPaths(BaseModel):
    """
    Images paths.
    """

    DIRECTORY: DirectoryPath = Paths().IMAGES
    EXTENSION: str = PlotConfig().FORMAT

    validate_images_paths = model_validator(mode="before")(validate_file_names)


class DataPaths(BaseModel):
    """
    Data paths.
    """

    DIRECTORY: DirectoryPath = Paths().DATA
    EXTENSION: str = "parquet"
    DUMMY: Path = "dummy"

    validate_data_paths = model_validator(mode="before")(validate_file_names)


class LoggerConfig(BaseSettings):
    """
    Logger configuration for the project using :mod:`logging`.
    """

    DIRECTORY: DirectoryPath = Paths().LOGS
    NAME: ClassVar[str] = ProjectConfig().NAME
    LEVEL: LogLevel
    FORMAT: str
    DATEFMT: str
    LOG_FILE: ClassVar[FilePath] = Path(DIRECTORY, f"{NAME}.log")
    CONSOLE_LEVEL: LogLevel
    FILE_LEVEL: LogLevel

    model_config = settings_from_env(prefix="LOG_")

    @field_validator("DATEFMT", mode="after")
    @classmethod
    def validate_datefmt(cls, v):
        try:
            datetime.now().strftime(v)
        except ValueError:
            raise ValueError("DATEFMT must be a valid datetime format")
        return v


class Parameters(BaseModel):
    """
    Parameters for the project.
    """

    RANDOM_SEED: PositiveInt = 19210102


class Settings(BaseSettings):
    """
    Settings for the project.
    """

    project_config: ProjectConfig = ProjectConfig()
    paths: Paths = Paths()
    logger_config: LoggerConfig = LoggerConfig()
    parameters: Parameters = Parameters()
    plot_config: PlotConfig = PlotConfig()
