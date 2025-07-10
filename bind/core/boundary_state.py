"""
Boundary state representation for BIND framework.

Author: Hillary Danan
Date: July 2025
"""

from dataclasses import dataclass
import numpy as np


@dataclass
class BoundaryState:
    """
    Represents the state of an information boundary at a specific time.
    
    This class encapsulates all relevant measurements of a boundary's
    information-theoretic properties at a given moment.
    
    Attributes:
        entropy_gradient: The gradient of entropy across the boundary (∇S)
        normal_vector: The unit normal vector to the boundary (n̂)
        information_flux: Information flow across boundary I(B) = ∇S · n̂
        decoherence_rate: Rate of quantum decoherence D(t)
        phi_integrated: Integrated information measure Φ(I)
        timestamp: When this state was measured
    """
    
    entropy_gradient: np.ndarray
    normal_vector: np.ndarray
    information_flux: float
    decoherence_rate: float
    phi_integrated: float
    timestamp: float
    
    def __post_init__(self):
        """Validate the boundary state."""
        # Ensure arrays are numpy arrays
        self.entropy_gradient = np.asarray(self.entropy_gradient)
        self.normal_vector = np.asarray(self.normal_vector)
        
        # Normalize the normal vector
        norm = np.linalg.norm(self.normal_vector)
        if norm > 0:
            self.normal_vector = self.normal_vector / norm
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            'entropy_gradient': self.entropy_gradient.tolist(),
            'normal_vector': self.normal_vector.tolist(),
            'information_flux': float(self.information_flux),
            'decoherence_rate': float(self.decoherence_rate),
            'phi_integrated': float(self.phi_integrated),
            'timestamp': float(self.timestamp)
        }
