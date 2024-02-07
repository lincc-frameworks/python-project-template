Pre-Commit
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

``pre-commit`` is installed when running ``pip install -e '.[dev]'``. It's an industry 
standard tool that executes a set of tests prior to completing a ``git commit`` action. 
Using pre-commit enables a quick check of your code before it's committed and checked 
by GitHub workflows. This cuts down on code feedback time, and allows for faster 
development. Additional documentation can be found 
`here <https://pre-commit.com/index.html>`_.

To configure pre-commit for your project, run the following command to register 
pre-commit hooks with ``.git/hooks/pre-commit``.

.. code-block:: bash
    
    pre-commit install

List of ``pre-commit`` hooks
-----------------------------

The following is a list of pre-commit hooks that will be run each time you 
commit code locally. The configuration file that defines these hooks is called 
``.pre-commit-config.yaml``, you should feel free to update or remove any 
of these that are not useful for your project. 

.. list-table:: Pre-commit hooks
   :widths: auto
   :header-rows: 1

   * - **Hook name**
     - **Purpose**
   * - Check template version
     - Compare the current local LINCC python project template version against latest 
       remote version and alert user if an update is recommended.
   * - Clear output from Jupyter notebooks
     - Clear output from Jupyter notebooks to avoid committing large binary files.
   * - Prevent main branch commits
     - Prevents accidental commits directly to the ``main`` (or ``master``) branches.
   * - Check for large files
     - Prevents committing very large files. The default file size threshold is 500kb 
       and is configurable.
   * - Validate pyproject.toml
     - Verify pyproject.toml adheres to the required schema to avoid changes that 
       would break the build.
   * - Run isort
     - Runs isort to sort and organize your python package imports on .py and .pyi files. 
       One can add more file extensions by editing this hook on ``.pre-commit-config.yaml``
       directly. *(Optionally installed when project is created.)*
   * - pylint (python files in src/)
     - Runs pylint to enforce a particular code style on python files in the src/ directory. 
       *(Optionally installed when project is created.)*
   * - pylint (python files in tests/ and benchmarks/)
     - Same as above, but for the tests/ and benchmarks/ directory. 
       *(Optionally installed when project is created.)*
   * - Format code using black
     - Runs black to enforce a particular code style on .py, .pyi and .ipynb files. 
       One can add more file extensions by editing this hook on ``.pre-commit-config.yaml`` 
       directly. *(Optionally installed when project is created.)*
   * - Lint code using ruff
     - Runs ruff to enforce a particular code style on .py, .pyi and .ipynb files. 
       One can add more file extensions by editing this hook on ``.pre-commit-config.yaml`` 
       directly. *(Optionally installed when project is created.)*
   * - Format code using ruff
     - Runs ruff to enforce a particular code style on .py, .pyi and .ipynb files. 
       One can add more file extensions by editing this hook on ``.pre-commit-config.yaml`` 
       directly. *(Optionally installed when project is created.)*
   * - mypy
     - Runs static type checking on python files in the src/ and tests/ directories. 
       *(Optionally installed when project is created.)*
   * - Run unit tests
     - Run all unit tests that are discovered by pytest.
   * - Build documentation with Sphinx
     - Ensures that automatically generated documentation and, optionally, jupyter notebooks 
       can be built successfully.

Many other pre-commit hooks exist, a partial list can be found in the pre-commit 
`documentation <https://pre-commit.com/hooks.html>`_.
