FuncProg Referential Transparency
=================================


Rationale
---------
* Value of a variable in a functional program never changes once defined
* This eliminates any chances of side effects
* Any variable can be replaced with its actual value at any point of execution [#Hughes1984]_

Bad:

>>> a = 1
>>> a += 2

Good:

>>> a = 1
>>> b = a + 2


Example
-------
>>> a = 1
>>> print(a)
>>> a += 2
1

>>> a = 1
>>> print(a)
>>> a += 2
>>> print(a)
1
3

>>> a = 1
>>> print(1)
>>> a += 2
>>> print(1)
1
1

>>> a = 1
>>> print(a)
>>> b = a + 2
>>> print(a)
>>> print(b)
1
1
3

>>> print(1)
>>> b = 1 + 2
>>> print(1)
>>> print(b)
1
1
3

Use Case - 0x01
---------------
>>> def add(a,b):
...     return a + b
>>>
>>>
>>> x = 1
>>> y = 2
>>>
>>> add(x,y)
3
>>> add(1,y)
3
>>> add(x,2)
3
>>> add(1,2)
3


References
----------
.. [#Hughes1984] Hughes, John. "Why Functional Programming Matters". Chalmers University of Technology. 1984.
