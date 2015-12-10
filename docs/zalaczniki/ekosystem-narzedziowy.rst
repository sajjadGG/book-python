********************
Ekosystem Narzędiowy
********************

Code Quality
============

``PEP8``
--------

:About:
    Python style guide checker. pep8 is a tool to check your Python code
    against some of the style conventions in PEP 8.

    * Plugin architecture: Adding new checks is easy.
    * Parseable output: Jump to error location in your editor.
    * Small: Just one Python file, requires only stdlib. You can use just the
    * pep8.py file for this purpose.
    * Comes with a comprehensive test suite.

:Installation:
    .. code:: bash

        pip install pep8
        pip install --upgrade pep8
        pip uninstall pep8

:Usage:
    .. code:: bash

        pep8 FILENAME.py
        pep8 DIRECTORY/
        pep8 --statistics -qq DIRECTORY/
        pep8 --show-source --show-pep8 FILENAME.py

:Config:
    ``setup.cfg``

    .. code:: ini

        [pep8]
        max-line-length = 939
        ignore = E402,W391

``SonarQube``
-------------

:About:
    SonarQube software (previously called Sonar) is an open source quality management platform, dedicated to continuously analyze and measure technical quality, from project portfolio to method.

:More information:
    * https://sonarqube.com
    * http://docs.sonarqube.org/display/SONAR/Documentation
    * https://sonarqube.com/dashboard/index?did=143
    * https://sonarqube.com/governance?id=662857


``Pylint``
----------

:About:
    Pylint is a Python source code analyzer which looks for programming errors, helps enforcing a coding standard and sniffs for some code smells (as defined in Martin Fowler’s Refactoring book). Pylint has many rules enabled by default, way too much to silence them all on a minimally sized program. It’s highly configurable and handle pragmas to control it from within your code. Additionally, it is possible to write plugins to add your own checks.

:Install:
    .. code:: bash

        pip install pylint
        pip install --upgrade pylint
        pip uninstall pylint

:Usage:
    .. code:: bash

        pylint DIRECTORY/
        pylint FILENAME.py

:More information:
    * https://pypi.python.org/pypi/pylint/


``Pyflakes``
------------

:About:
    A simple program which checks Python source files for errors. Pyflakes analyzes programs and detects various errors. It works by parsing the source file, not importing it, so it is safe to use on modules with side effects. It’s also much faster.

:Install:
    .. code:: shell

        pip install pyflakes
        pip install --upgrade pyflakes
        pip uninstall pyflakes

:Usage:
    .. code:: bash

        pyflakes DIRECTORY/
        python -m pyflakes DIRECTORY/

:More information:
    * https://pypi.python.org/pypi/pyflakes


``Coverage``
------------

:About:
    Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.

:Install:
    .. code:: bash

        pip install coverage
        pip install --upgrade coverage
        pip uninstall coverage

:Usage:
    .. code:: bash

        coverage run FILENAME.py
        coverage report -m

:More information:
    * https://pypi.python.org/pypi/coverage
    * https://coverage.readthedocs.io/


``unittest``
------------

:Usage:
    .. code:: bash

        python -m unittest FILENAME.py


Automation and Releases
=======================

Fabric
------

:Install:
    .. code:: bash

        pip install fabric
        pip install --upgrade fabric
        pip uninstall fabric

Testy Mutacyjne
===============

* https://pypi.python.org/pypi/MutPy

Transifex
=========

* https://www.transifex.com
