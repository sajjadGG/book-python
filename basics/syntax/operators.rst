*********
Operators
*********


Arithmetic Operators
====================
* ``+`` - Addition
* ``-`` - Subtraction
* ``*`` - Multiplication
* ``**`` - Power
* ``/`` - Division
* ``//`` - True division
* ``%`` - Modulo division (reminder)

.. code-block:: python

    10 + 2              # 12
    10 - 2              # 8
    10 * 2              # 20
    10 / 2              # 5

.. code-block:: python

    10 ** 2             # 100
    2 ** -1             # 0.5
    1.337 ** 3          # 2.389979753
    4 ** 0.5            # 2.0
    2 ** 0.5            # 1.4142135623730951

.. code-block:: python

    10 // 2             # 2
    10 // 3             # 3
    10 % 2              # 0
    10 % 3              # 1


Logic Operators
===============
* ``x < y`` - Less than
* ``x <= y`` - Less or equal
* ``x > y`` - Greater than
* ``x >= y`` - Greater or equal
* ``x == y`` - Equals
* ``x != y`` - Not Equals
* ``x is None`` - Object has value
* ``x is not None`` - Object don't have value

.. code-block:: python

    10 < 2              # False
    10 <= 2             # False
    10 > 2              # True
    10 >= 2             # True
    10 == 2             # False
    10 != 2             # True
    10 is None          # False
    10 is not None      # True


Increment Operators
===================
* ``+=``
* ``-=``
* ``*=``
* ``/=``

.. code-block:: python

    value = 10
    value += 1

    print(value)
    # 11

.. code-block:: python

    value = 10
    value -= 1

    print(value)
    # 9

.. code-block:: python

    value = 10
    value *= 2

    print(value)
    # 20

.. code-block:: python

    value = 10
    value /= 2

    print(value)
    # 5
