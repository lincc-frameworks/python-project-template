# Jupyter notebooks to run on-demand.

Jupyter notebooks in this directory will be run each time you render your documentation.

This means they should be able to be run with the resources in the repo, and in various environments:

- any other developer's machine
- github CI runners
- ReadTheDocs doc generation

This is great for notebooks that can run in a few minutes, on smaller datasets.

If you would like to include these notebooks in automatically generated documentation
simply add the notebook name to the ``../notebooks.rst`` file, and include a markdown
cell at the beginning of your notebook with ``# Title`` that will be used as the text
in the table of contents in the documentation.

Be aware that you may also need to update the ``../requirements.txt`` file if
your notebooks have dependencies that are not specified in ``../pyproject.toml``.

For notebooks that require large datasets, access to third party APIs, large CPU or GPU requirements, put them in `./pre_executed` instead.

For more information look here: https://lincc-ppt.readthedocs.io/en/latest/practices/sphinx.html#python-notebooks

Or if you still have questions contact us: https://lincc-ppt.readthedocs.io/en/latest/source/contact.html