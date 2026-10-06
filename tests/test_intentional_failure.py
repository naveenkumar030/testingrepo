def test_intentional_ci_failure():
    """Temporary failing check used to exercise the GitHub Actions failure path."""
    assert False, "Intentional CI failure for pipeline testing"
