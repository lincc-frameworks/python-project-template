Keeping your project up to date
===============================

Once your project is under version control you'll be able to keep your project up 
to date as new features are added to the template by running the following command:

.. code-block:: bash

    >> copier update

Copier will automatically check to see if a newer version of the original template 
is available and if so the changes will be automatically applied. Neato!

And of course, because your project is under version control, if you don't like 
the new changes, you can always revert back to the previous state.

There are a few additional flags that you can use to be more explicit about how and what you want to update.
We've found the following to be the most useful.

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

This tell copier to use the previous answers for all questions except the one you want to
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