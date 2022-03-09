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

>>> result = (float(x) for x in range(0,5))
>>> print(list(result))
[0.0, 1.0, 2.0, 3.0, 4.0]

>>> result = map(float, range(0,5))
>>> print(list(result))
[0.0, 1.0, 2.0, 3.0, 4.0]


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


Multi Parameters
----------------
>>> def myfunc(x):
...     return sum(x)
>>>
>>>
>>> DATA = [(1,2), (3,4)]
>>> result = map(myfunc, DATA)
>>> print(list(result))
[3, 7]


Starmap
-------
>>> from itertools import starmap
>>>
>>>
>>> DATA = [(3.1415,3), (2.71828,2)]
>>>
>>> result = starmap(round, DATA)  # round(number=3.1415, ndigits=2)
>>> print(list(result))
[3.142, 2.72]


Partial
-------
>>> from functools import partial
>>>
>>>
>>> myround = partial(round, ndigits=1)
>>> DATA = [1.111, 2.222, 3.333]
>>>
>>> result = map(myround, DATA)  # round(number=1.111, ndigits=1)
>>> print(list(result))
[1.1, 2.2, 3.3]


.. todo:: Assignments
