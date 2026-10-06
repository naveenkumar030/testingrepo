def test_intentional_ci_failure():
    """Temporary failing check used to exercise the GitHub Actions failure path."""
    assert False, "Intentional CI failure for pipeline testing"


def test_deliberate_github_ci_failure():
    """Explicit failing assertion created to trigger CI failure on GitHub Actions."""
    assert False, "Deliberate failure to trigger GitHub Actions CI pipeline"

