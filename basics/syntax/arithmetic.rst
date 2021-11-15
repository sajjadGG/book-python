Syntax Arithmetic
=================


Arithmetic Operators
--------------------
* ``+`` - Addition
* ``-`` - Subtraction
* ``*`` - Multiplication
* ``/`` - Division

>>> 10 + 2
12
>>>
>>> 10 - 2
8
>>>
>>> 10 * 2
20
>>>
>>> 10 / 2
5.0

>>> x = 10
>>> y = 2
>>>
>>> x + y
12


Power and Root
--------------
* ``a ** b`` - ``b`` power of the number ``a``
* ``a ** (1/b)`` - ``b``-th root of the number ``a``

>>> 10 ** 2
100
>>>
>>> 2 ** -1
0.5
>>>
>>> 1.337 ** 3
2.389979753

>>> 4 ** (1/2)
2.0
>>>
>>> 2 ** (1/2)
1.4142135623730951
>>>
>>> 27 ** (1/3)
3.0

>>> 4 ** 0.5
2.0
>>>
>>> 2 ** 0.5
1.4142135623730951
>>>
>>> 27 ** 0.333
2.9967059728946346


Divisions
---------
There are three (and even four if counting ``divmod``) ways of dividing numbers
in Python:

    * ``/`` - True Division (changes type to float)
    * ``//`` - Floor division (preserving data type)
    * ``%`` - Modulo division (reminder)

The most common is true division, which changes type to float to preserve
mathematical correctness:

>>> 12 / 6
2.0
>>>
>>> 12 / 5
2.4

Note, that the floor division preserves types, so it is more correct in
computer science way. However it will produce invalid values from math
perspective:

>>> 12 // 6
2
>>>
>>> 12 // 5
2

There is also a modulo division, which is more frequently used than you might
think. Modulo division is the reminder from true division:

>>> 12 % 6
0
>>>
>>> 12 % 5
2

Modulo division is most frequently used to test if value is even or odd.
In such case, you need to modulo divide number by 2 and check the reminder.
If the reminder is 0, than the original number was even, if the reminder
is false, the original number was odd:

>>> 12 % 2 == 0
True
>>>
>>> 11 % 2 == 0
False

