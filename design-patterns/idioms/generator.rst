.. _Generators:

**********
Generators
**********


Recap
=====
* Comprehensions executes instantly
* Generators are lazy evaluated

>>> data = [x for x in range(0,5)]
>>> list(data)
[0, 1, 2, 3, 4]
>>> print(data)
[0, 1, 2, 3, 4]

>>> data = (x for x in range(0,5))
>>> list(data)
[0, 1, 2, 3, 4]
>>> print(data)  # doctest: +ELLIPSIS
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


Rationale
=========
* Create generator object and assign pointer (do not execute)
* Comprehensions will be in the memory until end of a program
* Generators are cleared once they are executed
* Comprehensions - Using values more than one
* Generators - Using values once (for example in the loop iterator)

.. code-block:: python

    data = [x for x in range(0, 5)]

    list(data)
    # [0, 1, 2, 3, 4]

    list(data)
    # [0, 1, 2, 3, 4]

    print(data)
    # [0, 1, 2, 3, 4]

.. code-block:: python

    data = (x for x in range(0, 5))

    list(data)
    # [0, 1, 2, 3, 4]

    list(data)
    # []

    print(data)
    # <generator object <genexpr> at 0x11cb45950>


Instant Evaluation
==================
.. highlights::
    * If you need values evaluated instantly, there is no point in using generators

.. code-block:: python

    data = (x for x in range(0,5))

    list(data)
    # [0, 1, 2, 3, 4]


Lazy Evaluation
===============
.. highlights::
    * Code do not execute instantly
    * Sometimes code is not executed at all!

.. code-block:: python

    data = (x for x in range(0,3))

    next(data)
    # 0

    next(data)
    # 1

    next(data)
    # 2

    next(data)
    # Traceback (most recent call last):
    # StopIteration

None of those lines will generate any numbers (util executed)!:

.. code-block:: python

    a = (x for x in range(0,5))
    b = (x for x in range(0,5))
    c = (x for x in range(0,5))


Iterative Evaluation
====================
.. highlights::
    * Generator will calculate next number for every loop iteration
    * Generator forgets previous number
    * Generator doesn't know the next number

.. code-block:: python

    data = [x for x in range(0,10)]
    print(data)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    data = (x for x in range(0,10))
    print(data)
    # <generator object <genexpr> at 0x10ef1d040>

Comprehension:

.. code-block:: python

    data = [x for x in range(0,10)]

    for x in data:
        print(x, end=' ')
        if x == 3:
            break
    # 0 1 2 3

    for x in data:
        print(x, end=' ')
        if x == 6:
            break
    # 0 1 2 3 4 5 6

    print(list(data))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(list(data))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Generator:

.. code-block:: python

    data = (x for x in range(0,10))

    for x in data:
        print(x, end=' ')
        if x == 3:
            break
    # 0 1 2 3

    for x in data:
        print(x, end=' ')
        if x == 6:
            break
    # 4 5 6

    print(list(data))
    # [7, 8, 9]

    print(list(data))
    # []


Generator Function
==================
.. code-block:: python

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]


    def get_values(species):
        result = []
        for row in DATA:
            if row[4] == species:
                result.append(row)
        return result


    data = get_values('setosa')

    print(data)
    # [(5.1, 3.5, 1.4, 0.2, 'setosa'), (4.7, 3.2, 1.3, 0.2, 'setosa')]

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.7, 3.2, 1.3, 0.2, 'setosa')

.. code-block:: python

    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa')]


    def get_values(species):
        for row in DATA:
            if row[4] == species:
                yield row


    data = get_values('setosa')

    print(data)
    # <generator object get_values at 0x103632820>

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.7, 3.2, 1.3, 0.2, 'setosa')


Functools
=========
* https://docs.python.org/3/library/functools.html

.. code-block:: python

    from functools import *

    reduce(callable, iterable[, initializer])

.. code-block:: python

    1 + 2
    # 3

    1 + 2 + 3 + 4
    # 10

.. code-block:: python

    from functools import reduce


    def add(a,b):
        return a+b


    reduce(add, [1,2])
    # 3
    reduce(add, [1,2,3,4])
    # 10


Itertools
=========
* More information https://docs.python.org/3/library/itertools.html
* More information :ref:`Itertools`

.. code-block:: python

    from itertools import *

    count(start=0, step=1)
    cycle(iterable)
    repeat(object[, times])
    accumulate(iterable[, func, *, initial=None])
    chain(*iterables)
    compress(data, selectors)
    islice(iterable, start, stop[, step])
    starmap(function, iterable)
    product(*iterables, repeat=1)
    permutations(iterable, r=None)
    combinations(iterable, r)
    combinations_with_replacement(iterable, r)
    groupby(iterable, key=None)


Memory Footprint
================
* ``sys.getsizeof(obj)`` returns the size of an ``obj`` in bytes
* ``sys.getsizeof(obj)`` calls ``obj.__sizeof__()`` method
* ``sys.getsizeof(obj)`` adds an additional garbage collector overhead if the ``obj`` is managed by the garbage collector

.. code-block:: python

    from sys import getsizeof


    gen1 = (x for x in range(0,10))
    gen10 = (x for x in range(0,10))
    gen100 = (x for x in range(0,100))
    gen1000 = (x for x in range(0,1000))

    com1 = [x for x in range(0,1)]
    com10 = [x for x in range(0,10)]
    com100 = [x for x in range(0,100)]
    com1000 = [x for x in range(0,1000)]

    getsizeof(gen1)
    # 112

    getsizeof(gen10)
    # 112

    getsizeof(gen100)
    # 112

    getsizeof(gen1000)
    # 112

    getsizeof(com1)
    # 88

    getsizeof(com10)
    # 184

    getsizeof(com100)
    # 920

    getsizeof(com1000)
    # 8856


Inspection
==========
.. code-block:: python

    from inspect import isgenerator

    a = [x for x in range(0,5)]
    b = (x for x in range(0,5))

    isgenerator(a)
    # False

    isgenerator(b)
    # True

.. code-block:: python

    from inspect import isgenerator

    data = range(0, 10)

    isgenerator(data)
    # False


Introspection
=============
.. code-block:: python

    data = (x for x in range(0,10))

    next(data)
    # 0

    data.gi_code
    # <code object <genexpr> at 0x11fc4dc90, file "<input>", line 1>

    data.gi_running
    # False

    data.gi_yieldfrom

    data.gi_frame
    # <frame at 0x7f93a1723200, file '<input>', line 1, code <genexpr>>

    data.gi_frame.f_locals
    # {'.0': <range_iterator object at 0x11fc4c840>, 'x': 0}

    data.gi_frame.f_code
    # <code object <genexpr> at 0x11fc4dc90, file "<input>", line 1>

    data.gi_frame.f_lineno
    # 1

    data.gi_frame.f_lasti
    # 8


Assignments
===========

.. literalinclude:: ../_assignments/function_generators_chain.py
    :caption: :download:`Solution <../_assignments/function_generators_chain.py>`
    :end-before: # Solution

.. literalinclude:: ../_assignments/function_generator_iris.py
    :caption: :download:`Solution <../_assignments/function_generator_iris.py>`
    :end-before: # Solution

.. literalinclude:: ../_assignments/function_generator_passwd.py
    :caption: :download:`Solution <../_assignments/function_generator_passwd.py>`
    :end-before: # Solution
