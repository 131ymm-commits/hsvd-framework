# HSVD — Hierarchical Stochastic Variational Dynamics

**Mathematical framework for multi-scale stochastic systems.**

## Core Equation

```math
\frac{d\mathbf{x}_i}{dt} = -\gamma_i \nabla \mathcal{F}_i(\mathbf{x}_i) + \sqrt{2 \gamma_i^{-1} T_i} \, \boldsymbol{\xi}_i(t)
```

## Key Features
- Hierarchical scaling laws
- Variational free energy minimization
- Stochastic thermodynamics
- Phase transitions in control systems

## Repository Structure
- `core/` — core mathematics
- `models/` — specific level implementations
- `examples/` — simulations and demos
- `docs/` — mathematical documentation

See `docs/equations.md` for full mathematical specification.