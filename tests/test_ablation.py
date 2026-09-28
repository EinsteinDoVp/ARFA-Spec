from arfa.simulation import run_episode


def test_episode_contains_both_low_and_high_drift_regimes():
    rows = run_episode()
    assert any(r.drift < 0.25 for r in rows)
    assert any(r.drift >= 0.25 for r in rows)


def test_arfa_synthetic_safety_invariant():
    rows = run_episode()
    assert all(r.safe for r in rows)
