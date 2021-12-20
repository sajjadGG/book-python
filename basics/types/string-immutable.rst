String Immutable
================


Rationale
---------
* ``str`` is immutable
* ``str`` methods create a new modified ``str``

>>> a = 'Python'
>>> a.replace('P', 'C')
'Cython'
>>> print(a)
Python

>>> a = 'Python'
>>> b = a.replace('P', 'C')
>>>
>>> print(a)
Python
>>> print(b)
Cython

>>> a = 'Python'
>>> a = a.replace('P', 'C')
>>>
>>> print(a)
Cython


Memory
------
.. figure:: img/str-memory-1.png
.. figure:: img/str-memory-2.png
.. figure:: img/str-memory-3.png
.. figure:: img/str-immutable.png


Value Check
-----------
This is valid way to check str value:

>>> name = 'Mark Watney'
>>> name == 'Mark Watney'
True

The following code will produce SyntaxWarning due to the invalid operand
``<input>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?``:

>>> name = 'Mark Watney'
>>> name is 'Mark Watney'
False


Length
------
>>> len('hello')
5


Concatenation
-------------
* Preferred string concatenation is using ``f-string`` formatting

>>> 'a' + 'b'
'ab'

>>> 'a' 'b'
'ab'

>>> data = 'one' \
...        'two' \
...        'three'
>>>
>>> data
'onetwothree'


Concat "Numbers"
----------------
>>> 1 + 2
3

>>> '1' + '2'
'12'


Concat Multiply
---------------
>>> '*' * 10
'**********'

>>> text = 'Hello world'
>>> print(text + '\n' + '!'*len(text))
Hello world
!!!!!!!!!!!

>>> 'Beetlejuice' * 3
'BeetlejuiceBeetlejuiceBeetlejuice'

>>> 'Mua' + 'Ha' * 2
'MuaHaHa'
>>>
>>> 'Mua' + ('Ha'*2)
'MuaHaHa'
>>>
>>> ('Mua'+'Ha') * 2
'MuaHaMuaHa'


Concat Problem
--------------
>>> 'Mark' + 'Watney'
'MarkWatney'

>>> 'Mark' + ' ' + 'Watney'
'Mark Watney'

>>> 'Mark Watney'
'Mark Watney'


Use Case - 0x01
---------------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname + lastname
'MarkWatney'

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> firstname + ' ' + lastname
'Mark Watney'

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> f'{firstname} {lastname}'
'Mark Watney'


Use Case - 0x02
---------------
>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> 'Hello ' + firstname + ' ' + lastname + '!'
'Hello Mark Watney!'

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>>
>>> f'Hello {firstname} {lastname}!'
'Hello Mark Watney!'


Assignments
-----------
.. todo:: Create assignments
