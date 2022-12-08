Operator Left
=============
* ``x + y`` - will call "add" on object x (``x.__add__(y)``)
* ``x - y`` - will call "sub" on object x (``x.__sub__(y)``)
* ``x * y`` - will call "mul" on object x (``x.__mul__(y)``)
* ``x / y`` - will call "truediv" on object x (``x.__truediv__(y)``)
* ``x // y`` - will call "floordiv" on object x (``x.__floordiv__(y)``)
* ``x ** y`` - will call "pow" on object x (``x.__pow__(y)``)
* ``x % y`` - will call "mod" on object x (``x.__mod__(y)``)
* ``x @ y`` - will call "matmul" on object x (``x.__matmul__(y)``)


SetUp
-----
>>> from dataclasses import dataclass
>>> from functools import reduce


Example
-------
>>> class Vector:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...
...     def __repr__(self):
...         return f'Vector(x={self.x}, y={self.y})'
...
...     def __add__(self, other): ...               # x + y     calls x.__add__(y)
...     def __sub__(self, other): ...               # x - y     calls x.__sub__(y)
...     def __mul__(self, other): ...               # x * y     calls x.__mul__(y)
...     def __pow__(self, power, modulo=None): ...  # x ** y    calls x.__pow__(y)
...     def __matmul__(self, other): ...            # x @ y     calls x.__matmul__(y)
...     def __truediv__(self, other): ...           # x / y     calls x.__truediv__(y)
...     def __floordiv__(self, other): ...          # x // y    calls x.__floordiv__(y)
...     def __mod__(self, other): ...               # x % y     calls x.__mod__(y)


Left Operation
--------------
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __add__(self, other):
...         new_x = self.x + other.x
...         new_y = self.y + other.y
...         return Vector(new_x, new_y)
...
>>>
>>>
>>> a = Vector(x=1, y=2)
>>> b = Vector(x=3, y=4)
>>> c = Vector(x=5, y=6)
>>>
>>> (a+b) + c
Vector(x=9, y=12)


Increment Operation
-------------------
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __iadd__(self, other):
...         self.x += other.x
...         self.y += other.y
...         return self
...
>>>
>>>
>>> a = Vector(x=1, y=2)
>>> b = Vector(x=3, y=4)
>>> c = Vector(x=5, y=6)
>>>
>>>
>>> a += Vector(x=10, y=20)
>>> print(a)
Vector(x=11, y=22)


Use Case - 0x01
---------------
* Game

>>> hero @ Position(x=50, y=120)  # doctest: +SKIP
>>>
>>> hero['gold'] += dragon['gold']  # doctest: +SKIP


Use Case - 0x02
---------------
This is our function library.

Transformation functions (non-reducing) -
takes one argument and returns one value:

>>> def increment(x):
...     return x + 1
>>>
>>> def decrement(x):
...     return x - 1
>>>
>>> def square(x):
...     return x ** 2
>>>
>>> def cube(x):
...     return x ** 3

Reducing functions - takes two arguments returns one value:

>>> def add(x, y):
...     return x + y
>>>
>>> def sub(x, y):
...     return x - y
>>>
>>> def mul(x, y):
...     return x * x

We have data to compute:

>>> data = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9],
... ]

On this data, we want to apply the following transformations:

>>> transformations = [increment, square, decrement, cube]

We need to create apply function, which takes data and apply
the transformation:

>>> def apply(data, fn):
...     return map(fn, data)

Let's do it parallel. We will create three independent workers.
Each worker will get part of the data (one-third) and will apply
all the transformation (map) to their data subset.

>>> workerA = reduce(apply, transformations, data[0])  # [27, 512, 3375]
>>> workerB = reduce(apply, transformations, data[1])  # [13824, 42875, 110592]
>>> workerC = reduce(apply, transformations, data[2])  # [250047, 512000, 970299]

Note, that all workers will produce generators (maps).
We need to merge the results using ``reduce`` function,
but before that we need to evaluate maps to lists.

>>> def merge(x, y):
...     return list(x) + list(y)

>>> merged = reduce(merge, [workerA, workerB, workerC])
>>> result = reduce(add, merged)

>>> print(result)
1903551

>>> print(merged)
[27, 512, 3375, 13824, 42875, 110592, 250047, 512000, 970299]


Assignments
-----------
.. literalinclude:: assignments/operator_left_a.py
    :caption: :download:`Solution <assignments/operator_left_a.py>`
    :end-before: # Solution
