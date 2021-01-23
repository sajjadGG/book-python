Map
===


Rationale
---------
* Map (convert) elements in sequence
* Generator (lazy evaluated)
* Built-in


Syntax
------
* ``map(callable, *iterables)``
* required ``callable`` - Function
* required ``iterables`` - 1 or many sequence or iterator objects


Problem
-------
>>> data = [1, 2, 3]
>>> result = []
>>>
>>> for x in data:
...     result.append(float(x))
>>>
>>> print(result)
[1.0, 2.0, 3.0]


Solution
--------
>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> list(result)
[1.0, 2.0, 3.0]


Lazy Evaluation
---------------
>>> data = [1, 2, 3]
>>> result = map(float, data)
>>>
>>> next(result)
1.0
>>> next(result)
2.0
>>> next(result)
3.0
>>> next(result)
Traceback (most recent call last):
StopIteration


Use Cases
---------
Built-in functions:

>>> DATA = [1, 2, 3]
>>> result = map(float, DATA)
>>>
>>> tuple(map(float, DATA))
(1.0, 2.0, 3.0)

>>> DATA = [1, 2, 3]
>>> result = map(float, DATA)
>>>
>>> set(map(float, DATA))
{1.0, 2.0, 3.0}

>>> DATA = [1, 2, 3]
>>> result = (float(x) for x in DATA)
>>>
>>> list(result)
[1.0, 2.0, 3.0]

>>> DATA = [1.1, 2.2, 3.3]
>>> result = map(round, DATA)
>>>
>>> list(result)
[1, 2, 3]

Custom functions:

>>> def square(x):
...     return x ** 2
>>>
>>>
>>> DATA = [1, 2, 3]
>>> result = map(square, DATA)
>>>
>>> list(result)
[1, 4, 9]

>>> def increment(x):
...     return x + 1
>>>
>>>
>>> DATA = [1, 2, 3, 4]
>>> result = map(increment, DATA)
>>>
>>> list(result)
[2, 3, 4, 5]

>>> def translate(letter):
...     return PL.get(letter, letter)
>>>
>>>
>>> DATA = 'zażółć gęślą jaźń'
>>> PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
...       'ł': 'l', 'ń': 'n', 'ó': 'o',
...       'ś': 's', 'ż': 'z', 'ź': 'z'}
>>>
>>> result = map(translate, DATA)
>>> ''.join(result)
'zazolc gesla jazn'

Standard input:

>>> import sys
>>>
>>> # doctest: +SKIP
... print(sum(map(int, sys.stdin)))

.. code-block:: console

    $ cat ~/.profile |grep addnum
    alias addnum='python -c"import sys; print(sum(map(int, sys.stdin)))"'


Assignments
-----------
.. todo:: Create assignments
