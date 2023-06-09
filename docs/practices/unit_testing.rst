Unit testing
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Unit testing is a method for testing very specific aspects of a code base. The
various different types of tests cover a wide range of use cases, for a quick intro
take a look at RealPython's article about unit testing: https://realpython.com/python-testing/#unit-tests-vs-integration-tests

How to manage
-------------------------------------------------------------------------------

Our template makes use of `pytest <https://docs.pytest.org/en/latest/contents.html>`_
as the unit testing framework. You have the option to change that at any time,
but you'll need to make modifications in a few files:

* ``pyproject.toml``
* ``.github/workflows/testing-and-coverage.yml``
* ``.github/workflows/smoke-test.yml``
* ``.pre-commit-config.yaml``

Additionally, we advise that unit tests be placed in the ``./tests`` directory.
This is not a requirement, but the Continuous Integration and pre-commit checks
will only look in that directory for tests. If you decide to keep your tests
elsewhere, you should update the ``[tool.pytest.ini_options]`` section in
``pyproject.toml`` with the new location so that CI and pre-commit will work as
expected.

It's also worth noting that if you want to write exploratory tests as you develop
your code, but you *do not* want those tests to be included in automated test runs,
feel free to place those tests in a directory outside of the ``./tests`` directory.

Note that ``pytest`` will recursively search subdirectories inside of ``./tests``
while searching for tests to run.
