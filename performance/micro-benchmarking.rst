******************
Micro-benchmarking
******************

    We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil" -- Donald Knuth


Evaluation
==========
* Fresh start of Python process
* Clean memory before start
* Same data
* Same start conditions, CPU load, RAM usage, ``iostat``
* Do not measure how long Python wakes up
* Check what you measure

.. _timeit:

``timeit``
==========

Programmatic use
----------------
.. literalinclude:: src/utils-timeit-simple.py
    :language: python
    :caption: Timeit simple statement

.. literalinclude:: src/utils-timeit-multiple.py
    :language: python
    :caption: Timeit multiple statements with setup code

.. literalinclude:: src/utils-timeit-globals.py
    :language: python
    :caption: Timeit with ``globals()``

Console use
-----------
.. literalinclude:: src/utils-timeit.sh
    :language: console
    :caption: Timeit

.. code-block:: text

    -n N, --number=N
    how many times to execute ‘statement’

    -r N, --repeat=N
    how many times to repeat the timer (default 5)

    -s S, --setup=S
    statement to be executed once initially (default pass)

    -p, --process
    measure process time, not wallclock time, using time.process_time() instead of time.perf_counter(), which is the default

    -u, --unit=U
    specify a time unit for timer output; can select nsec, usec, msec, or sec

    -v, --verbose
    print raw timing results; repeat for more digits precision

    -h, --help
    print a short usage message and exit


Use cases
=========
.. _Micro-benchmarking use case:

Setup
-----
.. code-block:: python

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

Case Studies
============

Unique Keys
-----------
* Runtime: Jupyter ``%%timeit``

.. code-block:: python
    :caption: Code 1

    %%timeit

    fieldnames = set()

    for row in DATA:
        fieldnames.update(row.keys())

    # 1.55 µs ± 12.9 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

.. code-block:: python
    :caption: Code 2

    %%timeit

    fieldnames = set(key
        for record in DATA
            for key in record.keys())

    # 1.91 µs ± 16.7 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

.. code-block:: python
    :caption: Code 3 (Is it correct?!)

    %%timeit

    fieldnames = set()

    fieldnames.add(key
        for record in DATA
           for key in record.keys())

    # 416 ns ± 4.24 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

.. code-block:: python
    :caption: Code 4

    %%timeit

    fieldnames = set()
    fieldnames.update(tuple(x.keys()) for x in DATA)

    # 2.05 µs ± 48.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

.. code-block:: python
    :caption: Code 5

    %%timeit

    fieldnames = list()

    for row in DATA:
        for key in row.keys():
            fieldnames.append(key)

    set(fieldnames)

    # 2.28 µs ± 90.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

.. code-block:: python
    :caption: Code 6

    %%timeit

    fieldnames = set()

    for row in DATA:
        for key in row.keys():
            fieldnames.add(key)

    # 2.01 µs ± 54.5 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

.. code-block:: python
    :caption: Code 7

    %%timeit

    fieldnames = list()

    for row in DATA:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    # 2.09 µs ± 46.2 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

Summary
^^^^^^^
* Code 3 appends generator object not values, this is why it is so fast!

Fibonacci
---------
.. code-block:: python

    %%timeit

    def factorial_nocache(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial_nocache(n - 1)


    factorial_nocache(500)
    factorial_nocache(400)
    factorial_nocache(450)

    # 283 µs ± 6.63 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

.. code-block:: python

    %%timeit

    CACHE = {}

    def factorial_cache(n: int) -> int:
        if n in CACHE:
            return CACHE[n]

        if n == 0:
            return 1
        else:
            result = CACHE[n] = n * factorial_cache(n-1)
            return result


    factorial_cache(500)
    factorial_cache(400)
    factorial_cache(450)

    # 153 µs ± 2.49 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

.. code-block:: python

    %%timeit

    CACHE = {}

    def factorial_cache(n: int) -> int:
        result = CACHE.get(n)

        if result:
            return result

        if n == 0:
            return 1
        else:
            result = CACHE[n] = n * factorial_cache(n-1)
            return result


    factorial_cache(500)
    factorial_cache(400)
    factorial_cache(450)

    # 181 µs ± 10.3 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

.. code-block:: python

    %%timeit

    CACHE = {}

    def factorial_cache(n: int) -> int:
        if n == 0:
            return 1

        try:
            return CACHE[n]
        except KeyError:
            CACHE[n] = result = n * factorial_cache(n-1)
            return result


    factorial_cache(500)
    factorial_cache(400)
    factorial_cache(450)

    # 618 µs ± 6.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

.. code-block:: python

    %%timeit

    CACHE = {}

    def factorial_1(n: int) -> int:

        def factorial(n: int) -> int:
            if n == 0:
                return 1
            return n * factorial(n-1)

        if not n in CACHE:
            CACHE[n] = factorial(n)

        return CACHE[n]


    factorial_1(500)
    factorial_1(400)
    factorial_1(450)

    # 283 µs ± 6.44 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

.. code-block:: python

    %%timeit

    CACHE = {}

    def factorial2(n: int) -> int:
        if n == 0:
            return 1

        if n in CACHE:
            return CACHE[n]

        result = CACHE[n] = n * factorial2(n-1)
        return result


    factorial2(500)
    factorial2(400)
    factorial2(450)

    # 153 µs ± 9.64 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

References
==========
* https://www.youtube.com/watch?v=RT88FrHttRI
