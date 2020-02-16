.. _Conditional Operators:

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

Is even number
--------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/operators_is_even.py`

:English:
    #. Read a number from user
    #. User will pass only valid ``int``
    #. Number is even, when divided modulo (``%``) by 2 has no reminder
    #. Print whether number is odd
    #. Do not use ``if`` statement

:Polish:
    #. Wczytaj liczbę od użytkownika
    #. Użytkownika poda tylko poprawne ``int``
    #. Liczba jest nieparzysta, gdy dzielona modulo (``%``) przez 2 nie ma reszty
    #. Wypisz czy liczba jest nieparzysta
    #. Nie używaj instrukcji ``if``

:The whys and wherefores:
    * Reading input from user
    * Type casting
    * Print formatting
    * Numerical operators

:Hints:
    * ``%`` has different meaning for ``int`` and ``str``
