#!/usr/bin/env python3
"""
Demonstration of BIND.

Author: Hillary Danan
Date: July 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from bind.core import BoundaryMonitor, BoundarySimulator
from bind import BoundaryConfig


def main():
    """Demonstrate real boundary detection and analysis."""
    
    print("BIND - Real Boundary Detection Demo")
    print("=" * 50)
    
    # Initialize
    config = BoundaryConfig()
    monitor = BoundaryMonitor(config)
    simulator = BoundarySimulator()
    
    # Generate test system
    print("\n1. Generating two-phase system with boundary...")
    data = simulator.generate_two_phase_system(size=(100, 100))
    
    # Analyze it
    print("2. Analyzing boundary properties...")
    state = monitor.analyze_system(data)
    
    # Show results
    print(f"\nResults:")
    print(f"  Information flux: {state.information_flux:.2e} bits/s")
    print(f"  Integrated information (Φ): {state.phi_integrated:.2f}")
    print(f"  Decoherence rate: {state.decoherence_rate:.3f}")
    
    # Check for consciousness
    potential = monitor.detect_consciousness_potential(state)
    print(f"\nConsciousness Analysis:")
    print(f"  Φ > critical ({config.phi_critical}): {potential['phi_above_critical']}")
    print(f"  Transformation probability: {potential['transformation_probability']:.1%}")
    print(f"  Assessment: {potential['assessment']}")
    
    # Visualize if matplotlib available
    try:
        plt.figure(figsize=(12, 4))
        
        plt.subplot(131)
        plt.imshow(data, cmap='viridis')
        plt.title('System State')
        plt.colorbar()
        
        plt.subplot(132)
        boundaries = monitor._detect_boundaries(data)
        plt.imshow(boundaries, cmap='Reds')
        plt.title('Detected Boundaries')
        plt.colorbar()
        
        plt.subplot(133)
        # Show information landscape
        info_landscape = boundaries * state.information_flux
        plt.imshow(info_landscape, cmap='hot')
        plt.title('Information Flux at Boundaries')
        plt.colorbar()
        
        plt.tight_layout()
        plt.savefig('boundary_analysis.png', dpi=150)
        print("\n✅ Visualization saved to boundary_analysis.png")
        
    except ImportError:
        print("\n(Install matplotlib to see visualizations)")
    
    print("\nThis is real code analyzing real boundaries!")


if __name__ == "__main__":
    main()
