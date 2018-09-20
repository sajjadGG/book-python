****************************************
IDE - Integrated Development Environment
****************************************


What is IDE?
============
* Refactoring
* Syntax helping and highlighting
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


How to choose?
==============
* Nie ma znaczenia z jakiego IDE skorzystasz!
* Do edycji skryptów Pythona wystarczy sam Notatnik lub Jupyter
* W miarę rośnięcia złożoności projektu oraz ilości plików przyda nam się coś co ułatwi nam pracę
* Dobre IDE pomoże Ci w Refactoringu, podpowiedziach typów, debuggingu oraz pracy z systemem kontroli wersji
* PyCharm ma dwie wersję płatną oraz darmową, wersja darmowa w zupełności nam wystarczy
* Ciekawą alternatywą może być PyDev - plugin do środowiska Eclipse


Which one is the best?
======================
#. PyCharm Professional EAP
#. PyCharm Community
#. PyCharm Professional
#. PyDev

* https://www.jetbrains.com/pycharm/download/
* http://www.pydev.org/download.html


Assignments
===========

Create Project
--------------
#. Stwórz projekt w Twoim IDE
#. Jeżeli prowadzący podał Ci link do repozytorium GIT, to:

    * wykorzystaj opcję 'Create from VCS'
    * stwórz plik ``.gitignore``
    * wpisz linię ``.idea/`` do pliku

#. Jeżeli nie było podanego linku do repozytorium, to:

    * to stwórz projekt w języku Python

#. Po stworzeniu projektu, załóż katalog o nazwie jak twoje nazwisko i imie (np. ``nazwisko_imie``)
#. WAŻNE: Już do końca książki w nim będą tworzone rozwiązania do wszystkich zadań

Check Environment
-----------------
#. Stwórz skrypt o nazwie wypisanej w sekcji "About"
#. Plik ma mieć zawartość:

    .. code-block:: python

        import sys
        import os

        print(f'Version: {sys.version}')
        print(f'Installation: {sys.executable}')
        print(f'Virtualenv: {os.getenv("VIRTUAL_ENV")}')

#. Uruchom go w swoim IDE (menu ``Run -> Run... -> nazwa Twojego skryptu``)
#. Jaka wersja Python jest zainstalowana?
#. Gdzie Python jest zainstalowany?
#. Czy korzystasz z "Virtualenv"?
#. Upewnij się, że w linijce z "Virtualenv" nie masz ``None``

:About:
    * Filename: ``python_version.py``
    * Lines of code to write: 0 lines
    * Estimated time of completion: 5 min

:The whys and wherefores:
    * Czy Python działa
    * Jaka jest wersja Python
    * Czy korzystasz z Virtualenv
    * Korzystanie z print
    * Umiejętność uruchamiania skryptów
    * Szukanie rozwiązań zadań z książki

Know thou IDE
-------------
#. Jak zrobić w Twoim IDE:

    * Run...
    * Run in console
    * Debug...
    * Python Console
    * Terminal
    * Full Screen
    * Distraction Free Mode
    * Reformat Code
    * Scope

#. Jakie są skróty klawiszowe do poszczególnych opcji?
#. Czym się różni ``Run...`` od ``Debug...```?
#. Czym się różni ``Python Console`` od ``Terminal``
#. Czym się różni ``Distraction Free Mode`` od ``Full Screen``
#. Ustaw Scope tak, aby ukryć katalog z Virtualenv

:About:
    * Lines of code to write: 0 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Korzystanie z IDE
    * Uruchamianie debuggera
    * Znajomość różnicy między uruchamianiem i debuggingiem
    * Znajomość różnicy między terminalem i konsolą

Keyboard shortcuts
------------------
.. csv-table:: Keyboard shortcuts
    :header-rows: 1

    "Key Combination", "Action"
    "``ctrl+/``", "Comment multiple lines"
#. Indent, unindent
#. Run
#. Show terminal
#. Show console
#. Actions
#. Show file drawer

Spellchecker
------------
#. Zainstaluj plugin 'Hunspell'
#. Pobierz z https://github.com/LibreOffice/dictionaries słownik ``.dic`` oraz ``.aff`` dla języka polskiego
#. Skonfiguruj IDE do korzystania z tego słownika

:About:
    * Lines of code to write: 0 lines
    * Estimated time of completion: 3 min

:The whys and wherefores:
    * Korzystanie z IDE
    * Konfiguracja IDE
