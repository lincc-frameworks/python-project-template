Python namespace project
========================

`Pep 420 <https://peps.python.org/pep-0420/>`_ defines a standard for namespace packages. This standard allows for separately versioned and maintained subpackages to present under a single top level package name.
While the organization name *should* be globally unique to the python community the subpackage names are not so restricted.

For example the following code uses a namespace **acme** to contain two separately maintained projects **acme-supernovae** that uses a package name supernovae and **acme-utilities** that uses a package name utilities.

.. code-block:: python

    from acme.supernovae import orbits
    from acme.utilities import fits, wcs

A python project template created project can be converted to a `pep 420 <https://peps.python.org/pep-0420/>`_ compliant namespace package with a few steps.
The example provided here is for a new project but the procedure can be applied to existing projects that have not strayed signficiantly from the template file structure.

Synopsis
--------

#. Choose an organization namespace shared by all related packages. For example **acme**.
#. Rename the **src** directory to the organization name **acme**.
#. Replace references to **src** with references to **acme**.
#. Add a clause to pyproject.toml to declare this as a namespace package.
#. Change import statements to reflect the namespace package.
#. Test

Example
-------

Follow the instructions at :doc:`New Project <../source/new_project>` to create a new project named **acme-supernovae** with a package named **supernovae**.

.. code-block:: bash

    copier copy gh:lincc-frameworks/python-project-template acme-supernovae
    cd acme-supernovae
    git init --initial-branch=main
    git add README.md && git commit -m 'initial commit'
    git checkout -b acme/main
    mv src acme
    git add . && git commit -m 'initial branch commit'

Change references to directory **src** to **acme** in all files. This part of the example might break over time
as code changes and other uses of **src** are confused by the sed expression.

Define bash functions to find the files containing **src** and to perform the change using sed so first add the shell functions.

.. code-block:: bash

    organization=acme
    subpackage=supernovae
    project=acme-supernovae
    myfiles1() { find . -name .git -prune -o -type f -print | xargs -r grep -l src; }
    mysed1() { sed -e '/^_src_path/!s%src%'"${organization}"'%g;' "${1}" >.tmpfile && mv "${1}" .oldfile && mv .tmpfile "${1}" && rm .oldfile; }
    myfiles() { find . -name .git -prune -o -type f -print | xargs -r grep -l src; }
    for i in $(myfiles1); do
        mysed1 "${i}"
    done

It is wise to review the changes before committing them.

.. code-block:: bash

    git diff

Assuming all is good

.. code-block:: bash

    git add .
    git commit -m "finished move from src to ${organization}"

Add a clause to pyproject.toml to declare this as a namespace package. Again, you might want to
review the results before committing. At least take a look so you see what it added.

.. code-block:: bash

    tr '|' '\n' <<<'|[tool.setuptools.packages.find]|where = ["."]|include = ["'"${organization}"'"]|namespaces = true' >>pyproject.toml
    git add .
    git commit -m "finished conversion to namespace ${organization}"

All code that imports the package must be changed to reflect that
the package is now a namespace package. This is done by adding a clause to the import statement.

This might be the trickiest bit although for a brand new project it does very little.

.. code-block:: bash

    myfiles2() { find . -name .git -prune -o -type f \( -name '*.py' -o -name '*.ipynb' \) -print; }
    mysed2() { sed -e "/import/s%${subpackage}%${organization}.${subpackage}%g;" "${1}" >.tmpfile && mv "${1}" .oldfile && mv .tmpfile "${1}" && rm .oldfile; }
    for i in $(myfiles2); do
        mysed2 "${i}"
    done
    git diff
    git add .
    git commit -m "finished conversion if import statements to include ${organization}"

Build the project and install. We recommend that you do this in a virtual environment.
In this example we build for '.[dev]' and also run the pre-commit hooks as a verification step.

.. code-block:: bash

    pip install -e '.[dev]'
    pre-commit run --all-files

Create a new project named **acme-utilities** with a package named **utilities** and convert it to a namespace package
using exactly the same process as above but with different names.  Then install and check with pre-commit hooks.

.. code-block:: bash

    cd ..
    copier copy gh:lincc-frameworks/python-project-template acme-utilities
    cd acme-utilities
    git init --initial-branch=main
    git add README.md && git commit -m 'initial commit'
    git checkout -b acme/main
    mv src acme
    git add . && git commit -m 'initial branch commit'

    organization=acme
    subpackage=utilities
    project=acme-utilities
    myfiles1() { find . -name .git -prune -o -type f -print | xargs -r grep -l src; }
    mysed1() { sed -e '/^_src_path/!s%src%'"${organization}"'%g;' "${1}" >.tmpfile && mv "${1}" .oldfile && mv .tmpfile "${1}" && rm .oldfile; }
    myfiles() { find . -name .git -prune -o -type f -print | xargs -r grep -l src; }
    for i in $(myfiles1); do
        mysed1 "${i}"
    done

    git diff

    git add .
    git commit -m "finished move from src to ${organization}"
    tr '|' '\n' <<<'|[tool.setuptools.packages.find]|where = ["."]|include = ["'"${organization}"'"]|namespaces = true' >>pyproject.toml
    git add .
    git commit -m "finished conversion to namespace ${organization}"
    myfiles2() { find . -name .git -prune -o -type f \( -name '*.py' -o -name '*.ipynb' \) -print; }
    mysed2() { sed -e "/import/s%${subpackage}%${organization}.${subpackage}%g;" "${1}" >.tmpfile && mv "${1}" .oldfile && mv .tmpfile "${1}" && rm .oldfile; }
    for i in $(myfiles2); do
        mysed2 "${i}"
    done
    git diff
    git add .
    git commit -m "finished conversion if import statements to include ${organization}"
    pip install -e '.[dev]'
    pre-commit run --all-files
    cd ..

Try it out.  In this example we use the python interpreter to import the subpackages and run the examples.

.. code-block:: bash

    $ python
    >>> from acme import supernovae, utilities
    >>> supernovae.greetings()
    'Hello from LINCC-Frameworks!'
    >>> utilities.greetings()
    'Hello from LINCC-Frameworks!'
    >>> utilities.meaning()
    42
    >>> exit()

You might want to uninstall the packages to avoid python environment bloat!

.. code-block:: bash

    pip uninstall acme-supernovae acme-utilities
