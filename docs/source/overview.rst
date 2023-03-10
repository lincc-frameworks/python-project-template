Get Started
===============================================================================

What is this?
-------------------------------------------------------------------------------

This project template codifies LINCC-Framework's best practices for python code organization, testing, documentation, and automation. It is meant to help new python projects get started quickly, letting the user focus on writing code. The template takes care of the minutia of directory structures, tool configurations, and automated testing until the user is ready to take over.

`Copier <https://copier.readthedocs.io/en/latest/>`_  is required to use this template. Copier is an open source tool that hydrates projects from templates and natively supports updating projects as the original template matures. It's really neat!


Prerequisites
-------------------------------------------------------------------------------
These prerequisites for Copier are defined `here <https://copier.readthedocs.io/en/latest/#installation>`_.

1. Python > 3.7
2. Git > 2.27
3. ``pipx`` (nice to have, conda and pip work too, but can be more difficult to reason about later)

.. note::
    ``pipx`` is a tool to enable installation of end-user applications written in Python. The main difference
    from ``pip`` is that any tool (such as copier below) installed with pip is only executable from the conda
    environment that ``pip`` installs it into, while ``pipx`` makes the tool executable from any environment.

    While we will assume the use of ``pipx`` in this documentation, be aware that you are able to use 
    ``conda`` or ``pip`` if you'd rather have it installed just in one environment.

    For ``pipx`` installation, please be aware that ``pipx ensurepath`` should be run after install, shown 
    here:

    .. code-block:: bash
    
        >> conda install -c conda-forge pipx
        >> pipx ensurepath

.. code-block:: bash

   >> python --version
   Python 3.10.9

   >> git --version
   git version 2.34.1

   >> which pipx
   /usr/bin/pipx



Install Copier
-------------------------------------------------------------------------------

Given that you have all the prerequisites satisfied, go ahead and install Copier.

.. code-block:: bash

    >> pipx install copier

Now you can either create a new project, or use the template configuration in an existing project:


Next Steps
-------------------------------------------------------------------------------

* :doc:`new_project`
* :doc:`existing_project`