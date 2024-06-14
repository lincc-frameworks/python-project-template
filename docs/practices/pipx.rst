pipx
====================================================================================================

``pipx`` is a tool to enable installation of end-user applications written 
in Python.
The main difference from ``pip`` is that any application installed with ``pip`` 
is only executable from an environment that ``pip`` installs it into, while 
``pipx`` makes the tool executable from any environment.

This means that ``pipx`` can install Python command line tools (such as Copier) 
so that they can be used from any virtual environment. 
Additionally, ``pipx`` installs these tools and their dependencies into 
isolated locations. 
Doing so avoids dependency version conflicts and makes uninstalling packages 
easy and safe.


How we use it
-------------

We use ``pipx`` to install Copier (the technology that powers our template) as 
a command line tool, so that we can call ``copier`` from any virtual environment.
Beyond that, we don't use ``pipx`` for anything else in the template.

In the :doc:`Getting Started <../source/overview>` section, we assume the use 
of ``pipx``. 
But you can use ``conda`` or ``pip`` if you'd rather have ``copier`` installed 
in a specific environment. 
We have not yet documented the differences to the getting started workflow that 
this would require.

How to install ``pipx``
-----------------------

There are a few different ways to install ``pipx`` depending on your operating 
system. 
Using ``conda`` to install ``pipx`` is probably easiest.
However, if you don't have ``conda`` already, take a look at the 
`pipx documentation <https://pypa.github.io/pipx/>`_ to find the 
installation process that is most straightforward for you system.

An example installation of ``pipx`` might look like this. 

.. code-block:: console
    
        >> conda install -c conda-forge pipx
        >> pipx ensurepath

.. important::
    Don't forget to run ``pipx ensurepath`` to finalize the installation.