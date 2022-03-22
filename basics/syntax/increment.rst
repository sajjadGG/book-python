Syntax Increment Operators
==========================
* ``+=`` - Incremental addition
* ``-=`` - Incremental subtraction
* ``*=`` - Incremental multiplication
* ``**=`` - Incremental power
* ``/=`` - Incremental true division
* ``//=`` - Incremental floor division
* ``%=`` - Incremental modulo division

In Python for each operator there is also an increment version of it.
However, most of a time only ``+=`` and ``-=`` are used. Others uses are rare.


Incremental Addition
--------------------
>>> x = 10
>>> x = x + 1
>>>
>>> print(x)
11

>>> x = 10
>>> x += 1
>>>
>>> print(x)
11


Incremental Subtraction
-----------------------
>>> x = 10
>>> x -= 1
>>>
>>> print(x)
9


Prefix and Postfix Notation
---------------------------
In other programming languages you may find postfix and prefix increment
notation. There is no such thing in Python.

>>> x = 1
>>> x++
Traceback (most recent call last):
SyntaxError: invalid syntax

>>> x = 1
>>> ++x
1
