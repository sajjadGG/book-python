Operator Numerical
==================
* ``+`` - add
* ``-`` - sub
* ``*`` - mul
* ``/`` - truediv
* ``//`` - floordiv
* ``**`` - pow
* ``%`` - mod
* ``@`` - matmul
* ``+=`` - iadd
* ``-=`` - isub
* ``*=`` - imul
* ``/=`` - idiv
* ``//=`` - itruediv
* ``**=`` - ipow
* ``%=`` - imod
* ``@=`` - imatmul
* ``-obj`` - neg
* ``+obj`` - pos
* ``~obj`` - invert


SetUp
-----
>>> from dataclasses import dataclass
>>> from functools import reduce


About
-----
.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj + other``",     "``obj.__add__(other)``"
    "``obj - other``",     "``obj.__sub__(other)``"
    "``obj * other``",     "``obj.__mul__(other)``"
    "``obj / other``",     "``obj.__truediv__(other)``"
    "``obj // other``",    "``obj.__floordiv__(other)``"
    "``obj ** other``",    "``obj.__pow__(other)``"
    "``obj % other``",     "``obj.__mod__(other)``"
    "``obj @ other``",     "``obj.__matmul__(other)``"

    "``obj += other``",    "``obj.__iadd__(other)``"
    "``obj -= other``",    "``obj.__isub__(other)``"
    "``obj *= other``",    "``obj.__imul__(other)``"
    "``obj /= other``",    "``obj.__idiv__(other)``"
    "``obj //= other``",   "``obj.__itruediv__(other)``"
    "``obj **= other``",   "``obj.__ipow__(other)``"
    "``obj %= other``",    "``obj.__imod__(other)``"
    "``obj @= other``",    "``obj.__imatmul__(other)``"

    "``-obj``",           "``obj.__neg__()``"
    "``+obj``",           "``obj.__pos__()``"
    "``~obj``",           "``obj.__invert__()``"


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
...
...     def __iadd__(self, other): ...              # x += y    calls x.__iadd__(y)
...     def __isub__(self, other): ...              # x -= y    calls x.__isub__(y)
...     def __imul__(self, other): ...              # x *= y    calls x.__imul__(y)
...     def __ipow__(self, power, modulo=None): ... # x **= y   calls x.__ipow__(y)
...     def __imatmul__(self, other): ...           # x @= y    calls x.__imatmul__(y)
...     def __itruediv__(self, other): ...          # x /= y    calls x.__itruediv__(y)
...     def __ifloordiv__(self, other): ...         # x //= y   calls x.__ifloordiv__(y)
...     def __imod__(self, other): ...              # x %= y    calls x.__imod__(y)
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


Right Operation
---------------
Left operation:

>>> class Left:
...     def __add__(self, other):
...         ...
>>>
>>> class Right:
...     pass
>>>
>>>
>>> left = Left()
>>> right = Right()
>>>
>>> left + right  # left.__add__(right)

What if ``Left`` class does not define ``__add__`` attribute?

>>> class Left:
...     pass
>>>
>>> class Right:
...     pass
>>>
>>>
>>> left = Left()
>>> right = Right()
>>>
>>> left + right  # left.__add__(right) -> error (Left.__add__ not defined)
Traceback (most recent call last):
TypeError: unsupported operand type(s) for +: 'Left' and 'Right'

Then Python will search for ``__radd__`` attribute in ``Right`` class:

>>> class Left:
...     pass
>>>
>>> class Right:
...     def __radd__(self, other):
...         ...
>>>
>>>
>>>
>>> left = Left()
>>> right = Right()
>>>
>>>
>>> left + right  # left.__add__(right) -> error (Left.__add__ not defined)
...               # right.__radd__(left)

Example:

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

Use Case:

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
.. literalinclude:: assignments/operator_numerical_a.py
    :caption: :download:`Solution <assignments/operator_numerical_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operator_numerical_b.py
    :caption: :download:`Solution <assignments/operator_numerical_b.py>`
    :end-before: # Solution
