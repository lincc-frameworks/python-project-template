Hydrate a pre-template project
===============================================================================

These instructions are for those who want to incorporate the latest version of the 
LINCC Frameworks Python Project Template into an existing project that has not 
previously used our template. 

If you want to update a project that already uses the template, please see 
:doc:`Keeping your project up to date <update_project>`.

Disclaimers
-----------

Every pre-existing project is unique
....................................

We can't enumerate all the possible sticking points that you may encounter 
when attempting to incorporate the LINCC Frameworks Python Project Template 
into a pre-existing project. 

We're here to help though! We have called out some gotchas below and we want to 
hear from you if you encounter problems. Feel free to :doc:`/source/contact`

Newer projects are easier to upgrade
....................................

The newer a pre-existing project is, the easier it will be to incorporate the 
LINCC Frameworks Python Project Template.

That being said, we have successfully used this template to bring dormant 
projects up to date with modern development standards.

Before you begin
----------------

Check the prerequisites
.......................

Make sure your system satisfies the :ref:`prerequisites <prerequisites>`. Copier, 
the tool that powers our template, requires recent versions of Python and Git. 
We have seen a handful of instances, particularly when working on computing 
clusters, where users have encountered error messages resulting from older 
versions of the dependencies.

Start clean
...........

It's best to start with a clean local repository and a new git branch just for this task. 
Copier will not allow the user to merge a template with a git tracked local repository 
if there are uncommitted changes or untracked files.

It's not explicitly necessary, but removing ``cache`` and ``build`` directories will 
make it easier to see what changes are being made.

Hydrate a copy of the template into your project
................................................

.. code:: console

    >> cd <existing_project_directory>
    >> copier copy gh:lincc-frameworks/python-project-template .


A note on directory structure
.............................

The LINCC Frameworks template does not impose a rigid directory structure. 
However, some of the tools that the template includes expect that 
the package source code will be in a first level directory named ``src``, and 
that tests will be contained in a first level directory named ``tests``.

For example, if your project is in a directory named ``/science``, and your package
is named ``new_science``, your source code and tests might look like this:

.. code:: console

    /science/src/new_science/module.py
    /science/tests/new_science/test_module.py

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

.. code-block:: console
    :class: no-copybutton

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

Look at what changed
....................

You should run ``git diff`` to see what code has changed.
If you don't like the new changes, you can always revert back to the previous state.

Additionally, if Copier encounters a merge conflict between your existing code and 
the updated template, it will produce ``.rej`` files that contain the unresolved diffs. 
If you see a ``.rej`` file, resolve the merge conflict and check that your code 
was updated correctly. 
There is no need to commit ``.rej`` files, you should remove them as 
the merge conflicts are resolved.

Confirm that your package builds
................................
You should attempt to use ``pip`` to build your package and install dependencies. 
Failure to build successfully may be an indicator of a corrupted pyproject.toml file
or missing dependencies.

.. code:: console

    >> pip install -e .'[dev]'

.. note:: 

    If your existing package uses a setup.py file to build, you will need to move the 
    important definitions over to pyproject.toml.

    It's likely that you'll only need to move the list of dependencies. But if 
    there is a significant amount of embedded logic, then this task will become
    more involved.

    After porting the definitions, remove setup.py and build with ``pip install``. 
    This will ensure that pyproject.toml is being used for build configuration.

.. warning::

    If your existing package uses a pyproject.toml file and has a hardcoded "version"
    line similar to ``version: "1.2.0"`` in the ``[project]`` section, please 
    remove that line.

    The LINCC Frameworks template makes use of dynamic versioning with 
    ``dynamic = ["version"]``. 
    A build error will occur if both a hardcoded and dynamic version definition 
    are present in the same pyproject.toml file.


Run all unit tests
..................

Once you are sure the package still builds, run all the unit tests to ensure that 
the built package can be imported. The Copier template should not cause any tests 
to fail.


Use pre-commit
..............

Install and use ``pre-commit``. It may seem annoying at first, but it will save 
you many cycles of "see a test fail on GitHub, make and push a change, hope the 
test passes". Installation is easy!

.. code:: console

    >> pre-commit install

For more information about ``pre-commit`` including a list of the checks that 
will be run before each commit, check out :doc:`pre-commit <../practices/precommit>`.

Import sorting
..............

If your project wasn't using ``isort`` or something similar before, there's a good 
chance that pre-commit hook will fail. It will automatically reorder the offending 
imports. You'll just need to ``git add`` the modified files again.


Linters
.......

If your project wasn't using a linter before, and you chose to include pylint, black, 
or another linting tool, it's reasonable to skip the linting check on the first commit. 

For instance if you selected ``black`` as your new linter, use the following to 
bypass the pre-commit linting check on the first commit.

.. code:: bash

    >> SKIP=black git commit -m 'Incorporating LINCC Frameworks PPT'

Linters are opinionated and if your project wasn't using one before there will 
be a lot of linting errors that will block committing your code.

It's highly recommended that in the next commit after incorporating the template 
that you address the linting errors so that you don't have to continue to use the 
``SKIP=...`` command for the rest of your days.

Benchmarking
............

If your project wasn't using benchmarking before, and you chose to include it, please 
make sure you follow the instructions under :doc:`Continuous Integration Benchmarking <../practices/ci_benchmarking>`
to conclude the setup.

Still have questions?
----------------------------------------

:doc:`/source/contact`