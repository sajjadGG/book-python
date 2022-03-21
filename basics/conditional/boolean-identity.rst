Boolean Identity
================


Important
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

>>> data = None
>>>
>>> data is None
True
>>> data is not None
False

Is empty:

>>> data = None
>>>
>>> if not data:
...     print('Empty')
Empty

>>> data = None
>>>
>>> if data is None:
...     print('Empty')
Empty

Has value:

>>> data = 1
>>>
>>> if data:
...     print('Has value')
Has value

>>> data = 1
>>>
>>> if data is not None:
...     print('Has value')
Has value


Bool Identity
-------------
* `True` and `False` are singletons
* Comparing identity is faster
* Comparing values will yield the same result

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

Example:

>>> adult = True
>>>
>>>
>>> if adult:
...     print('Yes')
Yes
>>>
>>> if adult is True:
...     print('Yes')
Yes
>>>
>>> if adult == True:
...     print('Yes')
Yes


String Identity
---------------
* String instances differs
* You cannot compare their identity
* There is a caching mechanism in Python, which sometimes yield the same result
* In order to compare strings, you should compare their values, not identities

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


Type Checking
-------------
>>> data = 1337
>>>
>>> if type(data) is int:
...     print('Integer')
Integer
>>>
>>> if type(data) in (int, float):
...     print('Numeric')
Numeric

>>> data = 'Mark'
>>>
>>> if type(data) is str:
...     print('String')
String

>>> data = []
>>>
>>> if type(data) is list:
...     print('List')
List
>>>
>>> if type(data) in (list, tuple, set):
...     print('Sequence')
Sequence

>>> data = {}
>>>
>>> if type(data) is dict:
...     print('Dict')
Dict


.. todo:: Assignments
