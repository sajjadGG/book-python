**********
Instalacja
**********

Wymagania szkolenia
===================
- założone darmowe konto na Github (proszę znać swój login)
- można korzystać ze swojego komputera
- dowolny system operacyjny wspierany przez Python 3.6.5
- ściągnięty, niezainstalowany Python 3.6.5 (https://www.python.org/downloads/release/python-365/)
- ściągnięty, niezainstalowany najnowszy PyCharm Community (https://www.jetbrains.com/pycharm/download/)
- ściągnięty, niezainstalowany GIT (https://git-scm.com/download/win)

.. warning:: powyższe rzeczy mają być ściągnięte, ale nie zainstalowane!


Instalacja
==========

Windows
-------
- Zainstalować GIT (zostawić domyślne opcje)
- Zainstalować


OS X
----
Jeżeli posiadasz OS X to Python powinien być domyślnie zainstalowany na Twoim komputerze. Apple w najnowszych systemach operacyjnych standardowo dostarcza Pythona w wersji 2.7 i 2.6. Domyślnie po wpisaniu polecenia ``python`` uruchamiany jest 2.7. Aby zainstalować Pythona w wersji 3 możemy skorzystać z managera pakietów ``brew`` albo z tzw. macports. Osobiście polecam to pierwsze podejście. Brew dostępny jest za darmo i można pobrać go z internetu uruchamiając polecenie ze strony `Brew <http://brew.sh>`_. Najpierw jednak konieczne będzie zainstalowanie najnowszej wersji Xcode z AppStore. Brew powinien zrobić to za Ciebie.

Sama instalacja brew sprowadza do uruchomienia polecenia wyglądającego jak następujące:

.. code-block:: console

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Następnie po instalacji:

.. code-block:: console

    $ brew install python3

I już możemy cieszyć się najnowszym Pythonem.


Linux
-----
Niemalże wszystkie dystrybucje Linuxa posiadają zainstalowaną wersję Pythona w wersji 2. Aby zainstalować trójkę użyj swojego managera pakietów ``apt-get``, ``yum`` czy ``emerge`` czy ``rpm`` w zależności od dystrybucji.

PATH
====

PYTHON_PATH
===========
