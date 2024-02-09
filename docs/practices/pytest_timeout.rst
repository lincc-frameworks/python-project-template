pytest-timeout
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

`pytest-timeout <https://pypi.org/project/pytest-timeout/>`_ is an additional
pytest package that enforces the run length of your unit tests by causing
long-running tests to fail.

This is not a replacement for full-fledged benchmarking, but can be another
good signal that you're introducing a performance regression if tests that
were previously passing are now timing out.

See also:

* :doc:`ci_testing`
* :doc:`ci_benchmarking`

.. note::
    Because this requires additional configuration, we do not enable it by
    default, but are providing some instructions on enabling it 

How to enable in your project
-------------------------------------------------------------------------------

Add the dependency in your ``pyproject.toml`` file, under the ``dev`` 
section, e.g.:

.. code-block::

    [project.optional-dependencies]
    dev = [
        ...
        "pytest",
        "pytest-timeout", # Used to test for code efficiency
        ...
    ]

Then add a default timeout (in seconds) lower down in the file:

.. code-block::

    [tool.pytest.ini_options]
    timeout = 1
    testpaths = [
        "tests",
    ]

With this configuration, any test taking longer than 1 second will time out
and fail.

Note that your local development environment is likely faster than the 
machines you will be allocated for github actions, often by a factor of 2-5x.
If your tests take ~1 second locally, you should be setting your timeout to some
larger value so the failures are less common.

How to customize
-------------------------------------------------------------------------------

If you have some tests that you know will take longer than the default (e.g.
end-to-end or integration tests), you can set a longer timeout for those tests
with the pytest annotation:

.. code-block::

    @pytest.mark.timeout(5)
    def test_long_running_operation():
        ...

Setting a timeout to 0 seconds disables the timeout entirely.

Other fun things you can do
-------------------------------------------------------------------------------

Even if you're not using this package, you can find slow-running tests in your
suite with the ``--durations`` flag.

.. code-block:: console

    pytest --durations=10

This will run your test suite as normal, outputting a list of the 10 slowest 
calls after the execution. Note that this is not the 10 slowest **tests**: 
the setup and teardown will be counted separately so put slow, shared fixture
setup in a shared fixture!