**********
Virtualenv
**********



``venv`` Module
===============
* What is Virtualenv
* Isolated Python installation for project
* Allows to have multiple versions of Python for one project (i.e. for testing)
* Allows to test libraries and frameworks before upgrading
* Allows to have different versions of libraries and frameworks for each project


Create Virtualenv
=================
.. code-block:: console

    cd PROJECT_DIRECTORY
    python3.7 -m venv venv-3.7.4

Directory Naming Convention
---------------------------
* No standard naming convention
* Naming per Python version
* Naming per main framework/library version

.. code-block:: text
    :caption: Naming directory like module name is a good idea
    :emphasize-lines: 1

    venv/
    virtualenv/

.. code-block:: text
    :caption: Dot at the beginning hides directory on Linux and macOS, but still, it's not a module name
    :emphasize-lines: 1

    venv/
    .venv/

.. code-block:: text
    :caption: Points to which Python version is installed, but no bugfix information
    :emphasize-lines: 2

    venv-3.6/
    venv-3.7/
    venv-3.8/

.. code-block:: text
    :caption: Explicitly states which Python version is installed (in my opinion the best solution)
    :emphasize-lines: 5

    venv-3.7.0/
    venv-3.7.1/
    venv-3.7.2/
    venv-3.7.3/
    venv-3.7.4/

    venv-3.8-beta1/
    venv-3.8-beta2/

.. code-block:: text
    :caption: You can specify version of the main framework/library used, but no Python version information
    :emphasize-lines: 2

    venv-django-2.1
    venv-django-2.2
    venv-django-3.0beta1
    venv-django-3.0beta2

.. code-block:: text
    :caption: You can specify Python version and version of the main framework/library used

    venv-py37-dj22
    venv-python37-django22
    venv-python38beta-django30beta

.. code-block:: text
    :caption: This convention is from ``virtualenv-wrapper`` module (mostly used in Python 2)

    ~/.virtualenv/PROJECT_NAME/


Activate Virtualenv
===================

Windows
-------
.. code-block:: console

    cd PROJECT_DIRECTORY
    venv-3.7.4\Scripts\activate.bat

macOS, Linux, BSD
-----------------
.. code-block:: console

    cd PROJECT_DIRECTORY
    venv-3.7.4/bin/activate


Good practices
==============
* name as version ``venv-3.7.4``
* place in your project directory
* add folder to ``.gitignore``


Assignments
===========

Virtualenv
----------
* Lines of code to write: 0 lines
* Estimated time of completion: 2 min

#. Stwórz virtualenv z instalacją Python
#. Dodaj virtualenv do Python Interpreter w Twoim IDE
