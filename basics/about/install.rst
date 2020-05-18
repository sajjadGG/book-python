.. _Install:

*****************
Installing Python
*****************


System Requirements
===================
#. Można korzystać ze swojego komputera i dowolnego systemu operacyjnego
#. Zainstalowane najnowsze stabilne oficjalne wydanie Python (https://www.python.org/downloads/)
#. Posiadać uprawnienia na komputerze do instalacji pakietów Python za pomocą ``pip``
#. Dostęp do internetu (zapewniany przez organizatora szkolenia)
#. Jeżeli szkolenie będzie również dotyczyło współpracy z wykorzystaniem Git:

    * zainstalowany Git (https://git-scm.com/download/)
    * założone darmowe konto na Github (proszę znać swój login)

#. Dla szkolenia z podstaw programowania w Python

    #. Pobierz i zainstaluj najnowszy PyCharm Community (https://www.jetbrains.com/pycharm/download/)
    #. Zaznaczaj domyślne opcje dla PyCharm
    #. Pamiętaj aby powiązać z plikami ``.py``

#. Dla szkolenia z Analizy Numerycznej lub Machine Learning

    #. Zainstalować: ``pip3 install --upgrade jupyter numpy pandas matplotlib``


Python Installation on Windows
==============================
* Pozostaw domyślne opcje
* Dodaj do ``PATH`` (ważne! - inaczej nie uruchomi się w trybie poleceń ``cmd``)
* Uwaga: Jeżeli zainstalujesz Python, ale nie zaznaczysz aby dodać go do ``PATH``, plik wykonywalny możesz znaleźć w ``C:\Users\%User_name%\AppData\Local\Programs\Python\Python_version\Scripts\``


Python Installation on macOS
============================
* Pobierz i zainstaluj najnowszą wersję Pythona z oficjalnej strony internetowej (https://www.python.org/downloads/)
* Alternatywnie użyj ``brew install python3`` - (opis instalacji brew: https://brew.sh)


Python Installation on Linux
============================
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
