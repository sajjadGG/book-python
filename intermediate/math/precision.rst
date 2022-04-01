Math Precision
==============


Minimal and Maximal Values
--------------------------
Maximal and minimal ``float`` values:

.. code-block:: python

    import sys

    sys.float_info.min      # 2.2250738585072014e-308
    sys.float_info.max      # 1.7976931348623157e+308


Infinity
--------
Infinity representation:

.. code-block:: python

    1e308                   # 1e+308
    -1e308                  # -1e+308

    1e309                   # inf
    -1e309                  # -inf

    float('inf')            # inf
    float('-inf')           # -inf

    float('Infinity')       # inf
    float('-Infinity')      # -inf


Not-a-Number
------------
.. code-block:: python

    float('nan')
    # nan

    float('-nan')
    # nan


NaN vs Inf
----------
.. code-block:: python

    float('inf') + float('inf')     # inf
    float('inf') + float('-inf')    # nan
    float('-inf') + float('inf')    # nan
    float('-inf') + float('-inf')   # -inf

    float('inf') - float('inf')     # nan
    float('inf') - float('-inf')    # inf
    float('-inf') - float('inf')    # -inf
    float('-inf') - float('-inf')   # nan

    float('inf') * float('inf')     # inf
    float('inf') * float('-inf')    # -inf
    float('-inf') * float('inf')    # -inf
    float('-inf') * float('-inf')   # inf

    float('inf') / float('inf')     # nan
    float('inf') / float('-inf')    # nan
    float('-inf') / float('inf')    # nan
    float('-inf') / float('-inf')   # nan


Floating Numbers Precision
--------------------------
>>> 0.1
0.1
>>>
>>> 0.2
0.2
>>>
>>> 0.3
0.3
>>>
>>> 0.1 + 0.2 == 0.3
False

>>> round(0.1+0.2, 16) == 0.3
True
>>>
>>> round(0.1+0.2, 17) == 0.3
False

>>> 0.1 + 0.2
0.30000000000000004


IEEE 754 standard
-----------------
>>> a = 1.234
>>> b = 1234 * 10e-4
>>>
>>> a == b
True

>>> 1234 * 10e-4
1.234

>>> 1.234 == 1234 * 10e-4
True

.. figure:: img/float-anatomy.png

    What is ``float`` as defined by IEEE 754 standard

.. figure:: img/float-expression.png

    Points chart

.. figure:: img/float-mantissa-1.png

    How computer store ``float``?
    As defined by IEEE 754 standard

.. figure:: img/float-mantissa-2.png

    How to read/write ``float`` from/to memory?

.. figure:: img/float-normalized.png

    Normalized Line


Floats in Doctest
-----------------
>>> def add(a, b):
...     """
...     >>> add(1.0, 2.0)
...     3.0
...
...     >>> add(0.1, 0.2)
...     0.30000000000000004
...
...     >>> add(0.1, 0.2)   # doctest: +ELLIPSIS
...     0.3000...
...     """
...     return a + b


Decimal Type
------------
.. code-block:: python

    from decimal import Decimal


    a = Decimal('0.1')
    b = Decimal('0.2')

    a + b
    # Decimal('0.3')

.. code-block:: python

    from decimal import Decimal


    a = Decimal('0.3')

    float(a)
    # 0.3


Solutions
---------
* Round values to 4 decimal places (generally acceptable)
* Store values as ``int``, do operation and then divide. For example instead of 1.99 USD, store price as 199 US cents
* Use ``Decimal`` type
* ``Decimal`` type is much slower

Problem:

>>> candy = 0.10      # price in dollars
>>> cookie = 0.20     # price in dollars
>>>
>>> result = candy + cookie
>>> print(result)
0.30000000000000004

Round values to 4 decimal places (generally acceptable):

>>> candy = 0.10      # price in dollars
>>> cookie = 0.20     # price in dollars
>>>
>>> result = round(candy + cookie, 4)
>>> print(result)
0.3

Store values as ``int``, do operation and then divide:

>>> CENT = 1
>>> DOLLAR = 100 * CENT
>>>
>>> candy = 10*CENT
>>> cookie = 20*CENT
>>>
>>> result = (candy + cookie) / DOLLAR
>>> print(result)
0.3

Use ``Decimal`` type:

>>> from decimal import Decimal
>>>
>>>
>>> candy = Decimal('0.10')     # price in dollars
>>> cookie = Decimal('0.20')    # price in dollars
>>>
>>> result = candy + cookie
>>> print(result)
0.30
