Starting a new project
===============================================================================


Create a new project from the template
-------------------------------------------------------------------------------

Choose where you would like to create your new project, and call copier with the template.

.. code-block:: bash

    >> copier gh:lincc-frameworks/python-project-template <path/to/destination>

Copier will ask you questions for how to set up the project. These questions will be used to fill in aspects of the project's configuration, including both metadata and parameters. Below we provide some high-level overview of the questions:

  * *What is the name of your project?* (``project_name``): The name of your project.
  * *What is your python module name?* (``module_name``): The name of your (first) module. The main thing this controls is where your source code will live (``src/{{module_name}}``).
  * *Your first and last name?* (``author_name``): The name of code's author.  This will be used in the project and documentation metadata.
  * *Your preferred email address?* (``author_email``): The contact email for the code's author. This will be used in the project and documentation metadata.
  * *What tooling would you like to use to enforce code style?* (``preferred_linter``): A linter is a tool to automatically format for consistency (see :doc:`Linting <../practices/linting>`). We provide options for `black <https://black.readthedocs.io/en/stable/>`_, `pylint <https://pypi.org/project/pylint/>`_, or no linter. Choosing a linter will include it as a project dependency and include it in the :doc:`pre-commit <../practices/precommit>` hooks.
  * *Do you want to use a tool to maintain a specific ordering for module imports?* (``use_isort``): `isort <https://pycqa.github.io/isort/>`_ is a tool for ordering imports in a standard order. Enabling the option will include ``isort`` as part of github's :doc:`pre-commit <../practices/precommit>`.
  * *Do you want to create some example module code?* (``create_example_module``): If this option is selected the template will create a model in ``src/{{module_name}}`` and create a corresponding example test file.

While these choices will provide the initial structure for your project, most can be changed later. See Copier's `documentation for changing answers to the question <https://copier.readthedocs.io/en/stable/updating/>`_

After providing answers to the prompts, Copier will hydrate a project template and save it in the specified location. Additionally Copier will run ``git init`` in the new project directory to initialize it as a local repository.

Create a new environment and install your new package
-------------------------------------------------------------------------------

If you are using `virtual environments <https://packaging.python.org/en/latest/glossary/#term-Virtual-Environment>`_ create a new environment with your choice of environment tools (virtualenv, conda, etc.) and activate it. This step is optional, but we recommend using virtual environments to better manage different project's dependencies. See Python's `description of virtual environments <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>`_ for more details.

Go to the new package's directory (e.g. ``cd {{project_name}}``)

Install the newly created python package. Use ``pip`` to install both the standard set of dependencies as well as the ``[dev]`` dependencies. (Note: depending on your system, you may not need the single quotes about ``'.[dev]'``)

.. code-block:: bash

    >> pip install -e .
    ...
    Lots of output
    ...

    >> pip install '.[dev]'
    ...
    Lots more output
    ...

You could stop here
-------------------------------------------------------------------------------

At this point, your new project is hydrated and ready for you to start coding. But there's a lot more that this template has to offer. Keep reading to find out more about built in pre-commit hooks, GitHub CI, automatic documentation, and more.

Commit your new project locally
-------------------------------------------------------------------------------

If you're interested in using pre-commit hooks to crosscheck your code before you commit it, now is a good time to set that up (it's just one command) - check out `"Helpful pre-commit hooks" <https://github.com/lincc-frameworks/python-project-template#helpful-pre-commit-hooks>`_.

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

Keep your project up to date
-------------------------------------------------------------------------------

Once your project is under version control you'll be able to keep your project up to date by running the following:

.. code-block:: bash

    >> copier

Yep. That's it.

Copier will automatically check to see if a newer version of the original template is available and if so the changes will be automatically applied. Neato!

And of course, because your project is under version control, if you don't like the new changes, you can always revert back to the previous state.