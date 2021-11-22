Numeric Int
===========


Syntax
------
Python 3 dynamically extends ``int`` when it's too big, hence there is no
maximal or minimal ``int`` value:

>>> data = 1337
>>> data = +1337
>>> data = -1337

You can use ``_`` for easier read especially with big numbers:

>>> million = 1000000
>>>
>>> print(million)
1000000

>>> million = 1_000_000
>>>
>>> print(million)
1000000


Type Casting
------------
Builtin function ``int()`` converts argument to ``int``:

>>> int(1)
1
>>>
>>> int(+1)
1
>>>
>>> int(-1)
-1

>>> int(1.337)
1
>>>
>>> int(+1.1337)
1
>>>
>>> int(-1.337)
-1

>>> int('1')
1
>>>
>>> int('+1')
1
>>>
>>> int('-1')
-1

>>> int('1_000_000')
1000000


Type Casting Errors
-------------------
Builtin function ``int()`` fails when in argument there are parameters
other than a digit, ``+`` or ``-`` sign and ``_``

>>> int('1.337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '13.37'

>>> int('+1.337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '+13.37'

>>> int('-1.337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '-13.37'

>>> int('1,337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '13,37'

>>> int('+1,337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '+13,37'

>>> int('-1,337')
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: '-13,37'


Rounding
--------
Builtin function ``int()`` does not round numbers:

>>> int(1.11111)
1
>>>
>>> int(1.9999)
1

Builtin function ``round()`` does that:

>>> round(1.11111)
1
>>>
>>> round(1.9999)
2


Binary
------
* Base 2
* Allowed: 0, 1
* Prefix: ``0b...``

>>> data = 0b1000101
>>> print(data)
69

>>> int('0b1000101', base=2)
69
>>>
>>> int('1000101', base=2)
69

>>> bin(69)
'0b1000101'

>>> int(1000101, base=2)
Traceback (most recent call last):
TypeError: int() can't convert non-string with explicit base
>>>
>>> bin('69')
Traceback (most recent call last):
TypeError: 'str' object cannot be interpreted as an integer


Octal
-----
* Base 8
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7
* Prefix: ``0o...``

>>> data = 0o105
>>> print(data)
69

>>> int('0o105', base=8)
69
>>>
>>> int('105', base=8)
69

>>> oct(69)
'0o105'

>>> int(0o105, base=8)
Traceback (most recent call last):
TypeError: int() can't convert non-string with explicit base
>>>
>>> int(105, base=8)
Traceback (most recent call last):
TypeError: int() can't convert non-string with explicit base


Decimal
-------
* Base 10
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

>>> data = 69
>>> print(data)
69

>>> int('69', base=10)
69

>>> int(69, base=10)
Traceback (most recent call last):
TypeError: int() can't convert non-string with explicit base


Hexadecimal
-----------
* Base 16
* Allowed: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f, A, B, C, D, E, F
* Prefix: ``0x...``

>>> data = 0x45
>>> print(data)
69

>>> int('45', base=16)
69
>>>
>>> int('0x45', base=16)
69

>>> hex(69)
'0x45'

Other examples:

>>> int('100', base=16)
256
>>>
>>> int('0x69', base=16)
105
>>>
>>> int('0x3C', base=16)
60


Type Checking
-------------
* ``type()`` - Returns type of an argument

>>> type(1)
<class 'int'>
>>>
>>> type(+1)
<class 'int'>
>>>
>>> type(-1)
<class 'int'>

>>> type(0)
<class 'int'>
>>>
>>> type(+0)
<class 'int'>
>>>
>>> type(-0)
<class 'int'>


Use Case - 0x01
---------------
>>> SECOND = 1
>>> MINUTE = 60 * SECOND
>>> HOUR = 60 * MINUTE
>>> DAY = 24 * HOUR
>>>
>>>
>>> duration = 123456 * SECOND
>>>
>>> duration // DAY
1
>>> duration // HOUR
34
>>> duration // MINUTE
2057
>>> duration // SECOND
123456


Assignments
-----------
.. literalinclude:: assignments/type_int_a.py
    :caption: :download:`Solution <assignments/type_int_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_b.py
    :caption: :download:`Solution <assignments/type_int_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_c.py
    :caption: :download:`Solution <assignments/type_int_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_d.py
    :caption: :download:`Solution <assignments/type_int_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_e.py
    :caption: :download:`Solution <assignments/type_int_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_f.py
    :caption: :download:`Solution <assignments/type_int_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_g.py
    :caption: :download:`Solution <assignments/type_int_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_h.py
    :caption: :download:`Solution <assignments/type_int_h.py>`
    :end-before: # Solution
