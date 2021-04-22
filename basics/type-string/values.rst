Str Value
=========


Rationale
---------
* ``str`` is immutable

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
.. figure:: img/memory-str-1.png
.. figure:: img/memory-str-2.png
.. figure:: img/memory-str-3.png


Concatenation
-------------
* Preferred string concatenation is using ``f-string`` formatting

>>> 'a' + 'b'
'ab'

>>> 'h' + 'e' + 'l' + 'l' + 'o'
'hello'
>>> 'h' 'e' 'l' 'l' 'o'
'hello'

>>> '1' + '2'
'12'

>>> a = '1'
>>> b = '2'
>>>
>>> a + b
'12'

>>> '*' * 10
'**********'
>>> 'Beetlejuice' * 3
'BeetlejuiceBeetlejuiceBeetlejuice'
>>> 'Mua' + 'Ha' * 2
'MuaHaHa'
>>> 'Mua' + ('Ha'*2)
'MuaHaHa'
>>> ('Mua'+'Ha') * 2
'MuaHaMuaHa'

>>> firstname = 'Jan'
>>> lastname = 'Twardowski'
>>>
>>> firstname + lastname
'JanTwardowski'
>>>
>>> firstname + ' ' + lastname
'Jan Twardowski'


>>> firstname = 'Jan'
>>> lastname = 'Twardowski'
>>>
>>> firstname + ' ' + lastname
'Jan Twardowski'

>>> firstname = 'Jan'
>>> lastname = 'Twardowski'
>>>
>>> f'{firstname} {lastname}'
'Jan Twardowski'

>>> firstname = 'Jan'
>>> lastname = 'Twardowski'
>>> age = 42
>>>
>>> 'Hello ' + firstname + ' ' + lastname + ' ' + str(age) + '!'
'Hello Jan Twardowski 42!'

>>> firstname = 'Jan'
>>> lastname = 'Twardowski'
>>> age = 42
>>>
>>> f'Hello {firstname} {lastname} {age}!'
'Hello Jan Twardowski 42!'


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


Assignments
-----------
.. todo:: Create assignments
