*********************
About Python Language
*********************


What is Python?
===============
* Turing complete, general purpose language
* Lingua franca in Machine Learning and Data Science
* Dynamic typing with automatic memory allocation and GC
* Batteries included (standard system library)
* Code readability and simplicity is important
* White space are important
* Everything is an Object, but you can write functional code too
* Multi platform
* Open Source created by non-profit Python Software Foundation


Which version?
==============
* newest Python 3


What changed?
=============

Python 3
--------
* All strings are Unicode
* Changes in standard library naming
* In Python 3 ``print()`` is a function, not a keyword

Python 2
--------
* Python 2 is no longer developed and stopped on 2.7, End of Life 2020 (`PEP 373 <https://legacy.python.org/dev/peps/pep-0373/>`_)
* There won't be Python 2.8 (`PEP 404 <https://legacy.python.org/dev/peps/pep-0404/>`_)


File types and extensions
=========================
* Pliki źródłowe języka Python mają rozszerzenie ``.py``.
* Podczas wytwarzania oprogramowania spotkasz się jeszcze z kilkoma innymi rozszerzeniami.
* Mogą to być:

    .. csv-table:: Python file types and extensions
        :header-rows: 1
        :file: data/extensions.csv

Scripts
=======
Ta metoda przydaje nam się gdy nasze programy zaczną rosnąć na więcej niż jedną dwie linijki.
Warto zwrócić uwagę na pierwszą linię, na tzw. shebang ``#!`` i następujące po nim polecenie.
To jest deklaracja programu, którego kod źródłowy znajduje się poniżej.
Linijka ta jest opcjonalna, ale dla zachowania poprawności i warto w naszych skryptach coś takiego zadeklarować.
Już po pierwszej linii widzimy, że skrypt będzie zinterpretowany jako kod źródłowy trzeciej wersji Pythona.

.. code-block:: python

    #!/usr/bin/env python3

    print('Ehlo World!')

Wynik uruchomienia powyższego skryptu będzie identyczny z efektem uzyskanym w REPL, tzn, na naszym ekranie ukaże się napis ``Ehlo World``.
Dla wszystkich, którzy potrzebują wiedzieć jak wygląda najmniejszy kod, który wyświetli nam te słowa polecam poniższy kod.

.. code-block:: python

    print('Ehlo World!')

Interpreter declaration
-----------------------
Jest to specjalny rodzaj komentarza który opisaliśmy pokrótce powyżej. Ten typ komentarza występuje tylko w pierwszej linii programu i definiuje interpreter kodu źródłowego dla kodu poniżej.

.. code-block:: bash

    #!/usr/bin/env python3

PATH
----

PYTHON_PATH
-----------


Read–Eval–Print Loop
====================
Python spopularyzował wykorzystanie tzw. interpretera REPL (read–eval–print loop). REPL to interaktywny interpreter poleceń wykonujący wyrażenia z języka (zwykle linie), których wyniki są wyświetlane użytkownikowi natychmiast po ich wykonaniu. W uproszczeniu można powiedzieć, że REPL jest to linia poleceń programu ``python``. Znakiem zachęty do wprowadzania tekstu takiego programu są trzy znaki większości ``>>>``. Polecenia wpisane po tych znaczkach są interpretowane i natychmiast wykonywane. Ich wynik przedstawiany jest w następnej linijce. Jeżeli wykorzystamy konstrukcję, która wymaga więcej niż jednej linii, każda kolejna linijka będzie poprzedzona trzema kropkami ``...``. Przykłady takiej interakcji zobaczymy przy omawianiu "Hello World".

Rozwiązanie REPL idealnie pasuje do szybkiego testowania składni oraz funkcjonalności programów i bibliotek. Dzięki REPL jesteśmy w stanie przeprowadzić interaktywną sesję z linią poleceń a po przetestowaniu rozwiązania wkleić działające linie do naszego skryptu. Taki styl znacząco przyspiesza development i debugging.

Uproszczoną implementację takiego rozwiązania można przedstawić w następujący sposób:

.. code-block:: python

    while True:
        command = raw_input('>>> ')
        output = eval(command)
        print(output)

W dalszej części omówimy poszczególne elementy, które są tu wymienione.

Skrypty czy programy tego typu nie mają na celu pokazania jak minimalną ilością znaków da się wyświetlić coś na ekranie, a sposób interakcji i przepływu programista-komputer.
W Pythonie mamy możliwość wykorzystania interpretera REPL, przykład poniżej oraz stworzenia skryptu, który wykonamy z linii poleceń.

.. code-block:: console

    $ python

    Python 3.6.0 (default, Dec 24 2016, 08:01:42)
    [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Ehlo World!')
    Ehlo World!

Zwróć uwagę na wersję Pythona.
Jeżeli po wpisaniu polecenia ``python`` uruchomi się wersja 2.x, możesz spróbować polecenia ``python3``

Powyższy przykład ilustruje moment wpisania polecenia ``python``.
Standardowy tekst informujący o wersji i kompilacji języka oraz znak zachęty ``>>>`` (ang. prompt).
Polecenia wpisujemy po tym znaku a ich wynik wyświetla się poniżej (i nie zawiera wcięcia).
Dalej w materiałach będziemy posługiwali się już samym znakiem zachęty.


Jupyter
=======
The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.
