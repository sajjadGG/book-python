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


Printing Values
---------------
* Prints on the screen
* f-string formatting for variable substitution
* More information in `Builtin Printing`

>>> print('My name... José Jiménez')
My name... José Jiménez

>>> name = 'José Jiménez'
>>> print(name)
José Jiménez

>>> name = 'José Jiménez'
>>> print('My name... {name}')
My name... {name}

>>> name = 'José Jiménez'
>>> print(f'My name... {name}')
My name... José Jiménez


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
