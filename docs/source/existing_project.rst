Incorporating the template into a prior project
===============================================================================

These instructions are for those who want to incorporate the latest version of the 
LINCC Frameworks Python Project Template into an existing project that has not 
previously used our template. 

If you want to update a project that already uses the template, please see 
:doc:`Keeping your project up to date <update_project>`.

.. attention ::

    Every pre-existing project is unique - it's a snowflake - even if the developers followed 
    accepted guidelines and best practices. 
    
    Because of that, we can't we enumerate all the possible sticking points that may be 
    encounter when attempting to incorporate the LINCC Frameworks Python Project Template 
    into a pre-existing project.

.. tip ::

    The newer a pre-existing project is, the easier it will be to incorporate the 
    LINCC Frameworks Python Project Template.

    That being said, we have used this template to bring dormant projects up to date with 
    modern development standards.

Before you begin
----------------

Start clean
...........

It's best to start with a clean local repository and a new git branch just for this task. 
Copier will not allow the user to merge a template with a git tracked local repository 
if there are uncommitted changes. 

It's not explicitly necessary, but removing ``cache`` and ``build`` directories will 
make it easier to see what changes are being made.

Check your environment
......................

Make sure your system satisfies the :doc:`prerequisites <overview>`.

Hydrate a copy of the template into your project
................................................

.. code:: bash

    >> cd <existing_project_directory>
    >> copier gh:lincc-frameworks/python-project-template .


A note on directory structure
.............................

The LINCC Frameworks template does not impose a rigid directory structure. 
However, some of the tools that the template includes expect that 
the package source code will be in a first level directory named ``src``, and 
that tests will be contained in a first level directory named ``tests``.

For example, if your project is in a directory named ``/science``, your source 
code and tests might look like this:

.. code:: bash

    /science/src/module.py
    /science/tests/test_module.py

If your directory structure for source code and tests is significantly 
different than this, it might be worth reorganizing the files in order to make use 
of the tools (CI, linting, auto documentation) that the template provides.

While running Copier
--------------------

Reasonable responses to questions
.................................
If your project already has a name, especially if it's published on PyPI, it's 
advised that you use the same name when asked "What is the name of your project?".

If your project has a license already, and it is not one of the licenses listed 
in the "What license would you like to use?", select "None".

Respond **no** when asked "Do you want to create some example module code?". 
It's fine to respond "yes", however, given that your project already has an established 
source code and test directory structure, there's no benefit to including an example 
module.

Copier work summary
...................

After Copier has received all your answers, it will begin to hydrate the template 
with your responses and inject them into your project. 
As it does so, don't be scared of ``conflict`` markers - remember that everything is git tracked, 
and Copier does not have the ability permanently overwrite your files.

The following example is output from a Copier update. Note again that ``conflict`` is 
simply an indicator that you should review that file before committing.

.. code :: bash

    Copying from template version 1.2.1
    identical  .
    identical  README.md
    conflict  .copier-answers.yml
    overwrite  .copier-answers.yml
    identical  .gitignore
    identical  .github/workflows
    conflict  .github/workflows/linting.yml
    overwrite  .github/workflows/linting.yml
    identical  nb/README.md
    conflict  .pre-commit-config.yaml
    overwrite  .pre-commit-config.yaml
    conflict  pyproject.toml
    overwrite  pyproject.toml


After running Copier
--------------------

Confirm that your package builds
................................
You should attempt to use ``pip`` to build your package and install dependencies. 
Failure to build successfully may be an indicator of a corrupted pyproject.toml file
or missing dependencies.

.. code:: bash

    >> pip install -e .
    >> pip install .'[dev]'

.. note:: 

    If your existing package uses a setup.py file to build, you will need to move the 
    important definitions over to pyproject.toml.

    It's likely that you'll only need to move the list of dependencies. But if 
    there is a significant amount of embedded logic, then this task will become
    more involved.

    After porting the definitions, remove setup.py and build with ``pip install``. 
    This will ensure that pyproject.toml is being used for build configuration.


Run all unit tests
..................

Once you are sure the package still builds, run all the unit tests to ensure that 
the built package can be imported. The Copier template should not cause any tests 
to fail.


Use pre-commit
..............

Install and use ``pre-commit``. It may seem annoying at first, but it will save 
you many cycles of "see a test fail on GitHub, make and push a change, hope the test passes".


Import sorting
..............

If your project wasn't using ``isort`` or something similar before, there's a good 
change that pre-commit hook will fail. It will automatically reorder the offending 
imports. You'll just need to ``git add`` the modified files again.


Linters
.......

If your project wasn't using a linter before, and you chose to include pylint, black, 
or another linting tool, it's reasonable to skip the linting check on the first commit. 

For instance if you selected ``black`` as your new linter, use the following to 
bypass the pre-commit linting check on the first commit.

.. code :: bash

    >> SKIP=black git commit -m 'Incorporating LINCC Frameworks PPT'

Linters are opinionated and if your project wasn't using one before there will 
be a lot of linting errors that will block committing your code.

It's highly recommended that in the next commit after incorporating the template 
that you address the linting errors so that you don't have to continue to use the 
``SKIP=...`` command for the rest of your days.
