Continuous Integration Benchmarking
===============================================================================


What is it? Why do it?
-------------------------------------------------------------------------------

Continuous integration benchmarking is the practice of running a suite of carefully
catered benchmarks against your codebase to assess its performance over time.

There are three main ways this template enables automated benchmarking:

1. On all pushes to main. It allows to keep track of the performance of your benchmarks 
   over a long period of time. This workflow is responsible for creating and deploying
   a dashboard to Github Pages to visualize plots on performance and its regressions.
2. On pull requests to main. This evaluates the impact of the new code changes on the
   performance.
3. On a scheduled "nightly run". Its primary goal is to make sure that upstream dependencies
   don't introduce breaking changes that degrade performance significantly.

The benchmarking tool responsible to compute the runtime and memory benchmarks is 
`airspeed velocity (ASV) <https://asv.readthedocs.io/en/stable/>`_.


How to manage
-------------------------------------------------------------------------------

Set-up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the ``benchmarks`` directory there's a file called ``asv.conf.json`` which configures 
airspeed velocity. You may need to perform minor changes to this file. For example, if you need
to install dependencies declared on a ``requirements.txt`` file, you may want to set the
``install_command`` as follows:

    .. code:: bash

        python -m pip install -r requirements.txt {wheel_file}

For more information about this configuration file, visit the
`asv.conf.json reference <https://asv.readthedocs.io/en/stable/asv.conf.json.html>`_.

.. important::
   Activate GitHub Pages for your repository, otherwise the dashboard webpage won't be accessible. 
   You can either create an orphan "gh-pages" branch on your own, or wait until the Github workflow 
   creates it on its first execution. In any case, after the creation of this branch perform the following steps:

   * Navigate to the repository main page - `<https://github.com/{{organization}}/{{project_name}}>`_
   * Click "Settings"
   * Click "Pages" on the left navigation menu
   * Under "Build and deployment" set "Source" to "Deploy from a branch"
   * Under "Branch" select "gh-pages", folder should be "/ (root)"

   .. image:: ../static/practices/ci_benchmarking/config.jpg
      :alt: Configuration page screenshot

A dashboard deployment is automatically triggered when the "gh-pages" branch is updated.
Within a couple of minutes, the changes should be reflected on the dashboard.

asv-main
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflow is triggered on pushes to the main branch.

- Computes the benchmarks for for all the commits on main for which there are no benchmark results. As such, 
  the first run will take a while because it will process every commit on the repository to the present day, 
  but subsequent runs will be faster.
   
   .. code:: bash

      >> asv run ALL --skip-existing

- Publishes the results to a dashboard on GitHub Pages (`<https://{{organization}}.github.io/{{project_name}}>`_).
  
.. note::
   * A Github actions bot pushes the benchmark results to a separate branch (``benchmarks``), creating
     it if it does not yet exist. The workflows run consecutively to avoid any conflicts between jobs attempting to submit
     results simultaneously. A workflow is queued up until the previous workflow running on main is finished.
   * ASV uses the most recent benchmarking suites to compute results for the range of commits in question. 
     Any direct change to these suites with the intent to affect the runtime or memory usage produces no 
     change of behavior. Only changes to your project source modules do.

asv-pr
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflow is triggered on pull requests targeting the main branch.

* Compares the benchmarks of the main branch with those of main merged with the new changes.
* Uses `asv-formatter <https://github.com/lincc-frameworks/asv-formatter>`_ to process the output.
* Publishes a comment on the pull request with the final assessment.

Below is an example of the results generated.

+-------------+------------+----------+------------------------------------+
| Before      | After      | Ratio    | Method                             |
+=============+============+==========+====================================+
| [fcd6c976]  | [bc939276] |          |                                    |
+-------------+------------+----------+------------------------------------+
| 2.1k        | 2.1k       | 1.00     | benchmarks.MemSuite.mem_list       |
+-------------+------------+----------+------------------------------------+
| failed      | 304±2ms    | n/a      | benchmarks.TimeSuite.time_iterkeys |
+-------------+------------+----------+------------------------------------+
| 2.43±0.05μs | 205±0.7ms  | 84400.48 | benchmarks.TimeSuite.time_keys     |
+-------------+------------+----------+------------------------------------+
| 9.67±0.03μs | 505±1ms    | 52177.14 | benchmarks.TimeSuite.time_range    |
+-------------+------------+----------+------------------------------------+
| failed      | 1.01±0s    | n/a      | benchmarks.TimeSuite.time_xrange   |
+-------------+------------+----------+------------------------------------+

asv-nightly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``.github/workflows/asv-nightly.yml`` file configures a scheduled run of benchmarks.
It uses standard cron notation to start the job at 0645 every day and it compares the
most recent code on main with that of the previous day.


Use during development
-------------------------------------------------------------------------------

Running ASV locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may want to run ``asv`` locally, during development. Verify that it has been 
properly installed on your environment by executing the following command. There 
are several questions you'll be asked the first time, and you may need to instal 
a new python venv. When your local environment is properly configured, it runs 
the benchmarking suite for your most recent commit

.. code:: bash

    >> cd benchmarks
    >> asv run

You will need to commit changes locally for the new code to be picked up by ASV.
Having benchmarks for several revisions, you can find them and compare them with ease.

.. code:: bash
    
    >> asv show
      Commits with results:

      Machine    : XPS8104-L
      Environment: virtualenv-py3.10-Cython-build-packaging

          d02787f1
          5dd46d87
    >> asv compare d02787f1 5dd46d87

The commands use a very flexible and powerful syntax which allows to specify a range 
of commits and even tags. For more information visit ASV's
`Benchmarking section <https://asv.readthedocs.io/en/stable/using.html#benchmarking>`_.

If your benchmark fails, you can re-run and find more information with the following:

.. code:: bash

    >> asv run --show-stderr

Since you've had to create many commits while working on benchmarks, be sure
to squash before merging to main!

Writing benchmarks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Performance is measured for suites defined under ``benchmarks``.

The functions benchmarked must follow a predefined prefix.

* **time_**: measures runtime.
* **mem_**: measures memory consumption for a specific Python object.
* **peakmem_**: measures maximum size of the process in memory.

More information about available methods
`here <https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-types-and-attributes>`_.


Demo
-------------------------------------------------------------------------------

.. note::
   Project ``benchmarking-asv`` showcases the integration with these workflows.

   * `Repository <https://github.com/lincc-frameworks/benchmarking-asv>`_
   * `Dashboard <https://lincc-frameworks.github.io/benchmarking-asv>`_
