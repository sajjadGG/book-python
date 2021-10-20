Development Environment
=======================


What is IDE?
------------
* Integrated Development Environment
* Refactoring
* Syntax autocompletion and highlighting
* Type hinting and checking
* VCS support
* Virtualenv support
* Debugging
* Spell checking
* Running code and inspections
* File Scopes and views
* Database explorer
* Support for testing (doctest, unittest)
* Jump to line in exceptions


How to Choose?
--------------
Python is about the source code, so in the end, it doesn't matter which
IDE you choose. For editing plain source code you can also use Windows
Notepad or VIM. However the bigger your program grows, and the more files
it will contain, the harder it will be to maintain all that without proper
tool. Good IDE will help you in refactoring, type hinting, debugging and
working with Version Control System such as Git.

PyCharm has two versions: Community and Professional. For the regular
development Community version will be more then enough. Professional
version include better support for web-development (such as Java Script
debugger, support for Django, FastAPI, and some other frameworks too).
Database viewer is also available in paid version. Professional also better
equipped for Data Science and Machine Learning. However as I said before
you don't have to use all of that, because in the end the source code is
what matters.

There is also a free alternative PyDev plugin for Eclipse.


Which One is the Best?
----------------------
#. `PyCharm Professional <https://www.jetbrains.com/pycharm/download/>`_ (Not-free)
#. `PyCharm Community <https://www.jetbrains.com/pycharm/download/>`_
#. Jupyter Notebook
#. Visual Studio Code
#. `PyDev <http://www.pydev.org/download.html>`_
#. Spyder
#. Atom
#. Vim

This are my preferences. Choosing best IDE is very opinionated.


Keyboard Shortcuts
------------------
.. csv-table:: PyCharm Keyboard shortcuts
    :header-rows: 1
    :widths: 25, 75

    "Key Combination", "Action"
    "``ctrl`` + ``/``", "Comment multiple lines"
    "``alt`` + ``F12``", "Open Terminal"
    "``shift`` + ``F6``", "Refactor... Rename"
    "``tab``", "Indent (also used on multiple lines)"
    "``shift`` + ``tab``", "Un-indent (also used on multiple lines)"
    "``alt`` + ``1``", "Show file drawer"
    "", "Run"
    "", "Show console"
    "", "Actions"
    "``ctrl`` + ``g``", "Jump to line"
    "``ctrl`` + ``f``", "Search in file"
    "``ctrl`` + ``r``", "Replace in file"


Assignments
-----------
.. literalinclude:: assignments/about_ide_a.py
    :caption: :download:`Solution <assignments/about_ide_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/about_ide_b.py
    :caption: :download:`Solution <assignments/about_ide_b.py>`
    :end-before: # Solution
