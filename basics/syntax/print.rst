Syntax Print
============


String
------
Either quotes (") or apostrophes (') will work. This topic will be covered
in depth while talking about string type.

>>> name = 'Mark'
>>> name = "Mark"

>>> name = "Mark'
Traceback (most recent call last):
SyntaxError: unterminated string literal (detected at line 1)

>>> name = 'Mark"
Traceback (most recent call last):
SyntaxError: unterminated string literal (detected at line 1)


String Interpolation
--------------------
* String interpolation will find and substitute variable
* F-string (since Python 3.6)
* ``str.format()`` (since Python 3.0)
* %-string (legacy)
* More information in `String Literals`

>>> name = 'Mark'
>>> result = 'Hello {name}'
>>> result
'Hello {name}'

F-string (preferred):

>>> name = 'Mark'
>>> result = f'Hello {name}'
>>> result
'Hello Mark'

String format (legacy):

>>> name = 'Mark'
>>> result = 'Hello {}'.format(name)
>>> result
'Hello Mark'

>>> name = 'Mark'
>>> result = 'Hello {0}'.format(name)
>>> result
'Hello Mark'

>>> name = 'Mark'
>>> result = 'Hello {x}'.format(x=name)
>>> result
'Hello Mark'

%-format (legacy):

>>> name = 'Mark'
>>> result = 'Hello %s' % name
>>> result
'Hello Mark'


Print
-----
* Prints on the screen
* Print string
* Print variable
* Print interpolated string
* More information in `Builtin Printing`

Print string:

>>> print('Hello World')
Hello World

Print variable:

>>> text = 'Hello World'
>>> print(text)
Hello World

Print interpolated string:

>>> name = 'Mark'
>>> print('Hello {name}')
Hello {name}

>>> name = 'Mark'
>>> print(f'Hello {name}')
Hello Mark


End of Lines
------------
* No semicolon (``;``) at the end of lines
* :pep:`8` -- Style Guide for Python Code: Use ``\n`` for newline

>>> print('Hello World')
Hello World

>>> print('Hello\nWorld')
Hello
World

>>> print('Hello\n World')
Hello
 World


Assignments
-----------
.. literalinclude:: assignments/syntax_print_a.py
    :caption: :download:`assignments/syntax_print_a.py`
    :end-before: # Solution

.. literalinclude:: assignments/syntax_print_b.py
    :caption: :download:`assignments/syntax_print_b.py`
    :end-before: # Solution
