File Path Errors
================

.. testsetup::

    from pathlib import Path
    Path('/tmp/myfile.txt').unlink(missing_ok=True)


Recap
-----
* Raw Strings
* Always use raw-strings (``r"..."``) for paths
* Raw String turns-off escape characters

>>> print(r'C:\Users\Admin\file.txt')
C:\Users\Admin\file.txt

>>> print('C:\\Users\\Admin\\file.txt')
C:\Users\Admin\file.txt

>>> print('C:\Users\Admin\file.txt')
Traceback (most recent call last):
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

Problem is with ``\Users``. After escape sequence ``\U...`` Python expects
hexadecimal Unicode codepoint, i.e. '\\U0001F680' which is a rocket 🚀
emoticon. In this example, Python finds letter ``s``, which is invalid
hexadecimal character and therefore raises an ``SyntaxError`` telling user
that there is an error with decoding bytes. The only valid hexadecimal
numbers are ``0123456789abcdefABCDEF`` and ``s`` isn't one of them.


Escaping Characters in Path
---------------------------
* "\\ " (backslash space) - escapes space
* Note that in Python escapes in paths are not required

>>> FILE = '/tmp/my file.txt'

>>> FILE = r'/tmp/my file.txt'

>>> FILE = r'C:\Users\Admin\myfile.txt'
>>>
>>>
>>> repr(FILE)
"'C:\\\\Users\\\\Admin\\\\myfile.txt'"
>>>
>>> str(FILE)
'C:\\Users\\Admin\\myfile.txt'
>>>
>>> print(repr(FILE))
'C:\\Users\\Admin\\myfile.txt'
>>>
>>> print(FILE)
C:\Users\Admin\myfile.txt


FileNotFoundError
-----------------
>>> open('/tmp/myfile.txt')
Traceback (most recent call last):
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/myfile.txt'

>>> try:
...     file = open('/tmp/myfile.txt')
... except FileNotFoundError:
...     print('Sorry, file not found')
Sorry, file not found


PermissionError
---------------
>>> open('/etc/sudoers')  # doctest: +SKIP
Traceback (most recent call last):
PermissionError: [Errno 13] Permission denied: '/etc/sudoers'

>>> # doctest: +SKIP
... try:
...     file = open('/etc/sudoers')
... except PermissionError:
...     print('Sorry, permission denied')
Sorry, permission denied


IsADirectoryError
-----------------
>>> open('/tmp')
Traceback (most recent call last):
IsADirectoryError: [Errno 21] Is a directory: '/tmp'

>>> try:
...     file = open('/tmp')
... except IsADirectoryError:
...     print('Sorry, path leads to directory')
Sorry, path leads to directory


Use Case - 0x01
---------------
>>> try:
...     file = open('/tmp/myfile.txt')
... except FileNotFoundError:
...     print('Sorry, file not found')
... except PermissionError:
...     print('Sorry, permission denied')
... except IsADirectoryError:
...     print('Sorry, path leads to directory')
Sorry, file not found


Assignments
-----------
.. literalinclude:: assignments/file_path_a.py
    :caption: :download:`Solution <assignments/file_path_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/file_path_b.py
    :caption: :download:`Solution <assignments/file_path_b.py>`
    :end-before: # Solution
