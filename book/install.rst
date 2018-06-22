**********
Instalacja
**********


Wymagania sprzętowe i systemowe
===============================
* można korzystać ze swojego komputera
* dowolny system operacyjny wspierany przez najnowszego Pythona


Wymagania oprogramowania
========================
* zainstalowany najnowszy oficjalny release Pythona (https://www.python.org/downloads/)
* zainstalowany PyCharm Professional EAP (https://www.jetbrains.com/pycharm/nextversion/)
* zaznaczaj domyślne opcje zarówno dla GIT i PyCharm

.. warning:: Jak będziesz instalował Python pamiętaj o zaznaczeniu opcji dodania do ``PATH``!

.. note:: Jeżeli szkolenie będzie również odnośnie korzystania z GIT

    * zainstalowany GIT (https://git-scm.com/download/)
    * założone darmowe konto na Github (proszę znać swój login)


Przygotowanie środowiska
========================

Windows
-------
* Zostawić domyślne opcje
* Dodać do ``PATH``
* Python uruchamia się z ``cmd``
* Znać ścieżkę do katalogu gdzie zainstalowany jest Python

macOS
----
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
* Polecenie ``which python`` ma zwracać ``/usr/bin/python3``

Linux
-----
* Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowanego Pythona.
* Aby zainstalować nowszą wersję użyj swojego managera pakietów:

    - ``apt-get`` - Debian, Ubuntu
    - ``yum`` - Suse
    - ``emerge`` - Gentoo
    - ``rpm`` - Redhat, Fedora

* Python uruchamia się z terminala
* Polecenie ``which python`` ma zwracać ``/usr/bin/python3``