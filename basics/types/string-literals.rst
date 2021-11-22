Str Literals
============


Escape Characters
-----------------
* ``\n`` - New line (ENTER)
* ``\t`` - Horizontal Tab (TAB)
* ``\'`` - Single quote ``'`` (escape in single quoted strings)
* ``\"`` - Double quote ``"`` (escape in double quoted strings)
* ``\\`` - Backslash ``\`` (to indicate, that this is not escape char)
* More information in `Builtin Printing`
* https://en.wikipedia.org/wiki/List_of_Unicode_characters

>>> print('\U0001F680')
🚀

>>> a = '\U0001F9D1'  # 🧑
>>> b = '\U0000200D'  # ''
>>> c = '\U0001F680'  # 🚀
>>>
>>> astronaut = a + b + c
>>> print(astronaut)
🧑‍🚀


Format String
-------------
* String interpolation (variable substitution)
* Since Python 3.6
* Used for ``str`` concatenation

>>> name = 'José Jiménez'
>>>
>>> print(f'My name... {name}')
My name... José Jiménez

>>> firstname = 'José'
>>> lastname = 'Jiménez'
>>>
>>> result = f'My name... {firstname} {lastname}'
>>> print(result)
My name... José Jiménez


Unicode Literal
---------------
* In Python 3 ``str`` is Unicode
* In Python 2 ``str`` is Bytes
* In Python 3 ``u'...'`` is only for compatibility with Python 2

>>> u'zażółć gęślą jaźń'
'zażółć gęślą jaźń'


Bytes Literal
-------------
* Used while reading from low level devices and drivers
* Used in sockets and HTTP connections
* ``bytes`` is a sequence of octets (integers between 0 and 255)
* ``bytes.decode()`` conversion to unicode ``str``
* ``str.encode()`` conversion to ``bytes``

>>> data = 'Moon'   # Unicode Literal
>>> data = u'Moon'  # Unicode Literal
>>> data = b'Moon'  # Bytes Literal

>>> data = 'Moon'
>>>
>>> type(data)
<class 'str'>
>>> data.encode()
b'Moon'

>>> data = b'Moon'
>>>
>>> type(data)
<class 'bytes'>
>>> data.decode()
'Moon'


Raw String
----------
* Escapes does not matters

In Regular Expressions:

>>> r'[a-z0-9]\n'
'[a-z0-9]\\n'

>>> print('C:\Program Files\new-file.txt')
C:\Program Files
ew-file.txt
>>>
>>> print('C:\\Program Files\\new-file.txt')
C:\Program Files\new-file.txt
>>> print(r'C:\Program Files\new-file.txt')
C:\Program Files\new-file.txt

More serious problem represents other use case:

>>> print(r'C:\Users\Admin\file.txt')
C:\Users\Admin\file.txt
>>>
>>> print('C:\\Users\\Admin\\file.txt')
C:\Users\Admin\file.txt
>>>
>>> print('C:\Users\Admin\file.txt')
Traceback (most recent call last):
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

* Problem: ``\Users``
* after ``\U...`` python expects Unicode codepoint in hex
  i.e. '\\U0001F680' which is 🚀 emoticon
* ``s`` is invalid hexadecimal character
* Only valid characters are ``0123456789abcdefABCDEF``


Assignments
-----------
.. literalinclude:: assignments/type_strliterals_a.py
    :caption: :download:`Solution <assignments/type_strliterals_a.py>`
    :end-before: # Solution
