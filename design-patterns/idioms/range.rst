Range
=====


Rationale
---------
* Return sequence of numbers
* It is not a generator
* Generator (lazy evaluated)
* Built-in


Syntax
------
* ``range([start], <stop>, [step])``
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive,
* optional ``step``, default: ``1``


Problem
-------


Solution
--------
Lazy Evaluation:

>>> for i in range(0,3):
...     print(i)
0
1
2

Instant Evaluation:

>>> data = range(0,3)
>>> list(data)
[0, 1, 2]


Use Cases
---------
>>> list(range(0,3))
[0, 1, 2]
>>> tuple(range(0,3))
(0, 1, 2)
>>> set(range(0,3))
{0, 1, 2}
>>> list(range(4,11,2))
[4, 6, 8, 10]


Itertools
---------
* More information https://docs.python.org/3/library/itertools.html
* More information :ref:`Itertools`
* ``itertools.count(start=0, step=1)``

.. code-block:: python

    from itertools import count


    data = count(3, 2)

    next(data)
    # 3

    next(data)
    # 5

    next(data)
    # 7
