Numeric Int
===========
* There is no maximal or minimal ``int`` value
* Python 3 dynamically extends ``int`` when it's too big


Syntax
------
>>> data = 1
>>> data = +1
>>> data = -1

You can use ``_`` for easier read especially with big numbers:

>>> million = 1000000
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


Type Checking
-------------
* ``type()`` - Returns type of an argument

>>> x = 1
>>>
>>> type(x)
<class 'int'>
>>>
>>> type(x) is int
True

>>> x = 1
>>>
>>> isinstance(x, int)
True

Rounding
--------
Builtin function ``int()`` does not round numbers:

>>> int(1.111)
1
>>>
>>> int(1.999)
1

Builtin function ``round()`` does that:

>>> round(1.111)
1
>>>
>>> round(1.999)
2


Built-in Functions
------------------
Absolute value:

>>> abs(1)
1
>>>
>>> abs(-1)
1

Power (the same as ``**``):

>>> pow(2, 4)
16
>>>
>>> pow(16, 1/2)
4.0


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


Homework
--------
.. literalinclude:: assignments/type_int_f.py
    :caption: :download:`Solution <assignments/type_int_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_g.py
    :caption: :download:`Solution <assignments/type_int_g.py>`
    :end-before: # Solution

.. literalinclude:: assignments/type_int_h.py
    :caption: :download:`Solution <assignments/type_int_h.py>`
    :end-before: # Solution
