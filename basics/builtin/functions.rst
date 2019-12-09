*****************
Builtin Functions
*****************


Type Casting
============
* ``int()`` converts argument to ``int``
* ``int()`` does not round numbers, it returns integer value
* ``float()`` converts argument to ``float``

.. code-block:: python
    :caption: ``int()`` converts argument to ``int``

    int(10)                     # 10
    int(10.0)                   # 10
    int(10.9)                   # 10
    int(13.37)                  # 13
    int(-13.37)                 # -13
    int('1')                    # 1
    int('-1')                   # -1
    int('13.37')                # ValueError: invalid literal for int() with base 10: '1.23'
    int('-13.37')               # ValueError: invalid literal for int() with base 10: '-1.23'

.. code-block:: python
    :caption: ``float()`` converts argument to ``float``

    float(10)                   # 10.0
    float(-10)                  # -10.0
    float(10.5)                 # 10.5
    float(-10.5)                # -10.5
    float(13.37)                # 13.37
    float(-13.37)               # -13.37
    float('+13.37')             # 13.37
    float('-13.37')             # -13.37
    float('13,37')              # ValueError: could not convert string to float: '13,37'
    float('-13,37')             # ValueError: could not convert string to float: '-13,37'

.. code-block:: python
    :caption: ``bool()`` converts argument to ``bool``

    bool(1)                     # True
    bool(0)                     # False
    bool(1.0)                   # True
    bool(0.0)                   # False
    bool('Jan Twardowski')      # True
    bool('')                    # False

.. code-block:: python
    :caption: ``str()`` converts argument to ``str``

    str('hello')        # 'hello'
    str(1969)           # '1969'
    str(13.37)          # '13.37'


Numeric Functions
=================
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``abs()`` - Absolute value
* ``sum()`` - Sum of elements
* ``len()`` - Length of a list
* ``pow()`` - Number to the ``n-th`` power

.. code-block:: python

    min(3, 1, 5)
    # 1
    min([1, 2, 3, 4, 5])
    # 1

.. code-block:: python

    max(3, 1, 5)
    # 5
    max([1, 2, 3, 4, 5])
    # 5

.. code-block:: python

    sum([1, 2, 3, 4, 5])
    # 15

.. code-block:: python

    len([1, 2, 3])
    # 3

.. code-block:: python
    :caption: Absolute value

    abs(1)          # 1
    abs(-1)         # 1
    abs(13.37)              # 13.37
    abs(-13.37)             # 13.37

.. code-block:: python
    :caption: Number to the ``n-th`` power

    pow(10, 2)      # 100
    pow(3, 4)       # 81
    pow(-1, 2)      # 1
    pow(2, -1)              # 0.5
    pow(1.337, 3)           # 2.389979753
    pow(4, 0.5)             # 2.0
    pow(2, 0.5)             # 1.4142135623730951
