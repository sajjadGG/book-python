Generator Yield From
====================


Rationale
---------
* Since Python 3.3: :pep:`380` -- Syntax for Delegating to a Subgenerator
* Helps with refactoring generators
* Useful for large generators which can be split into smaller ones
* Delegation call
* ``yield from`` terminates on ``GeneratorExit`` from other function
* The value of the ``yield from`` expression is the first argument to the ``StopIteration`` exception raised by the iterator when it terminates
* Return expr in a generator causes ``StopIteration(expr)`` to be raised upon exit from the generator


Example
-------
>>> def run():
...     for x in range(0, 3):
...         yield x
...     for x in range(10, 13):
...         yield x

>>> def generator1():
...     for x in range(0, 3):
...         yield x
>>>
>>> def generator2():
...     for x in range(10, 13):
...         yield x
>>>
>>> def run():
...     yield from generator1()
...     yield from generator2()


Why?
----
This will not work at all! Mind that no code is executed by a function
after the ``return`` keyword.

>>> def generator1():
...     for x in range(0, 3):
...         yield x
>>>
>>> def generator2():
...     for x in range(10, 13):
...         yield x
>>>
>>> def run():
...     return generator1()
...     return generator2()

This will yield generators (not their values):

>>> def generator1():
...     for x in range(0, 3):
...         yield x
>>>
>>> def generator2():
...     for x in range(10, 13):
...         yield x
>>>
>>> def run():
...     yield generator1()
...     yield generator2()


Execute
-------
>>> def generator1():
...     for x in range(0, 3):
...         yield x
>>>
>>> def generator2():
...     for x in range(10, 13):
...         yield x
>>>
>>> def run():
...     yield from generator1()
...     yield from generator2()
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


Itertools Chain
---------------
The code is equivalent to ``itertools.chain()``:

>>> from itertools import chain
>>>
>>>
>>> def generator1():
...     for x in range(0, 3):
...         yield x
>>>
>>> def generator2():
...     for x in range(10, 13):
...         yield x
>>>
>>> def run():
...     for x in chain(generator1(), generator2()):
...         yield x
>>>
>>>
>>> result = run()
>>>
>>> type(result)
<class 'generator'>
>>>
>>> list(result)
[0, 1, 2, 10, 11, 12]


Delegation call
---------------
``yield from`` turns ordinary function, into a delegation call:

>>> def worker():
...     return [1, 2, 3]
>>>
>>> def run():
...     yield from worker()
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

>>> def worker():
...     return [x for x in range(0,3)]
>>>
>>> def run():
...     yield from worker()
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


Yield From Sequences
--------------------
>>> def run():
...     yield from [0, 1, 2]
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
Traceback (most recent call last):
StopIteration


Yield From Comprehensions
-------------------------
>>> def run():
...     yield from [x for x in range(0,3)]
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
Traceback (most recent call last):
StopIteration


Yield From Generator Expression
-------------------------------
>>> def run():
...     yield from (x for x in range(0,3))
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
Traceback (most recent call last):
StopIteration


Conclusion
----------
* Python yield keyword creates a generator function.
* It's useful when the function returns a large amount of data by
  splitting it into multiple chunks.
* We can also send values to the generator using its ``send()`` function.
* The ``yield from`` statement is used to create a sub-iterator from the
  generator function.


Assignments
-----------
.. literalinclude:: assignments/generator_yieldfrom_a.py
    :caption: :download:`Solution <assignments/generator_yieldfrom_a.py>`
    :end-before: # Solution
