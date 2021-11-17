Boolean Identity
================


Rationale
---------
* ``=`` assignment
* ``==`` checks for object equality
* ``is`` checks for object identity


Identity Check
--------------
* ``is`` checks for object identity
* ``is`` compares ``id()`` output for both objects
* CPython: compares the memory address a object resides in
* Testing strings with ``is`` only works when the strings are interned

Since Python 3.8 - Compiler produces a ``SyntaxWarning`` when identity checks
(``is`` and ``is not``) are used with certain types of literals (e.g. ``str``,
``int``). These can often work by accident in *CPython*, but are not guaranteed
by the language spec. The warning advises users to use equality tests
(``==`` and ``!=``) instead.

>>> name = None
>>>
>>> name is None
True
>>> name is not None
False


Bool Identity
-------------
>>> name = None
>>>
>>> name is None
True
>>> name is False
False

>>> found = True
>>>
>>> found == True
True
>>> found is True
True


String Identity
---------------
>>> a = 'Mark Watney'
>>> b = 'Mark Watney'
>>>
>>> a == b
True
>>> a is b
False

>>> 'Mark Watney' is 'Mark Watney'  # doctest: +SKIP
<...>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True



Control Flow
------------
>>> name = None
>>>
>>> if name is None:
...     print('Name is empty')
Name is empty



Assignments
-----------
.. todo:: Create assignments
