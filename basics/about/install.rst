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
* Można korzystać ze swojego komputera
* Dowolny system operacyjny wspierany przez Python
* Zainstalowane najnowsze oficjalne wydanie Python 3.7 (https://www.python.org/downloads/)
* Posiadać uprawnienia na komputerze do instalacji pakietów Python za pomocą ``pip``
* Dostęp do internetu

.. warning:: Na chwilę obecną jest problem z uruchomieniem ``Jupyter Notebook`` na Python 3.8 na systemie Windows. Ma to związek ze zmianami w API biblioteki ``asyncio`` wykorzystywanej przez serwer ``Tornado``, na którym uruchamia się ``Jupyter``. Jeżeli szkolenie będzie z Machine Learning lub analizy numerycznej to zalecam najnowszą wersję gałęzi **Python 3.7**. Więcej szczegółów na https://stackoverflow.com/questions/58422817/jupyter-notebook-with-python-3-8-notimplementederror


Python Installation
===================

Windows
-------
* Pozostaw domyślne opcje
* Dodaj do ``PATH`` (ważne! - inaczej nie uruchomi się w trybie poleceń ``cmd``)

.. note:: Jeżeli zainstalujesz Python, ale nie zaznaczysz aby dodać go do ``PATH``, plik wykonywalny możesz znaleźć w ``C:\Users\%User_name%\AppData\Local\Programs\Python\Python_version\Scripts\``

macOS
-----
* Pobierz i zainstaluj najnowszą wersję Pythona z oficjalnej strony internetowej (https://www.python.org/downloads/)
* Alternatywnie użyj ``brew install python3`` - (opis instalacji brew: https://brew.sh)

Linux
-----
* Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowanego Pythona.
* Pobierz i zainstaluj najnowszą wersję Pythona z oficjalnej strony internetowej (https://www.python.org/downloads/)
* Alternatywnie zainstaluj używając managera pakietów dla dystrybucji z której korzystasz:

    * ``apt`` - Debian, Ubuntu
    * ``snap`` - Ubuntu
    * ``yum`` - SuSe
    * ``emerge`` - Gentoo
    * ``rpm`` - RedHat, Fedora


Verification
============
#. Wykonaj w terminalu ``python3 --version`` - sprawdzanie wersji Python
#. Wykonaj w terminalu ``pip3 --version`` - sprawdzanie wersji managera pakietów ``pip``
#. Wykonaj w terminalu ``python3`` - weryfikacja uruchomienia interpretera Python

System environment variable ``PATH``
------------------------------------
* While installing Python, add its executable to one of system ``$PATH`` directories

System environment variable ``PYTHON_PATH``
-------------------------------------------
* Python search for libraries and modules in directories listed in system ``$PYTHON_PATH``
* ``$PYTHON_PATH`` is a base for ``sys.path``


IDE Installation
================

Szkolenie z programowania w Python
----------------------------------
#. Pobierz i zainstaluj najnowszy PyCharm Community (https://www.jetbrains.com/pycharm/download/)
#. Zaznaczaj domyślne opcje dla PyCharm
#. Pamiętaj aby powiązać z plikami ``.py``

Szkolenie z Analizy Numerycznej lub Machine Learning
----------------------------------------------------
#. ``pip3 install jupyter``
