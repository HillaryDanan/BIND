#!/usr/bin/env python3
"""
Demonstration of boundary analysis using BIND framework.

This shows BIND analyzing information dynamics at system boundaries.

Author: Hillary Danan
Date: July 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from bind.core import BoundaryMonitor, BoundarySimulator
from bind import BoundaryConfig


def main():
    """Demonstrate boundary analysis and metrics."""
    
    print("BIND - Boundary Analysis Demo")
    print("=" * 50)
    
    # Initialize
    config = BoundaryConfig()
    monitor = BoundaryMonitor(config)
    simulator = BoundarySimulator()
    
    # Generate test system
    print("\\n1. Generating test system with boundaries...")
    data = simulator.generate_two_phase_system(size=(100, 100))
    
    # Analyze it
    print("2. Analyzing boundary dynamics...")
    state = monitor.analyze_system(data)
    
    # Show results
    print(f"\\nAnalysis Results:")
    print(f"  Information flux: {state.information_flux:.2e} bits/s")
    print(f"  Integration measure (Φ): {state.phi_integrated:.2f}")
    print(f"  Transformation rate: {state.decoherence_rate:.3f}")
    
    # Check system state
    analysis = monitor.analyze_integration_potential(state)
    print(f"\\nSystem Analysis:")
    print(f"  High integration (Φ > {config.phi_critical}): {analysis[\\"high_integration\\"]}")
    print(f"  Transformation probability: {analysis[\\"transformation_probability\\"]:.1%}")
    print(f"  Assessment: {analysis[\\"assessment\\"]}")
    
    # Visualize if matplotlib available
    try:
        plt.figure(figsize=(12, 4))
        
        plt.subplot(131)
        plt.imshow(data, cmap="viridis")
        plt.title("System State")
        plt.colorbar()
        
        plt.subplot(132)
        boundaries = monitor._detect_boundaries(data)
        plt.imshow(boundaries, cmap="Reds")
        plt.title("Detected Boundaries")
        plt.colorbar()
        
        plt.subplot(133)
        # Show information landscape
        info_landscape = boundaries * state.information_flux
        plt.imshow(info_landscape, cmap="hot")
        plt.title("Information Flux at Boundaries")
        plt.colorbar()
        
        plt.tight_layout()
        plt.savefig("boundary_analysis.png", dpi=150)
        print("\\n✅ Visualization saved to boundary_analysis.png")
        
    except ImportError:
        print("\\n(Install matplotlib to see visualizations)")
    
    print("\\nBoundary analysis complete!")


if __name__ == "__main__":
    main()
