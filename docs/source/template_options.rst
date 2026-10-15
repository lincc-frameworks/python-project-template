1. Purpose of the project
--------------------------------
  
   +------------+------------------------------------------------------------+
   | Question   | What is the purpose of this installation?                  |
   +------------+------------------------------------------------------------+
   | Options    | library, command, notebook, retrofit, **✱ customized**     |
   +------------+------------------------------------------------------------+

This question will determine how the project is set up and what options are presented. The options include:

* library: python library - This creates a standard Python library meant to be installed with something like `pip` and called from other applications. It includes benchmarking and notebook options, but not commandline utils.
* command: command line application - This sets up the project as a command line tool.
* notebook: collection of notebooks - This sets up the project to include Jupyter notebooks. By default it won't create a source tree, benchmarks, etc.
* retrofit: retrofitting existing project - This adapts an existing project to fit the template structure.
* custom: custom (DEFAULT) - This allows for a fully customized setup.


2. Name of your project
-----------------------

   +------------+-----------------------------------------------+
   | Question   | What is the name of your project?             |
   +------------+-----------------------------------------------+
   | Default    | `my_project`                                  |
   +------------+-----------------------------------------------+

The name of your project.

Must start with a lowercase letter, followed by one or more of the following (a-z, 0-9, _, -).

This will be used to connect to your project on github, as in ``https://github.com/{{project_organization}}/{{project_name}}``.

If you distribute your code via PyPI, this is the name that will be used. This will allow users to install like so: ``pip install <project_name>``.

Read more at :doc:`../practices/pypi`.


3. Python package name
-----------------------

   +------------+-----------------------------------------------+
   | Question   | What is the name of your Python package?      |
   +------------+-----------------------------------------------+
   | Default    | `example_package`                             |
   +------------+-----------------------------------------------+

The name of your top level package. 

Must start with a lowercase letter, followed by one or more of the following (a-z, 0-9, _).

Specifies the location of the source code, as in::

    project_name/
    ├─ src/
    │  ├─ package_name/
    │  │  ├─ __init__.py
    │  │  ├─ module.py
    │  │  ├─ ...



4. Github organization name
----------------------------

   +------------+--------------------------------------------------------+
   | Question   | What github organization will your project live under? |
   +------------+--------------------------------------------------------+
   | Default    | `my-organization`                                      |
   +------------+--------------------------------------------------------+

This will be:

    * The name of the GitHub organization that will host your project, or

    * Your GitHub username, if you're working outside of an organization. 

This is used to construct URLs to your project, as in: ``https://github.com/{{project_organization}}/{{project_name}}``.


5. Name of the code author
--------------------------

   +------------+-----------------------------------------------+
   | Question   | What is the name of the code author?          |
   +------------+-----------------------------------------------+
   | Default    | `Your Name`                                   |
   +------------+-----------------------------------------------+

The name of the code's author, or the organization that is responsible for the code.

This will be used in the project and documentation metadata. 

This name will also be included as part of the copyright license.


6. Email address
----------------

   +------------+-----------------------------------------------+
   | Question   | Code author's preferred email address?        |
   +------------+-----------------------------------------------+
   | Default    | `name@you.com`                                |
   +------------+-----------------------------------------------+

The contact email for the code's author. 

This will be used in the project and documentation metadata.


7. License
----------

   +------------+-----------------------------------------------+
   | Question   | What license would you like to use?           |
   +------------+-----------------------------------------------+
   | Options    | **✱ MIT**, BSD, none                          |
   +------------+-----------------------------------------------+

The license type you want to use for this project. 

.. Tip:: 

    * For more information on these options, see `Github's license page <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository>`_.

    * You can also check out `choosealicense.com <https://choosealicense.com/>`_ for more information on open source licenses.


8. Versions of Python
---------------------

   +------------+----------------------------------------------------+
   | Question   | What versions of Python will your project support? |
   +------------+----------------------------------------------------+
   | Options    | 3.10 (end-of-life), **✱ 3.11**,                    |
   |            | **✱ 3.12**, **✱ 3.13**,                            |
   |            | 3.14, 3.15                                         |
   +------------+----------------------------------------------------+

Select all versions of python that you are targeting for execution.

We will add automated testing for all of these versions. 


9. Linters/Reformatters
----------------------------

   +------------+---------------------------------------------------------------+
   | Question   | What tooling set would you like to use to enforce code style? |
   +------------+---------------------------------------------------------------+
   | Options    | **✱ ruff_lint**, **✱ ruff_format**, pylint, black, isort      |
   +------------+---------------------------------------------------------------+

See :doc:`/practices/linting`.

We provide several compatible options for linters and autoformatters.

Choosing a formatter or linter will include it as a project dependency and include it in the :doc:`pre-commit <../practices/precommit>` hooks.


10. Failure notifications
-------------------------

   +------------+---------------------------------------------------------------+
   | Question   | How would you like to receive workflow failure notifications? |
   +------------+---------------------------------------------------------------+
   | Options    | email, slack bot integration, *(✱ none)*                      |
   +------------+---------------------------------------------------------------+

See :doc:`/practices/ci_testing`. 

Some GitHub workflows are not loud about their failures, so we have some configuration for sending alerts to you or your team.


11. Static type checking
------------------------

    +------------+--------------------------------------------------------------------------------+
    | Question   | Would you like to include mypy to perform static type checking for type hints? |
    +------------+--------------------------------------------------------------------------------+
    | Options    | **✱ none**, basic, strict                                                      |
    +------------+--------------------------------------------------------------------------------+

`mypy <https://www.mypy-lang.org>`_ performs static type checking on python code that uses `type hints <https://docs.python.org/3/library/typing.html>`_. 
       
This type checking makes sure that the correct data types are being used where type hints are defined. 

If basic or strict type checking is selected, a pre-commit hook and GitHub actions workflow that perform the type checking are added. 

Basic type checking performs type checks but ignores code or imports for which type hints are not written. 

Strict type checking enforces type hints are used by giving errors where no type hints are found.


12. Example module code
-----------------------

   +------------+---------------------------------------------------------------+
   | Question   | Do you want to create some example module code?               |
   +------------+---------------------------------------------------------------+
   | Options    | **✱ yes**, no                                                 |
   +------------+---------------------------------------------------------------+

If this option is selected, the template will create an example module and test file::

    project_name/
    ├─ src/
    │  ├─ package_name/
    │  │  ├─ example_module.py
    ├─ tests/
    │  ├─ package_name/
    │  │  ├─ test_example_module.py
    ├─ ...


13. Sphinx and autoapi directory
--------------------------------

   +------------+------------------------------------------------------------------------+
   | Question   | Do you want to include a directory for sphinx, and autoapi generation? |
   +------------+------------------------------------------------------------------------+
   | Options    | **✱ yes**, no                                                          |
   +------------+------------------------------------------------------------------------+

See :doc:`../practices/sphinx`.

If this option is selected, any docstrings in your Python files will be turned into API documentation via Sphinx autodoc.

The template will create directories and configuration files to enable Sphinx document generation and ReadTheDocs integration::

    project_name/
    ├─ docs/
    │  ├─ conf.py
    │  ├─ index.rst
    │  ├─ Makefile
    │  ├─ requirements.txt
    |  ├─ ...
    ├─ readthedocs.yml
    ├─ ...


14. Rendered notebooks
----------------------

   +------------+------------------------------------------------------------------+
   | Question   | Do you want to include rendered notebooks in your documentation? |
   +------------+------------------------------------------------------------------+
   | Options    | yes, no *(defaults to choice for option 13)*                     |
   +------------+------------------------------------------------------------------+

The requirements to host rendered notebooks on your Read the Docs (or just build them locally) will be included in your project.

A sample notebook will be generated and added to your docs as an example.

.. Caution:: ReadTheDocs builds timeout after 30 minutes, which means all included notebooks must be able to render in that time frame.


15. Commandline Files
--------------------

   +------------+---------------------------------------------------------------+
   | Question   | Do you want to include commandline files for your project?    |
   +------------+---------------------------------------------------------------+
   | Options    | **✱ yes**, no                                                 |
   +------------+---------------------------------------------------------------+

The template will create directories and configuration files to enable commandline scripts::

    project_name/
    ├─ src/
    │  ├─ {package_name}_cli/
    │  │  ├─ __init__.py
    │  │  ├─ {package_name}_version.py

The commandline files are located under ``src/{package_name}_cli/`` and must be linked from the pyproject.toml to be installed as commandline scripts.


16. Developer Guide
-------------------

   +------------+--------------------------------------------------------------------------------+
   | Question   | Do you want to include a development guide markdown file for your repository?  |
   +------------+--------------------------------------------------------------------------------+
   | Options    | **✱ yes**, no                                                                  |
   +------------+--------------------------------------------------------------------------------+

Include a basic development guide for your repository, outlining guiding design principles, how to setup and run tests, and coding conventions. This document is meant to be read by both humans and AI agents to enable consistent contributions to the project. An AGENTS.md file is also created with default instructions for the agent to read the development guide.

    project_name/
    ├─ DEVELOPMENT_GUIDE.md
    ├─ AGENTS.md


17. Benchmarking
----------------

   +------------+-------------------------------------------------+
   | Question   | Do you want to enable benchmarking?             |
   +------------+-------------------------------------------------+
   | Options    | **✱ yes**, no                                   |
   +------------+-------------------------------------------------+

Enables benchmarking using `airspeed velocity (ASV) <https://asv.readthedocs.io/en/stable/>`_.

The template will add the GitHub workflows for continuous integration.

It will also create a sample benchmarking suite under ``benchmarks/``::

    project_name/
    ├─ benchmarks/
    │  ├─ benchmarks/
    │  │  ├─ benchmarks.py
    ├─ ...

Read more at :doc:`../practices/ci_benchmarking`.


18. Test against lowest versions
------------------------------------------------

   +------------+---------------------------------------------------------------+
   | Question   | Run pull request tests with the lowest versions of python     |
   |            | and dependencies?                                             |
   +------------+---------------------------------------------------------------+
   | Options    | | **(none)** Do not test with lowest versions of dependencies |
   |            | | (direct) Test with lowest versions of direct                |
   |            |   dependencies only (those listed in pyproject.toml)          |
   |            | | (all) Test with lowest versions of all dependencies         |
   +------------+---------------------------------------------------------------+

Adds an optional stage to the end of the testing and coverage github CI workflow
using the oldest version of python you've selected above, and will determine 
the oldest versions of dependencies indicated in the pyproject file.

A new environment has these dependencies installed, and we try to run the pytest
unit tests against these versions.

This can be useful if your project is a library, and folks may want to depend on 
you and your dependencies. Understanding the true range of versions you support
in your application can make dependency resolution much easier for your users!
