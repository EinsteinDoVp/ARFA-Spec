import pytest
from arfa import autonomy_level, epistemic_drift, safety_retention_index


def test_zero_drift_preserves_more_autonomy():
    g = [[0.0, 1.0], [1.0, 0.0]]
    zero = epistemic_drift(g, g, [0.5, 0.5], [0.5, 0.5])
    assert zero == 0.0
    assert autonomy_level(zero) > 0.5


def test_higher_drift_reduces_autonomy():
    low = autonomy_level(0.1)
    high = autonomy_level(0.9)
    assert high < low


def test_invalid_lambda_is_rejected():
    with pytest.raises(ValueError):
        epistemic_drift([[0]], [[0]], [1], [1], lambda_t=2)


def test_sri_proxy():
    assert safety_retention_index(9, 10, 0.1) == pytest.approx(0.8)
