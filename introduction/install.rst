.. _Install:

*****************
Installing Python
*****************


System Requirements
===================
* Można korzystać ze swojego komputera
* Dowolny system operacyjny wspierany przez najnowszego Pythona
* Zainstalowane najnowsze oficjalne wydanie Pythona (https://www.python.org/downloads/)
* Zainstalowany najnowszy PyCharm Professional EAP (https://www.jetbrains.com/pycharm/nextversion/)
* Jeżeli szkolenie będzie również dotyczyło współpracy z wykorzystaniem Git:

    * zainstalowany Git (https://git-scm.com/download/)
    * założone darmowe konto na Github (proszę znać swój login)


Setting-up Environment
======================

Windows
-------
* Zostawić domyślne opcje
* Dodać do ``PATH`` (ważne!)
* Python uruchamia się z ``cmd``
* Znać ścieżkę do katalogu gdzie zainstalowany jest Python
* Zaznaczaj domyślne opcje zarówno dla Git i PyCharm (pamiętaj aby powiązać z plikami ``.py``)
* zweryfikować za pomocą polecenia ``python --version``

.. note:: Gdybyś miał zainstalowanego Pythona, ale nie dodałeś go do ``PATH``, plik wykonywalny możesz znaleźć w ``C:\Users\%User_name%\AppData\Local\Programs\Python\Python_version\Scripts\``


macOS
-----
* macOS powinien mieć już zainstalowanego Pythona
* Możesz zainstalować najnowszą wersję Pythona z oficjalnej strony internetowej
* Alternatywnie możesz użyć ``brew`` (darmowy manager pakietów)
* Uprzednio konieczne będzie zainstalowanie najnowszej wersji Xcode z AppStore, Brew powinien zrobić to za Ciebie
* Instalacja brew sprowadza się do uruchomienia polecenia:

    .. code-block:: console

        $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

* Następnie po instalacji:

    .. code-block:: console

        $ brew install python3

* Python uruchamia się z terminala
* Zweryfikować za pomocą polecenia ``python --version``

Linux
-----
* Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowanego Pythona.
* Aby zainstalować nowszą wersję użyj swojego managera pakietów:

    - ``apt-get`` - Debian, Ubuntu
    - ``yum`` - Suse
    - ``emerge`` - Gentoo
    - ``rpm`` - Redhat, Fedora

* Python uruchamia się z terminala
* Zweryfikować za pomocą polecenia ``python --version``
