Generator Expression
====================


Comprehensions and Generator Expression
---------------------------------------
* Comprehensions executes instantly
* Generator expression executes lazily

List Comprehension:

>>> list(x for x in range(0,5))
[0, 1, 2, 3, 4]
>>>
>>> [x for x in range(0,5)]
[0, 1, 2, 3, 4]

Set Comprehension:

>>> set(x for x in range(0,5))
{0, 1, 2, 3, 4}
>>>
>>> {x for x in range(0,5)}
{0, 1, 2, 3, 4}

Dict Comprehension:

>>> dict((x,x) for x in range(0,5))
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
>>>
>>> {x:x for x in range(0,5)}
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

Tuple Comprehension:

>>> tuple(x for x in range(0,5))
(0, 1, 2, 3, 4)

Generator Expression:

>>> (x for x in range(0,5))  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>


>>> _ = list(x for x in range(0,5))      # list comprehension
>>> _ = tuple(x for x in range(0,5))     # tuple comprehension
>>> _ = set(x for x in range(0,5))       # set comprehension
>>> _ = dict((x,x) for x in range(0,5))  # dict comprehension
>>>
>>> _ = [x for x in range(0,5)]          # list comprehension
>>> _ = (x for x in range(0,5))          # generator expression
>>> _ = {x for x in range(0,5)}          # set comprehension
>>> _ = {x:x for x in range(0,5)}        # dict comprehension



Comprehensions or Generator Expression
--------------------------------------
Comprehensions vs Generator Expression:

>>> data = [x for x in range(0,10)]
>>> print(data)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> data = (x for x in range(0,10))
>>> print(data)  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>

Comprehension:

>>> data = [x for x in range(0,10)]
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 3:
...         break
0 1 2 3
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 6:
...         break
0 1 2 3 4 5 6
>>>
>>> print(list(data))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> print(list(data))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Generator Expressions:

>>> data = (x for x in range(0,10))
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 3:
...         break
0 1 2 3
>>>
>>> for x in data:  # doctest: +NORMALIZE_WHITESPACE
...     print(x, end=' ')
...     if x == 6:
...         break
4 5 6
>>>
>>> print(list(data))
[7, 8, 9]
>>>
>>> print(list(data))
[]


Tuple Comprehension?!
---------------------
* Tuple Comprehension vs. Generator Expression
* More information in `Generators`

Tuple Comprehension:

>>> tuple(x+10 for x in range(0,5))
(10, 11, 12, 13, 14)

Generator Expression:

>>> (x+10 for x in range(0,5))  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>


Assignments
-----------
.. todo:: Create Assignments
