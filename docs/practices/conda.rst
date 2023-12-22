Conda
===============================================================================

What is it? Why do it?
-------------------------------------------------------------------------------

Conda is a package manager.

It's pretty special because it works across whatever language you're using, in
whatever platform you're using. 

See also packaging with :doc:`pypi`.

How to manage
-------------------------------------------------------------------------------

Set-up
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Conda requires the version information to be contained in the bundled source tree.
We include a file in the root-level of the project directory - ``.git_archival.txt`` -
that ``setuptools_scm`` knows how to hydrate. This is triggered in git via a line
in the ``.gitattributes`` file. You shouldn't need to change anything in your
main project repo.

There is some initial set-up that requires human intervention.
Read `conda's instructions for adding packages <https://conda-forge.org/docs/maintainer/adding_pkgs.html>`_.

You will want to fork `staged-recipes <https://github.com/conda-forge/staged-recipes/>`_
and add your "recipe" to a subdirectory in ``staged-recipes/recipes``.
You will send this off as a PR to the conda-forge team and 
once approved, your recipe will be moved to a "feedstock" repo of its own.

Releasing new versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will 
`create a new release <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release>`_ 
from your repository as normal.

conda-forge periodically looks at your source repo for any new releases/tags, 
tries to build a new release, and pre-generates the PR (against your "feedstock"
repo created above) to publish the new version of the package.