Module VENV
===========
* Isolated Python environment
* Allows to have multiple versions of Python for one project
* For testing on different versions: ``py38``, ``py39``, ``py310``
* Test libraries and frameworks before upgrading (create venv, install requirements, run tests, delete if fails)
* Allows to have different versions of libraries and frameworks for each project
* Difference between ``venv`` and ``virtualenv``
* ``venv`` is bundled with Python since 3.3 (no installation required)
* ``virtualenv`` is independent package installed via ``pip``
* ``virtualenvwrapper`` is additionally installed command line tools


Venv vs Virtualenv
------------------
Both ``venv`` and ``virtualenv`` are used to create isolated
Python environments.

Since Python 3.3, a subset of ``virtualenv`` has been integrated into
the standard library under the ``venv`` module.

Module ``venv``:

    * Python: version 3 only
    * Install: not required - bundled with Python since Python 3.3
    * Usage: ``python3.10 -m venv DIRECTORY``
    * Development: slower and synchronized with Python releases
    * Features: all you need
    * Author: Bernat Gabor

Module ``virtualenv``:

    * Python: version 2 and 3
    * Install: ``pip install virtualenv``
    * Usage: ``virtualenv DIRECTORY``
    * Development: faster and independent from Python releases
    * Features: all from ``venv`` plus extra (which typically you don't need)
    * Author: Bernat Gabor

In my opinion builtin ``venv`` is all you need. Moreover no installation
is required to use it.


Create
------
* ``DIRECTORY`` is the name of venv folder (see "Directory Naming Convention" below)

.. code-block:: console

    $ cd PROJECT
    $ python3.10 -m venv DIRECTORY

Example:

.. code-block:: console

    $ cd PROJECT
    $ python3.10 -m venv venv-py310


Run Ad-Hoc
----------
* Will run python with from virtual environment
* With all the modules already installed

.. code-block:: console

    $ cd PROJECT
    $ venv-py310/bin/python3 myscript.py


Activate
--------
* ``bin`` for macOS, Linux, BSD
* ``Scripts`` for Windows
* Note the direction of slash and backslash (OS dependent)

macOS, Linux, BSD:

.. code-block:: console

    $ cd PROJECT
    $ source venv-py310/bin/activate

Windows:

.. code-block:: console

    $ cd PROJECT
    $ venv-py310\Scripts\activate.bat


Install Modules
---------------
Ad-hoc:

.. code-block:: console

    $ cd PROJECT

    # Install new module
    $ venv-py310/bin/python3 -m pip install MODULE

    # Install modules listed in `requirements.txt`
    $ venv-py310/bin/python3 -m pip install -r requirements.txt

    # Upgrade modules listed in `requirements.txt`
    $ venv-py310/bin/python3 -m pip install --upgrade -r requirements.txt

    # Check installed modules
    $ venv-py310/bin/python3 -m pip freeze

Activated:

.. code-block:: console

    $ cd PROJECT
    $ source venv-py310/bin/activate

    # Install new module
    $ python3 -m pip install MODULE

    # Install modules listed in `requirements.txt`
    $ python3 -m pip install -r requirements.txt

    # Upgrade modules listed in `requirements.txt`
    $ python3 -m pip pip install --upgrade -r requirements.txt

    # Check installed modules
    $ python3 -m pip freeze


Directory Naming Convention
---------------------------
* No standard naming convention
* Naming directory like module (``venv``) name is a good idea
* Adding Python version is also a good practice
* Optionally naming per main framework/library version
* Dot at the beginning hides directory on Linux and macOS (but doesn't work on Windows)
* Underscore is Python convention for private/protected, but does not work for OS and Git

.. code-block:: text

    venv/
    .venv/
    _venv/

    virtualenv/
    .virtualenv/
    _virtualenv/

    venv-py
    .venv-py

    py-3.10
    python-3.10
    python-3.10.0

    .py-3.10
    .python-3.10
    .python-3.10.0

    venv-py3.8/
    venv-py3.9/
    venv-py3.10/

    venv-py3.10.0/
    venv-py3.10.1/
    venv-py3.10.2/
    venv-py3.10.3/
    venv-py3.10.4/
    venv-py3.10.5/
    venv-py3.10.6/
    venv-py3.10.7/

    venv-py3.11-alpha1/
    venv-py3.11-alpha2/
    venv-py3.11-beta1/
    venv-py3.11-beta2/
    venv-py3.11-rc1/

    venv-django-3.0
    venv-django-3.1
    venv-django-3.2
    venv-django-4.0
    venv-django-4.1
    venv-django-4.2
    venv-django-5.0a1
    venv-django-5.0a2
    venv-django-5.0b1
    venv-django-5.0b2
    venv-django-5.0rc1
    venv-django-5.0rc2

    venv-py310-dj32
    venv-py310-dj40
    venv-py310-dj41a1
    venv-py310-dj41b1
    venv-py310-dj41rc1

    venv-python310-django32
    venv-python310-django40
    venv-python310-django41a1
    venv-python310-django41b1
    venv-python310-django41rc1

This convention is from ``virtualenv-wrapper`` module
(mostly used in Python 2):

.. code-block:: text

    ~/.venv-py3.10/PROJECT_NAME/


Good Practices
--------------
* ``python3.10 -m venv -h``
* ``python3.10 -m venv --upgrade-deps venv-py310``
* name as version ``venv-3.10``
* place in your project directory and add folder to ``.gitignore`` (important!)
* otherwise place it in ``~/.virtualenv/``, but some meaningful name is required
* Append at the end of ``venv-3.10/bin/activate``:

``bash`` (Linux):

.. code-block:: bash

    project_name='My Project'

    red='\[\033[00;31m\]'
    green='\[\033[00;32m\]'
    blue='\[\033[00;36m\]'
    white='\[\033[00;39m\]'

    export PS1="\n${blue}${project_name}> ${white}"

``zsh`` (macOS):

.. code-block:: zsh

    export PS1=$'\n%F{blue}project_name> %F{white}'


Further Reading
---------------
* https://github.com/pypa/virtualenv/issues/2007


Assignments
-----------
.. todo:: Convert assignments to literalinclude

Virtualenv
^^^^^^^^^^
* Assignment: Virtualenv
* Complexity: easy
* Lines of code: 0 lines
* Time: 2 min

English:
    1. Create ``venv``
    2. Add ``venv`` as a Python interpreter in your IDE
    3. Run doctests - all must succeed

Polish:
    1. Stwórz ``venv``
    2. Dodaj ``venv`` jako interpreter Python w Twoim IDE
    3. Uruchom doctesty - wszystkie muszą się powieść
