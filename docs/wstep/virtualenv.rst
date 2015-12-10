**********
Virtualenv
**********

Tworzenie wirtualnego środowiska
================================

Wraz z wersją Python 3.3 do języka został dodany ten genialny moduł. Aplikacja ta odpowiada na problem zarządzania zależnościami na Twojej maszynie. Dzięki użyciu Virtualenv (po włączeniu jako standard zwany ``pyvenv``. Mamy możliwość do tworzenia tzw. wirtualnych środowisk Pythona. Środowisko to zawiera w sobie plik wykonywalny języka oraz wszystkie potrzebne biblioteki wewnętrzne i zewnętrzne. Takie środowiska możemy tworzyć per projekt i nie musimy martwić się, że Projekt A wymaga np. Django w wersji 1.8 a Projekt B w 1.9.

Tworzenie takiego środowiska jest bardzo łatwe i szybkie:

.. code:: bash

    pyvenv .virtualenv

lub na Windowsie:

.. code:: bat

    python3 -m venv .virtualenv

Aktywacja i korzystanie ze środowiska
=====================================

I po chwili w pojawi się katalog .virtualenv ze środowiskiem. Następnie za każdym razem kiedy będziesz chciał pracować wykorzystując to środowisko będzie konieczna jego aktywacja:

.. code:: bash

    source .virtualenv/bin/activate

lub na Windowsie:

.. code:: bat

    .virtualenv\bin\activate.bat

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
