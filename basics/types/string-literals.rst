String Literals
===============


Escape Characters
-----------------
* ``\n`` - New line (ENTER)
* ``\t`` - Horizontal Tab (TAB)
* ``\'`` - Single quote ``'`` (escape in single quoted strings)
* ``\"`` - Double quote ``"`` (escape in double quoted strings)
* ``\\`` - Backslash ``\`` (to indicate, that this is not escape char)
* More information in `Builtin Printing`
* https://en.wikipedia.org/wiki/List_of_Unicode_characters


>>> print('Hello\World')
Hello\World

>>> print('Hello\tWorld')
Hello	World

>>> print('Hello \new World')
Hello
ew World

>>> print('Hello \\new World')
Hello \new World



Unicode
-------
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

>>> name = 'Mark'
>>> 'Witaj {name}'
'Witaj {name}'

>>> name = 'Mark'
>>> f'Witaj {name}'
'Witaj Mark'


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

>>> text = 'cześć'
>>> text.encode()
b'cze\xc5\x9b\xc4\x87'

>>> data = b'cze\xc5\x9b\xc4\x87'
data.decode()
'cześć'

>>> text.encode()
b'cze\xc5\x9b\xc4\x87'
>>>
>>> text.encode('utf-8')
b'cze\xc5\x9b\xc4\x87'
>>>
>>> text.encode('iso-8859-2')
b'cze\xb6\xe6'
>>>
>>> text.encode('windows-1250')
b'cze\x9c\xe6'
>>>
>>> text.encode('cp1250')
b'cze\x9c\xe6'


Raw String
----------
* Escapes does not matters

>>> print('hello\nworld')
hello
world

>>> print(r'hello\nworld')
hello\nworld


In Regular Expressions:

>>> '\\b[a-z]+\\b'
'\\b[a-z]+\\b'

>>> r'\b[a-z]+\b'
'\\b[a-z]+\\b'

Escape character in paths:

>>> path = '/home/mwatney/myfile.txt'  # Linux
>>> path = '/User/mwatney/myfile.txt'  # macOS
>>> path = 'c:/Users/mwatney/myfile.txt'  # Windows (with slashes instead of backslashes)
>>> path = 'c:\\Users\\mwatney\\myfile.txt'  # Windows
>>> path = r'c:\Users\mwatney\myfile.txt'  # Windows

path = 'c:\Users\mwatney\myfile.txt'  # Windows
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
