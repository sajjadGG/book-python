Generator Function
==================


Rationale
---------
* ``yield`` keyword turns function into generator function


Recap
-----
>>> def run():
...     return 1
>>>
>>>
>>> result = run()
>>> print(result)
1

>>> def run():
...     return 1
...     return 2  # this will not execute
>>>
>>>
>>> result = run()
>>> print(result)
1

>>> def run():
...     return 1, 2
>>>
>>>
>>> result = run()
>>> print(result)
(1, 2)


Definition
----------
Generators can return (or yield) something:

>>> def run():
...     yield 'something'

Generators can be defined with required and optional parameters just like
a regular function:

>>> def mygenerator(a, b, c=0):
...     yield a + b + c


Call Generator
--------------
Generators are called just like a regular function:

>>> def mygenerator():
...     yield 'something'
>>>
>>>
>>> result = mygenerator()

The rule with positional and keyword arguments are identical tp regular
functions:

>>> def mygenerator(a, b, c=0):
...     yield a + b + c
>>>
>>>
>>> result = mygenerator(1, b=2)


Get Results
-----------
* All generators implements Iterator protocol
* Iterator has ``obj.__iter__()`` method which enable use of ``iter(obj)``
* Iterator has ``obj.__next__()`` method which enable use of ``next(obj)``

One does not simple get data from generator:

>>> def run():
...     yield 1
>>>
>>>
>>> result = run()
>>> print(result)  # doctest: +ELLIPSIS
<generator object run at 0x...>

In Order to do so, you need to generate next item using ``next()``

>>> def run():
...     yield 1
>>>
>>>
>>> result = run()
>>> next(result)
1
>>> next(result)
Traceback (most recent call last):
StopIteration


Yield Keyword
-------------
>>> def run():
...     yield 1
>>>
>>>
>>> result = run()
>>>
>>> next(result)
1
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> def run():
...     yield 1
...     yield 2
...     yield 3
>>>
>>>
>>> result = run()
>>>
>>> next(result)
1
>>> next(result)
2
>>> next(result)
3
>>> next(result)
Traceback (most recent call last):
StopIteration

>>> def run():
...     print('a')
...     print('aa')
...     yield 1
...     print('b')
...     print('bb')
...     yield 2
...     print('c')
...     print('cc')
...     yield 3
>>>
>>>
>>> result = run()
>>>
>>> next(result)
a
aa
1
>>> next(result)
b
bb
2
>>> next(result)
c
cc
3
>>> next(result)
Traceback (most recent call last):
StopIteration


Yield in a Loop
---------------
>>> def run():
...     for x in range(0,3):
...         yield x
>>>
>>>
>>> result = run()
>>>
>>> next(result)
0
>>> next(result)
1
>>> next(result)
2
>>> next(result)
Traceback (most recent call last):
StopIteration


Yields in Loops
---------------
>>> def run():
...     for x in range(0, 3):
...         yield x
...     for y in range(10, 13):
...         yield y
>>>
>>>
>>> result = run()
>>>
>>> type(result)
<class 'generator'>
>>>
>>> next(result)
0
>>> next(result)
1
>>> next(result)
2
>>> next(result)
10
>>> next(result)
11
>>> next(result)
12
>>> next(result)
Traceback (most recent call last):
StopIteration


Yield in a Zip Loop
-------------------
>>> def names():
...     yield 'Mark Watney'
...     yield 'Melissa Lewis'
...     yield 'Rick Martinez'
>>>
>>>
>>> def roles():
...     yield 'botanist'
...     yield 'commander'
...     yield 'pilot'
>>>
>>>
>>> for n, r in zip(names(), roles()):
...     print(r, n)
botanist Mark Watney
commander Melissa Lewis
pilot Rick Martinez


Example
-------
Function:

>>> def even(data):
...     result = []
...     for x in data:
...         if x % 2 == 0:
...             result.append(x)
...     return result
>>>
>>>
>>> DATA = [0, 1, 2, 3, 4, 5]
>>>
>>> result = even(DATA)
>>>
>>> print(result)
[0, 2, 4]

Generator:

>>> def even(data):
...     for x in data:
...         if x % 2 == 0:
...             yield x
>>>
>>>
>>> DATA = [0, 1, 2, 3, 4, 5]
>>>
>>> result = even(DATA)
>>>
>>> print(result)  # doctest: +ELLIPSIS
<generator object even at 0x...>
>>> list(result)
[0, 2, 4]


Assignments
-----------
.. literalinclude:: assignments/generator_function_a.py
    :caption: :download:`Solution <assignments/generator_function_a.py>`
    :end-before: # Solution
