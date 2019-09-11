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

To ``float`` or to ``int``?
---------------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/operators_integers.py`

:English:
    #. Read a number from user
    #. User will pass only valid ``int`` or ``float``
    #. Integer is when number modulo divided by one has no reminder
    #. Print whether number is ``int`` or ``float``

:Polish:
    #. Wczytaj od użytkownika liczbę
    #. Poda tylko ``int`` albo ``float``
    #. Liczba jest całkowitą gdy podzielona modulo przez jeden nie ma reszty
    #. Wyświetl informację czy jest to liczba całkowita, czy rzeczywista

:The whys and wherefores:
    * Reading input
    * Type casting
    * Conditional statements
    * Defining variables
    * Magic Number
