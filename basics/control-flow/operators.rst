.. _Conditional Operators:

*********************
Conditional Operators
*********************


Equals
======
* ``==`` - ``eq`` (equals)

.. code-block:: python
    :caption: Comparing ``str``

    'Monty Python' == 'Python'      # False
    'Python' == 'Python'            # True
    'python' == 'Python'            # False

.. code-block:: python
    :caption: Comparing ``tuple``

    (1, 2, 3) == (1, 2)             # False
    (1, 2) == (1, 2)                # True
    (1, 2) == (2, 1)                # False

.. code-block:: python
    :caption: Comparing ``list``

    [1, 2, 3] == [1, 2]             # False
    [1, 2] == [1, 2]                # True
    [1, 2] == [2, 1]                # False

.. code-block:: python
    :caption: Comparing ``set``

    {1, 2, 3} == {1, 2}             # False
    {1, 2} == {1, 2}                # True
    {1, 2} == {2, 1}                # True


Not-Equals
==========
* ``!=`` - ``ne`` (not-equals)

.. code-block:: python
    :caption: Comparing ``str``

    'Monty Python' != 'Python'      # True
    'Python' != 'Python'            # False
    'python' != 'Python'            # True

.. code-block:: python
    :caption: Comparing ``tuple``

    (1, 2, 3) != (1, 2)             # True

.. code-block:: python
    :caption: Comparing ``list``

    [1, 2, 3] != [1, 2]             # True

.. code-block:: python
    :caption: Comparing ``set``

    {1, 2, 3} != {1, 2}             # True


Greater Than
============
* ``>`` - ``gt`` (greater than)
* Set uses ``>`` for ``set.issuperset()``. More information in :ref:`Sequence Set`

.. code-block:: python

    'a' > 'b'       # False
    'b' > 'a'       # True

    'abc' > 'ab'    # True
    'abc' > 'abc'   # False
    'abc' > 'abcd'  # False

    'def' > 'abc'   # True
    'abc' > 'xy'    # False
    'abc' > 'xyz'   # False

.. code-block:: python

    (3, 9) > (3, 8)         # True
    (3, 8, 3) > (3, 7, 6)   # True
    (3, 8) > (3, 9)         # False

    (2, 7) > (3, 6)         # False
    (3, 6) > (2, 7)         # True

.. code-block:: python

    [3, 9] > [3, 8]         # True
    [3, 8, 3] > [3, 7, 6]   # True
    [3, 8] > [3, 9]         # False

    [2, 7] > [3, 6]         # False
    [3, 6] > [2, 7]         # True


Operator Precedence
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

Conditional Operators Modulo
----------------------------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/csonditional_operators_modulo.py`

:English:
    #. Read a number from user
    #. User will input ``int`` and will not input invalid data
    #. Define ``result: bool`` with parity check of input number
    #. Number is even, when divided modulo (``%``) by 2 reminder equal to 0
    #. Print ``result``
    #. Do not use ``if`` statement

:Polish:
    #. Wczytaj liczbę od użytkownika
    #. Użytkownika poda ``int`` i nie będzie wprowadzał danych niepoprawnych
    #. Zdefiniuj ``result: bool`` z wynikiem sprawdzania parzystości liczby wprowadzonej
    #. Liczba jest parzysta, gdy dzielona modulo (``%``) przez 2 ma resztę równą 0
    #. Wypisz ``result``
    #. Nie używaj instrukcji ``if``

:The whys and wherefores:
    * Reading input from user
    * Type casting
    * Print formatting
    * Numerical operators

:Hints:
    * ``%`` has different meaning for ``int`` and ``str``
