***********************
Development Environment
***********************


What is IDE?
============
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
==============
* Nie ma znaczenia z jakiego IDE skorzystasz!
* Do edycji skryptów Pythona wystarczy sam Notatnik lub Jupyter
* W miarę rośnięcia złożoności projektu oraz ilości plików przyda nam się coś co ułatwi nam pracę
* Dobre IDE pomoże Ci w refaktoringu, podpowiedziach typów, debuggingu oraz pracy z systemem kontroli wersji
* PyCharm ma dwie wersję płatną oraz darmową, wersja darmowa w zupełności nam wystarczy
* Ciekawą alternatywą może być PyDev - plugin do środowiska Eclipse


Which One is the Best?
======================
#. `PyCharm Professional <https://www.jetbrains.com/pycharm/download/>`_ (Not-free)
#. `PyCharm Community <https://www.jetbrains.com/pycharm/download/>`_
#. Jupyter Notebook
#. Visual Studio Code
#. `PyDev <http://www.pydev.org/download.html>`_
#. Spyder
#. Atom
#. Vim

.. note:: This are my preferences. Choosing best IDE is very opinionated.


Keyboard Shortcuts
==================
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
===========

.. todo:: Convert assignments to literalinclude

About IDE Usage
---------------
* Assignment: About IDE Usage
* Filename: None
* Complexity: easy
* Lines of code: 0 lines
* Time: 8 min

English:
    .. todo:: English Translation

Polish:
    1. Jak zrobić w Twoim IDE:

        a. Run...
        b. Run in console
        c. Debug...
        d. Python Console
        e. Terminal
        f. Full Screen
        g. Distraction Free Mode
        h. Reformat Code
        i. Scope

    2. Jakie są skróty klawiszowe do poszczególnych opcji?
    3. Czym się różni ``Run...`` od ``Debug...``?
    4. Czym się różni ``Python Console`` od ``Terminal``
    5. Czym się różni ``Distraction Free Mode`` od ``Full Screen``
    6. Ustaw Scope tak, aby ukryć katalog z Virtualenv

About IDE Spellchecker
----------------------
* Assignment: About IDE Spellchecker
* Filename: None
* Complexity: easy
* Lines of code: 0 lines
* Time: 5 min

English:
    .. todo:: English Translation

Polish:
    1. Zainstaluj w PyCharm plugin 'Hunspell' (File -> Settings -> Plugins -> Marketplace -> 'Hunspell')
    2. Pobierz z https://github.com/LibreOffice/dictionaries/tree/master/pl_PL słownik ``.dic`` oraz ``.aff`` dla języka polskiego

        a. https://raw.githubusercontent.com/LibreOffice/dictionaries/master/pl_PL/pl_PL.aff
        b. https://raw.githubusercontent.com/LibreOffice/dictionaries/master/pl_PL/pl_PL.dic

    3. Skonfiguruj IDE do korzystania z tego słownika (File -> Settings -> Editor -> Spelling -> Add custom dictionary)

