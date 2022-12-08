Operator Right
==============
* ``+`` - radd
* ``-`` - rsub
* ``*`` - rmul
* ``/`` - rtruediv
* ``//`` - rfloordiv
* ``**`` - rpow
* ``%`` - rmod
* ``@`` - rmatmul


SetUp
-----
>>> from dataclasses import dataclass
>>> from functools import reduce


About
-----
.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",     "``obj.__radd__(other)``"
    "``obj - other``",     "``obj.__rsub__(other)``"
    "``obj * other``",     "``obj.__rmul__(other)``"
    "``obj / other``",     "``obj.__rtruediv__(other)``"
    "``obj // other``",    "``obj.__rfloordiv__(other)``"
    "``obj ** other``",    "``obj.__rpow__(other)``"
    "``obj % other``",     "``obj.__rmod__(other)``"
    "``obj @ other``",     "``obj.__rmatmul__(other)``"


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
...     def __radd__(self, other): ...              # x + y     if fails, then calls y.__radd__(x)
...     def __rsub__(self, other): ...              # x - y     if fails, then calls y.__rsub__(x)
...     def __rmul__(self, other): ...              # x * y     if fails, then calls y.__rmul__(x)
...     def __rpow__(self, power, modulo=None): ... # x ** y    if fails, then calls y.__rpow__(x)
...     def __rmatmul__(self, other): ...           # x @ y     if fails, then calls y.__rmatmul__(x)
...     def __rtruediv__(self, other): ...          # x / y     if fails, then calls y.__rtruediv__(x)
...     def __rfloordiv__(self, other): ...         # x // y    if fails, then calls y.__rfloordiv__(x)
...     def __rmod__(self, other): ...              # x % y     if fails, then calls y.__rmod__(x)


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


Left Operation
--------------
>>> class Left:
...     def __add__(self, other):
...         return 'left'
>>>
>>> class Right:
...     pass

Left operation:

>>> Left() + Right()   # left.__add__(right)
'left'

What if ``Right`` class does not define ``__add__`` attribute?

>>> Right() + Left()    # right.__add__(left)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Right' and 'Left'


Right Operation
---------------
>>> class Left:
...     def __add__(self, other):
...         return 'left'
...
...     def __radd__(self, other):
...         return 'left too'
>>>
>>>
>>> class Right:
...     pass

Left operation:

>>> Left() + Right()   # left.__add__(right)
'left'

What if ``Right`` class does not define ``__add__`` attribute?
Python will search for ``__radd__`` attribute in ``Right`` class:

>>> Right() + Left()     # Right.__add__(left) -> error -> # left.__radd__(right)
'left too'


Both
----
>>> class Left:
...     def __add__(self, other):
...         return 'left'
...
...     def __radd__(self, other):
...         return 'left too'
>>>
>>>
>>> class Right:
...     def __add__(self, other):
...         return 'right'
>>>
>>>
>>> Left() + Right()    # left.__add__(right)
'left'
>>>
>>> Right() + Left()    # right.__add__(left)
'right'


Example
-------
>>> a = 1
>>> b = 2
>>>
>>>
>>> a - b
-1
>>>
>>> a.__sub__(b)
-1
>>> b.__rsub__(a)
-1
>>>
>>>
>>> b - a
1
>>>
>>> b.__sub__(a)
1
>>> a.__rsub__(b)
1

Use Case
--------
>>> import numpy as np
>>>
>>>
>>> mylist = [1, 2, 3]
>>> myarr = np.array([4,5,6])
>>>
>>>
>>> myarr + mylist
array([5, 7, 9])
>>>
>>>
>>> mylist + myarr
array([5, 7, 9])
>>>
>>>
>>> mylist.__add__(myarr)
Traceback (most recent call last):
TypeError: can only concatenate list (not "numpy.ndarray") to list
>>>
>>> myarr.__radd__(mylist)
array([5, 7, 9])

>>> class ndarray:
...     def __add__(self, other):
...         if isinstance(other, list):
...             other = np.array(other)
...         if isinstance(other, np.array):
...             ...
...
...     def __radd__(self, other):
...         if isinstance(other, list):
...             other = np.array(other)
...         if isinstance(other, np.array):
...             ...


Use Case - 0x01
---------------
* Game

>>> hero @ Position(x=50, y=120)  # doctest: +SKIP
>>>
>>> hero['gold'] += dragon['gold']  # doctest: +SKIP


Use Case - 0x02
---------------
>>> from dataclasses import dataclass, field
>>>
>>>
>>> @dataclass
... class Astronaut:
...     firstname: str
...     lastname: str
>>>
>>>
>>> @dataclass
... class Crew:
...     members: list[Astronaut] = field(default_factory=list)
...
...     def __iadd__(self, other):
...         self.members.append(other)
...         return self
>>>
>>>
>>> ares3 = Crew()
>>> ares3 += Astronaut('Mark', 'Watney')
>>> ares3 += Astronaut('Melissa', 'Lewis')
>>>
>>> print(ares3)
Crew(members=[Astronaut(firstname='Mark', lastname='Watney'), Astronaut(firstname='Melissa', lastname='Lewis')])
>>>
>>> for member in ares3.members:
...     print(member)
Astronaut(firstname='Mark', lastname='Watney')
Astronaut(firstname='Melissa', lastname='Lewis')


Use Case - 0x03
---------------
>>> a = np.array([1, 2, 3])
>>> b = [4, 5, 6]
>>>
>>> a
array([1, 2, 3])
>>>
>>> b
[4, 5, 6]

>>> a + b
array([5, 7, 9])
>>>
>>> a.__add__(b)
array([5, 7, 9])

>>> b + a
array([5, 7, 9])
>>>
>>> b.__add__(a)
Traceback (most recent call last):
TypeError: can only concatenate list (not "numpy.ndarray") to list

>>> a.__radd__(b)
array([5, 7, 9])


Use Case - 0x04
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
