# ARFA Research Roadmap

## Current: Prototype 0.2
- executable drift/autonomy control-loop baseline
- deterministic synthetic cascade environment
- reproducible experiment runner
- minimal fixed-autonomy ablation
- automated tests and GitHub Actions CI

## Prototype 0.3
Goal: improve scientific reproducibility without overstating validation.

Planned:
- Jensen-Shannon Divergence implementation for state distributions
- Frobenius structural distance aligned more closely with the specification
- parameter sweeps for theta, k, and lambda
- machine-readable experiment outputs
- expanded ablations
- documented limitations and threat-to-validity notes

## Prototype 0.4
- temporal predictor baseline before any T-GNN claim
- multi-seed stochastic synthetic environments
- comparative guardrail baselines
- reproducibility package and versioned release

## Research boundary
ARFA remains a research-stage architecture. Synthetic experiments test internal
properties of the prototype; they do not establish real-world AI safety,
governance effectiveness, or deployment readiness.
