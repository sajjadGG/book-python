Reduce
======

Rationale
---------
* Reduce sequence using function
* Generator (lazy evaluated)
* Built-in


Syntax
------
* ``functools.reduce(callable, iterable)``
* required ``callable`` - Function
* required ``iterable`` - Sequence or iterator object


Built-in
--------
* https://docs.python.org/3/library/functools.html
* ``functools.reduce(callable, iterable[, initializer])``

>>> 1 + 2
3
>>> 1 + 2 + 3 + 4
10

>>> from functools import reduce
>>>
>>>
>>> def add(x, y):
...     return x + y
>>>
>>>
>>> reduce(add, [1, 2])
3
>>> reduce(add, [1, 2, 3, 4])
10
