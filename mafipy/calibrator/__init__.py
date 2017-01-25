"""
======================================
calibrator (:mod:`mafipy.calibrator`)
======================================

.. currentmodule:: mafipy.calibrator


Implied volatility
==================

Basics
------

.. autosummary::
    :toctree: generated/

    black_scholes_implied_vol
    black_swaption_implied_vol

SABR calibration
================

.. autosummary::
    :toctree: generated/

    sabr_caibration_simple
    sabr_caibration_west
"""

from __future__ import division, print_function, absolute_import

from .implied_vol import *
from .sabr import *

__all__ = [s for s in dir() if not s.startswith('_')]
