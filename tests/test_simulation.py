from arfa.simulation import cascade_graph, run_episode


def test_no_shock_before_threshold_step():
    _, _, shock = cascade_graph(4)
    assert shock == 0.0


def test_shock_increases_after_start():
    _, _, a = cascade_graph(5)
    _, _, b = cascade_graph(6)
    assert b > a > 0


def test_episode_is_deterministic():
    assert run_episode() == run_episode()


def test_controller_restrains_when_drift_crosses_threshold():
    rows = run_episode()
    high = [r for r in rows if r.drift >= 0.25]
    assert high
    assert all(r.autonomy <= 0.5 and r.safe for r in high)
