Starting a new project
===============================================================================


Create a new project from the template
-------------------------------------------------------------------------------

Choose where you would like to create your new project, and call copier with the template.

.. code-block:: bash

    >> copier gh:lincc-frameworks/python-project-template <path/to/destination>

Copier will ask you questions for how to set up the project. These questions will be used to fill in aspects of the project's configuration, including both metadata and parameters. Below we provide some high-level overview of the questions:

.. list-table::
   :header-rows: 1

   * - **Question**
     - **Notes**
   * - *Would you like to use simple (default tooling) or customized installation?*
     - If a simple install is used, the template automatically selects the recommended tooling options (linter, isort, and create example module). 
   * - *What is the name of your project?*
     - The name of your project.
   * - *What is your python module name?*
     - The name of your (first) module. This controls where your source code will live (``src/{{module_name}}``).
   * - *Your first and last name?* 
     -  The name of code's author. This will be used in the project and documentation metadata. This name will also be included as part of the copyright license.
   * - *Your preferred email address?*
     - The contact email for the code's author. This will be used in the project and documentation metadata.
   * - *What license would you like to use?*
     - The license type you want to use for this project. Options are MIT and BSD. For more information on these options see `Github's license page <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository>`_.
   * - *What tooling would you like to use to enforce code style?*
     - A linter is a tool to automatically format for consistency (see :doc:`Linting <../practices/linting>`). We provide options for `black <https://black.readthedocs.io/en/stable/>`_, `pylint <https://pypi.org/project/pylint/>`_, or no linter. Choosing a linter will include it as a project dependency and include it in the :doc:`pre-commit <../practices/precommit>` hooks. Defaults to ``pylint`` during simple installation. 
   * - *Do you want to use isort to maintain a specific ordering for module imports?*
     - `isort <https://pycqa.github.io/isort/>`_ is a tool for ordering imports in a standard order. Enabling the option will include ``isort`` as part of github's :doc:`pre-commit <../practices/precommit>`. Defaults to ``True`` during simple installation.
   * - *Would you like to include mypy to perform static type checking for type hints?*
     - `mypy <https://www.mypy-lang.org>`_ performs static type checking on python code that uses `type hints <https://docs.python.org/3/library/typing.html>`_. This type checking makes sure that the correct data types are being used where type hints are defined. If basic or strict type checking is selected, a pre-commit hook and GitHub actions workflow that perform the type checking are added. Basic type checking performs type checks but ignores code or imports for which type hints are not written. Strict type checking enforces type hints are used by giving errors where no type hints are found.
   * - *Do you want to create some example module code?*
     - If this option is selected the template will create a model in ``src/{{module_name}}`` and create a corresponding example test file. Defaults to ``True`` during simple installation.
   * - *Do you want to include rendered notebooks in your documentation?*
     - The requirements to host rendered notebooks on your Read the Docs (or just build them locally) will be included in your project. A sample notebook will be generated and added to your docs as an example.
   * - *Do you want to add a .gitattributes with entries for git-lfs?*
     - Support for large files for use in git. This option is primarily informational and no answer locks you in to using (or not using) git-lfs. Importantly, selecting this option does not install git-lfs for your project (see :doc:`Git_Large_File_Support <../practices/git-lfs>`).


While these choices will provide the initial structure for your project, most can be changed later. See Copier's `documentation for changing answers to the question <https://copier.readthedocs.io/en/stable/updating/>`_.

After providing answers to the prompts, Copier will hydrate a project template and save it in the specified location. Additionally Copier will run ``git init`` in the new project directory to initialize it as a local repository.

Create a new environment
---------------------------

If you are using `virtual environments <https://packaging.python.org/en/latest/glossary/#term-Virtual-Environment>`_ 
create a new environment with your choice of environment tools (virtualenv, conda, etc.) and activate it. 
This step is optional, but we recommend using virtual environments to better manage different project's dependencies. 
See Python's `description of virtual environments <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>`_ for more details.

.. tip::
  Projects using Python notebooks will need to have ``pandoc`` installed to convert notebooks to html locally. 
  Pandoc is `available on conda-forge <https://github.com/conda-forge/pandoc-feedstock>`_, so conda can be a convenient way to keep these dependencies grouped together.

Install your new package
----------------------------------------------------

Go to the new package directory and install the newly created python package.
Use ``pip`` to install both the standard set of dependencies as well as the ``[dev]`` dependencies.

.. note::
  Depending on your system you may not need the single quotes around ``'.[dev]'``.

.. code-block:: bash

    >> cd {{project_name}}
    >> pip install -e .
    ...
    Lots of output
    ...

    >> pip install '.[dev]'
    ...
    Lots more output
    ...

Great, but don't stop here
-------------------------------------------------------------------------------

At this point, your new project is hydrated and ready for you to start coding. But there's a lot more that this template has to offer. Keep reading to find out more about built in pre-commit hooks, GitHub CI, automatic documentation, and more.

Commit your new project locally
-------------------------------------------------------------------------------

Commit the project to your local version control like so to see the pre-commit checks run.

.. code-block:: bash

    >> git checkout -b initial_branch
    Switched to a new branch 'initial_branch'
    >> git add .
    >> git commit -m 'Initial commit'

Push your work to GitHub
-------------------------------------------------------------------------------

Create a new repository in GitHub: (`GitHub How-to <https://docs.github.com/en/get-started/quickstart/create-a-repo>`_)

.. code-block:: bash

    >> git remote add origin https://github.com/<the_remote_project>/<the_remote_repository>
    >> git push origin <local_branch_name>

Notice that when you create a PR in GitHub, a set of tests for Continuous Integration starts up to verify that the project can build successfully and that all the unit tests pass. Neato!

Install pre-commit
----------------------------

Now that your project has been pushed to a GitHub remote repository, it's a good 
time to install ``pre-commit`` so that future commits will run a suite of checks 
before pushing code to the remote repository. 
Run the following command in your terminal.

.. code:: bash

    >> pre-commit install

For more information about ``pre-commit`` including a list of the checks that 
will be run before each commit, please see :doc:`pre-commit <../practices/precommit>`.