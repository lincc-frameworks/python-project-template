"""Common testing fixtures"""

import pytest

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12", "3.13", "3.14"]


def pytest_addoption(parser):
    """Command line option for python version(s) to use in the hydrated project."""
    parser.addoption("--python_version", action="store", default="3.12", choices=PYTHON_VERSIONS)


@pytest.fixture(scope="session", name="python_version")
def python_version(request):
    """Python version(s) to use in the hydrated python project."""
    yield request.config.getoption("--python_version")


# pylint: disable=redefined-outer-name
@pytest.fixture
def default_answers(python_version):
    """Python version(s) to use in the hydrated python project."""
    return {"python_versions": [python_version]}
