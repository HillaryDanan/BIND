"""
BIND - Boundary Information Neural Dynamics Framework

A mathematical framework for understanding consciousness emergence at system boundaries.

Author: Hillary Danan, Ph.D.
Email: hillarydanan@gmail.com
"""

__version__ = "0.1.0"
__author__ = "Hillary Danan"
__email__ = "hillarydanan@gmail.com"

# Import main components
from .config import BoundaryConfig
from .core.boundary_state import BoundaryState

__all__ = ['BoundaryConfig', 'BoundaryState']
