Continuous Integration Pre-Commit
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Continuous integration Pre-Commit is the practice of running a set of hooks 
that enforce code styling consistency whenever new changes are proposed.

`pre-commit <https://pre-commit.com>`_ hooks should be setup locally, so one can
apply the required fixes before committing. That is an assumption not all
developers comply with, and therefore, it's useful to have a GitHub workflow 
to help enforcing code style and keeping it consistent during development.

Using `pre-commit.ci lite <https://pre-commit.ci/lite>`_, we incorporate a bot
into our project that performs as many automatic fixes as possible and reports
any code style issues that it could not resolve but should be fixed.

For each pull request, our ``pre-commit.ci`` workflow will:

* Clear outputs from Jupyter notebooks
* Analyze the src code style and report code that doesn't adhere, using 
  the options you selected for your tooling set:

  * "ruff": checks for linting rules, sorts imports, auto-formats code
  * "pylint": checks for compliance with pylint rules
  * "black": auto-formats code (including notebooks)
  * "isort": Sort imports using ``isort``

* Analyze type hints (if mypy type checking is enabled)

.. note::
  * Only a small subset of hooks declared in the ``.pre-commit-config.yaml`` file
    is relevant for the CI pipeline. Some checks are simply not relevant, while 
    others are performed in other github workflows instead.
    
    For more information on the list of available
    hooks visit :doc:`Pre-Commit <../practices/precommit>`.

How to activate
-------------------------------------------------------------------------------

The template will automatically generate the ``pre-commit-ci.yml`` workflow file. 
To finish the configuration of this feature and activate the automatic fixes on
pull requests, you need to 
`install <https://github.com/apps/pre-commit-ci-lite/installations/new>`_
the pre-commit application for your relevant GitHub repository.
