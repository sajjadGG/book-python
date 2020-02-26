*********************************
Function Decorator with Functions
*********************************


Syntax
======
* ``decorator`` is a decorator name
* ``function`` is a function name
* ``args`` arbitrary number of positional arguments
* ``kwargs`` arbitrary number of keyword arguments

Syntax:
    .. code-block:: python

        @decorator
        def my_function(*args, **kwargs):
            pass

Is equivalent to:
    .. code-block:: python

        my_function = decorator(my_function)


Definition
==========
* ``function`` is a pointer to function which is being decorated
* By calling ``function(*args, **kwargs)`` you actually run original (wrapped) function with it's original arguments
* Decorator must return pointer to ``wrapper``
* ``wrapper`` is a closure function
* ``wrapper`` name is a convention, but you can name it anyhow
* ``wrapper`` gets arguments passed to ``function``

.. code-block:: python

    def decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper


Usage
=====
.. code-block:: python

    def decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper

    @my_decorator
    def my_function(x):
        print(x)


    my_function('hello')
    # hello


Examples
========

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

Debug
-----
.. code-block:: python

    def debug(fn):
        def wrapper(*args, **kwargs):
            print(f'Calling "{fn.__name__}()", args: {args}, kwargs: {kwargs}')
            result = fn(*args, **kwargs)
            print(f'Result is {result}')
            return result
        return wrapper


    @debug
    def add_numbers(a, b):
        return a + b


    add_numbers(1, 2)
    # Calling "add_numbers()", args: (1, 2), kwargs: {}
    # Result is 3

    add_numbers(1, b=2)
    # Calling "add_numbers()", args: (1,), kwargs: {'b': 2}
    # Result is 3

    add_numbers(a=1, b=2)
    # Calling "add_numbers()", args: (), kwargs: {'a': 1, 'b': 2}
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

Memoize
-------
.. code-block:: python

    def cache(fn):
        def wrapper(n):
            cache = getattr(wrapper, '__cache__', {})
            if n not in cache:
                print(f'"n={n}" Not in cache. Calculating...')
                cache[n] = fn(n)
                setattr(wrapper, '__cache__', cache)
            else:
                print(f'"n={n}" Found in cache. Fetching...')
            return cache[n]
        return wrapper


    @cache
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


    print(factorial(3))
    # "n=3" Not in cache. Calculating...
    # "n=2" Not in cache. Calculating...
    # "n=1" Not in cache. Calculating...
    # "n=0" Not in cache. Calculating...
    # 6

    print(factorial.__cache__)
    # {3: 6}

    print(factorial(5))
    # "n=5" Not in cache. Calculating...
    # "n=4" Not in cache. Calculating...
    # "n=3" Found in cache. Fetching...
    # 120

    print(factorial.__cache__)
    # {3: 6, 4: 24, 5: 120}

    print(factorial(6))
    # "n=6" Not in cache. Calculating...
    # "n=5" Found in cache. Fetching...
    # 720

    print(factorial.__cache__)
    # {3: 6, 4: 24, 5: 120, 6: 720}

    print(factorial(4))
    # "n=4" Found in cache. Fetching...
    # 24

    print(factorial.__cache__)
    # {3: 6, 4: 24, 5: 120, 6: 720}

Flask URL Routing
-----------------
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

Django Login Required
---------------------
* Decorator checks whether user is_authenticated.
* If not, user will be redirected to login page.

.. code-block:: python

    from django.shortcuts import render


    def edit_profile(request):
        if not request.user.is_authenticated:
            return render(request, 'templates/login_error.html')
        else:
            return render(request, 'templates/edit-profile.html')


    def delete_profile(request):
        if not request.user.is_authenticated:
            return render(request, 'templates/login_error.html')
        else:
            return render(request, 'templates/delete-profile.html')

.. code-block:: python

    from django.shortcuts import render
    from django.contrib.auth.decorators import login_required


    @login_required
    def edit_profile(request):
        return render(request, 'templates/edit-profile.html')


    @login_required
    def delete_profile(request):
        return render(request, 'templates/delete-profile.html')


Assignments
===========

Memoization
-----------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/decorator_memoize.py`

:English:
    #. Create function ``factorial_cache(n: int) -> int``
    #. Create ``CACHE: Dict[int, int]`` with computation results from function

        - key: function argument
        - value: computation result

    #. Create decorator ``@cache``
    #. Decorator must check before running function, if for given argument the computation was already done:

        - if yes, return from ``CACHE``
        - if not, calculate new result, update cache and return computed value

    #. Using ``timeit``

:Polish:
    #. Stwórz funkcję ``factorial_cache(n: int) -> int``
    #. Stwórz ``CACHE: Dict[int, int]`` z wynikami wyliczenia funkcji

        - klucz: argument funkcji
        - wartość: wynik obliczeń

    #. Stwórz dekorator ``@cache``
    #. Decorator ma sprawdzać przed uruchomieniem funkcji, czy dla danego argumenu wynik został już wcześniej obliczony:

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

Type Checking Decorator
-----------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/decorator_check_types.py`

:English:
    .. todo:: English translation

:Polish:
    #. Na podstawie kodu (patrz sekcja input)
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
