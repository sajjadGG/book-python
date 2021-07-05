Generator Expression
====================


Rationale
---------
* Comprehensions executes instantly
* Comprehensions will be in the memory until end of a program
* Comprehensions - Using values more than one

* Generator Expression are lazy evaluated
* Generator Expression are cleared once they are executed
* Generators - Using values once (for example in the loop iterator)


List Comprehension
------------------
* Comprehensions executes instantly

>>> data = [x for x in range(0,5)]
>>>
>>> print(data)
[0, 1, 2, 3, 4]
>>> list(data)
[0, 1, 2, 3, 4]


Generator Expression
--------------------
* Generators are lazy evaluated

>>> data = (x for x in range(0,5))
>>>
>>> print(data)  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>
>>> list(data)
[0, 1, 2, 3, 4]


Example
-------
>>> _ = list(x for x in range(0,5))      # list comprehension
>>> _ = tuple(x for x in range(0,5))     # tuple comprehension
>>> _ = set(x for x in range(0,5))       # set comprehension
>>> _ = dict((x,x) for x in range(0,5))  # dict comprehension

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
