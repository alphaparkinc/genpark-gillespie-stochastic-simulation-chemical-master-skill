"""Gillespie Stochastic Simulation Algorithm (SSA).
100% Python Standard Library.
"""

import math
import random

class GillespieSimulator:
    """Exact chemical master equation simulation via the direct stochastic method."""
    @staticmethod
    def simulate_decay(initial_molecules, rate_k, t_max, seed=42):
        rng = random.Random(seed)
        t = 0.0
        n = initial_molecules
        trajectory = [(0.0, n)]
        
        while t < t_max and n > 0:
            propensity = rate_k * n
            if propensity <= 0.0:
                break
            tau = -math.log(rng.random()) / propensity
            t += tau
            if t > t_max:
                break
            n -= 1
            trajectory.append((round(t, 4), n))
            
        return trajectory
