Starting a new project
===============================================================================


Create a new project from the template
-------------------------------------------------------------------------------

Choose where you would like to create your new project, and call copier with the template.

.. code-block:: bash

    >> copier gh:lincc-frameworks/python-project-template <path/to/destination>

After providing answers to the prompts, Copier will hydrate a project template and save it in the specified location. Additionally Copier will run ``git init`` in the new project directory to initialize it as a local repository.

Create a new environment and install your new package
-------------------------------------------------------------------------------

Create a new environment with your choice of environment tools (virtualenv, conda, etc.). Activate it, and change into the package directory.

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