# ARFA Prototype 0.2

This repository contains an executable research baseline derived from a limited
subset of the ARFA specification.

## Implemented
- lightweight proxy for epistemic drift;
- sigmoidal autonomy modulation;
- simple Safety Retention Index proxy;
- deterministic synthetic cascade environment;
- reproducible baseline experiment;
- minimal fixed-autonomy ablation;
- unit tests and GitHub Actions CI.

## Not implemented yet
- Temporal GNN prediction;
- Granger Causality / Directed Mutual Information initialization;
- Jensen-Shannon Divergence as specified;
- adaptive threshold learning;
- stochastic multi-seed experiments;
- external or real-world validation.

## Scientific status
This is a **research prototype**, not a validated safety system. Results from
the included experiments describe behavior in the repository's synthetic
environment only.

## Run locally

```bash
python -m pip install pytest
pytest
PYTHONPATH=src python experiments/run_baseline.py
PYTHONPATH=src python experiments/run_ablation.py
```

## Next milestone
Prototype 0.3 will move the implemented metrics closer to the written
specification, add parameter sweeps and machine-readable outputs, and expand
the ablation methodology. See `ROADMAP.md`.
