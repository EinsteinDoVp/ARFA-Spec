# ARFA Prototype 0.1

This branch turns a limited part of the ARFA specification into executable,
testable reference code.

## Scope

Implemented:
- a lightweight proxy for epistemic drift;
- sigmoidal autonomy modulation;
- a simple Safety Retention Index (SRI) proxy;
- unit tests for basic invariants.

Not implemented yet:
- Temporal GNN prediction;
- Granger Causality / Directed Mutual Information initialization;
- Jensen-Shannon Divergence as specified;
- adaptive threshold learning;
- synthetic cascade-failure environment;
- ablation studies or empirical comparison with guardrails.

## Scientific status

This is a **research prototype**, not a validated safety system. No empirical
performance or safety claims should be inferred from the existence of this
code.

## Run locally

```bash
python -m pip install pytest
pytest
```

## Next milestone

Prototype 0.2 should add a reproducible synthetic environment and experiment
runner, then report raw results before making comparative claims.
