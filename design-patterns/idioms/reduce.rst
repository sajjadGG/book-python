Reduce
======

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
