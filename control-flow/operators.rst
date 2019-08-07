.. _Operators:

*********
Operators
*********


Operator precedence
===================
.. csv-table:: Operator precedence
    :header-rows: 1
    :widths: 25, 75

    "Operator", "Description"
    "``lambda``", "Lambda expression"
    "``if``, ``elif``, ``else``", "Conditional expression"
    "``and``", "Boolean AND"
    "``or``", "Boolean OR"
    "``not x``", "Boolean NOT"
    "``in``, ``not in``, ``is``, ``is not``,

    ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``", "Comparisons, including membership tests and identity tests"
    "``|``", "Bitwise OR"
    "``^``", "Bitwise XOR"
    "``&``", "Bitwise AND"
    "``<<``, ``>>``", "Shifts"
    "``**``", "Exponentiation"
    "``*``, ``@``, ``/``, ``//``, ``%``", "Multiplication, matrix multiplication, division, floor division, remainder"
    "``+``, ``-``", "Addition and subtraction"
    "``+x``, ``-x``, ``~x``", "Positive, negative, bitwise NOT"
    "``await``", "Await expression"
    "``x[index]``, ``x[index:index]``,

    ``x(arguments...)``, ``x.attribute``", "Subscription, slicing, call, attribute reference"
    "``(expressions...)``, ``[expressions...]``,

    ``{key: value...}``, ``{expressions...}``", "Binding or tuple display, list display, dictionary display, set display"


Assignments
===========

Even and odd numbers
--------------------
* Complexity level: Easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/operators_even_odd.py`

#. Wczytaj od użytkownika ciąg znaków dowolnej długości
#. Użytkownik będzie podawał wyłącznie ``int``
#. Sprawdź czy jest to liczba parzysta, czy nieparzysta

:The whys and wherefores:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * konwersja typów i rzutowanie
    * wykorzystanie operatorów matematycznych

:Hints:
    * Zero jest parzyste: https://en.wikipedia.org/wiki/Parity_of_zero
    * Liczba parzysta, to taka, która po podzieleniu przez dwa nie ma reszty
    * Zwróć uwagę, że operator ``%`` ma inne znaczenie dla ``int`` oraz ``str``
