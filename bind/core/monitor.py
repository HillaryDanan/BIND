"""
Boundary monitoring implementation for BIND framework.

Author: Hillary Danan
Date: July 2025
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from scipy.stats import entropy
from scipy.ndimage import laplace, gaussian_gradient_magnitude
import time

from ..config import BoundaryConfig
from .boundary_state import BoundaryState


class BoundaryMonitor:
    """
    Monitors and analyzes information boundaries in real systems.
    
    This is the core engine of BIND - it detects where information
    transforms and consciousness might emerge.
    """
    
    def __init__(self, config: Optional[BoundaryConfig] = None):
        self.config = config or BoundaryConfig()
        self.history: List[BoundaryState] = []
        
    def analyze_system(self, data: np.ndarray) -> BoundaryState:
        """
        Analyze a system to find and characterize its boundaries.
        
        Args:
            data: System state as numpy array (any dimensionality)
            
        Returns:
            BoundaryState with all computed metrics
        """
        # Detect boundaries
        boundaries = self._detect_boundaries(data)
        
        # Calculate entropy gradient
        entropy_grad = self._calculate_entropy_gradient(data, boundaries)
        
        # Calculate normal vectors
        normal = self._estimate_normal_vector(data, boundaries)
        
        # Information flux: I(B) = ∇S · n̂
        info_flux = np.abs(np.dot(entropy_grad, normal))
        
        # Decoherence rate (simplified - based on boundary sharpness)
        decoherence = self._calculate_decoherence(data, boundaries)
        
        # Integrated information (simplified Φ calculation)
        phi = self._calculate_phi(data, boundaries, info_flux)
        
        state = BoundaryState(
            entropy_gradient=entropy_grad,
            normal_vector=normal,
            information_flux=info_flux,
            decoherence_rate=decoherence,
            phi_integrated=phi,
            timestamp=time.time()
        )
        
        self.history.append(state)
        return state
    
    def _detect_boundaries(self, data: np.ndarray) -> np.ndarray:
        """Detect boundaries using configured method."""
        if self.config.boundary_detection_method == "gradient":
            # Gradient magnitude
            grad = gaussian_gradient_magnitude(data, sigma=1.0)
            threshold = np.percentile(grad, 90)
            return grad > threshold
        else:  # laplacian
            lap = laplace(data)
            threshold = np.percentile(np.abs(lap), 90)
            return np.abs(lap) > threshold
    
    def _calculate_entropy_gradient(self, data: np.ndarray, 
                                  boundaries: np.ndarray) -> np.ndarray:
        """Calculate entropy gradient at boundaries."""
        # Local entropy calculation
        window_size = 5
        pad_width = window_size // 2
        padded = np.pad(data, pad_width, mode='edge')
        
        local_entropy = np.zeros_like(data, dtype=float)
        
        for i in range(data.shape[0]):
            for j in range(data.shape[1] if data.ndim > 1 else 1):
                if data.ndim == 1:
                    window = padded[i:i+window_size]
                else:
                    window = padded[i:i+window_size, j:j+window_size]
                
                # Calculate entropy of local window
                hist, _ = np.histogram(window.flatten(), bins=10)
                hist = hist + self.config.epsilon  # Avoid log(0)
                local_entropy[i, j] = entropy(hist)
        
        # Gradient of entropy
        if data.ndim == 1:
            grad = np.gradient(local_entropy)
            return np.array([grad, 0, 0])[:data.ndim]
        else:
            grad = np.gradient(local_entropy)
            return np.array([grad[0].mean(), grad[1].mean(), 0])[:data.ndim]
    
    def _estimate_normal_vector(self, data: np.ndarray, 
                               boundaries: np.ndarray) -> np.ndarray:
        """Estimate normal vector at boundaries."""
        if data.ndim == 1:
            return np.array([1.0, 0, 0])[:data.ndim]
        
        # For 2D, use gradient direction
        grad_y, grad_x = np.gradient(data)
        
        # Average over boundary points
        boundary_points = np.where(boundaries)
        if len(boundary_points[0]) > 0:
            avg_grad_x = grad_x[boundary_points].mean()
            avg_grad_y = grad_y[boundary_points].mean()
            
            # Normalize
            norm = np.sqrt(avg_grad_x**2 + avg_grad_y**2) + self.config.epsilon
            return np.array([avg_grad_x/norm, avg_grad_y/norm, 0])[:data.ndim]
        
        return np.array([1.0, 0, 0])[:data.ndim]
    
    def _calculate_decoherence(self, data: np.ndarray, 
                              boundaries: np.ndarray) -> float:
        """Calculate decoherence rate at boundaries."""
        # Simplified: based on boundary sharpness
        if boundaries.sum() == 0:
            return 0.0
        
        # Measure local variance at boundaries
        boundary_values = data[boundaries]
        if len(boundary_values) > 0:
            return float(np.std(boundary_values))
        return 0.0
    
    def _calculate_phi(self, data: np.ndarray, boundaries: np.ndarray,
                      flux: float) -> float:
        """
        Calculate integrated information Φ.
        Simplified version based on Tononi's IIT.
        """
        if boundaries.sum() == 0:
            return 0.0
        
        # Partition coefficient (how much the boundary divides the system)
        partition_ratio = boundaries.sum() / boundaries.size
        
        # Information integration based on flux and partition
        phi = flux * partition_ratio * np.log2(data.size)
        
        # Normalize to typical range [0, 10]
        return float(np.clip(phi / 1e6, 0, 10))
    
    def detect_consciousness_potential(self, state: BoundaryState) -> Dict:
        """
        Determine if conditions for consciousness emergence are met.
        
        Returns dict with detailed analysis.
        """
        results = {
            'phi_above_critical': state.phi_integrated > self.config.phi_critical,
            'high_flux': state.information_flux > self.config.high_flux_threshold,
            'creative_decoherence': state.decoherence_rate > self.config.creative_decoherence_threshold,
            'transformation_probability': 1 - np.exp(-self.config.transformation_beta * state.information_flux),
        }
        
        # Overall assessment
        if results['phi_above_critical']:
            results['assessment'] = "CRITICAL: Consciousness emergence conditions met"
        elif results['high_flux']:
            results['assessment'] = "HIGH FLUX: Transformation imminent"
        elif results['creative_decoherence']:
            results['assessment'] = "CREATIVE: Novel states emerging"
        else:
            results['assessment'] = "SUBCRITICAL: Building toward emergence"
            
        return results
