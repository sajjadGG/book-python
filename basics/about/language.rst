Python Language
===============
* Turing complete, general purpose language
* Multi platform
* Dynamic typing with automatic memory allocation and GC
* Code readability and simplicity is important
* White space are important
* Everything is an object, but you can write functional code too
* Standard language in Machine Learning and Data Science
* Very good standard system library
* Huge ecosystem of external open source libraries
* Open Source created by non-profit Python Software Foundation

.. figure:: img/python-logo.png

    Python Logo


Scripts
-------
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
    "``.pyz``", "`zipapp <https://docs.python.org/3/library/zipapp.html>`_ compressed archive"


Python Console (REPL)
---------------------
* Read–Eval–Print Loop
* Quickly test and evaluate code
* Lines starts with ``>>>``
* Line continuation starts with ``...``
* Result is printed below
* Open REPL with ``python3`` command in terminal

.. code-block:: console

    $ python3.10
    Python 3.10.0 (default, Oct 13 2021, 06:45:00) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    >>> print('Ehlo World!')
    Ehlo World!

In documentation and books you may find ``>>>`` and ``...`` at the beginning of code listing lines

>>> if True:
...     print('yes')
... else:
...     print('no')
yes


Jupyter
-------
* Open Source web application REPL
* Very popular in Machine Learning and Data Science world
* Create and share documents that contain live code, equations, visualizations
  and narrative text
* Uses include: data cleaning and transformation, numerical simulation,
  statistical modeling, data visualization, machine learning, etc


References
----------
.. [#pyDevGuideVersions] https://devguide.python.org/#status-of-python-branches


Assignments
-----------
.. literalinclude:: assignments/about_language_a.py
    :caption: :download:`Solution <assignments/about_language_a.py>`
    :end-before: # Solution
