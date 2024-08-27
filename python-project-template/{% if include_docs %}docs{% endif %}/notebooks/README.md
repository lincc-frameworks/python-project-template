# Jupyter notebooks to run on-demand.

Jupyter notebooks in this directory will be run each time you render your documentation.

This means they should be able to be run with the resources in the repo, and in various environments:

- any other developer's machine
- github CI runners
- ReadTheDocs doc generation

This is great for notebooks that can run in a few minutes, on smaller datasets.

For notebooks that require large datasets, access to third party APIs, large CPU or GPU requirements, put them in `./pre_executed` instead.
