***************
Python Language
***************


What is Python?
===============
.. figure:: img/python-logo.png
    :width: 75%
    :align: center

    Python Logo

Python as a Language
--------------------
* Turing complete, general purpose language
* Multi platform
* Dynamic typing with automatic memory allocation and GC
* Code readability and simplicity is important
* White space are important
* Everything is an object, but you can write functional code too

Python as a Community
---------------------
* Standard language in Machine Learning and Data Science
* Very good standard system library
* Huge ecosystem of external open source libraries
* Open Source created by non-profit Python Software Foundation


Which version?
==============
* newest Python 3

What changed in Python 3?
-------------------------
* All strings are Unicode
* Changes in standard library naming
* In Python 3 ``print()`` is a function, not a keyword
* New string formatting

Why not Python 2?
-----------------
* Python 2 is no longer developed after 2020-04-01 [`1 <https://www.python.org/psf/press-release/pr20191220/>`_, `2 <https://mail.python.org/archives/list/python-dev@python.org/message/N6JIGTTJCJHS47AYSI76SJPCQS25EBWR/>`_]
* Python 2.7 is the last in 2.x branch
* There won't be Python 2.8 :pep:`404`
* End of Life for Python 2.7 is 2020 :pep:`373`

Currently supported versions
----------------------------
.. csv-table::
    :header: "Version", "PEP", "Status", "Release", "End-of-life", "Release Manager"

    "3.10", "TBA",        "future",       "2020-10-05", "2025-10",     "TBA"
    "3.9",  ":pep:`596`", "development",  "2020-10-05", "2025-10",     "Łukasz Langa"
    "3.8",  ":pep:`569`", "features",     "2019-10-20", "2024-10",     "Łukasz Langa"
    "3.7",  ":pep:`537`", "bugfix",       "2018-06-27", "2023-06-27",  "Ned Deily"
    "3.6",  ":pep:`494`", "security",     "2016-12-23", "2021-12-23",  "Ned Deily"
    "3.5",  ":pep:`478`", "security",     "2015-09-13", "2020-09-13",  "Larry Hastings"
    "3.4",  ":pep:`429`", "end of life",  "2014-03-16", "2019-03-16",  "Larry Hastings"
    "3.3",  ":pep:`398`", "end of life",  "2012-09-29", "2017-09-29",  "Georg Brandl"
    "3.2",  ":pep:`392`", "end of life",  "2011-02-20", "2016-02-20",  "Georg Brandl"
    "3.1",  ":pep:`375`", "end of life",  "2009-06-27", "2012-04-09",  "Benjamin Peterson"
    "3.0",  ":pep:`361`", "end of life",  "2008-12-03", "2009-01-13",  "Barry Warsaw"
    "2.7",  ":pep:`373`", "bugfix",       "2010-07-03", "2020-04-01",  "Benjamin Peterson"
    "2.6",  ":pep:`361`", "end of life",  "2008-10-01", "2013-10-29",  "Barry Warsaw"


Release Cycle
=============
.. versionadded:: Python 3.9
    See :pep:`602`

* 12 months (1 year) release cycle
* 18 months (1.5 year) of bugfix updates
* 42 months (3.5 year) of security updates

.. figure:: img/pep602-release-calendar.png
    :width: 75%
    :align: center

    Python 12 months release cycle.


Scripts
=======

File types and extensions
-------------------------
* Python files use ``.py`` as an extension
* Compiled files are in ``__pycache__`` directory
* Python also uses other extensions

.. csv-table:: Python file types and extensions
    :header-rows: 1
    :widths: 15, 85

    "Extension", "Description"
    "``.pyc``", "Compiled source code (bytecode)"
    "``.pyd``", "Compiled Windows DLL file"
    "``.pyw``", "Compiled Windows file. Executable with ``pythonw.exe``"
    "``.pyx``", "cPythona source for C/C++ conversion"
    "``.pyz``", "`zipapp <https://docs.python.org/3/library/zipapp.html>`_ compressed archive. Since Python 3.5"


Minimal script
--------------
.. code-block:: python

    print('Ehlo World!')

Interpreter declaration
-----------------------
* Declare interpreter for standalone scripts ``#!/usr/bin/env python3``

.. code-block:: python

    #!/usr/bin/env python3

    print('Ehlo World!')

System environment variable ``PATH``
------------------------------------
* While installing Python, add its executable to one of system ``$PATH`` directories

System environment variable ``PYTHON_PATH``
-------------------------------------------
* Python search for libraries and modules in directories listed in system ``$PYTHON_PATH``
* ``$PYTHON_PATH`` is a base for ``sys.path``


Python Console (REPL)
=====================
* Read–Eval–Print Loop
* Quickly test and evaluate code
* Lines starts with ``>>>``
* Line continuation starts with ``...``
* Result is printed below
* Open REPL with ``python3`` command in terminal

.. code-block:: console

    $ python3
    Python 3.7.5 (default, Nov  1 2019, 02:16:23)
    [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Ehlo World!')
    Ehlo World!

.. note:: In documentation and books you may find ``>>>`` and ``...`` at the beginning of code listing lines

    .. code-block:: python

        >>> if True:
        ...     print('yes')
        ... else:
        ...     print('no')
        yes


Jupyter
=======
* Open Source web application REPL
* Very popular in Machine Learning and Data Science world
* Create and share documents that contain live code, equations, visualizations and narrative text
* Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, etc
