Updating a project
==================

Updating a project comes in two flavors. 
Updating to incorporate a new version of the template, or updating 
one or more specific responses to the questions used to hydrate the project.

Either way, the process starts with a single-line command in the directory containing
your project:

.. code-block:: console

    >> copier update ./<project directory>

Updating the template version
-----------------------------

As LINCC Frameworks release new template features, you can keep your project up 
to date by running the ``copier`` command which will do two things. 

1) Bring in any updates to the template.
2) Provide an opportunity to update responses used to hydrate the project.

While that may sound trivial, Copier uses a (necessarily) complicated workflow 
to do this successfully.
Take a look at the 
`Copier documentation <https://copier.readthedocs.io/en/latest/updating/#how-the-update-works>`_ 
get an appreciation for complexity of the task.

.. note::

    While the update is running, you'll likely be asked if you want to overwrite 
    files where the changes can't be automatically merged. 
    For example, you might see this on the command line:

    .. code-block:: console

        >> copier update
          ...
          identical  README.md
          identical  tests
          conflict  .pre-commit-config.yaml
            Overwrite .pre-commit-config.yaml? [Y/n]

    Responding ``y`` will allow Copier to attempt to update a file.
    While ``n`` will usually result in the creation of a ``.rej`` file - 
    ``.pre-commit-config.yaml.rej`` in this case.
    The contents will resemble a git merge conflict, and 
    allow you to decide how to incorporate the template changes.

    Remember, don't commit ``.rej`` files, you should remove them as 
    the merge conflicts are resolved.

Once Copier has finished, you should run ``git diff`` to see what code has changed.
If you don't like the new changes, you can always revert back to the previous state.

Clean up after the update
.........................

If you change any of the initial responses during the update you should 
take some time to review your project for any files or directories that are no 
longer needed. 

For instance, if you change the ``package_name`` response from "new_project" to 
"great_project", it is unlikely that Copier will be able to create a new 
directory structure, move and rename your existing files, *and* remove the old 
directory structure.

Updates to pyproject.toml
.........................

The pyproject.toml file is the primary configuration file for your project. 
When a project is initially hydrated from the template, a custom pyproject.toml file 
will be created. Generally Copier updates won't significantly affect this file, 
so be sure to take a close look at any differences.

If something looks incorrect, remember that changes made by Copier are only *staged for 
commit*, they are't permanent and can easily be unstaged.

Get the absolute latest version of the template
...............................................

By default, Copier will find and apply the latest tagged release of a template 
when creating or updating a project. 
However, there may be new template features that you want to incorporate into 
your project before they are tagged for release.
Copier provides the ``--vcs-ref`` flag for this purpose. 

.. code-block:: console

    >> copier update --vcs-ref=HEAD

Here Copier will use the latest template from the ``main`` branch and apply it 
to your project.
Note that ``HEAD`` can be replaced with any reasonable git tag such as a 
branch name or commit hash.

Update a response to a single question
-----------------------------------------

The documentation for Copier indicates that it is a bad idea to manually edit the 
file that records your responses to the template questions. If you decide that you 
answered one of the questions incorrectly or you just want to update the 
response, you can change it without having to edit the rest.

.. code-block:: console

    >> copier update --force --data <question_name>="new answer"

This tells copier to use the previous answers for all questions except the one you want to
update. Copier will not attempt to update the template, and it will not review 
the responses to the questions. 

For example, if you initialized your project by selecting ``pylint`` as your 
preferred linter, but now would like to change to ``black``, you could use the 
following command:

.. code-block:: console

    >> copier update --force --data include_benchmarks=true

The full list of questions can be found 
`here <https://github.com/lincc-frameworks/python-project-template/blob/main/copier.yml>`_.

Depending on the response that is being updated there may be several files that 
are changed. See the note above about merge conflicts and ``.rej`` files for 
more context.

Remember, the changes from these updates are only *staged for commit*, they 
aren't permanent and can easily be unstaged.

More information about Copier updates
-------------------------------------

The maintainers of Copier have written good instructions and there's no point 
in reproducing it all here. 
For all the details about updating with Copier checkout the 
`original documentation <https://copier.readthedocs.io/en/latest/updating/>`_.


Still have questions?
-------------------------------------

:doc:`/source/contact`