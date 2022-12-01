Operator Arithmetic Increment
=============================
* ``+=`` - iadd
* ``-=`` - isub
* ``*=`` - imul
* ``/=`` - idiv
* ``//=`` - itruediv
* ``**=`` - ipow
* ``%=`` - imod
* ``@=`` - imatmul


About
-----
.. csv-table:: Numerical Operator Overload
    :header: "Operator", "Method"

    "``obj += other``",    "``obj.__iadd__(other)``"
    "``obj -= other``",    "``obj.__isub__(other)``"
    "``obj *= other``",    "``obj.__imul__(other)``"
    "``obj /= other``",    "``obj.__idiv__(other)``"
    "``obj //= other``",   "``obj.__itruediv__(other)``"
    "``obj **= other``",   "``obj.__ipow__(other)``"
    "``obj %= other``",    "``obj.__imod__(other)``"
    "``obj @= other``",    "``obj.__imatmul__(other)``"


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
...     def __iadd__(self, other): ...              # x += y    calls x.__iadd__(y)
...     def __isub__(self, other): ...              # x -= y    calls x.__isub__(y)
...     def __imul__(self, other): ...              # x *= y    calls x.__imul__(y)
...     def __ipow__(self, power, modulo=None): ... # x **= y   calls x.__ipow__(y)
...     def __imatmul__(self, other): ...           # x @= y    calls x.__imatmul__(y)
...     def __itruediv__(self, other): ...          # x /= y    calls x.__itruediv__(y)
...     def __ifloordiv__(self, other): ...         # x //= y   calls x.__ifloordiv__(y)
...     def __imod__(self, other): ...              # x %= y    calls x.__imod__(y)


Increment Operation
-------------------
>>> from dataclasses import dataclass

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
