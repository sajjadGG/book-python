*********
Decorator
*********


Definition
==========

Decorating functions
--------------------
* ``my_decorator`` is decorator name
* ``func`` is a pointer to function which is being decorated (``my_function`` in this case)
* ``wrapper`` is a closure function
* ``wrapper`` name is a convention, but you can name it anyhow
* ``wrapper`` gets arguments passed to ``my_function``
* by calling ``func(*func_args, **func_kwargs)`` you actually run original (wrapped) function
* decorator must return pointer to ``wrapper``

.. code-block:: python

    def my_decorator(func):
        def wrapper(*func_args, **func_kwargs):
            return func(*func_args, **func_kwargs)
        return wrapper


    @my_decorator
    def my_function(x):
        print(x)


    my_function('hello')
    # hello

Decorating classes
------------------
* ``my_decorator`` is decorator name
* ``cls`` is a pointer to class which is being decorated (``MyClass`` in this case)
* ``Wrapper`` is a closure class
* ``Wrapper`` name is a convention, but you can name it anyhow
* ``Wrapper`` inherits from ``MyClass`` so it is similar
* decorator must return pointer to ``Wrapper``


.. code-block:: python

    def my_decorator(cls):
        class Wrapper(cls):
            my_value = 'some value'
        return Wrapper


    @my_decorator
    class MyClass:
        pass


    print(MyClass.my_value)
    # some value


Zastosowanie
============
* Modify arguments
* Modify returned value
* Do things before call
* Do things after call
* Avoid calling
* Modify global state (not a good idea)
* Metadata


Example
=======

Example 1
---------
.. code-block:: python

    import os
    import logging


    def if_file_exists(func):

        def check(filename):
            if os.path.exists(filename):
                return func(filename)
            else:
                logging.error(f'File "{filename}" does not exists')

        return check


    @if_file_exists
    def print_file(filename):
        with open(filename) as file:
            content = file.read()
            print(content)


    if __name__ == '__main__':
        print_file('/etc/passwd')
        print_file('/tmp/passwd')


Example 2
---------
.. code-block:: python

    import warnings
    import functools


    def deprecated(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            warnings.warn(f"Call to deprecated function {func.__name__}.",
                category=DeprecationWarning,
                filename=func.func_code.co_filename,
                lineno=func.func_code.co_firstlineno + 1)

            return func(*args, **kwargs)
        return wrapper


    @deprecated
    def my_function():
        pass


Example 3
---------
.. literalinclude:: src/decorators-function.py
    :language: python
    :caption: Decorator usage


Przykład zastosowania
---------------------
- Zagnieżdżone
- wykonywane od góry

.. code-block:: python

    @timeout(seconds=10)
    def calculate(operations=[], collection):
        total = 0

        for operation in operations:
            total += operations(collection)

        return total


Function Decorators
===================

Decorator as function
---------------------
.. code-block:: python

    def my_decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    @my_decorator
    def func(x):
        return x

Decorator as class
------------------
.. code-block:: python

    class memoize(dict):
        def __init__(self, function):
            self.function = function

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            result = self[key] = self.function(*key)
            return result


    @memoize
    def foo(a, b):
        return a * b


    foo(2, 4)       # 8
    foo             # {(2, 4): 8}

    foo('hi', 3)    # 'hihihi'
    foo             # {(2, 4): 8, ('hi', 3): 'hihihi'}


Class Decorators
================

@staticmethod
-------------
.. code-block:: python
    :caption: Functions on a high level of a module lack namespace

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b


    add(1, 2)
    sub(8, 4)

.. code-block:: python
    :caption: When ``add`` and ``sub`` are in ``Calculator`` class (namespace) they get instance (``self``) as a first argument. Instantiating Calculator is not needed, as of functions do not read or write to instance variables.

    class Calculator:

        def add(self, a, b):
            return a + b

        def sub(self, a, b):
            return a - b


    Calculator.add(10, 20)  # TypeError: add() missing 1 required positional argument: 'b'
    Calculator.sub(8, 4)    # TypeError: add() missing 1 required positional argument: 'b'

    calc = Calculator()
    calc.add(1, 2)          # 3
    calc.sub(8, 4)          # 4

.. code-block:: python
    :caption: Class ``Calculator`` is a namespace for functions. ``@staticmethod`` remove instance (``self``) argument to method.

    class Calculator:

        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def sub(a, b):
            return a - b


    Calculator.add(1, 2)
    Calculator.sub(8, 4)

@classmethod
------------
- ``@classmethod`` turns a normal method to a factory method.
- first argument for ``@classmethod`` function must always be ``cls`` (class)
- Factory methods, that are used to create an instance for a class using for example some sort of pre-processing.
- Static methods calling static methods: if you split a static methods in several static methods, you shouldn't hard-code the class name but use class methods

.. code-block:: python
    :emphasize-lines: 7-10,21,24,30,31

    import json

    class JSONSerializable:
        def to_json(self):
            return json.dumps(self.__dict__)

        @classmethod
        def from_json(cls, data):
            data = json.loads(data)
            return cls(**data)


    class User:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

    class Guest(User, JSONSerializable):
        pass

    class SuperUser(User, JSONSerializable):
        pass


    DATA = '{"first_name": "Jan", "last_name": "Twardowski"}'

    guest = Guest.from_json(DATA)
    root = SuperUser.from_json(DATA)

    type(guest)     # <class '__main__.Guest'>
    type(root)      # <class '__main__.SuperUser'>


``functools``
=============

``@functools.cached_property(func)``
------------------------------------
.. code-block:: python

    class DataSet:
        def __init__(self, sequence_of_numbers):
            self._data = sequence_of_numbers

        @cached_property
        def stdev(self):
            return statistics.stdev(self._data)

        @cached_property
        def variance(self):
            return statistics.variance(self._data)

LRU (least recently used) cache
-------------------------------
.. code-block:: python

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    >>> [fib(n) for n in range(16)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    >>> fib.cache_info()
    CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)

``memoize``
-----------
.. code-block:: python

    def memoize(function):
        from functools import wraps

        memo = {}

        @wraps(function)
        def wrapper(*args):
            if args in memo:
                return memo[args]
            else:
                rv = function(*args)
                memo[args] = rv
                return rv
        return wrapper


    @memoize
    def fibonacci(n):
        if n < 2: return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    fibonacci(25)


Przykład
========

Example 2
---------
.. code-block:: python

    class LoginCheck:
        '''
        This class checks whether a user
        has logged in properly via
        the global "check_function". If so,
        the requested routine is called.
        Otherwise, an alternative page is
        displayed via the global "alt_function"
        '''
        def __init__(self, f):
            self._f = f

        def __call__(self, *args):
            Status = check_function()
            if Status is 1:
                return self._f(*args)
            else:
                return alt_function()

    def check_function():
        return test

    def alt_function():
        return 'Sorry - this is the forced behaviour'

    @LoginCheck
    def display_members_page():
        print 'This is the members page'

Example 3
---------
.. code-block:: python

    import functools

    def singleton(cls):
        ''' Use class as singleton. '''

        cls.__new_original__ = cls.__new__

        @functools.wraps(cls.__new__)
        def singleton_new(cls, *args, **kw):
            it =  cls.__dict__.get('__it__')
            if it is not None:
                return it

            cls.__it__ = it = cls.__new_original__(cls, *args, **kw)
            it.__init_original__(*args, **kw)
            return it

        cls.__new__ = singleton_new
        cls.__init_original__ = cls.__init__
        cls.__init__ = object.__init__

        return cls

    #
    # Sample use:
    #

    @singleton
    class Foo:
        def __new__(cls):
            cls.x = 10
            return object.__new__(cls)

        def __init__(self):
            assert self.x == 10
            self.x = 15

    assert Foo().x == 15
    Foo().x = 20
    assert Foo().x == 20


Use cases
---------
.. literalinclude:: src/decorators-case-study-flask.py
    :name: listing-decorators-case-study-flask
    :language: python
    :caption: Use case wykorzystania dekotatorów do poprawienia czytelności kodu Flask

.. literalinclude:: src/decorators-case-study-django.py
    :name: listing-decorators-case-study-django
    :language: python
    :caption: Use case wykorzystania dekotatorów do poprawienia czytelności kodu Django


Decorator library
-----------------
- https://wiki.python.org/moin/PythonDecoratorLibrary


Assignments
===========

Memoization
-----------
* Filename: :download:`solution/decorator_memoize.py`
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min

.. code-block:: python

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

#. Dla danego kodu funkcji ``factorial``
#. Stwórz ``dict`` o nazwie ``CACHE`` z wynikami wyliczenia funkcji

    - klucz: argument funkcji
    - wartość: wynik obliczeń

#. Dodaj dekorator do funkcji ``factorial(n: int)`` z listingu poniżej
#. Decorator ma sprawdzać przed uruchomieniem funkcji, sprawdź czy wynik został już wcześniej obliczony:

    - jeżeli tak, to zwraca dane z ``CACHE``
    - jeżeli nie, to oblicza, aktualizuje ``CACHE``, a następnie zwraca wartość

#. Wykorzystując ``timeit`` porównaj prędkość działania z obliczaniem na bieżąco dla parametru 100

Prosty dekorator
----------------
* Filename: :download:`solution/decorator_abspath.py`
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min

#. Program przechodzi przez pliki i katalogi wykorzystując ``os.walk``.
#. Stwórz funkcję, która wypisuje na ekranie nazwę pliku lub katalogu.
#. Stwórz dekorator do funkcji, który przed wyświetleniem jej na ekranie podmieni ścieżkę na bezwzględną (``path`` + ``filename``).

Type Checking Decorator
-----------------------
* Filename: :download:`solution/decorator_check_types.py`
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min

.. code-block:: python
    :name: code-listing-decorator-type-check
    :caption: Force type checking for function

    def function(a: str, b: int) -> bool:
        return bool(a * b)

    print(function.__annotations__)
    # {'a': <class 'str'>, 'return': <class 'bool'>, 'b': <class 'int'>}

#. Na podstawie kodu :numref:`code-listing-decorator-type-check`
#. Stwórz dekorator ``check_types``
#. Dekorator ma sprawdzać typy danych, wszystkich parametrów wchodzących do funkcji
#. Jeżeli, którykolwiek się nie zgadza, wyrzuć wyjątek ``TypeError``
#. Wyjątek ma wypisywać:

    - nazwę parametru, który ma nieprawidłowy typ,
    - listę dozwolonych typów.
