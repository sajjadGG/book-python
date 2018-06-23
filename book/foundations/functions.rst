*********
Functions
*********


* Funkcje pozwalają na wielokrotne używanie tego samego kodu.
* Znacznie poprawiają także czytelność kodu i go porządkują.


Function definition
===================
.. code-block:: python

    def hello():
        print('My name José Jiménez')

Callable
--------
.. code-block:: python

    def hello():
        print('My name José Jiménez')

    hello  # <function hello at 0x0C55D420>
    type(hello)  # <class 'function'>

.. code-block:: python

    type(str)  # <class 'type'>
    type('hello')  # <class 'str'>
    'hello'()  # TypeError: 'str' object is not callable


Naming convention
=================
#. Nie robimy CamelCase
#. Używanie ``_`` w nazwach (snake_case)
#. Funkcje o nazwie zaczynającej się od ``_`` przez konwencję są traktowane jako prywatne (w Pythonie nie ma private/protected/public).
#. Funkcje o nazwie zaczynającej się od ``__`` i kończących się na ``__`` przez konwencję są traktowane jako systemowe.
#. Nazwy opisowe funkcji
#. ``print_()``
#. ``__nazwa_funkcji()``


Returning values
================
#. Słowo kluczowe ``return`` wskazuje funkcji jaką wartość ma dana funkcja zwrócić.
#. Wykonanie linii ze słowem kluczowym ``return`` kończy wykonywanie funkcji.

.. code-block:: python

    def sum(a, b):
        return a + b

    sum(2, 3)  # 5

.. code-block:: python

    def sum(a, b):
        return a + b
        print('Total is', a + b)  # this won't be executed

    sum(2, 3)  # 5

Returning simple types
----------------------
.. code-block:: python

    def function():
        return 'José Jiménez'

    def function():
        return True

    def function():
        return None

    def function():
        # Python always return something, in this case ``return None``
        pass

    def function():
        return {'first_name': 'José', 'last_name': 'Jiménez'}

    def function():
        return 1, 'foobar'

    def function():
        return (5, 10, 15, 'foobar')

    def function():
        return [1, 2.5, 'foobar']

Returning nested types
----------------------
.. code-block:: python

    def function():
        return [
            {'first_name': 'Max', 'last_name': 'Peck'},
            {'first_name': 'Иван', 'last_name': 'Иванович', 'agency': {'name': 'roscosmos'}},
            {'first_name': 'José', 'last_name': 'Jiménez', 'missions': ['mercury', 'apollo']},
        ]

Returning function (callable)
-----------------------------
.. code-block:: python

    def my_func():
        return 'José Jiménez'

    def function():
        return my_func


    foo = function()
    # <function __main__.my_func()>

    foo()
    # 'José Jiménez'

.. code-block:: python

    import datetime

    print(datetime.datetime.now())

    now = datetime.datetime.now
    print(now())
    print(now())

    now = datetime.datetime.now()
    print(now)
    print(now)


Function arguments
==================
Argumenty funkcji to wartości na których ta funkcja wykonuje operacje. W idealnym przypadku wartość wyjściowa funkcji powinna zależeć jedynie od jej argumentów.

.. code-block:: python

    def add(a, b):
        return a + b

    add(1, 2)
    # 3

Variable scope
--------------
* ``globals()``
* ``locals()``

.. code-block:: python

    def add(a, b):
        print(locals())

    add(1, 2)
    # {'a': 1, 'b': 2}

Type annotations
----------------
* Od Python 3.5

.. code-block:: python

    >>> def dodaj(a: int, b: float) -> float:
    ...    return float(a + b)

    >>> dodaj(1, 2.0)
    3.0

.. note:: więcej na ten temat w rozdziale dotyczącym :numref:`Type Annotation`

Named arguments
---------------
Każdy argument ma swoją nazwę przez którą uzyskujemy dostęp do wartości argumentu w ciele funkcji. Ta nazwa może też być używana do przypisania wartości przy wywołaniu funkcji.

.. code-block:: python

    def substract(a, b):
        return a - b

    substract(a=0, b=1)
    # -1

    substract(0, b=1)
    # -1

    substract(b=1, a=0)
    # -1

    substract(1, 0)
    # 0

Arguments with default value
----------------------------
#. Argument funkcji może mieć wartość domyślną.
#. Funkcja przyjmie tą wartość jeżeli użytkownik nie zdefiniuje tego argumentu.
#. Argumenty z wartością domyślną muszą być skrajnie po prawej stronie.

.. code-block:: python

    def echo(text='default string'):
         print(text)

    echo('my string')
    # my string

    echo(text='my string')
    # my string

    echo()
    # default string

.. code-block:: python

    def server(username, password, host='127.0.0.1', port=80, ssl=True):
        print(f'host={host}, username={username}, password={password}, port={port}, ssl={ssl})


    # Kolejność ma znaczenie i łatwo się pomylić
    # Trudno również powiedzieć co znaczy ostatni parametr True
    server('admin', 'admin', 'localhost', 80, True)

    # argumenty definiowane są jawnie i trudniej się pomylić
    # kod jest bardziej przejrzysty
    # dla nazwanych argumentów kolejność nie ma znaczenia
    server(host='localhost', user='admin', password='admin', ssl=True)

    server(
        host='localhost',
        user='admin',
        password='admin',
        port=443,
        ssl=True,
    )


Recurrence
==========
.. code-block:: python

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)


Assignments
===========

Integer to string
-----------------
#. Napisz funkcję ``int_to_str``
#. Funkcja zamieni dowolego ``int`` lub ``float`` na formę tekstową.

    .. code-block:: python

        >>> int_to_str(1969)
        'one nine six nine'

        >>> int_to_str(31337)
        'three one three three seven'

        >>> int_to_str(13.37)
        'one three and three seven'

        >>> int_to_str(31.337)
        'three one and three three seven'

#. Wersja zaawansowana - pełne nazwy liczb

    .. code-block:: python

        >>> int_to_str(1969)
        'one thousand nine hundred sixty nine'

        >>> int_to_str(13.37)
        'thirteen and thirty seven hundredths'

:Założenia:
    * Nazwa pliku: ``functions_int_str.py``
    * Szacunkowa długość kodu: około 15 linii
    * Maksymalny czas na zadanie: 15 min

:Wymagania:
    * max 6 cyfr przed przecinkiem
    * max 5 cyfr po przecinku

:Co zadanie sprawdza?:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Roman numbers
-------------
#. Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.
#. Napisz drugą funkcję, która dokona procesu odwrotnego.

:Co zadanie sprawdza?:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Sprawdzanie czy element istnieje w ``dict``
    * Rzutowanie i konwersja typów

:Założenia:
    * Nazwa pliku: ``functions_roman.py``
    * Szacunkowa długość kodu: około 15 linii
    * Maksymalny czas na zadanie: 15 min