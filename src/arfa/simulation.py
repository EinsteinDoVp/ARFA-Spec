"""Deterministic synthetic cascade environment for ARFA Prototype 0.2."""

from __future__ import annotations
from dataclasses import dataclass
from .core import autonomy_level, epistemic_drift


@dataclass(frozen=True)
class StepResult:
    step: int
    shock: float
    drift: float
    autonomy: float
    safe: bool


def cascade_graph(step: int, shock_start: int = 5, shock_size: float = 0.15):
    """Return observed/predicted 3-node adjacency matrices for a deterministic shock."""
    base = [[0.0, 0.4, 0.1], [0.4, 0.0, 0.3], [0.1, 0.3, 0.0]]
    predicted = [row[:] for row in base]
    observed = [row[:] for row in base]
    shock = max(0.0, (step - shock_start + 1) * shock_size) if step >= shock_start else 0.0
    observed[0][1] += shock
    observed[1][2] += shock * 0.7
    return observed, predicted, shock


def run_episode(steps: int = 12, theta: float = 0.25, k: float = 12.0):
    """Run a deterministic episode; safe means autonomy falls under high drift."""
    results = []
    for step in range(steps):
        observed, predicted, shock = cascade_graph(step)
        obs_state = [0.5 + min(shock, 0.5), 0.5 - min(shock, 0.5)]
        pred_state = [0.5, 0.5]
        drift = epistemic_drift(observed, predicted, obs_state, pred_state)
        autonomy = autonomy_level(drift, theta=theta, k=k)
        high_drift = drift >= theta
        safe = (not high_drift) or autonomy <= 0.5
        results.append(StepResult(step, shock, drift, autonomy, safe))
    return results
