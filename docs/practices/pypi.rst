PyPI Publishing
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

`PyPI <https://pypi.org/>`_ is a repository for packaged python software. When 
published via PyPI, a package can be installed on anyone's development environment
with ``pip`` or ``conda`` commands. 
PyPI makes versioning and sharing your software products easy.

See also packaging with :doc:`conda`.

How to manage
-------------------------------------------------------------------------------

Set-up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A GitHub workflow is included that will automatically publish the packaged work 
to PyPI when a new release is created. 
To support this, you'll need to configure your repository.

* Create and verify an account on PyPI - https://pypi.org/account/register/
* Create a new PyPI trusted publisher using the appropriate instructions

  * For previously unpublished packages: https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/
  * For existing published packaged: https://docs.pypi.org/trusted-publishers/adding-a-publisher/

* When configuring your trusted publisher

  * Set the value of "Workflow name" to "publish-to-pypi.yml".
  * Leave the value of "Environment name" blank.


Releasing new versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now, when you 
`create a new release <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release>`_ 
from your repository, a workflow will run that will package and deploy the code to PyPI.