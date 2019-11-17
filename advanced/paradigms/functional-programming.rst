**********************
Functional Programming
**********************


Lambda - Anonymous functions
============================

Example 1
---------
.. code-block:: python

    DATA = [1, 2, 3, 4]


    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False


    output = filter(is_even, DATA)
    print(list(output))
    # [2, 4]

.. code-block:: python

    DATA = [1, 2, 3, 4]

    output = filter(lambda x: x % 2 == 0, DATA)
    print(list(output))
    # [2, 4]

Example 2
---------
.. code-block:: python

    DATA = [
        {'user': 'twardowski', 'uid': 1000},
        {'user': 'root', 'uid': 0},
    ]

    def is_system_user(data):
        if data['uid'] < 1000:
            return True
        else:
            return False

    system_users = []

    for user in DATA:
        if is_system_user(user):
            system_users.append(user)

    print(system_users)
    # [{'user': 'root', 'uid': 0}]


.. code-block:: python

    DATA = [
        {'user': 'twardowski', 'uid': 1000},
        {'user': 'root', 'uid': 0},
    ]


    system_users = filter(lambda x: x['uid'] < 1000, DATA)

    print(list(system_users))
    # [{'user': 'root', 'uid': 0}]

Monkey patching
---------------
.. code-block:: python

    class Astronaut:
        pass

    jan = Astronaut()
    jan.say_hello = lambda: print('hello')

    jan.say_hello()

Built-in functions
==================

``map()``
---------
.. code-block:: python

    DATA = [1, 2, 3]

    output = map(float, DATA)

    print(output)
    # <map object at 0x11d2241d0>

    print(list(output))
    # [1.0, 2.0, 3.0]

.. code-block:: python

    DATA = [1, 2, 3]

    def square(x):
        return pow(x, 2)

    output = map(square, DATA)

    print(list(output))
    # [1, 4, 9]

.. code-block:: python

    DATA = [1, 2, 3]

    output = map(lambda x: pow(x, 2), DATA)

    print(list(output))
    # [1, 4, 9]

``zip()``
---------
.. code-block:: python

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    output = zip(keys, values)

    print(output)
    # <zip object at 0x11cfea280>

    print(list(output))
    # [('a', 1), ('b', 2), ('c', 3)]

.. code-block:: python

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]

    output = zip(keys, values)

    print(dict(output))
    # {'a': 1, 'b': 2, 'c': 3}

``filter()``
------------
.. code-block:: python

    DATA = [
        {'name': 'Jan Twardowski', 'age': 21},
        {'name': 'Mark Watney', 'age': 25},
        {'name': 'Melissa Lewis', 'age': 18},
    ]

    def is_adult(person):
        if person['age'] >= 21:
            return True
        else:
            return False


    output = filter(is_adult, DATA)
    print(list(output))
    # [
    #   {'name': 'Jan Twardowski', 'age': 21},
    #   {'name': 'Mark Watney', 'age': 25},
    # ]

.. code-block:: python

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False


    DATA = range(0, 10)

    output = filter(is_even, DATA)

    print(list(output))
    # [0, 2, 4, 6, 8]

.. code-block:: python

    DATA = range(0, 10)

    output = filter(lambda x: x % 2 == 0, DATA)

    print(list(output))
    # [0, 2, 4, 6, 8]


.. code-block:: python

    output = filter(lambda x: x % 2 == 0, range(0, 10))

    print(list(output))
    # [0, 2, 4, 6, 8]

``all()``
---------
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

.. code-block:: python

    def all(iterable):
        if not iterable:
            return False

        for element in iterable:
            if not element:
                return False

        return True

``any()``
---------
Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

.. code-block:: python

    def any(iterable):
        if not iterable:
            return False

        for element in iterable:
            if element:
                return True

        return False


``functools``
=============

.. code-block:: python

    from functools import reduce


    DATA = [1, 2, 3, 4, 5]

    def add(x, y):
        return (x + y)

    output = reduce(add, DATA)

    print(output)
    # 15

.. code-block:: python

    from functools import reduce


    DATA = [1, 2, 3, 4, 5]

    output = reduce(lambda x, y: x + y, DATA)

    print(output)
    # 15

``lru_cache``
-------------
.. code-block:: python

    from functools import lru_cache


    @lru_cache(maxsize=None)
    def fib(num):
        if num < 2:
            return num
        else:
            return fib(num-1) + fib(num-2)


    fib(16)
    # 987

    fib
    # <functools._lru_cache_wrapper object at 0x11cce6730>

    fib.cache_info()
    # CacheInfo(hits=14, misses=17, maxsize=None, currsize=17)

memoize
-------
.. code-block:: python

    def factorial(n):
        if not hasattr(factorial, '__cache__'):
            factorial.__cache__ = {1: 1}

        if not n in factorial.__cache__:
            factorial.__cache__[n] = n * factorial(n - 1)

        return factorial.__cache__[n]


    factorial(5)
    # 120

    factorial.__cache__
    # {1:1, 2:2, 3:6, 4:24, 5:120}

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

Callback
========
.. code-block:: python

    def http(obj):
        response = requests.request(
            method=obj.method,
            data=obj.data,
            path=obj.path)

        if response == 200:
            return obj.on_success(response)
        else:
            return obj.on_error(response)


    class Request:
        method = 'GET'
        path = '/index'
        data = None

        def on_success(self, response):
            print('Success!')

        def on_error(self, response):
            print('Error')

    http(
        Request()
    )


Assignments
===========

``map()``, ``filter()`` i ``lambda``
------------------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functional_map_filter_lambda.py`

#. Używając generatora zbuduj listę zawierającą wszystkie liczby podzielne przez 3 z zakresu od 1 do 33:
#. Używając funkcji ``filter()`` usuń z niej wszystkie liczby parzyste
#. Używając wyrażenia ``lambda`` i funkcji ``map()`` podnieś wszystkie elementy tak otrzymanej listy do sześcianu
#. Odpowiednio używając funkcji ``sum()``  i ``len()`` oblicz średnią arytmetyczną z elementów tak otrzymanej listy.

Zbalansowanie nawiasów
----------------------
* Complexity level: medium
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/functional_brackets.py`

#. Napisz kod, który za pomocą rekurencji sprawdzi zbalansowanie nawiasów, tzn. czy ilość otwieranych nawiasów jest równa ilości nawiasów zamykanych.
#. Zwórć uwagę, że mogą być cztery typy nawiasów:

    #. okrągłe: ``(`` i ``)``
    #. kwadratowe: ``[`` i ``]``
    #. klamrowe ``{`` i ``}``
    #. trójkątne ``<`` i ``>``

.. code-block:: python

    def zbalansowanie_nawiasow(ciag_znakow: str) -> bool:
        """
        >>> zbalansowanie_nawiasow('{}')
        True
        >>> zbalansowanie_nawiasow('()')
        True
        >>> zbalansowanie_nawiasow('[]')
        True
        >>> zbalansowanie_nawiasow('<>')
        True
        >>> zbalansowanie_nawiasow('')
        True
        >>> zbalansowanie_nawiasow('(')
        False
        >>> zbalansowanie_nawiasow('}')
        False
        >>> zbalansowanie_nawiasow('(]')
        False
        >>> zbalansowanie_nawiasow('([)')
        False
        >>> zbalansowanie_nawiasow('[()')
        False
        >>> zbalansowanie_nawiasow('{()[]}')
        True
        >>> zbalansowanie_nawiasow('() [] () ([]()[])')
        True
        >>> zbalansowanie_nawiasow("( (] ([)]")
        False
        """
        pass

