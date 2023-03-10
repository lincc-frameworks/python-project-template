PyPI
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

`PyPI <https://pypi.org/>`_ is a repository for packaged python software. When 
published via PyPI, a package can be installed on anyone's development environment
with ``pip`` or ``conda`` commands. 
PyPI makes versioning and sharing your software products easy.


How to manage
-------------------------------------------------------------------------------

Set-up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A GitHub workflow is included that will automatically publish the packaged work 
to PyPI when a new release is created. 
To support this, you'll need to configure your repository.

* Create and verify an account on PyPI - https://pypi.org/account/register/
* Create a PyPI API token - https://pypi.org/help/#apitoken
* Save the API token in your repository **as an "Action Secret"** following
  `these instructions <https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/managing-encrypted-secrets-for-your-repository-and-organization-for-github-codespaces#adding-secrets-for-a-repository>`_. 
  Save your secret API token with the name: ``PYPI_API_TOKEN``


Releasing new versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, when you 
`create a new release <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release>`_ 
from your repository, a workflow will run that will package and deploy the code to PyPI.