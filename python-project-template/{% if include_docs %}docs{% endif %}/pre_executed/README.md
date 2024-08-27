# Pre-executed Jupyter notebooks 

Jupyter notebooks in this directory will NOT be run in the docs workflows, and will be rendered with 
the provided output cells as-is.

This is useful for notebooks that require large datasets, access to third party APIs, large CPU or GPU requirements.

Where possible, instead write smaller notebooks that can be run as part of a github worker, and within the ReadTheDocs rendering process.

To ensure that the notebooks are not run by the notebook conversion process, you can add the following metadata block to the notebook:

```
   "nbsphinx": {
    "execute": "never"
   },
```
