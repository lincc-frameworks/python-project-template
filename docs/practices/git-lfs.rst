Git Large File Support
===============================================================================

Quick Start
-------------------------------------------------------------------------------

After cloning a repository and connecting to the resulting working tree confirm 
that you have ``git-lfs`` and then issue ``git lfs install`` to install 
configuration and hooks and then ``git lfs track`` to designate targets for git-lfs.

.. code-block:: bash

    git-lfs --version
    git lfs install --local
    git lfs track '*.fits' '*.fits.fz' '*.gz'


.. list-table::
  :header-rows: 1

  * - **Common Problems**
    - **Resolution**
  * - git-lfs: command not found
    - Install git-lfs, see :ref:`get-git-lfs-label`
  * - git: 'lfs' is not a git command
    - Install git-lfs, see :ref:`get-git-lfs-label`

What is it? Why do it?
-------------------------------------------------------------------------------

`Git-lfs <https://git-lfs.com/>`_ replaces large files such as datasets, and 
graphics with text pointers inside Git, while storing the file contents on a remote server.
This can be very useful for projects that have large data files that change 
infrequently. 
It does require a remote that supports git-lfs and so if you are unsure about
whether you want to use git-lfs you probably do not want to use it until you 
understand it better.

This template provides a starting point for using git-lfs with a project.
Note that you need to install the program ``git-lfs`` separately as that is not 
easily done as part of the installation. See :ref:`get-git-lfs-label`.

How to manage
-------------------------------------------------------------------------------

.. _get-git-lfs-label:

Get git-lfs
^^^^^^^^^^^

The preferred installation instructions are at `Git-lfs <https://git-lfs.com/>`_.
That site will show you instructions most appropriate for your platform.

You may also use conda as it has a ``git-lfs`` package appropriately named.

.. code-block:: bash

    conda install git-lfs

At this time it is not available using ``pip``  or ``pipx``.
Note that while there is a pip package named ``git-lfs`` it does not in fact contain
``git-lfs``. Please do not use it.

Install git-lfs in the local repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once you have git-lfs use it to install support into the repository with the command

.. code-block:: bash

    git lfs install --local

The option ``--local`` is necessary only if you want to avoid modifications to .gitconfig in
your home directory. Quite likely you do not care and so may omit the option. Note that you must
run the command for each repository requiring git-lfs support and you must run it after each
clone because it installs hooks in .git/hooks.

You will need to use a remote that supports git-lfs. Git-hub, the default for LINCC Frameworks,
and several other git servers do support git-lfs. If you use another remote you should check.

Designate files for git-lfs tracking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You will also want add paths to ``.gitattributes`` that designate the files git-lfs will manage for git.
While you can edit ``.gitattributes`` directly there is a command that will make 
the needed changes and create the file if necessary.
For example, if you want to specify that ``FITS`` files are handled by git-lfs 
then you might use these commands

.. code-block:: bash

    git lfs track '*.fits' '*.fits.fz'

You can see a list of currently tracked names

.. code-block:: bash

    git lfs track

See ``Getting Started`` at `Git-lfs <https://git-lfs.com/>`_ for more details.

We also recommend you review `Using Git LFS-enabled repositories <https://developer.lsst.io/git/git-lfs.html#using-git-lfs-enabled-repositories>`_
in the lsst developer documentation and adapt its recommendations to your project.

Uninstall git-lfs from the repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to stop using git-lfs going forward then you can uninstall it. 
You should use the same options used on installation, in particular if you 
specified the ``--local`` option you should also specify it here. 
Probably it is safer to always include the ``--local`` option so you restrict 
impact to the current repository.

.. code-block:: bash

    git lfs uninstall --local

Any files modified after uninstalling git-lfs will become part of the regular 
git repository but the git-lfs artifacts will remain.

Note that we recommend against uninstalling git-lfs as it causes confusion.

You can see what files are controlled by git-lfs using the ``git lfs ls-files`` command

.. code-block:: bash

    git lfs ls-files

Then if you want to copy them to the regular git repository you can change their 
modification dates using ``touch`` and commit the changes.



