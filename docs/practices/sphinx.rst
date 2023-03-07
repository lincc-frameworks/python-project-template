Sphinx - ReadTheDocs and AutoAPI
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

`Sphinx <https://www.sphinx-doc.org/>`_ is a documentation generation engine 
that uses ReStructured Text (RST) files to make pretty websites for hosting 
technical documentation. You write your documentation in RST markdown, using 
Sphinx directives, and they are compiled into html. This very document is
an example!

This template provides additional scaffolding for autoapi documentation. This 
pulls docstrings from python source code and creates pretty API reference documents.

How to get started
-------------------------------------------------------------------------------

If you have connected your GitHub account to `ReadTheDocs <https://readthedocs.org/>`_
you should be able to automatically import the documentation from your project. 
To connect your GitHub account to ReadTheDocs, simply sign in to ReadTheDocs using your GitHub account.

On your dashboard, you'll see an "Import a Project" button that will take you to a 
list of repositories that can be 
`automatically imported <https://docs.readthedocs.io/en/stable/intro/import-guide.html#automatically-import-your-docs>`_. 
If you don't see the repository you expect, it is possible that you do not have 
sufficient permissions configured in your GitHub organization. Talk to an administrator 
of the organization, and let them know what you're trying to do.

How to manage
-------------------------------------------------------------------------------

To build the documentation in your local development environment, it's best to 
follow the same steps as readthedocs will perform when building your documentation.

.. code-block:: bash

    cd $project_directory
    pip install -e .
    cd docs
    python -m sphinx -T -E -b html -d _build/doctrees -D language=en . ../_readthedocs/html

This will build your document source tree into ``$project_directory/_readthedocs/html/``,
and you can inspect the built HTML by opening the ``index.html`` file.