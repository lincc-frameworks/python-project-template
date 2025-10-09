import pytest

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12", "3.13"]


def pytest_addoption(parser):
    parser.addoption("--python_version", action="store", default="3.12", choices=PYTHON_VERSIONS)


@pytest.fixture(scope="session", name="python_version")
def python_version(request):
    yield request.config.getoption("--python_version")


@pytest.fixture
def default_answers(python_version):
    return {"python_versions": [python_version]}
