Str Literals
============


Docstring
---------
* :pep:`257` -- Docstring Conventions: For multiline ``str`` always use three
  double quote (``"""``) characters
* More information in `Function Doctest`

If assigned to variable, it serves as multiline ``str`` otherwise
it's a docstring:

>>> TEXT = """We choose to go to the Moon!
... We choose to go to the Moon in this decade and do the other things,
... not because they are easy, but because they are hard;
... because that goal will serve to organize and measure the best of our
... energies and skills, because that challenge is one that we are willing
... to accept, one we are unwilling to postpone, and one we intend to win,
... and the others, too."""


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
