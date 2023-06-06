Getting Started
===============================================================================

This project template codifies LINCC Framework's best practices for python code 
organization, testing, documentation, and automation.
It is meant to help python projects get started quickly and allow the user 
to focus on writing code. 

We built this tool with a few assumptions in mind.
The following are **not** considered requirements to use the template.
However, some of the included tooling may not work as expected if your project 
doesn't follow these guidelines.

1. Your project is mostly Python based.
2. GitHub will be used as a remote repository.
3. Your remote repository will be publicly available.

We have seen the template used successfully in projects that don't adhere to 
these guidelines. But if you meet these guidelines, you'll be guaranteed to get 
the full benefit of the template.

.. _prerequisites:

Prerequisites
--------------

To use our template you'll need to install 
`Copier <https://copier.readthedocs.io/en/latest/>`_. 
Copier is an open source tool that hydrates projects from templates and 
natively supports updating projects as the original template matures. 
It's really neat!

.. important::
    Copier has two requirements and one recommended tool:

    1. Python > 3.7 (required)
    2. Git > 2.27 (required)
    3. pipx (recommended - more info about pipx :doc:`here<../practices/pipx>`)

    You can check your requirements like so:

    .. code-block:: bash

        >> python --version
            Python 3.10.9

        >> git --version
            git version 2.34.1

        >> which pipx
            /usr/bin/pipx

Given that your system satisfies the requirements, go ahead and install Copier.

.. important::
    A new version of Copier was released June 4, 2023. Please ensure that your
    installed version of Copier >= 8.0.0.

    ``pipx list`` will display installed the currently install version of Copier.

.. code-block:: bash

    >> pipx install --force copier>8.0.0

Now choose your next adventure...
-------------------------------------
* :doc:`Start a new project<new_project>`
* :doc:`Upgrade an existing project<existing_project>`