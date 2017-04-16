**********
Virtualenv
**********

Tworzenie wirtualnego środowiska
================================

Wraz z wersją Python 3.3 do języka został dodany ten genialny moduł. Aplikacja ta odpowiada na problem zarządzania zależnościami na Twojej maszynie. Dzięki użyciu Virtualenv (po włączeniu jako standard zwany ``venv``. Mamy możliwość do tworzenia tzw. wirtualnych środowisk Pythona. Środowisko to zawiera w sobie plik wykonywalny języka oraz wszystkie potrzebne biblioteki wewnętrzne i zewnętrzne. Takie środowiska możemy tworzyć per projekt i nie musimy martwić się, że Projekt A wymaga np. Django w wersji 1.10 a Projekt B w 1.11.

Tworzenie takiego środowiska jest bardzo łatwe i szybkie:

.. code:: bash

    python3 -m venv .virtualenv

Aktywacja i korzystanie ze środowiska
=====================================

I po chwili w pojawi się katalog .virtualenv ze środowiskiem. Następnie za każdym razem kiedy będziesz chciał pracować wykorzystując to środowisko będzie konieczna jego aktywacja:

.. code:: bash

    source .virtualenv/bin/activate

lub na Windowsie:

.. code:: bat

    .virtualenv\bin\activate.bat

Dobra praktyka
==============

Dobrą praktyką jest trzymanie wirtualnych środowisk w jednym katalogu, np. ``~/.virtualenvs/``, dzięki temu łatwo będzie wyłączyć ten katalog z tworzenia kopii zapasowych w systemie (ang. backup).

Tworząc nowe środowisko nazwij je tak jak projekt, np. ``python3 -m venv ~/.virtualenvs/moj-projekt``.

Polecam dodać poniższe linijki do ``~/.virtualenvs/moj-projekt/bin/activate``:

.. code-block:: bash

    project_name='Moj projekt'

    red='\[\033[00;31m\]'
    green='\[\033[00;32m\]'
    blue='\[\033[00;36m\]'
    white='\[\033[00;39m\]'

    export PS1="\n${blue}${project_name}> ${white}"

Dodaj poniższą linikję do ``~/.profile``:

.. code-block:: bash

    alias work='source ~/.virtualenvs/$(basename $PWD)/bin/activate'

Później aby aktywować środowisko wystarczy przejść do katalogu z projektem i wpisać w terminalu:

.. code-block:: bash

    $ work

To powinno automatycznie uruchomić virtualenv i załadować wszystkie zależności.


Pakiety i zależności
====================

Instalacja pakietów
-------------------

Każda instalacja pakietów oraz bibliotek wykona się w środowisku. Skrypt który uruchomisz wykorzysta właśnie te wersje, które masz w nim zainstalowane.

Aby zainstalować jakieś nowe paczki należy użyć polecenia ``pip``. Od wersji Python 3.4 ``pip`` jest zainstalowany domyślnie.

.. code:: bash

    pip install pep8

lub na Windows:

.. code:: bat

    python -m pip install pep8

Lista zainstalowanych paczek
----------------------------

Aby zobaczyć zainstalowane paczki, użyj polecenia ``pip freeze``. Przekierowując wynik tego polecenia do pliku ``requirements.txt`` stworzysz listę zależności wraz z wersjami, które są niezbędne dla uruchomienia Twojego programu.

.. code:: bash

    pip freeze > requirements.txt

lub na Windows:

.. code:: bat

    python -m pip install pep8

Więcej na temat instalowania paczek, modularyzacji itp. znajdziesz w rozdziale tej książki poświęconym temu tematowi.
