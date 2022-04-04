Syntax Indentation
==================
* Python uses indentation instead of braces
* Code indented on the same level belongs to block
* :pep:`8` -- Style Guide for Python Code: 4 spaces indentation
* Python throws ``IndentationError`` exception on problem


Block Statement
---------------
* First line of block statement ends with semicolon ``:``
* Code indented on the same level belongs to block

>>> if True:
...     print('True statement, first line')
... else:
...     print('Else statement, first line')
True statement, first line


Multiline Blocks
----------------
>>> if True:
...     print('True statement, first line')
...     print('True statement, second line')
...     print('True statement, third line')
... else:
...     print('Else statement, first line')
...     print('Else statement, second line')
...     print('Else statement, third line')
True statement, first line
True statement, second line
True statement, third line


Nested Blocks
-------------
>>> if True:
...     print('Outer block, true statement, first line')
...     if True:
...         print('Inner block, true statement, first line')
...     else:
...         print('Inner block, else statement, fist line')
... else:
...     print('Outer block, else statement, first line')
Outer block, true statement, first line
Inner block, true statement, first line


Good Practices
--------------
>>> if True:
...     print('Outer block, true statement, first line')
...     print('Outer block, true statement, second line')
...     print('Outer block, true statement, third line')
...
...     if True:
...         print('Inner block, true statement, first line')
...         print('Inner block, true statement, second line')
...         print('Inner block, true statement, third line')
...     else:
...         print('Inner block, else statement, fist line')
...         print('Inner block, else statement, second line')
...         print('Inner block, else statement, third line')
...
... else:
...     print('Outer block, else statement, first line')
...     print('Outer block, else statement, second line')
...     print('Outer block, else statement, third line')
Outer block, true statement, first line
Outer block, true statement, second line
Outer block, true statement, third line
Inner block, true statement, first line
Inner block, true statement, second line
Inner block, true statement, third line


Further Reading
---------------
* `Silicon Valley: Tabs vs Spaces <https://youtu.be/SsoOG6ZeyUI>`_


.. todo:: Assignments
