Configuration with pyproject.toml
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

The ``pyproject.toml`` file is used to define many different project configurations.
It replaces the need for setup.py, requirements.txt, and other configuration files.

A fundamental use for ``pyproject.toml`` is to define a dependencies. You should
make an effort to add all the required dependencies to the ``[dependencies]``
section of the file.

In addition to dependencies, ``pyproject.toml`` centralizes the project's
configuration and makes it easier to manage. If you examine your ``pyproject.toml``
file, you'll see sections with titles like ``[tool.<blah>]``. These sections are
used to configure tools that are used in the project that would otherwise require
their own configuration files.

A ``pyproject.toml`` file provides a vast number of customization options well
beyond what can be covered here. For an in-depth look at how the file can be used
and how it compares to the older ``setup.py`` checkout the
`Python Packaging User Guide <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/>`_.
