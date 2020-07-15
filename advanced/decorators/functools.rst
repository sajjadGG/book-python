*********
Functools
*********


Wraps
=====
* ``@functools.wraps(fn)``

.. code-block:: python
    :emphasize-lines: 15,18

    def my_decorator(fn):
        def wrapper(*args, **kwargs):
            """wrapper docstring"""
            return fn(*args, **kwargs)
        return wrapper


    @my_decorator
    def my_function(x):
        """my_function docstring"""
        print(x)


    print(my_function.__name__)
    # wrapper

    print(my_function.__doc__)
    # wrapper docstring

.. code-block:: python
    :emphasize-lines: 1,5,19,22

    from functools import wraps


    def my_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            """wrapper docstring"""
            return fn(*args, **kwargs)
        return wrapper


    @my_decorator
    def my_function(x):
        """my_function docstring"""
        print(x)


    print(my_function.__name__)
    # my_function

    print(my_function.__doc__)
    # my_function docstring


Cached Property
===============
* ``@functools.cached_property(fn)``

.. code-block:: python

    import statistics
    from functools import cached_property


    class Iris:
        def __init__(self, *args):
            self._measurements = args

        @cached_property
        def mean(self):
            return statistics.mean(self._measurements)

        @cached_property
        def stdev(self):
            return statistics.stdev(self._measurements)


    flower = Iris(5.1, 3.5, 1.4, 0.2)
    flower.stdev()
    flower.mean()


LRU (least recently used) cache
===============================
.. code-block:: python

    from functools import lru_cache


    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    [fib(n) for n in range(16)]
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    fib.cache_info()
    # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)


Assignments
===========

Decorator Functools Func
------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/decorator_functools_func.py`

:English:
    #. Use code from "Input" section (see below)
    #. Use ``functools.wraps`` in correct place
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Użyj ``functools.wraps`` w odpowiednim miejscu
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

.. code-block:: python

    def mydecorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


    @mydecorator
    def hello(name):
        """Some documentation"""
        return f'My name... {name}'

    print('Function:', hello.__name__)
    print('Doctring:', hello.__doc__)

:Ouput:
    .. code-block:: python

        Function: hello
        Doctring: Some documentation

Decorator Functools Args
------------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/decorator_functools_args.py`

:English:
    #. Use code from "Input" section (see below)
    #. Use ``functools.wraps`` in correct place
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Użyj ``functools.wraps`` w odpowiednim miejscu
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

.. code-block:: python

    def mydecorator(happy=True):
        def decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator


    @mydecorator(happy=False)
    def hello(name):
        """Some documentation"""
        return f'My name... {name}'

    print('Function:', hello.__name__)
    print('Doctring:', hello.__doc__)

:Ouput:
    .. code-block:: python

        Function: hello
        Doctring: Some documentation

Decorator Functools Cls
-----------------------
* Complexity level: easy
* Lines of code to write: 2 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/decorator_functools_cls.py`

:English:
    #. Use code from "Input" section (see below)
    #. Modify code to restore docstring and name from decorated class
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj kodu z sekcji "Input" (patrz poniżej)
    #. Zmodyfikuj kod aby przywrócić doctring oraz nazwę z dekorowanej klasy
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

.. code-block:: python

    def mydecorator(cls):
        class Wrapper(cls):
            attribute = 'some value...'
        return Wrapper


    @mydecorator
    class Hello:
        """Some documentation"""

    hello = Hello()
    print('Class:', hello.__name__)
    print('Doctring:', hello.__doc__)

.. code-block:: python

    Class: Hello
    Doctring: Some documentation
