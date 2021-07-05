Generator Function
==================


Rationale
---------
* ``yield`` keyword turns function into generator function


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
.. literalinclude:: assignments/generator_function_a.py
    :caption: :download:`Solution <assignments/generator_function_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/generator_function_b.py
    :caption: :download:`Solution <assignments/generator_function_b.py>`
    :end-before: # Solution
