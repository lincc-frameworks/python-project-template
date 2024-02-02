Code Style
===============================================================================

TODO - this needs a big overhaul.

What is it? Why do it?
-------------------------------------------------------------------------------

Linting is a form of static program checking, meaning that it analyzes code 
without running it.

A linter checks code for code errors, violations of some agreed-upon coding 
standards, or gives its opinion on code smells. A "code smell" is when something 
isn't exactly **wrong**, but could be an indicator that your code is inefficient 
or could be refactored to be cleaner.

When code is reliably run through a linter, then code reviewers can assume that 
the code they're looking at adheres to that agreed-upon coding standard. 
A code reviewer won't be distracted by improper spacing, and can focus their 
reviewing effort on the meat of the code.

There are three main linters suggested by this template: pylint, black, and ruff. While
they have a lot of the same opinions, we recommend picking a single standard for 
your project and sticking to it.
If some folks use one linter, this may cause undue churn in your source files as
each developer creates some formatting changes each time they touch a file (and 
then another developer undoes them the next time they touch the same file).


Note about our pylint configuration
-------------------------------------------------------------------------------

Pylint is one of the linter options included in the template. While there are a
number of errors and coding standards that the linter can search for, you may not
want to include all of them, or modify the values of certain checks such as line
length to fit the agreed standards in your project. To do this, pylint allows
project wide configuration in either the project's ``pyproject.toml`` file, or in
a separate ``.pylintrc`` file.

We have found in our projects that one configuration across both source and test
files is inadequate, and that separate standards are needed in each, for example,
in requiring that methods contain docstrings. So we generate two ``.pylintrc``
files, one under ``src`` and the other under ``tests``. When pylint is run in
the pre-commit hooks and the github actions, it is run twice, once on the
source files with the src config, and once on the test files with the tests
config.

For more on how to configure the pylint options, `take a look at pylint's
documentation.
<https://pylint.readthedocs.io/en/stable/user_guide/configuration/index.html>`_


How to modify
--------------

Currently the template offers three choices for linters - None, Black, or pylint.

Modifying Black
................

`Black <https://black.readthedocs.io/en/latest/index.html>`_ is a very opinionated
linting tool, and doesn't permit much in the way of customization. The
configurations that are available are defined in ``pyproject.toml`` under the
``[tool.black]`` section. For more details see Black's documentation on configuration:
https://black.readthedocs.io/en/latest/usage_and_configuration/the_basics.html#configuration-via-a-file


Modifying pylint
.................

`pylint <https://pylint.readthedocs.io/en/latest/>`_ is a highly customizable linting
tool. The configuration for pylint is maintained in two ``.pylintrc`` files in 
the ``./src`` and ``./tests`` directories. This allows separate configurations
for source versus test code. Take a look at the configuration documentation
for pylint here: https://pylint.readthedocs.io/en/latest/user_guide/configuration/index.html


Modifying ruff
.................

`Ruff <https://docs.astral.sh/ruff/>`_ is a very performant and highly customizable linting
tool. The configuration for ruff is maintained in the ``pyproject.toml`` file.
Ruff has many rules split into groups that can be selected to use when checking code.
By default, we mostly follow the set of rules suggested by the
`ruff documentation <https://docs.astral.sh/ruff/linter/#rule-selection>`_, with a few extra
rules as suggested by
`Rubin Data Management <https://developer.lsst.io/python/style.html#ruff-configuration-files>`_.
For more information on configuration, see ruff's documentation here:
https://docs.astral.sh/ruff/configuration/

How to switch or remove linters
-------------------------------

If you started a project without selecting a linter, or you want to change or 
remove the linter entirely, use the ``copier update`` command to change the
response to the "What tooling would you like to use to enforce code style?"
question.
