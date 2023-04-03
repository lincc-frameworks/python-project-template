Get Started
===============================================================================

This project template codifies LINCC-Framework's best practices for python code organization, testing, documentation, and automation.
It is meant to help new python projects get started quickly, letting the user focus on writing code.
The template takes care of the minutia of directory structures, tool configurations, and automated testing until the user is ready to take over.

`Copier <https://copier.readthedocs.io/en/latest/>`_  is required to use this template. 
Copier is an open source tool that hydrates projects from templates and natively supports updating projects as the original template matures. 
It's really neat!

.. _prerequisites:

Prerequisites
-------------------------------------------------------------------------------
These prerequisites for Copier are defined `here <https://copier.readthedocs.io/en/latest/#installation>`_ 
but summarized below.

1. Python > 3.7
2. Git > 2.27
3. Pipx (recommended - pip and conda work too, but require a different work flow)

.. tip:: 
    You check your prerequisite versions as shown below

    .. code-block:: bash

        >> python --version
            Python 3.10.9

        >> git --version
            git version 2.34.1

        >> which pipx
            /usr/bin/pipx

.. note::
    ``pipx`` is a tool to enable installation of end-user applications written in Python. The main difference
    from ``pip`` is that any tool (such as copier in the next section) installed with pip is only executable from an
    environment that ``pip`` installs it into, while ``pipx`` makes the tool executable from any environment.

    While we will assume the use of ``pipx`` in this documentation, be aware that you are able to use 
    ``conda`` or ``pip`` if you'd rather have it installed just in one environment.

    Please be aware that ``pipx ensurepath`` should be run after installing ``pipx``, as shown below

    .. code-block:: bash
    
        >> conda install -c conda-forge pipx
        >> pipx ensurepath

    For more information about ``pipx`` see the `documentation <https://pypa.github.io/pipx/>`_.


Install Copier
-------------------------------------------------------------------------------

Given that you have all the prerequisites satisfied, go ahead and install Copier.

.. code-block:: bash

    >> pipx install copier

Now you can either create a new project, or use the template configuration in an existing project.
Choose your next adventure...


Next Steps
-------------------------------------------------------------------------------

* :doc:`new_project`
* :doc:`existing_project`