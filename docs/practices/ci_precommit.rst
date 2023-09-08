Continuous Integration Pre-Commit
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Continuous integration Pre-Commit is the practice of running a set of hooks 
that enforce code styling consistency whenever new changes are proposed.

`pre-commit <https://pre-commit.com>`_ hooks should be setup locally, so one can
apply the required fixes before committing. That is an assumption not all
developers comply with, and therefore, it's useful to have a GitHub workflow 
to help enforcing code style and keep it consistent during development.

Using `pre-commit.ci lite <https://pre-commit.ci/lite>`_, we incorporate a bot
into our project that performs as many automatic fixes as possible and reports
any linting issues that it could not resolve but should be fixed.

For each pull request, our ``pre-commit.ci`` workflow will:

* Clear outputs from Jupyter notebooks
* Format code using ``black`` (python and notebook files)
* Sort imports using ``isort`` (python and notebook files)
* Check compliance with ``pylint`` rules (python files under ``src`` and ``test``)

.. note::
   * Only a small subset of hooks declared in the ``.pre-commit-config.yaml`` file
     are relevant for the CI pipeline. For more information on the list of available
     hooks visit :doc:`Pre-Commit <../practices/precommit>`.

How to activate
-------------------------------------------------------------------------------

The template will automatically generate the ``pre-commit-ci.yml`` workflow file
if you have chosen a linter when setting up the project with ``copier``.

To finish the configuration of this feature and activate the automatic fixes on the
pull requests, you need to install the pre-commit application for your relevant 
GitHub repository (`link <https://github.com/apps/pre-commit-ci-lite/installations/new>`_).
