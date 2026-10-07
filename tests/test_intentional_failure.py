def test_deliberate_ci_failure():
    """Intentional failing test to trigger CI pipeline failure."""
    assert False, "Deliberate test failure for CI pipeline verification"
