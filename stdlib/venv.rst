**********
Virtualenv
**********



``venv`` Module
===============
* What is Virtualenv


Directory Naming Convention
===========================
* No standard

.. code-block:: text
    :caption: Those names are common, but don't have Python version

    venv/
    .venv/

    virtualenv/
    .virtualenv/

.. code-block:: text
    :caption: Those names has version, but lack of standard

    .virtualenv-3.6/
    .virtualenv-3.7/
    .virtualenv-3.8/

    venv-3.6/
    venv-3.7/
    venv-3.8/

    .venv-3.6/
    .venv-3.7/
    .venv-3.8/

.. code-block:: text
    :caption: This convention is from ``virtualenv-wrapper`` module

    ~/.virtualenv/PROJECT_NAME/

Create Virtualenv
=================
.. code-block:: console

    cd PROJECT_DIRECTORY
    python3.7 -m venv venv-3.7

Activate Virtualenv
===================

Windows
-------
.. code-block:: console

    cd PROJECT_DIRECTORY
    venv-3.7\Scripts\activate.bat

macOS, Linux, BSD
-----------------
.. code-block:: console

    cd PROJECT_DIRECTORY
    venv-3.7/bin/activate

Good practices
==============


Assignments
===========

Virtualenv
----------
* Lines of code to write: 0 lines
* Estimated time of completion: 2 min

#. Stwórz virtualenv z instalacją Python
#. Dodaj virtualenv do Python Interpreter w Twoim IDE
