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
>>> i = 0
>>> result = []
>>> while i < 3:
...     result.append(i)
...     i += 1
>>>
>>> result
[0, 1, 2]


Solution
--------
>>> result = range(0,3)
>>> list(result)
[0, 1, 2]


Lazy Evaluation
---------------
>>> for i in range(0,3):
...     print(i)
0
1
2


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

>>> from itertools import count
>>>
>>>
>>> result = count(3, 2)
>>>
>>> next(result)
3
>>> next(result)
5
>>> next(result)
7

Assignments
-----------
.. literalinclude:: ../_assignments/designpatterns_idioms_range.py
    :caption: :download:`Solution <../_assignments/designpatterns_idioms_range.py>`
    :end-before: # Solution

