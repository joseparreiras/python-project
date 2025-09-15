"""tables.py

This module contains the functions to read and write tables. It uses the :class:`src.config.settings.DataPaths` class for the parameters.
"""

import pandas as pd
from pydantic import FilePath

from .config.settings import DataPaths


def read_table(path: FilePath, **kwargs) -> pd.DataFrame:
    """
    Read a table from a file. The read function is chosen based on :attr:`DataPaths.EXTENSION`.
    """
    if DataPaths().EXTENSION == "parquet":
        return pd.read_parquet(path, **kwargs)
    elif DataPaths().EXTENSION == "csv":
        return pd.read_csv(path, **kwargs)
    else:
        raise ValueError(f"Unsupported extension: {DataPaths().EXTENSION}")


def write_table(df: pd.DataFrame, path: FilePath, **kwargs) -> None:
    """
    Write a table to a file. The write function is chosen based on :attr:`DataPaths.EXTENSION`.
    """
    if DataPaths().EXTENSION == "parquet":
        df.to_parquet(path, **kwargs)
    elif DataPaths().EXTENSION == "csv":
        df.to_csv(path, **kwargs)
    else:
        raise ValueError(f"Unsupported extension: {DataPaths().EXTENSION}")
