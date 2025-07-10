#!/usr/bin/env python3
"""
Basic usage example for BIND framework.

Author: Hillary Danan
Date: July 2025
"""

import numpy as np
from bind import BoundaryConfig, BoundaryState


def main():
    """Run basic BIND demonstration."""
    
    print("BIND - Boundary Information Neural Dynamics")
    print("=" * 50)
    
    # Create configuration
    config = BoundaryConfig()
    print(f"\\nConfiguration loaded with Φ critical = {config.phi_critical}")
    
    # Create a sample boundary state
    state = BoundaryState(
        entropy_gradient=np.array([0.5, 0.3, 0.2]),
        normal_vector=np.array([1.0, 0.0, 0.0]),
        information_flux=1.5e7,
        decoherence_rate=0.8,
        phi_integrated=3.2,
        timestamp=0.0
    )
    
    print(f"\\nBoundary State Analysis:")
    print(f"  Information flux: {state.information_flux:.2e} bits/s")
    print(f"  Integrated information (Φ): {state.phi_integrated:.2f}")
    print(f"  Below critical threshold: {state.phi_integrated < config.phi_critical}")
    
    print("\\n✅ Basic example complete!")


if __name__ == "__main__":
    main()
