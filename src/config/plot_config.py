"""plot_config.py

This module contains the configuration for the :mod:`matplotlib` and :mod:`seaborn` plots. It uses the :class:`src.config.settings.PlotConfig` class for the parameters.
"""

from seaborn import set_theme
from src.config.settings import PlotConfig


def setup_plot() -> None:
    """
    Setup the plot configuration using the :class:`src.config.settings.PlotConfig` parameters.
    """
    set_theme(
        context=PlotConfig.CONTEXT,
        style=PlotConfig.STYLE,
        palette=PlotConfig.PALETTE,
        rc={
            "figure.figsize": PlotConfig.FIGSIZE,
            "figure.dpi": PlotConfig.DPI,
            "savefig.format": PlotConfig.FORMAT.lower(),
            "savefig.bbox": PlotConfig.BBOX,
            "savefig.directory": PlotConfig.DIRECTORY,
        },
    )
