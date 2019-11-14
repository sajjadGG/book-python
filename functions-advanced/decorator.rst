*********
Decorator
*********


What is decorator
=================
* Decorator is a function, which takes another function as it's argument
* Decorators can:

    * Do things before call
    * Do things after call
    * Modify arguments
    * Modify returned value
    * Avoid calling
    * Modify globals
    * Add or change metadata

Code:
    .. code-block:: python

        @my_decorator
        def my_function(*args, **kwargs):
            pass

Is equal to:
    .. code-block:: python

        my_function = my_decorator(my_function)


Definition
==========

Decorating functions
--------------------
* ``my_decorator`` is decorator name
* ``fn`` is a pointer to function which is being decorated (``my_function`` in this case)
* ``wrapper`` is a closure function
* ``wrapper`` name is a convention, but you can name it anyhow
* ``wrapper`` gets arguments passed to ``my_function``
* by calling ``fn(*args, **kwargs)`` you actually run original (wrapped) function with it's original arguments
* decorator must return pointer to ``wrapper``

.. code-block:: python

    def my_decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
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

Method decorator
----------------
.. code-block:: python

    def if_permitted(method):
        def wrapper(instance, *args, **kwargs):
            if instance.can_something:
                return method(instance, *args, **kwargs)
            else:
                print('Sorry, you cannot do anything')
        return wrapper


    class MyClass:
        def __init__(self):
            self.can_something = True

        @if_permitted
        def do_something(self):
            print('Doing...')

        @if_permitted
        def do_something_else(self):
            print('Doing something else...')


    my = MyClass()

    my.do_something()           # Doing...
    my.do_something_else()      # Doing something else...

    my.can_something = False

    my.do_something()           # Sorry, you cannot do anything
    my.do_something_else()      # Sorry, you cannot do anything

Decorator with arguments
------------------------
Code:
    .. code-block:: python

        @my_decorator(my_param)
        def my_function(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        my_function = my_decorator(a, b)(my_function)

.. code-block:: python

    def my_decorator(a=1, b=2):
        def decorator(fn):
            def wrapper(*args, **kwargs):
                return fn(*args, **kwargs)
            return wrapper
        return decorator


    @my_decorator(a=1)
    def my_function(name):
        print(name)


    my_function('Jan Twardowski')
    # Jan Twardowski


Example
=======

Debug
-----
.. code-block:: python

    def debug(fn):
        def wrapper(*args, **kwargs):
            print(f'Calling {fn.__name__}, args: {args}, kwargs: {kwargs}')
            result = fn(*args, **kwargs)
            print(f'Result is {result}')
        return wrapper


    @debug
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # Calling add_numbers, args: (1, 2), kwargs: {}
    # Result is 3

    add_numbers(1, b=2)
    # Calling add_numbers, args: (1,), kwargs: {'b': 2}
    # Result is 3

    add_numbers(a=1, b=2)
    # Calling add_numbers, args: (), kwargs: {'a': 1, 'b': 2}
    # Result is 3

Cache
-----
.. code-block:: python

    CACHE = {}


    def cache(fn):
        def wrapper(n):
            if n not in CACHE:
                CACHE[n] = fn(n)
            return CACHE[n]
        return wrapper


    @cache
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    factorial(5)
    # 120

    print(CACHE)
    # {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}

File exists
-----------
.. code-block:: python

    import os


    def if_file_exists(fn):
        def check_path(filename):
            if os.path.exists(filename):
                return fn(filename)
            else:
                print(f'File "{filename}" does not exists')
        return check_path


    @if_file_exists
    def print_file(filename):
        with open(filename) as file:
            content = file.read()
            print(content)


    if __name__ == '__main__':
        print_file('/etc/passwd')
        print_file('/tmp/passwd')

Deprecated
----------
.. code-block:: python

    def deprecated(removed_in_version=None):
        def decorator(fn):
            def write_message(*args, **kwargs):
                name = fn.__name__
                file = fn.__code__.co_filename
                line = fn.__code__.co_firstlineno + 1
                message = f"Call to deprecated function {name} in {file} at line {line}"
                message += f'\nIt will be removed in {removed_in_version}'

                import warnings
                warnings.warn(message, DeprecationWarning)
                return fn(*args, **kwargs)

            return write_message
        return decorator


    @deprecated(removed_in_version=2.0)
    def my_function():
        pass


    my_function()
    # /tmp/my_script.py:11: DeprecationWarning: Call to deprecated function my_function in /tmp/my_script.py at line 19
    # It will be removed in 2.0

Timeout
-------
.. code-block:: python
    :caption: Decorator usage

    import signal
    from time import sleep


    def timeout(fn, seconds=2, error_message='Timeout'):

        def wrapper(*args, **kwargs):

            def handler(signum, frame):
                raise TimeoutError

            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            try:
                fn(*args, **kwargs)
            except TimeoutError:
                print(error_message)
            finally:
                signal.alarm(0)

        return wrapper


    @timeout
    def connect(username, password, host='127.0.0.1', port='80'):
        print('Connecting...')
        sleep(5)
        print('Connected')


    connect('admin', 'admin')

Cache
-----
.. code-block:: python

    class cache(dict):
        def __init__(self, fn):
            self.fn = fn

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            self[key] = self.fn(*key)
            return self[key]


    @cache
    def my_function(a, b):
        return a * b


    my_function(2, 4)       # 8
    my_function('hi', 3)    # 'hihihi'
    my_function('ha', 3)    # 'hahaha'
    my_function(2, 4)       # 8         # this is loaded from cache not computed

    my_function
    # {
    #   (2, 4): 8,
    #   ('hi', 3): 'hihihi',
    #   ('ha', 3): 'hahaha'
    # }


``functools``
=============

``@functools.wraps(fn)``
------------------------
.. code-block:: python
    :emphasize-lines: 19,22

    def my_decorator(fn):
        def wrapper(*args, **kwargs):
            """
            wrapper docstring
            """
            return fn(*args, **kwargs)
        return wrapper


    @my_decorator
    def my_function(x):
        """
        my_function docstring
        """
        print(x)


    print(my_function.__name__)
    # wrapper

    print(my_function.__doc__)
    # wrapper docstring

.. code-block:: python
    :emphasize-lines: 1,5,23,26

    from functools import wraps


    def my_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            """
            wrapper docstring
            """
            return fn(*args, **kwargs)
        return wrapper


    @my_decorator
    def my_function(x):
        """
        my_function docstring
        """
        print(x)


    print(my_function.__name__)
    # my_function

    print(my_function.__doc__)
    # my_function docstring

``@functools.cached_property(fn)``
------------------------------------
.. code-block:: python

    from functools import cached_property


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

    [fib(n) for n in range(16)]
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    fib.cache_info()
    # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)

``memoize``
-----------
.. code-block:: python

    from functools import wraps


    def memoize(func):
        cache = getattr(func, '__cache__', {})

        @wraps(func)
        def wrapper(*func_args):
            if func_args in cache:
                return cache[func_args]
            else:
                result = func(*func_args)
                cache[func_args] = result
                setattr(func, '__cache__', cache)
                return result

        return wrapper


    @memoize
    def fibonacci(n):
        if n < 2: return n
        return fibonacci(n - 1) + fibonacci(n - 2)


    print(fibonacci(25))


Przykład
========

Example 1
---------
.. code-block:: python

    def make_paragraph(fn):

        def decorator(*args, **kwargs):
            value = fn(*args, **kwargs)
            print(f'<p>{value}</p>')
            return value

        return decorator


    class HTMLReport:

        @make_paragraph
        def first_method(self, *args, **kwargs):
            return 'First Method'

        @make_paragraph
        def second_method(self, *args, **kwargs):
            return 'Second Method'


    if __name__ == "__main__":
        x = HTMLReport()
        x.first_method()
        x.second_method()

    """
    <p>First Method</p>
    <p>Second Method</p>
    """

Example 2
---------
.. code-block:: python

    class LoginCheck:
        def __init__(self, func):
            self._func = func

        def __call__(self, *args):
            if is_authenticated():
                return self._func(*func_args)
            else:
                return on_error()


    def is_authenticated():
        ...

    def on_error():
        print('Sorry - this site private')


    @LoginCheck
    def display_members_page():
        print('This is the members page')

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
.. code-block:: python
    :caption: Use case wykorzystania dekotatorów do poprawienia czytelności kodu Flask

    from flask import json
    from flask import Response
    from flask import render_template
    from flask import Flask

    app = Flask(__name__)


    @app.route('/summary')
    def summary():
        data = {'first_name': 'Jan', 'last_name': 'Twardowski'}
        return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        post = ... # get post from Database by post_id
        return render_template('post.html', post=post)


    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)


.. code-block:: python
    :caption: Use case wykorzystania dekotatorów do poprawienia czytelności kodu Django

    from django.shortcuts import render
    from django.contrib.auth.decorators import login_required


    def edit_profile(request):
        """
        Function checks whether user is_authenticated
        If not, user will be redirected to login page
        """
        if not request.user.is_authenticated:
            return render(request, 'templates/login_error.html')
        else:
            return render(request, 'templates/edit-profile.html')


    @login_required
    def edit_profile(request):
        """
        Decorator checks whether user is_authenticated
        If not, user will be redirected to login page
        """
        return render(request, 'templates/edit-profile.html')


Decorator library
=================
- https://wiki.python.org/moin/PythonDecoratorLibrary


Assignments
===========

Memoization
-----------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/decorator_memoize.py`

:English:
    .. todo:: English translation

:Polish:
    #. Dla danego kodu funkcji ``factorial`` (patrz poniżej)
    #. Stwórz ``CACHE: Dict[int, int]`` z wynikami wyliczenia funkcji

        - klucz: argument funkcji
        - wartość: wynik obliczeń

    #. Dodaj dekorator do funkcji ``factorial(n: int)`` z listingu poniżej
    #. Decorator ma sprawdzać przed uruchomieniem funkcji, sprawdź czy wynik został już wcześniej obliczony:

        - jeżeli tak, to zwraca dane z ``CACHE``
        - jeżeli nie, to oblicza, aktualizuje ``CACHE``, a następnie zwraca wartość

    #. Wykorzystując ``timeit`` porównaj prędkość działania z obliczaniem na bieżąco dla parametru 100


:Input:
    .. code-block:: python

        import sys
        from timeit import timeit

        sys.setrecursionlimit(5000)


        def factorial_nocache(n: int) -> int:
            if n == 0:
                return 1
            else:
                return n * factorial_nocache(n-1)

        duration_cache = timeit(
            stmt='factorial_cache(500); factorial_cache(400); factorial_cache(450); factorial_cache(350)',
            globals=globals(),
            number=10000,
        )

        duration_nocache = timeit(
            stmt='factorial_nocache(500); factorial_nocache(400); factorial_nocache(450); factorial_nocache(350)',
            globals=globals(),
            number=10000
        )

        print(f'factorial_cache time: {round(duration_cache, 4)} seconds')
        print(f'factorial_nocache time: {round(duration_nocache, 3)} seconds')
        print(f'Cached solution is {round(duration_nocache / duration_cache, 1)} times faster')

Prosty dekorator
----------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/decorator_abspath.py`

:English:
    .. todo:: English translation

:Polish:
    #. Program przechodzi przez pliki i katalogi wykorzystując ``os.walk``
    #. Wypisz nazwę pliku lub katalogu
    #. Stwórz dekorator do funkcji, który przed wypisaniem podmieni ścieżkę na bezwzględną (``path`` + ``filename``).

Type Checking Decorator
-----------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/decorator_check_types.py`

:English:
    .. todo:: English translation

:Polish:
    #. Na podstawie kodu (patrz poniżej)
    #. Stwórz dekorator ``check_types``
    #. Dekorator ma sprawdzać typy danych, wszystkich parametrów wchodzących do funkcji
    #. Jeżeli, którykolwiek się nie zgadza, wyrzuć wyjątek ``TypeError``
    #. Wyjątek ma wypisywać:

        - nazwę parametru, który ma nieprawidłowy typ,
        - listę dozwolonych typów.

:Input:
    .. code-block:: python

        def function(a: str, b: int) -> bool:
            return bool(a * b)

        print(function.__annotations__)
        # {'a': <class 'str'>, 'return': <class 'bool'>, 'b': <class 'int'>}
