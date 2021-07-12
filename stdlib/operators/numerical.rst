Operators Numerical
===================


Rationale
---------
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


Operator Module
---------------
>>> from operator import and_
>>> and_(True, True)
>>> True
>>> and_(True, False)
>>> False

>>> from operator import or_
>>> from operator import add
>>> from operator import mod
>>> from operator import truediv


Example
-------
>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Vector:
...     x: int
...     y: int
...
...     def __add__(self, other):
...         return Vector(x=self.x + other.x,
...                       y=self.y + other.y)
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
>>> (a+b) + c
Vector(x=9, y=12)
>>>
>>> a += Vector(x=10, y=20)
>>> print(a)
Vector(x=11, y=22)


Use Case
--------
* ``%`` (``__mod__``) operator behavior for ``int`` and ``str``:

>>> class Str:
...     def __mod__(self, other):
...         """str substitute"""
...
...         if type(other) is str:
...             ...
...         if type(other) is tuple:
...             ...
...         if type(other) is dict:
...             ...

>>> 'Echo' % 2
Traceback (most recent call last):
TypeError: not all arguments converted during string formatting
>>> 'Echo %s' % 2
'Echo 2'
>>> 'Echo %d' % 2
'Echo 2'
>>> 'Echo %f' % 2
'Echo 2.000000'
>>> 'Echo %s %s' % (1, 2)
'Echo 1 2'
>>> 'Echo %s %d %f' % (1, 2, 3)
'Echo 1 2 3.000000'
>>>
>>> 'Echo %(firstname)s %(lastname)s' % {'firstname': 'Mark', 'lastname': 'Watney'}
'Echo Mark Watney'
>>>
>>> 'Echo %(name)s %(age)d' % {'name': 'Mark Watney', 'age': 44}
'Echo Mark Watney 44'

``%s``, ``%d``, ``%f`` is currently deprecated in favor of ``f'...'`` string formatting.
More information in `Builtin Printing`


Assignments
-----------
.. literalinclude:: assignments/operators_numerical_a.py
    :caption: :download:`Solution <assignments/operators_numerical_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operators_numerical_b.py
    :caption: :download:`Solution <assignments/operators_numerical_b.py>`
    :end-before: # Solution
