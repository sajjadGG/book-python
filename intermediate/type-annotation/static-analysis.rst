Type Annotation Static Analysis
===============================


MyPy
----
* Type Checking
* http://mypy-lang.org/
* https://github.com/python/mypy

.. code-block:: console

    $ pip install mypy
    $ mypy FILE

``setup.cfg``

.. code-block:: ini

    [mypy]
    strict_optional = True


PyType
------
* Type Checking
* https://github.com/google/pytype

.. code-block:: console

    $ pip install pytype
    $ pytype -V 3.9 myfile.py


Pyre-check
----------
* Type Checking



PyAnnotate
----------
* Annotating existing code
* http://mypy-lang.blogspot.com/2017/11/dropbox-releases-pyannotate-auto.html

The -w flag means "go ahead, update the file":

.. code-block:: console

    $ pip install pyannotate
    $ pyannotate -w myfile.py


Monkeytype
----------
* Annotating existing code
* https://instagram-engineering.com/let-your-code-type-hint-itself-introducing-open-source-monkeytype-a855c7284881

.. code-block:: console

    $ pip install monkeytype
    $ monkeytype run runtests.py
    $ monkeytype stub some.module
    $ monkeytype apply some.module


Cython
------
* https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html

>>> # doctest: +SKIP
... import cython
...
...
... def primes(nb_primes: cython.int):
...     i: cython.int
...     p: cython.int[1000]
...
...     if nb_primes > 1000:
...         nb_primes = 1000
...
...     if not cython.compiled:  # Only if regular Python is running
...         p = [0] * 1000       # Make p work almost like a C array
...
...     len_p: cython.int = 0  # The current number of elements in p.
...     n: cython.int = 2
...     while len_p < nb_primes:
...         # Is n prime?
...         for i in p[:len_p]:
...             if n % i == 0:
...                 break
...
...         # If no break occurred in the loop, we have a prime.
...         else:
...             p[len_p] = n
...             len_p += 1
...         n += 1
...
...     # Let's copy the result into a Python list:
...     result_as_list = [prime for prime in p[:len_p]]
...     return result_as_list


Mypyc
-----
* Mypyc compiles Python modules to C extensions.
* It uses standard Python type hints to generate fast code.
* https://mypyc.readthedocs.io/en/latest/
