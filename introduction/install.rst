.. _Install:

*****************
Installing Python
*****************


System Requirements
===================

Szkolenie z programowania w Python
----------------------------------
* Można korzystać ze swojego komputera
* Dowolny system operacyjny wspierany przez Python
* Zainstalowane najnowsze oficjalne wydanie Python (https://www.python.org/downloads/)
* Zainstalowany najnowszy PyCharm Community (https://www.jetbrains.com/pycharm/download/)
* Posiadać uprawnienia na komputerze do instalacji pakietów Python za pomocą ``pip``
* Dostęp do internetu
* Jeżeli szkolenie będzie również dotyczyło współpracy z wykorzystaniem Git:

    * zainstalowany Git (https://git-scm.com/download/)
    * założone darmowe konto na Github (proszę znać swój login)

Szkolenie z Analizy Numerycznej lub Machine Learning
----------------------------------------------------
.. warning:: Na chwilę obecną jest problem z uruchomieniem ``Jupyter Notebook`` na Python 3.8 na systemie Windows. Ma to związek ze zmianami w API biblioteki ``asyncio`` wykorzystywanej przez serwer ``Tornado``, na którym uruchamia się ``Jupyter``. Jeżeli szkolenie będzie z Machine Learning lub analizy numerycznej to zalecam najnowszą wersję gałęzi **Python 3.7**. Więcej szczegółów na https://stackoverflow.com/questions/58422817/jupyter-notebook-with-python-3-8-notimplementederror

* Można korzystać ze swojego komputera
* Dowolny system operacyjny wspierany przez Python
* Zainstalowane najnowsze oficjalne wydanie Python 3.7 (https://www.python.org/downloads/)
* Posiadać uprawnienia na komputerze do instalacji pakietów Python za pomocą ``pip``
* Dostęp do internetu


Setting-up Environment
======================

Windows
-------
#. Instalacja Python:

    * Pozostaw domyślne opcje
    * Dodaj do ``PATH`` (ważne! - inaczej nie uruchomi się w trybie poleceń ``cmd``)

#. Weryfikacja instalacji (wykonaj polecenia w terminalu ``cmd``):

    * ``python3 --version`` - sprawdzanie wersji Python
    * ``pip3 --version`` - sprawdzanie wersji managera pakietów ``pip``
    * ``python3`` - weryfikacja uruchomienia interpretera Python

#. Instalacja PyCharm:

    * Pobierz i zainstaluj najnowszy PyCharm Community (https://www.jetbrains.com/pycharm/download/)
    * Zaznaczaj domyślne opcje dla PyCharm
    * pamiętaj aby powiązać z plikami ``.py``

.. note:: Jeżeli zainstalujesz Python, ale nie zaznaczysz aby dodać go do ``PATH``, plik wykonywalny możesz znaleźć w ``C:\Users\%User_name%\AppData\Local\Programs\Python\Python_version\Scripts\``

macOS
-----
#. Instalacja Python:

    * Pobierz i zainstaluj najnowszą wersję Pythona z oficjalnej strony internetowej (https://www.python.org/downloads/)
    * Alternatywnie użyj ``brew install python3`` - (opis instalacji brew: https://brew.sh)

#. Weryfikacja instalacji (wykonaj polecenia w terminalu ``Terminal.app``):

    * ``python3 --version`` - sprawdzanie wersji Python
    * ``pip3 --version`` - sprawdzanie wersji managera pakietów ``pip``
    * ``python3`` - weryfikacja uruchomienia interpretera Python

#. Instalacja PyCharm:

    * Pobierz i zainstaluj najnowszy PyCharm Community (https://www.jetbrains.com/pycharm/download/)

Linux
-----
#. Instalacja Python:

    * Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowanego Pythona.
    * Pobierz i zainstaluj najnowszą wersję Pythona z oficjalnej strony internetowej (https://www.python.org/downloads/)
    * Alternatywnie zainstaluj używając managera pakietów dla dystrybucji z której korzystasz:

        * ``apt`` - Debian, Ubuntu
        * ``snap`` - Ubuntu
        * ``yum`` - Suse
        * ``emerge`` - Gentoo
        * ``rpm`` - Redhat, Fedora

#. Weryfikacja instalacji (wykonaj polecenia w terminalu):

    * ``python3 --version`` - sprawdzanie wersji Python
    * ``pip3 --version`` - sprawdzanie wersji managera pakietów ``pip``
    * ``python3`` - weryfikacja uruchomienia interpretera Python

#. Instalacja PyCharm:

    * Pobierz i zainstaluj najnowszy PyCharm Community (https://www.jetbrains.com/pycharm/download/)


Assignments
===========

Check Python Version
--------------------
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 1 min

#. Uruchom terminal i wpisz ``python3``
#. Po uruchomieniu interpretera wpisz następujące linijki kodu:

    .. code-block:: python

        import sys

        print(sys.version)

#. Jaka wersja Python jest zainstalowana?

:The whys and wherefores:
    * Czy Python działa
    * Jaka jest wersja Python
    * Korzystanie z print
