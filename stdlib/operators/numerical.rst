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
>>> from operator import add
>>> from operator import sub
>>> from operator import mul
>>> from operator import truediv
>>> from operator import floordiv
>>> from operator import mod
>>> from operator import pow
>>> from operator import matmul
>>> from operator import neg
>>> from operator import pos
>>> from operator import invert


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
...         new_x = self.x + other.x
...         new_y = self.y + other.y
...         return Vector(new_x, new_y)
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


Use Case - Mod
--------------
* ``%`` (``__mod__``) operator behavior for ``int`` and ``str``:

>>> 13 % 4
1
>>>
>>> '13' % '4'
Traceback (most recent call last):
TypeError: not all arguments converted during string formatting

>>> pi = 3.1514
>>>
>>>
>>> 'String: %s' % pi
'String: 3.1514'
>>>
>>> 'Double: %d' % pi
'Double: 3'
>>>
>>> 'Float: %f' % pi
'Float: 3.151400'

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>>
>>> 'Hello %s' % firstname
'Hello Mark'
>>>
>>> 'Hello %s %s' % (firstname, lastname)
'Hello Mark Watney'
>>>
>>> 'Hello %(fname)s %(lname)s' % {'fname': firstname, 'lname': lastname}
'Hello Mark Watney'

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

Note, that using ``%s``, ``%d``, ``%f`` is currently deprecated in favor
of ``f'...'`` string formatting. More information in `Builtin Printing`


Assignments
-----------
.. literalinclude:: assignments/operators_numerical_a.py
    :caption: :download:`Solution <assignments/operators_numerical_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operators_numerical_b.py
    :caption: :download:`Solution <assignments/operators_numerical_b.py>`
    :end-before: # Solution
