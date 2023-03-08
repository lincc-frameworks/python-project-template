Pre-Commit
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

pre-commit is installed when running pip install '.[dev]'. It's an industry 
standard tool that executes a set of tests prior to completing a git commit action. 
Using pre-commit enables a quick check of your code before it's committed and checked 
by GitHub workflows. This cuts down on code feedback time, and allows for faster 
development. Additional documentation can be found `here <https://pre-commit.com/index.html>`_.

To configure pre-commit for your project, run the following command register 
pre-commit hooks with ``.git/hooks/pre-commit``.

.. code-block:: bash
    
    pre-commit install
