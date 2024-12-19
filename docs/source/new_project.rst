Create a new templated project
===============================================================================


Create a new project from the template
-------------------------------------------------------------------------------

Choose where you would like to create your new project, and call copier with 
the template.

.. important::
    This template is optimized to work well with Copier >= 9.1.0.

    ``pipx list`` will display the currently installed version of Copier.

.. code-block:: console

    >> copier copy gh:lincc-frameworks/python-project-template <new/project/directory>

Template questions
******************

Copier will ask you questions for how to set up the project. These questions 
will be used to fill in aspects of the project's configuration, including both 
metadata and parameters. Below we provide some high-level overview of the 
questions:

.. list-table::
   :header-rows: 1

   * - **Question**
     - **Notes**
   * - *Would you like to use simple (default tooling) or customized installation?*
     - If a simple install is used, the template automatically selects the recommended 
       tooling options (linter, isort, and create example module). 
   * - *What is the name of your project?*
     - The name of your project. If you distribute your code via PyPI, this is the name 
       that will be used. This will allow users to pip install like so: ``pip install <project_name>``. 
       The project name must start with a lowercase letter, followed by one or more of the 
       following (a-z, 0-9, _, -).
   * - *What is your python package name?*
     - The name of your top level package. Specifies the location of the source 
       code (``src/{{package_name}}``). The package name must start with a lowercase letter, 
       followed by one or more of the following (a-z, 0-9, _).
   * - *What github organization will your project live under?*
     - This will either be a github organization, or your github username, if you're working outside 
       of an organization. This is used to construct URLs to your project, like
       ``https://github.com/{{project_organization}}/{{project_name}}``
   * - *What is the name of the code author?* 
     - The name of the code's author, or the organization that is responsible for the code.
       This will be used in the project and documentation metadata. 
       This name will also be included as part of the copyright license.
   * - *Your preferred email address?*
     - The contact email for the code's author. This will be used in the project and documentation metadata.
   * - *What license would you like to use?*
     - The license type you want to use for this project. Options are MIT and BSD. For more information on these options see 
       `Github's license page <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository>`_.
   * - *What versions of python are you targeting?*
     - Select all versions of python that you are targeting for execution. We will add automated testing
       for all of these versions. 
   * - *What tooling set would you like to use to enforce code style?*
     - See :doc:`/practices/linting`. 
       We provide several compatible options for linters and autoformatters.
       Choosing a formatter or linter will include it as a project dependency and include it in the
       :doc:`pre-commit <../practices/precommit>` hooks.
       Defaults to ``ruff`` (linting and autoformatting) during simple installation. 
   * - *How would you like to receive workflow failure notifications?*
     - See :doc:`/practices/ci_testing`. 
       Some github workflows are not loud about their failures, so we have some configuration
       for sending alerts to you or your team.
   * - *Would you like to include mypy to perform static type checking for type hints?*
     - `mypy <https://www.mypy-lang.org>`_ performs static type checking on python code that uses 
       `type hints <https://docs.python.org/3/library/typing.html>`_. This type checking makes sure that the 
       correct data types are being used where type hints are defined. If basic or strict type checking is 
       selected, a pre-commit hook and GitHub actions workflow that perform the type checking are added. 
       Basic type checking performs type checks but ignores code or imports for which type hints are not written. 
       Strict type checking enforces type hints are used by giving errors where no type hints are found.
   * - *Do you want to create some example module code?*
     - If this option is selected the template will create an example module 
       ``src/{{package_name}}/example_module.py`` and test file 
       ``tests/{{package_name}}/test_example_module.py``. Defaults to ``True`` during simple installation.
   * - *Do you want to include a directory for sphinx, and autoapi generation?*
     - If this option is selected the template will create directories and configuration files
       to enable Sphinx document generation and ReadTheDocs integration. Any docstrings in your 
       python files will be turned into API documentation.
   * - *Do you want to include rendered notebooks in your documentation?*
     - The requirements to host rendered notebooks on your Read the Docs (or just build them locally) will 
       be included in your project. A sample notebook will be generated and added to your docs as an example.
   * - *Do you want to enable benchmarking?*
     - Answering `Yes` enables benchmarking using 
       `airspeed velocity (ASV) <https://asv.readthedocs.io/en/stable/>`_. The template will add the GitHub 
       workflows for continuous integration and create a sample benchmarking suite under 
       ``benchmarks/benchmarks/benchmarks.py``. Defaults to ``True`` during simple installation.

While these choices will provide the initial structure for your project, most 
can be changed later. 
See Copier's `documentation for changing answers to the question <https://copier.readthedocs.io/en/stable/updating/>`_.

After providing answers to the prompts, Copier will hydrate a project template 
and save it in the directory you specified.

Create and activate a new environment
--------------------------------------

.. note::
    This step is optional, but we recommend using virtual environments to better 
    manage different project's dependencies. 
    See Python's `description of virtual environments <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>`_ 
    for more details.

If you are using `virtual environments <https://packaging.python.org/en/latest/glossary/#term-Virtual-Environment>`_ 
create a new environment with your choice of environment tools (virtualenv, 
conda, etc.) and activate it.

Prepare your project
---------------------

Once your virtual environment has been created and activated run the following
script in your new project directory.

.. code-block:: console

    >> bash .initialize_new_project.sh

This script will initialize your local git repository, install the new Python
package in editable mode along with runtime and developer dependencies, and
initialize :doc:`pre-commit <../practices/precommit>`.

.. important::
    The script ends by creating a first commit to the initial branch with the template files.
    If you added other files to the repository before running the script they will be subject
    to the pre-commit hooks checks. If they are not compliant the bash script will exit
    with a verbose error code. You should apply the suggestions and re-run the script.

The full contents of the script can be seen on `Github <https://github.com/lincc-frameworks/python-project-template/tree/main/python-project-template/.initialize_new_project.sh>`_.

The script assumes that you have access to bash. If that is not true for your environment,
you should be able to run all the commands manually in your environment using
your available shell.

.. tip::
  Projects using Python notebooks will need to have ``pandoc`` installed to 
  convert notebooks to html locally.
  Pandoc is `available on conda-forge <https://github.com/conda-forge/pandoc-feedstock>`_, 
  so conda can be a convenient way to keep these dependencies grouped together.

Commit your new project locally
-------------------------------------------------------------------------------

Commit the project to your local version control like so to see the pre-commit 
checks run.

.. code-block:: console

    >> git add .
    >> git commit -m 'Initial commit'

Push your work to GitHub
-------------------------------------------------------------------------------

Create a new repository in GitHub: (`GitHub How-to <https://docs.github.com/en/get-started/quickstart/create-a-repo>`_)

.. code-block:: console

    >> git remote add origin https://github.com/<the_remote_project>/<the_remote_repository>
    >> git push origin <local_branch_name>

Notice that when you create a PR in GitHub, a set of tests for Continuous 
Integration starts up to verify that the project can build successfully and 
that all the unit tests pass. Neato!

Next steps
-------------------------------------------------------------------------------

:doc:`Configure a new project<configuration_checklist>`
