Generator Expression
====================


Rationale
---------
Comprehensions:

    * Executes instantly
    * Stored in the memory until end of a program
    * When using values more than one

Generator Expressions:

    * Lazy evaluated
    * Cleared once they are executed
    * When using value once (for example in the loop iterator)


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
>>> data = list(x for x in range(0,5))      # list comprehension
>>> data = tuple(x for x in range(0,5))     # tuple comprehension
>>> data = set(x for x in range(0,5))       # set comprehension
>>> data = dict((x,x) for x in range(0,5))  # dict comprehension

>>> data = [x for x in range(0,5)]          # list comprehension
>>> data = (x for x in range(0,5))          # generator expression
>>> data = {x for x in range(0,5)}          # set comprehension
>>> data = {x:x for x in range(0,5)}        # dict comprehension


Comprehensions or Generator Expression
--------------------------------------
Generator Expressions:

    * Creates generator object and assign pointer
    * Code is not executed instantly
    * Sometimes code is not executed at all!
    * Are cleared once they are executed
    * Generator will calculate next number for every loop iteration
    * Generator forgets previous number
    * Generator doesn't know the next number
    * It is used for one-time access to values
      (for example in the loop iterator)

Comprehensions:

    * Comprehensions will be in the memory until end of a program
    * Comprehensions - Using values more than one

Summary:

    * If you need values evaluated instantly, there is no point in using
      generators

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


Why Round Brackets?
-------------------
* Round brackets does not produce tuples (commas does)
* Round brackets bounds context

>>> data = [x for x in range(0,5)]  # list comprehension
>>> data = (x for x in range(0,5))  # generator expression

>>> data = [1, 2, 3]
>>> type(data)
<class 'list'>
>>>
>>> data = (1, 2, 3)
>>> type(data)
<class 'tuple'>
>>>
>>> data = 1, 2, 3
>>> type(data)
<class 'tuple'>

>>> data = 1 + 2
>>> type(data)
<class 'int'>
>>>
>>> data = (1 + 2)
>>> type(data)
<class 'int'>

>>> data = (1, 2, 3)
>>> type(data)
<class 'tuple'>
>>>
>>> data = (1, 2)
>>> type(data)
<class 'tuple'>
>>>
>>> data = (1,)
>>> type(data)
<class 'tuple'>
>>>
>>> data = (1)
>>> type(data)
<class 'int'>

>>> data = 1, 2, 3
>>> type(data)
<class 'tuple'>
>>>
>>> data = 1, 2
>>> type(data)
<class 'tuple'>
>>>
>>> data = 1,
>>> type(data)
<class 'tuple'>
>>>
>>> data = 1
>>> type(data)
<class 'int'>
