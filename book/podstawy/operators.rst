*********
Operatory
*********

Lista operatorów
================
.. csv-table:: Lista operatorów
    :header-rows: 1
    :widths: 25, 75
    :file: data/operators-general.csv

Operacje na typach numerycznych
===============================
.. csv-table:: Lista operatorów
    :header-rows: 1
    :widths: 25, 75
    :file: data/operators-numerical.csv

Operator precedence
====================
.. csv-table:: Operator precedence
    :header-rows: 1
    :widths: 25, 75
    :file: data/operators-precedence.csv

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

:Założenia:
    * Nazwa pliku: ``operators-even.py``
    * Linii kodu do napisania: około 7 linii
    * Maksymalny czas na zadanie: 10 min

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

Liczby całkowite
----------------
#. Wczytaj liczbę od użytkownika (poda tylko ``int`` albo ``float``)
#. Wyświetl informację czy jest to liczba całkowita, czy niecałkowita.

:Założenia:
    * Nazwa pliku: ``operators-integres.py``
    * Linii kodu do napisania: około 7 linii
    * Maksymalny czas na zadanie: 10 min

:Podpowiedź:
    * Liczba całkowita to taka, której część dziesiętna nie występuje lub jest równa zero.
    * Możesz to sprawdzić dzieląc liczbę z resztą przez *1* i sprawdzając resztę z dzielenia.
    * Zwróć uywagę, że ``input()`` zawsze zwraca ``str`` wiec trzeba rzutowac na ``int``, ale wtedy tracimy informację czy wczesniej mielismy ``float``

:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie


