Micro-benchmarking
==================


.. epigraph::

    We should forget about small efficiencies, say about 97% of the time:
    premature optimization is the root of all evil
    -- Donald Knuth

.. figure:: img/performance-optimization-knuth.jpg


Evaluation
----------
* Fresh start of Python process
* Clean memory before start
* Same data
* Same start conditions, CPU load, RAM usage, ``iostat``
* Do not measure how long Python wakes up
* Check what you measure


Timeit - Programmatic use
-------------------------
* ``timeit``

.. literalinclude:: src/utils-timeit-simple.py
    :language: python
    :caption: Timeit simple statement

.. literalinclude:: src/utils-timeit-multiple.py
    :language: python
    :caption: Timeit multiple statements with setup code

.. literalinclude:: src/utils-timeit-globals.py
    :language: python
    :caption: Timeit with ``globals()``


Timeit - Console use
--------------------
.. literalinclude:: src/utils-timeit.sh
    :language: console
    :caption: Timeit

.. code-block:: text

    -n N, --number=N
    how many times to execute 'statement'

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


PyPerformance
-------------
* ``pip install pyperformance``
* ``pyperformance run -b django_template`` - run django template benchmark

.. code-block:: console

    $ python3.10 -m venv venv-py310
    $ venv-py310/bin/pip install pyperformance
    $ venv-py310/bin/pyperformance run -b django_template

.. code-block:: console

    $ python3.11 -m venv venv-py311
    $ venv-py311/bin/pip install pyperformance
    $ venv-py311/bin/pyperformance run -b django_template


References
----------
* https://www.youtube.com/watch?v=RT88FrHttRI
