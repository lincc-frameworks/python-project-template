Keeping your project up to date
===============================

As we release new template features, you can keep your project up to date with 
a single-word command:

.. code-block:: bash

    >> copier

Copier will automatically check to see if a newer version of the original template 
is available and if so the changes will be automatically applied. Neato!

You should run ``git diff`` to see what code has changed.
If you don't like the new changes, you can always revert back to the previous state.

Additionally, if Copier encounters a merge conflict between your existing code and 
the updated template, it will produce ``.rej`` files that contain the unresolved diffs. 
If you see a ``.rej`` file, resolve the merge conflict and check that your code 
was updated correctly. 
There is no need to commit ``.rej`` files, you should remove them as 
the merge conflicts are resolved.

There are a few additional flags that you can use to be more explicit about how 
and what you want to update. We've found the following to be the most useful.

Get the absolute latest version of the template
-----------------------------------------------

By default, Copier will find and apply the latest tagged release of a template when creating 
or updating a project. 
However, there may be new template features that you want to incorporate into your project 
before they are tagged for release.
Copier provides the ``--vcs-ref`` flag for this purpose. 

.. code-block:: bash

    >> copier --vcs-ref=HEAD update

Copier will use the latest template from the ``main`` branch and apply it to your project.
Note that ``HEAD`` can be replaced with any reasonable git tag such as a branch name or 
commit hash.

Change your response to a single question
-----------------------------------------

The documentation for Copier indicates that it is a bad idea to manually edit the 
file that records your responses to the template questions. If you decide that you 
answered one of the questions incorrectly, you can update it without having to edit 
the rest.

.. code-block:: bash

    >> copier --force --data <question_name>="new answer" update

This tells copier to use the previous answers for all questions except the one you want to
update. For instance, if you initialized your project by selected ``pylint`` as your 
preferred linter, but now would like to change to ``black``, you could use the following:

.. code-block:: bash

    >> copier --force --data preferred_linter="black" update

The full list of questions can be found 
`here <https://github.com/lincc-frameworks/python-project-template/blob/main/copier.yml>`_.

More information about Copier
-----------------------------

The maintainers of Copier have written good instructions and there's no point 
in reproducing it all here. 
For all the details about updating with Copier checkout the 
`original documentation <https://copier.readthedocs.io/en/latest/updating/>`_.

Updates to pyproject.toml
-------------------------

The pyproject.toml file is the primary configuration file for your project. 
When a project is initially hydrated from the template, a custom pyproject.toml file 
will be created. Generally Copier updates shouldn't drastically affect this file, 
but if you are modifying prior answers, take a close look at any changes made to this file.

If something looks incorrect, remember that any changes made by Copier are only *staged for 
commit*, they are't permanent and can easily be unstaged.