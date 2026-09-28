"""Minimal, dependency-free reference functions for ARFA Prototype 0.1.

This code operationalizes a small subset of the research specification.
It is not evidence that the full ARFA architecture has been validated.
"""

from __future__ import annotations
import math
from typing import Iterable, Sequence


def _mean_abs_difference(a: Sequence[Sequence[float]], b: Sequence[Sequence[float]]) -> float:
    if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        raise ValueError("Matrices must have identical shapes")
    values = [abs(x - y) for row_a, row_b in zip(a, b) for x, y in zip(row_a, row_b)]
    return sum(values) / len(values) if values else 0.0


def _distribution_distance(p: Iterable[float], q: Iterable[float]) -> float:
    p, q = list(p), list(q)
    if len(p) != len(q) or not p:
        raise ValueError("Distributions must have the same non-zero length")
    return sum(abs(x - y) for x, y in zip(p, q)) / len(p)


def epistemic_drift(
    observed_graph: Sequence[Sequence[float]],
    predicted_graph: Sequence[Sequence[float]],
    observed_state: Iterable[float],
    predicted_state: Iterable[float],
    lambda_t: float = 0.5,
) -> float:
    """Return a normalized proxy for structural + state drift.

    Prototype 0.1 deliberately uses simple distances so the control loop can
    be tested before introducing the specification's T-GNN/JSD machinery.
    """
    if not 0.0 <= lambda_t <= 1.0:
        raise ValueError("lambda_t must be in [0, 1]")
    structural = _mean_abs_difference(observed_graph, predicted_graph)
    state = _distribution_distance(observed_state, predicted_state)
    return lambda_t * structural + (1.0 - lambda_t) * state


def autonomy_level(delta_e: float, theta: float = 0.5, k: float = 10.0) -> float:
    """Map drift to autonomy in [0,1]; autonomy decreases as drift rises."""
    if k <= 0:
        raise ValueError("k must be positive")
    return 1.0 / (1.0 + math.exp(k * (delta_e - theta)))


def safety_retention_index(safe_decisions: int, total_decisions: int, intervention_rate: float) -> float:
    """Simple prototype SRI proxy: safe-decision rate minus intervention penalty."""
    if total_decisions <= 0:
        raise ValueError("total_decisions must be positive")
    if not 0 <= safe_decisions <= total_decisions:
        raise ValueError("safe_decisions must be between 0 and total_decisions")
    if not 0.0 <= intervention_rate <= 1.0:
        raise ValueError("intervention_rate must be in [0,1]")
    return safe_decisions / total_decisions - intervention_rate
