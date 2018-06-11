*********
Operatory
*********

Lista operatorów
================
.. csv-table:: Lista operatorów
    :header-rows: 1

    "Operand", "Description"
    "``+=``", "dodanie i przypisanie"
    "``<``", "mniejsze niż"
    "``<=``", "mniejsze lub równe"
    "``>``", "większe niż"
    "``>=``", "większe lub równe"
    "``==``", "równe"
    "``!=``", "różne"
    "``in``", "obiekt jest w innym"
    "``not in``", "obiekt nie jest w innym"
    "``is``", "obiekty są tożsame (sprawdzanie czy ``None``)"
    "``is not``", "obiekty nie są tożsame (sprawdzanie czy nie ``None``)"


Operacje na typach numerycznych
===============================
.. csv-table:: Lista operatorów
    :header-rows: 1

    "Operand", "Description"
    "``-x``", ``x`` negacja"
    "``+x``", "``x`` bez zmiany"
    "``x + y``", "suma ``x`` i ``y``"
    "``x - y``", "różnica ``x`` i ``y``"
    "``x * y``", "iloczyn ``x`` i ``y``"
    "``x / y``", "iloraz ``x`` i ``y``"
    "``x ** y``", "``x`` do potęgi ``y``"
    "``x // y``", "podłoga z ilorazu ``x`` i ``y``"
    "``x % y``", "reszta z dzielenia ``x / y``"
    "``divmod(x, y)``", "para ``(x // y, x % y)``"
    "``abs(x)``", "wartość bezwzględna ``x``"
    "``int(x)``", "``x`` przekonwertowane do ``int``"
    "``float(x)``", "``x`` przekonwertowane do ``float``"
    "``round(x, y)``", "``x`` zaokrąglenie liczby z precyzją ``y``"
    "``complex(re, im)``", "liczba zespolona: ``re`` - część rzeczywista, ``im`` - część urojona"


Operator precedence
====================
.. csv-table:: Operator precedence
    :header-rows: 1

    "Operator", "Description"
    "``lambda``", "Lambda expression"
    "``if`` -- ``else``", "Conditional expression"
    "``or``", "Boolean OR"
    "``and``", "Boolean AND"
    "``not x``", "Boolean NOT"
    "``in``, ``not in``, ``is``, ``is not``, ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``", "Comparisons, including membership tests and identity tests"
    "``|``", "Bitwise OR"
    "``^``", "Bitwise XOR"
    "``&``", "Bitwise AND"
    "``<<``, ``>>``", "Shifts"
    "``+``, ``-``", "Addition and subtraction"
    "``*``, ``@``, ``/``, ``//``, ``%``", "Multiplication, matrix multiplication, division, floor division, remainder"
    "``+x``, ``-x``, ``~x``", "Positive, negative, bitwise NOT"
    "``**``", "Exponentiation"
    "``await``", "Await expression"
    "``x[index]``, ``x[index:index]``, ``x(arguments...)``, ``x.attribute``", "Subscription, slicing, call, attribute reference"
    "``(expressions...)``, ``[expressions...]``, ``{key: value...}``, ``{expressions...}``", "Binding or tuple display, list display, dictionary display, set display"

Bitwise
=======
- ``|`` - OR
- ``&`` - AND
- ``~`` - NOT
- ``^`` - XOR
- ``<<`` - Shift left
- ``>>`` - Shift right

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