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


Assignments
-----------
.. literalinclude:: assignments/operator_numerical_a.py
    :caption: :download:`Solution <assignments/operator_numerical_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/operator_numerical_b.py
    :caption: :download:`Solution <assignments/operator_numerical_b.py>`
    :end-before: # Solution
