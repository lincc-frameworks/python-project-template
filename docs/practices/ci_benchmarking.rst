Continuous Integration Benchmarking
===============================================================================


What is it? Why do it?
-------------------------------------------------------------------------------

Continuous integration benchmarking is the practice of running a suite of carefully
catered benchmarks against your code base to assess its performance over time.

There are three main ways this template enables automated benchmarking:

1. On all pushes to main. It allows to keep track of the performance of your codebase 
   over a long period of time. This workflow is responsible for creating and deploying
   a dashboard on Github Pages to visualize plots and performance regressions.
2. On pull requests to main. This evaluates the impact of the new code changes on the
   performance. 
3. On a scheduled "nightly run". The primary goal of this workflow is to make sure
   that upstream dependencies don't degrade performance significantly.


How to manage
-------------------------------------------------------------------------------

Set-up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the ``benchmarks`` directory there's a file called ``asv.conf.json`` which configures 
airspeed velocity. When first configuring the project one must manually define the following
two URLs. The remaining fields should remain unchanged.

- **project_url**: The project's homepage URL.
- **show_commit_url**: The base URL to show a commit for the project. It is used on the
  dashboard to enable performance data points on the plots to have a link to the respective commits. 
  It should be similar to `<https://github.com/{{organization}}/{{project_name}}/commit/>`_.

For more information about this configuration file, visit the `asv.conf.json reference <https://asv.readthedocs.io/en/stable/asv.conf.json.html>`_.

.. important::
   Activate GitHub Pages for your repository, otherwise the dashboard webpage won't be accessible. 
   You can either create an orphan "gh-pages" branch on your own, or wait until the Github workflow 
   creates it on its first execution. In any case, after the creation of this branch perform the following steps:

   * Navigate to the repository main page - `<https://github.com/{{organization}}/{{project_name}}>`_
   * Click "Settings"
   * Click "Pages" on the left navigation menu
   * Under "Build and deployment" set "Source" to "Deploy from a branch"
   * Under "Branch" select "gh-pages", folder should be "/root"

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

- Publishes the results to a dashboard on GH Pages. The URL should be similar to `<https://{{organization}}.github.io/{{project_name}}>`_.
  
.. note::
   - A github-actions[bot] pushes the benchmark results to the main branch. The workflows run consecutively to avoid any conflicts between jobs attempting to submit results simultaneously. A workflow is queued up until the previous workflow running on main is finished.
   - ASV uses the most recent benchmarking suites to compute results for the range of commits in question. Any direct change to these suites with the intent to affect the runtime or memory usage produces no change of behavior.

asv-pr
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This workflow is triggered on pull requests targeting the main branch.

- Compares the benchmarks of the main branch and compares it with those of main merged with the new changes.

   .. code:: bash

      >>> asv continuous upstream/main HEAD || true
      >>> asv compare upstream/main HEAD --sort ratio | tee output

- Invokes `lf-asv-formatter <https://github.com/lincc-frameworks/asv-formatter>`_ for output processing.

- Publishes a comment on the pull request with the final assessment.

Typical ASV table file (before processing):

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

.. note::
   The pipeline fails if the pull request degrades performance significantly. The threshold is set to ``110%``,
   by default.


asv-nightly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``.github/workflows/asv-nightly.yml`` file configures the scheduled benchmark test.
It uses standard cron notation to start the job at 0645 every day. This time was 
selected to be a little far away from an hour break, when most benchmarks would likely run.

This wokflow compares the performance of the main branch with the one from the previous day.

This workflow uses the repository cache to store the results for each nightly run. GitHub will remove any cache entries that have not been accessed in over 7 days so we should not worry about them compounding over time.


Use during development
-------------------------------------------------------------------------------

Running ASV locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One may want to execute ASV locally during the development process.

Running ASV locally for the current branch is as simple as executing:

.. code:: bash
    
    >> asv run

To run a comparison between two revisions, execute:

.. code:: bash
    
    >> asv compare revision1 revision2

ASV makes use of a very flexible and powerful syntax which allows to specify a range of commits and even tags. 
For more information visit the `ASV #Benchmarking <https://asv.readthedocs.io/en/stable/using.html#benchmarking>`_.

Writing benchmarks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In short, the benchmark suite should include methods that follow a predefined prefix.

`Benchmark types and attributes <https://asv.readthedocs.io/en/stable/benchmarks.html#benchmark-types-and-attributes>`_