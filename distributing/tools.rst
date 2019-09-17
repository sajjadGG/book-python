*****
Tools
*****


pyenv
=====
* pyenv lets you easily switch between multiple versions of Python
* pyenv intercepts Python commands using shim executables injected into your PATH, determines which Python version has been specified by your application, and passes your commands along to the correct Python installation.

When you execute a shim, pyenv determines which Python version to use by reading it from the following sources, in this order:

    #. The ``PYENV_VERSION`` environment variable (if specified)
    #. The application-specific ``.python-version`` file in the current directory (if present)
    #. The first ``.python-version`` file found (if any) by searching each parent directory, until reaching the root of your filesystem
    #. The global ``$(pyenv root)/version`` file.

If the global version file is not present, pyenv assumes you want to use the "system" Python

Each Python version is installed into its own directory under ``$(pyenv root)/versions``:

    * ``$(pyenv root)/versions/2.7.8/``
    * ``$(pyenv root)/versions/3.4.2/``
    * ``$(pyenv root)/versions/pypy-2.4.0/``

.. code-block:: console
    :caption: Installation

    curl https://pyenv.run | bash

.. code-block:: console
    :caption: Upgrade

    pyenv update


Cookiecutter
============
* template for a Python package

.. code-block:: console
    :caption: Installation

    pip install cookiecutter

Generate a Python package project:

.. code-block:: console

    cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git

#. Create a repo and put it there.
#. Add the repo to your Travis-CI account.
#. Install the dev requirements into a virtualenv. (pip install -r requirements_dev.txt)
#. Register your project with PyPI.
#. Run the Travis CLI command travis encrypt --add deploy.password to encrypt your PyPI password in Travis config and activate automated deployment on PyPI when you push a new tag to master branch.
#. Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
#. Release your package by pushing a new tag to master.
#. Add a requirements.txt file that specifies the packages you will need for your project and their versions. For more info see the pip docs for requirements files.
#. Activate your project on pyup.io.


pipenv
======
Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. Windows is a first-class citizen, in our world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important ``Pipfile.lock``, which is used to produce deterministic builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to setup a working environment. For the distinction between libraries and applications and the usage of ``setup.py`` vs ``Pipfile`` to define dependencies.

The problems that Pipenv seeks to solve are multi-faceted:

    #. You no longer need to use ``pip`` and ``virtualenv`` separately. They work together.
    #. Managing a ``requirements.txt`` file can be problematic, so Pipenv uses ``Pipfile`` and ``Pipfile.lock`` to separate abstract dependency declarations from the last tested combination.
    #. Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.
    #. Strongly encourage the use of the latest versions of dependencies to minimize security risks arising from outdated components.
    #. Give you insight into your dependency graph (e.g. ``pipenv graph``).
    #. Streamline development workflow by loading ``.env`` files.

.. code-block:: console
    :caption: Installation

    brew install pipenv


Conda
=====


