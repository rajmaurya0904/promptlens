"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import promptlens


def test_version_is_set() -> None:
    assert promptlens.__version__
