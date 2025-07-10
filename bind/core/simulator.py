"""
Data simulation for testing BIND framework.

Author: Hillary Danan
Date: July 2025
"""

import numpy as np
from typing import Dict, Tuple, Optional


class BoundarySimulator:
    """Generate test data with known boundary properties."""
    
    @staticmethod
    def generate_two_phase_system(size: Tuple[int, ...] = (100, 100),
                                 boundary_sharpness: float = 0.1) -> np.ndarray:
        """
        Generate a system with two distinct phases and a boundary.
        
        Args:
            size: Dimensions of the system
            boundary_sharpness: How sharp the boundary is (0-1)
            
        Returns:
            numpy array with two-phase system
        """
        if len(size) == 1:
            x = np.linspace(-5, 5, size[0])
            # Sigmoid boundary
            data = 1 / (1 + np.exp(-x/boundary_sharpness))
        else:
            x = np.linspace(-5, 5, size[0])
            y = np.linspace(-5, 5, size[1])
            X, Y = np.meshgrid(x, y)
            
            # Circular boundary
            R = np.sqrt(X**2 + Y**2)
            data = 1 / (1 + np.exp(-(R - 2.5)/boundary_sharpness))
            
        # Add some noise
        noise = np.random.normal(0, 0.05, size)
        return data + noise
    
    @staticmethod
    def generate_consciousness_emergence(timesteps: int = 100,
                                       size: Tuple[int, ...] = (50, 50)) -> List[np.ndarray]:
        """
        Generate a sequence showing consciousness emergence over time.
        
        Returns:
            List of arrays showing system evolution
        """
        states = []
        
        for t in range(timesteps):
            # System becomes more organized over time
            organization = t / timesteps
            
            # Generate increasingly complex boundaries
            if len(size) == 2:
                x = np.linspace(-5, 5, size[0])
                y = np.linspace(-5, 5, size[1])
                X, Y = np.meshgrid(x, y)
                
                # Multiple interacting regions
                data = np.zeros(size)
                
                # Add multiple boundaries that interact
                for i in range(int(1 + 3 * organization)):
                    cx = np.random.uniform(-3, 3)
                    cy = np.random.uniform(-3, 3)
                    R = np.sqrt((X - cx)**2 + (Y - cy)**2)
                    data += 1 / (1 + np.exp(-(R - 1.5)/(0.5 - 0.4*organization)))
                
                # Normalize
                data = (data - data.min()) / (data.max() - data.min() + 1e-10)
                
                # Add decreasing noise
                noise_level = 0.2 * (1 - organization)
                data += np.random.normal(0, noise_level, size)
                
            states.append(data)
        
        return states
