"""plot_config.py

This module contains the configuration for the :mod:`matplotlib` and :mod:`seaborn` plots. It uses the :class:`src.config.settings.PlotConfig` class for the parameters.
"""

from seaborn import set_theme

from .config.settings import PlotConfig


def setup_plots() -> None:
    """
    Setup the plot configuration using the :class:`src.config.settings.PlotConfig` parameters.
    """
    cfg = PlotConfig()
    set_theme(
        context=cfg.CONTEXT,
        style=cfg.STYLE,
        palette=cfg.PALETTE,
        rc={
            "figure.figsize": cfg.FIGSIZE,
            "figure.dpi": cfg.DPI,
            "savefig.format": cfg.FORMAT.lower(),
            "savefig.bbox": cfg.BBOX,
        },
    )
