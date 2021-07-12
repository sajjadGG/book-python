Operators Boolean
=================


Rationale
---------
.. csv-table:: Boolean Operators Overload
    :header: "Operator", "Method"

    "``obj & other``",     "``obj.__and__(other)``"
    "``obj | other``",     "``obj.__or__(other)``"
    "``obj ^ other``",     "``obj.__xor__(other)``"

    "``obj &= other``",    "``obj.__iand__(other)``"
    "``obj |= other``",    "``obj.__ior__(other)``"
    "``obj ^= other``",    "``obj.__ixor__(other)``"

    "``obj << other``",    "``obj.__lshift__(other)``"
    "``obj >> other``",    "``obj.__rshift__(other)``"
    "``obj <<= other``",   "``obj.__ilshift__(other)``"
    "``obj >>= other``",   "``obj.__irshift__(other)``"


Operator Module - AND
---------------------
.. code-block:: text

    1 & 1 = 1
    1 & 0 = 0
    0 & 1 = 0
    0 & 0 = 0

>>> from operator import and_
>>>
>>>
>>> and_(True, True)
True
>>> and_(True, False)
False
>>> and_(False, True)
False
>>> and_(False, False)
False


Operator Module - OR
--------------------
.. code-block:: text

    1 | 1 = 1
    1 | 0 = 1
    0 | 1 = 1
    0 | 0 = 0

>>> from operator import or_
>>>
>>>
>>> or_(True, True)
True
>>> or_(True, False)
True
>>> or_(False, True)
True
>>> or_(False, False)
False


Operator Module - XOR
---------------------
.. code-block:: text

    1 ^ 1 = 0
    1 ^ 0 = 1
    0 ^ 1 = 1
    0 ^ 0 = 0

>>> from operator import xor
>>>
>>>
>>> xor(True, True)
False
>>> xor(True, False)
True
>>> xor(False, True)
True
>>> xor(False, False)
False


Use Case - XOR as pow
---------------------
* Excel uses ``^`` to rise number to the power of a second number

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Number:
...     value: int
...
...     def __xor__(self, other):
...         return Number(self.value ** other.value)
>>>
>>>
>>> a = Number(2)
>>> b = Number(4)
>>>
>>> a ^ b
Number(value=16)


Use Case - Numpy
----------------
>>> import numpy as np
>>>
>>>
>>> a = np.arange(0, 100)
>>>
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
>>>
>>> a > 2
array([False, False, False,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True])
>>>
>>> (a>2) & (a<30)
array([False, False, False,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False])
>>>
>>> (a>2) & (a<30) | (a>50)
array([False, False, False,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True])
>>>
>>> ~( (a>2) & (a<30) | (a>50) )
array([ True,  True,  True, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False])
