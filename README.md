# Gillespie Stochastic Simulation Algorithm (SSA) Skill

Exact stochastic event simulation for chemical reaction networks and master equations.

```mermaid
flowchart TD
    State["Molecule Counts Vector X(t)"] --> Propensities["Calculate Reaction Propensities a_j(X)"]
    Propensities --> SumProp["Total Propensity a_0 = ∑ a_j"]
    SumProp --> WaitTime["Draw Exponential Waiting Time τ ~ Exp(a_0)"]
    WaitTime --> SelectReaction["Sample Discrete Reaction j with Probability a_j / a_0"]
    SelectReaction --> UpdateState["Update State X(t + τ) and Time t = t + τ"]
    UpdateState --> Loop{"t < t_max?"}
    Loop -- Yes --> State
    Loop -- No --> Done["Exact Stochastic Realization"]
```

## Features
- **100% Python Standard Library**: Inversion sampling of exponential waiting intervals.
- **Exact Master Equation Realization**: Captures genuine discrete stochastic noise in low-copy molecular systems.
