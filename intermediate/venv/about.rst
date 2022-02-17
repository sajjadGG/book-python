Module VENV
===========



Rationale
---------
* Isolated Python environment
* Allows to have multiple versions of Python for one project
* For testing on different versions: ``py38``, ``py39``, ``py310``
* Test libraries and frameworks before upgrading (create venv, install requirements, run tests, delete if fails)
* Allows to have different versions of libraries and frameworks for each project
* Difference between ``venv`` and ``virtualenv``
* ``venv`` is bundled with Python since 3.3 (no installation required)
* ``virtualenv`` is independent package installed via ``pip``
* ``virtualenvwrapper`` is additionally installed command line tools


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


Activate
--------
* ``Scripts`` for Windows
* ``bin`` for macOS, Linux, BSD
* Note the direction of slash and backslash (OS dependent)

Windows:

.. code-block:: console

    $ cd PROJECT
    $ venv-py310\Scripts\activate.bat

macOS, Linux, BSD:

.. code-block:: console

    $ cd PROJECT
    $ source venv-py310/bin/activate


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

    venv-3.8/
    venv-3.9/
    venv-3.10/

    venv-3.10.0/
    venv-3.10.2/
    venv-3.10.2/
    venv-3.10.3/
    venv-3.10.4/
    venv-3.10.5/

    venv-3.11-alpha1/
    venv-3.11-alpha2/
    venv-3.11-beta1/
    venv-3.11-beta2/
    venv-3.11-rc1/

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

    venv-py310-dj33
    venv-python310-django33
    venv-python310-django40a1

This convention is from ``virtualenv-wrapper`` module (mostly used in Python 2):

.. code-block:: text

    ~/.virtualenv/PROJECT_NAME/


Good practices
--------------
* ``python3.10 -m venv -h``
* ``python3.10 -m venv --upgrade-deps venv-py310``
* name as version ``venv-3.10.0``
* place in your project directory and add folder to ``.gitignore`` (important!)
* otherwise place it in ``~/.virtualenv/``, but some meaningful name is required
* Append at the end of ``venv-3.10.0/bin/activate``:

    .. code-block:: bash

        project_name='My Project'

        red='\[\033[00;31m\]'
        green='\[\033[00;32m\]'
        blue='\[\033[00;36m\]'
        white='\[\033[00;39m\]'

        export PS1="\n${blue}${project_name}> ${white}"


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
