Reduce
======


Rationale
---------
* Reduce sequence using function
* Built-in

>>> 1 + 2
3

>>> 1 + 2 + 3 + 4
10


Syntax
------
* ``functools.reduce(function, iterable[, initializer])``
* required ``callable`` - Function
* required ``iterable`` - Sequence or iterator object
* https://docs.python.org/library/functools.html

Problem
-------
>>> def add(x, y):
...     return x + y
>>>
>>>
>>> data = [1, 2, 3, 4]
>>> result = 0
>>>
>>> for element in data:
...     result = add(result, element)
>>>
>>> result
10


Solution
--------
>>> from functools import reduce
>>>
>>>
>>> def add(x, y):
...     return x + y
>>>
>>>
>>> data = [1, 2, 3, 4]
>>> reduce(add, data)
10


Use Cases
---------
* https://docs.python.org/library/operator.html

>>> from functools import reduce
>>> from operator import mul
>>>
>>>
>>> data = [1, 2, 3, 4]
>>> reduce(mul, data)
24

>>> from functools import reduce
>>>
>>>
>>> data = [1, 2, 3, 4]
>>>
>>> reduce(min, data)
1
>>> reduce(max, data)
4


Map Reduce
----------
* https://dask.org

.. figure:: ../_img/designpatterns-idioms-mapreduce.gif


Assignments
-----------
.. todo:: Create assignments
