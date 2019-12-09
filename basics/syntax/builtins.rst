*****************
Builtin Functions
*****************


Generic Functions
=================
* ``len()`` - Length of a list

.. code-block:: python
    :caption: ``len()`` - Length of a list

    len('hello')                # 5
    len([1, 2, 3])              # 3


Numeric Functions
=================
* ``abs()`` - Absolute value
* ``pow()`` - Number to the ``n-th`` power
* ``round()`` - Rounds a number

.. code-block:: python
    :caption: ``abs()`` - Absolute value

    abs(1)                      # 1
    abs(-1)                     # 1
    abs(13.37)                  # 13.37
    abs(-13.37)                 # 13.37

.. code-block:: python
    :caption: ``pow()`` - Number to the ``n-th`` power

    pow(10, 2)                  # 100
    pow(3, 4)                   # 81
    pow(-1, 2)                  # 1
    pow(2, -1)                  # 0.5
    pow(1.337, 3)               # 2.389979753
    pow(4, 0.5)                 # 2.0
    pow(2, 0.5)                 # 1.4142135623730951

.. code-block:: python
    :caption: ``round()`` - Rounds a number

    round(3.1415926)        # 3
    round(3.1415926, 2)     # 3.14
    round(3.1415926, 4)     # 3.1416


Sequence Functions
==================
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``sum()`` - Sum of elements

.. code-block:: python
    :caption: ``min()`` - Minimal value

    min([1, 2, 3, 4, 5])        # 1

.. code-block:: python
    :caption: ``max()`` - Maximal value

    max([1, 2, 3, 4, 5])        # 5

.. code-block:: python
    :caption: ``sum()`` - Sum of elements

    sum([1, 2, 3, 4, 5])        # 15
