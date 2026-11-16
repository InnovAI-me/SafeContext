"""
Utility and helper functions for research experiments.
"""
import random

def set_seed(seed: int = 42):
    """Set random seed for reproducibility."""
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except ImportError:
        pass
