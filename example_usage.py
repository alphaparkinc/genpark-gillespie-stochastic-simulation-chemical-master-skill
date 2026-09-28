"""Example demonstrating Gillespie decay simulation."""
from client import GillespieSimulator

def main():
    traj = GillespieSimulator.simulate_decay(initial_molecules=20, rate_k=0.5, t_max=5.0)
    print("Stochastic Jump Trajectory:")
    for t, n in traj[:6]:
        print(f"  t={t:.4f}s: {n} molecules remaining")

if __name__ == "__main__":
    main()
