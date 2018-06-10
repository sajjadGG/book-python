*********
Operatory
*********

Lista operatorów
================
.. csv-table:: Lista operatorów
    :header-rows: 1

    "Operand", "Description"
    "``%``", "modulo (reszta z dzielenia)"
    "``**``", "potęga"
    "``//``", "dzielenie bez reszty (ilość całkowitych)"
    "``+=``", "dodanie i przypisanie"
    "``<``", "mniejsze niż"
    "``<=``", "mniejsze lub równe"
    "``>``", "większe niż"
    "``>=``", "większe lub równe"
    "``==``", "równe"
    "``!=``", "różne"
    "``is``", "obiekty są tożsame (sprawdzanie czy ``None``)"
    "``is not``", "obiekty nie są tożsame (sprawdzanie czy nie ``None``)"
    "``in``", "obiekt jest w innym"
    "``not in``", "obiekt nie jest w innym"


Operacje na typach numerycznych
===============================
.. csv-table:: Lista operatorów
    :header-rows: 1

    "Operand", "Description"
    "``x + y``", "suma ``x`` i ``y``"
    "``x - y``", "różnica ``x`` i ``y``"
    "``x * y``", "iloczyn ``x`` i ``y``"
    "``x / y``", "iloraz ``x`` i ``y``"
    "``x // y``", "podłoga z ilorazu ``x`` i ``y``"
    "``x % y``", "reszta z dzielenia ``x / y``"
    "``-x``", ``x`` negacja"
    "``+x``", "``x`` bez zmiany"
    "``abs(x)``", "wartość bezwzględna ``x``"
    "``int(x)``", "``x`` przekonwertowane do ``int``"
    "``float(x)``", "``x`` przekonwertowane do ``float``"
    "``round(x, precyzja=0)``", "``x`` zaokrąglenie liczby z daną precyzją"
    "``complex(re, im)``", "liczba zespolona: ``re`` - część rzeczywista, ``im`` - część urojona"
    "``divmod(x, y)``", "para ``(x // y, x % y)``"
    "``pow(x, y)``", "``x`` podniesione do potęgi ``y``"
    "``x ** y``", "``x`` do potęgi ``y``"


Kolejność operatorów
====================
#. ``%``
#. ``//``, ``**``
#. ``=``, ``==``
#. ``+=``
#. ``in``, ``not in``

Bitwise
=======
- ``|`` - OR
- ``&`` - AND
- ``~`` - NOT
- ``^`` - XOR

.. code-block:: python

    >>> 0^0
    0
    >>> 1^1
    0
    >>> 1^0
    1
    >>> 0^1
    1
    >>> 8^5
    13


.. code-block:: text

    1000  # 8 (binary)
    0101  # 3 (binary)
    ----  # APPLY XOR ('vertically')
    1101  # result = 13 (dec)


Zadania kontrolne
=================

Parzystość
----------
#. napisz program, który wczyta od użytkownika ciąg znaków
#. zweryfikuje czy wprowadzony ciąg jest liczbą (``int`` lub ``float``)
#. sprawdzi czy jest to liczba parzysta, czy nieparzysta

:Podpowiedź:
    * Liczba parzysta, to taka, która po podzieleniu przez dwa nie ma reszty
    * Użyj dzielenia modulo ``%`` lub ``divmod()``
    * Zwróć uwagę, że operator ``%`` działa modulo tylko na ``int`` oraz na ``float``. Przy ``str`` ma zupełnie inne znaczenie.
    * .. code-block:: python

        if ... :
            print(True)
        else:
            print(False)

:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie
    * wykorzystanie operatorów matematycznych
    * sprawdzanie czy obiekt jest instancją klasy

Liczby całkowite
----------------
#. Napisz program, który wczyta od użytkownika liczbę i wyświetli informację, czy jest to liczba całkowita, czy niecałkowita.

:Podpowiedź:
    * Liczba całkowita to taka, której część dziesiętna nie występuje (``int``) lub jest równa zero ``float``. Możesz to sprawdzić dzieląc liczbę z resztą przez 1 i sprawdzając resztę z dzielenia.
    * Zwróć uywagę, że ``input()`` zawsze zwraca ``str`` wiec trzeba rzutowac na ``int``, ale wtedy tracimy informację czy wczesniej mielismy ``float`` oraz wyskakuje exception gdy podano inny niekompatybilny typ


:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie
    * sprawdzanie czy obiekt jest instancją klasy