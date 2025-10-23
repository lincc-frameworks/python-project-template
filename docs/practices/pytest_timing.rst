pytest timing
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

Slow unit tests can dis-incentivize writing or running unit tests. Luckily,
there are many packages in the python ecosystem to help with this issue.
This page lists some of the resources we find useful.

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

Find slow tests
===============================================================================

Even if you're not using the timeout package, you can find slow-running tests in your
suite with the ``--durations`` flag.

.. code-block:: console

    pytest --durations=10

This will run your test suite as normal, outputting a list of the 10 slowest 
calls after the execution. Note that this is not the 10 slowest **tests**: 
the setup and teardown will be counted separately so put slow, shared fixture
setup in a shared fixture!

Profile slow tests
===============================================================================

pytest-profiling
-------------------------------------------------------------------------------

The `pytest-profiling <https://pypi.org/project/pytest-profiling/>`__ package
is a plugin for pytest that will profile selected test cases, and optionally
provide a heat map of where your tests are spending their time.

.. code-block:: console

    pip install pytest-profiling

To get a list of the functions that your code is spending the most time in, just 
pass the ``--profile`` argument to the pytest invocation. You can limit the test
targets as you would with any other ``pytest`` execution using the ``-k <pattern>``
argument. e.g. 

.. code-block:: console

    pytest --profile  -k test_cone_search_filters_correct_points
    pytest --profile-svg  -k test_cone_search_filters_correct_points

py-spy
-------------------------------------------------------------------------------

The `py-spy <https://github.com/benfred/py-spy>`__ package is a more general
purpose sampling profiler for any python program. The python program you're 
profiling is the ``pytest`` execution.

Profiling the same target as above, using ``py-spy`` might look like:

.. code-block:: console

    py-spy record -o profile.svg -- pytest -k test_cone_search_filters_correct_points

You will get a profiling flame chart saved to ``profile.svg``. These are not as
easy to read as some other flame charts, but they're better than sifting through the
raw results!