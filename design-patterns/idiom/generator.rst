Generators
==========


Recap
-----
* Comprehensions executes instantly
* Generators are lazy evaluated

>>> data = [x for x in range(0,5)]
>>>
>>> print(data)
[0, 1, 2, 3, 4]
>>> list(data)
[0, 1, 2, 3, 4]

>>> data = (x for x in range(0,5))
>>>
>>> print(data)  # doctest: +ELLIPSIS
<generator object <genexpr> at 0x...>
>>> list(data)
[0, 1, 2, 3, 4]

>>> _ = list(x for x in range(0,5))      # list comprehension
>>> _ = tuple(x for x in range(0,5))     # tuple comprehension
>>> _ = set(x for x in range(0,5))       # set comprehension
>>> _ = dict((x,x) for x in range(0,5))  # dict comprehension

>>> _ = [x for x in range(0,5)]          # list comprehension
>>> _ = (x for x in range(0,5))          # generator expression
>>> _ = {x for x in range(0,5)}          # set comprehension
>>> _ = {x:x for x in range(0,5)}        # dict comprehension


Rationale
---------
* Create generator object and assign pointer (do not execute)
* Comprehensions will be in the memory until end of a program
* Generators are cleared once they are executed
* Comprehensions - Using values more than one
* Generators - Using values once (for example in the loop iterator)

* Generator will calculate next number for every loop iteration
* Generator forgets previous number
* Generator doesn't know the next number

* Code do not execute instantly
* Sometimes code is not executed at all!

* If you need values evaluated instantly, there is no point in using generators


Generator Function
------------------
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


Generator Filter
----------------
>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> def get_values(species):
...     result = []
...     for row in DATA:
...         if row[4] == species:
...             result.append(row)
...     return result
>>>
>>>
>>> data = get_values('setosa')
>>>
>>> print(data)
[(5.1, 3.5, 1.4, 0.2, 'setosa'), (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>> for row in data:
...     print(row)
(5.1, 3.5, 1.4, 0.2, 'setosa')
(4.7, 3.2, 1.3, 0.2, 'setosa')

>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> def get_values(species):
...     for row in DATA:
...         if row[4] == species:
...             yield row
>>>
>>>
>>> data = get_values('setosa')
>>>
>>> print(data)  # doctest: +ELLIPSIS
<generator object get_values at 0x...>
>>>
>>> for row in data:
...     print(row)
(5.1, 3.5, 1.4, 0.2, 'setosa')
(4.7, 3.2, 1.3, 0.2, 'setosa')


Itertools
---------
* Learn more at https://docs.python.org/library/itertools.html
* More information in `Itertools`
* ``from itertools import *``
* ``count(start=0, step=1)``
* ``cycle(iterable)``
* ``repeat(object[, times])``
* ``accumulate(iterable[, func, *, initial=None])``
* ``chain(*iterables)``
* ``compress(data, selectors)``
* ``islice(iterable, start, stop[, step])``
* ``starmap(function, iterable)``
* ``product(*iterables, repeat=1)``
* ``permutations(iterable, r=None)``
* ``combinations(iterable, r)``
* ``combinations_with_replacement(iterable, r)``
* ``groupby(iterable, key=None)``


Memory Footprint
----------------
* ``sys.getsizeof(obj)`` returns the size of an ``obj`` in bytes
* ``sys.getsizeof(obj)`` calls ``obj.__sizeof__()`` method
* ``sys.getsizeof(obj)`` adds an additional garbage collector overhead if the ``obj`` is managed by the garbage collector

>>> from sys import getsizeof
>>>
>>>
>>> gen1 = (x for x in range(0,1))
>>> gen10 = (x for x in range(0,10))
>>> gen100 = (x for x in range(0,100))
>>> gen1000 = (x for x in range(0,1000))
>>>
>>> getsizeof(gen1)
112
>>>
>>> getsizeof(gen10)
112
>>>
>>> getsizeof(gen100)
112
>>>
>>> getsizeof(gen1000)
112

>>> from sys import getsizeof
>>>
>>>
>>> com1 = [x for x in range(0,1)]
>>> com10 = [x for x in range(0,10)]
>>> com100 = [x for x in range(0,100)]
>>> com1000 = [x for x in range(0,1000)]
>>>
>>>
>>> getsizeof(com1)
88
>>>
>>> getsizeof(com10)
184
>>>
>>> getsizeof(com100)
920
>>>
>>> getsizeof(com1000)
8856

.. figure:: img/idiom-generator-performance.png

    Source: https://www.askpython.com/python/python-yield-examples


Inspection
----------
>>> from inspect import isgenerator
>>>
>>>
>>> a = [x for x in range(0,5)]
>>> b = (x for x in range(0,5))
>>>
>>> isgenerator(a)
False
>>> isgenerator(b)
True

>>> from inspect import isgenerator
>>>
>>>
>>> data = range(0, 10)
>>>
>>> isgenerator(data)
False


Introspection
-------------
>>> data = (x for x in range(0,10))
>>>
>>>
>>> next(data)
0
>>>
>>> data.gi_code  # doctest: +ELLIPSIS
<code object <genexpr> at 0x..., file "<...>", line 1>
>>>
>>> data.gi_running
False
>>>
>>> data.gi_frame  # doctest: +ELLIPSIS
<frame at 0x..., file '<...>', line 1, code <genexpr>>
>>>
>>> data.gi_frame.f_locals  # doctest: +ELLIPSIS
{'.0': <range_iterator object at 0x...>, 'x': 0}
>>>
>>> data.gi_frame.f_code  # doctest: +ELLIPSIS
<code object <genexpr> at 0x...0, file "<...>", line 1>
>>>
>>> data.gi_frame.f_lineno
1
>>>
>>> data.gi_frame.f_lasti
8
>>>
>>> data.gi_yieldfrom


Multiple Yields
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


Yield From
----------
* Since Python 3.3: :pep:`380` -- Syntax for Delegating to a Subgenerator
* Helps with refactoring generators
* Useful for large generators which can be split into smaller ones
* Delegation call
* ``yield from`` terminates on ``GeneratorExit`` from other function
* The value of the ``yield from`` expression is the first argument to the ``StopIteration`` exception raised by the iterator when it terminates
* Return expr in a generator causes ``StopIteration(expr)`` to be raised upon exit from the generator

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

`yield from` with sequences:

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

`yield from` with comprehensions:

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

`yield from` with generator expressions:

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


Send
----
* ``.send()`` method allows to pass value to the generator
* ``data = yield`` will receive this "sent" value
* After running you have to send ``None`` value to begin processing
* Sending anything other will raise ``TypeError``

>>> def run():
...     while True:
...         data = yield
...         print(f'Processing {data}')
>>>
>>>
>>> worker = run()
>>>
>>> type(worker)
<class 'generator'>
>>>
>>> worker.send('hello')
Traceback (most recent call last):
TypeError: can't send non-None value to a just-started generator

>>> def run():
...     while True:
...         data = yield
...         print(f'Processing {data}')
>>>
>>>
>>> worker = run()
>>> worker.send(None)
>>>
>>> for x in range(0,3):
...     worker.send(x)
Processing 0
Processing 1
Processing 2

>>> def worker():
...     while True:
...         data = yield
...         print(f'Processing {data}')
>>>
>>> def run(gen):
...     gen.send(None)
...     while True:
...         x = yield
...         gen.send(x)
>>>
>>>
>>> result = run(worker())
>>> result.send(None)
>>>
>>> for x in range(0,3):
...     result.send(x)
Processing 0
Processing 1
Processing 2


Conclusion
----------
* Python yield keyword creates a generator function.
* It’s useful when the function returns a large amount of data by splitting it into multiple chunks.
* We can also send values to the generator using its ``send()`` function.
* The ``yield from`` statement is used to create a sub-iterator from the generator function.
* Source: https://www.askpython.com/python/python-yield-examples


Assignments
-----------
.. literalinclude:: assignments/idioms_generator_a.py
    :caption: :download:`Solution <assignments/idioms_generator_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idioms_generator_b.py
    :caption: :download:`Solution <assignments/idioms_generator_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/idioms_generator_c.py
    :caption: :download:`Solution <assignments/idioms_generator_c.py>`
    :end-before: # Solution
