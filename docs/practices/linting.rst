Code Style
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

"Code style" describes the conventions you use in writing the source files 
for your code base. If there are multiple people working on a code base, 
it's important to establish an agreeable code style so everyone can easily read 
and modify the code.

Linters
...............................................................................

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

These tools often do *not* change your code to adhere to a standard, they just 
alert you to potential issues.

The template currently offers two tools for linting:

- **pylint** - slow and thorough
- **ruff** - very fast, usually good enough.

Auto-formatters
...............................................................................

Auto-formatting tools will *change* your source files, to adhere to a consistent
visual style. These tools often do *not* interpret your code for syntax errors
or code smells.

The template currently offers three tools for auto-formatting:

- **black** - general code formatting
- **isort** - import statement sorting and organizing
- **ruff** - does it all

Different formatters share a lot of the same opinions, but we recommend picking
a single standard for your project and sticking to it.
If some folks use different formatters, this may cause undue churn in your source 
files as each developer creates some formatting changes each time they touch a file 
(and then another developer undoes them the next time they touch the same file).
Two good configurations are to use ``ruff`` for all your code style needs OR 
use some combination of ``pylint``, ``black``, and ``isort``.

Ruff
-------------------------------------------------------------------------------

`Ruff <https://docs.astral.sh/ruff/>`_ is a very performant and highly customizable
linting tool, that can also perform auto-formatting. 

This tool can be run on its own in *linting* (warning) mode with command like:

.. code:: console

    >> ruff check

This tool can be run on its own in *auto-formatting* mode with command like:

.. code:: console

    >> ruff format

Modifying ruff
...............................................................................

The configuration for ruff is maintained in the ``pyproject.toml`` file.
Ruff has many rules split into groups that can be selected to use when checking code.
By default, we mostly follow the set of rules suggested by the
`ruff documentation <https://docs.astral.sh/ruff/linter/#rule-selection>`_, with a 
few extra rules as suggested by
`Rubin Data Management <https://developer.lsst.io/python/style.html#ruff-configuration-files>`_.
For more information on configuration, see ruff's documentation here:
https://docs.astral.sh/ruff/configuration/

Pylint
-------------------------------------------------------------------------------

`pylint <https://pylint.readthedocs.io/en/latest/>`_ is a linting
tool. It is fairly opinionated, but highly customizable. It's very thorough, but 
that means it's also among the slower of the linting options out there.

Modifying pylint
...............................................................................

There are lots of errors and coding standards that the linter can search for, 
but you may not want to include all of them, or modify the values of certain checks such as line
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

Black
-------------------------------------------------------------------------------

`Black <https://black.readthedocs.io/en/latest/index.html>`_ is a very opinionated
auto-formatting tool. It ensures that all code in your project uses consistent 
formatting (e.g. spacing, quote styles, line breaks).

This tool can be run on its own with command like:

.. code:: console

    >> black .

Modifying Black
...............................................................................

Black and doesn't permit much in the way of customization. The
configurations that are available are defined in ``pyproject.toml`` under the
``[tool.black]`` section. For more details see Black's documentation on configuration:
https://black.readthedocs.io/en/latest/usage_and_configuration/the_basics.html#configuration-via-a-file

isort 
-------------------------------------------------------------------------------

isort is a standalone tool that will sort and organization imports in all
the `.py` and `.pyi` files in your project.

This tool can be run on its own with command like:

.. code:: console

    >> isort .

How to switch or remove tools
-------------------------------------------------------------------------------

If you started a project without selecting a linter, or you want to change or 
remove the linter entirely, use the ``copier update`` command to change the
response to the "What tooling set would you like to use to enforce code style?"
question. This will add or remove steps to check code style against the selected
tools.
