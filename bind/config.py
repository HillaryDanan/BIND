"""
Configuration module for BIND (Boundary Information Neural Dynamics) framework.

This module provides configuration management for all BIND parameters,
allowing for easy customization and reproducibility of experiments.

Author: Hillary Danan
Date: July 2025
"""

from dataclasses import dataclass
import json
import os


@dataclass
class BoundaryConfig:
    """
    Configuration for BIND (Boundary Information Neural Dynamics) parameters.
    
    All parameters have sensible defaults based on theoretical predictions
    and empirical observations from neuroscience literature.
    """
    
    # Theoretical constants from literature
    phi_critical: float = 4.3  # Theoretical consciousness threshold (Tononi, 2015)
    transformation_beta: float = 0.73  # Empirical transformation rate
    high_flux_threshold: float = 1e8  # Information flux threshold (bits/second)
    creative_decoherence_threshold: float = 1.0  # Decoherence creativity threshold
    
    # System parameters
    boundary_detection_method: str = "gradient"  # Options: "gradient", "laplacian"
    entropy_calculation_method: str = "shannon"  # Options: "shannon", "renyi"
    integration_time_window: float = 0.1  # Time window in seconds
    spatial_resolution: float = 0.001  # Spatial resolution in meters
    
    # Hexagonal topology parameters
    hex_grid_size: int = 7  # Number of hexagons per side
    hex_connectivity: int = 6  # Hexagonal has 6 neighbors by definition
    
    # Trust dynamics parameters
    trust_decay_rate: float = 0.1  # How quickly trust decays
    trust_growth_rate: float = 0.3  # How quickly trust grows
    initial_trust: float = 0.5  # Starting trust level
    
    # Numerical stability parameters
    epsilon: float = 1e-10  # Small value to prevent division by zero
    max_iterations: int = 1000  # Maximum iterations for convergence
    convergence_threshold: float = 1e-6  # Convergence criterion
    
    @classmethod
    def from_json(cls, path: str) -> 'BoundaryConfig':
        """Load configuration from JSON file."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Configuration file not found: {path}")
            
        with open(path, 'r') as f:
            data = json.load(f)
            
        return cls(**data)
    
    def to_json(self, path: str) -> None:
        """Save configuration to JSON file."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        with open(path, 'w') as f:
            json.dump(self.__dict__, f, indent=2)
    
    def validate(self) -> bool:
        """Validate configuration parameters."""
        validations = [
            (self.phi_critical > 0, "phi_critical must be positive"),
            (self.transformation_beta > 0, "transformation_beta must be positive"),
            (self.boundary_detection_method in ["gradient", "laplacian"], 
             "Invalid boundary detection method"),
            (self.entropy_calculation_method in ["shannon", "renyi"], 
             "Invalid entropy calculation method"),
            (self.hex_grid_size > 0, "hex_grid_size must be positive"),
            (0 <= self.initial_trust <= 1, "initial_trust must be between 0 and 1"),
        ]
        
        for condition, message in validations:
            if not condition:
                raise ValueError(f"Configuration error: {message}")
                
        return True
