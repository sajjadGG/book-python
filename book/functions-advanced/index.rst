********************************
Zmienna ilość argumentów funkcji
********************************


Operator ``*`` i ``**``
=======================
- ``*`` zwykle nazywa się ``*args`` (arguments) - argumenty pozycyjne (anonimowe)
- ``**`` zwykle nazywa się ``**kwargs`` (keyword arguments) - argumenty nazwane


Przyjmowanie z funkcji zmiennej ilości argumentów
=================================================
.. code-block:: python

    a, b = [1, 2]
    a, b = (1, 2)
    a, b = 1, 2

.. code-block:: python

    def numbers():
        return 1, 2

    a, b = numbers()

.. code-block:: python

    line = 'jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash'
    line.split(':')
    # ['jimenez', 'x', '1001', '1001', 'José Jiménez', '/home/jimenez', '/bin/bash']


    # username, password, uid, gid, name, home, shell = line.split(':')

    username, password, *others = line.split(':')

    username  # jimenez
    password  # x
    others  # ['1001', '1001', 'José Jiménez', '/home/jimenez', '/bin/bash']



    *others, shell = line.split(':')

    others  # ['jimenez', 'x', '1001', '1001', 'José Jiménez', '/home/jimenez']
    shell  # /bin/bash


    # if you're not using ``others`` later in your code
    username, *_ = line.split(':')


.. code-block:: python

    def sensor_temperatury():
        # ładniej byłoby gdyby programista napisał
        # {'napiecie': 10, 'natezenie': 20, 'rezystancja': 30, 'czas': 5, 'location': 'laboratorium'}
        # ale programiści niskopoziomowi zwykle zwracają jako list...
        return (10, 20.6, 30, 5, 'laboratorium')

    napiecie, natezenie, *_ = sensor_temperatury()

.. code-block:: python

    *a, b, *c = [1, 2, 3, 4, 5, 6, 7]
    # SyntaxError: two starred expressions in assignment

Definiowanie funkcji ze zmienną ilością parametrów
==================================================
.. code-block:: python

    def wyswietl_argumenty(a, b, c=0, *pozycyjne, **nazwane):
        print(f'argument a: {a}')  # 1
        print(f'argument b: {b}')  # 2
        print(f'argument c: {c}')  # 3
        print(f'argumenty pozycyjne: {pozycyjne}')    # 4, 5, 6
        print(f'argumenty nazwane: {nazwane}')        # d=5, e=6


    wyswietl_argumenty(1, 2, 3, 4, 5, 6, d=5, e=6)

Wewnątrz funkcji będziemy mieli dostępną zmienną ``dopasowane`` o wartości 1, zmeinną ``pozycyjne``, zawierającą listę elementów (2, 3, 4) oraz zmienną słownikową ``nazwane``, która ma klucze 'c' i 'd', które przechowują wartości, odpowiednio, 5 i 6.

Przez konwencję:

    - ``pozycyjne`` - ``args``
    - ``nazwane`` - ``kwargs``

.. code-block:: python

    def wyswietl_argumenty(a, b, c=0, *args, **kwargs):
        print(f'argument a: {a}')  # 1
        print(f'argument b: {b}')  # 2
        print(f'argument c: {c}')  # 3
        print(f'argumenty args: {args}')    # 4, 5, 6
        print(f'argumenty kwargs: {kwargs}')        # d=5, e=6


    wyswietl_argumenty(1, 2, 3, 4, 5, 6, d=5, e=6)

Kiedy to się przydaje
---------------------
.. code-block:: python

    def celsius_to_fahrenheit(*degrees):
        return [degree*1.8+32 for degree in degrees]

    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]


Przekazywanie do funkcji zmiennej ilości parametrów
===================================================
Przykładowe zastosownaie operatorów ``*`` i ``**`` polega na wykorzystaniu ich przy wywołaniu funkcji. Wtedy, wykorzystując operator ``*``, kolejne elementy listy albo krotki będą przekazane jako kolejne argumenty funkcji, a wykorzystując operator ``**`` kolejne elementy zmiennej słownikowej będą przekazane jako nazwane argumenty. Oznacza to, że na przykład argument ``x`` funkcji, przyjmie wartość ``vector['x']``.

.. code-block:: python

    def my_function(x, y, z):
        print(x, y, z)

    vector = (1, 0, 1)
    my_function(*vector)
    # 1, 0, 1

    vector = {'y': 1, 'x': 0, 'z': 1}
    my_function(**vector)
    # 0, 1, 1


.. code-block:: python

    def wyswietl(a, b, c=0):
        print(locals())

    wyswietl(1, 2, 3)
    # {'a': 1, 'b': 2, 'c': 3}

    dane = (1, 2, 3)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3}

    dane = (1, 2)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 0}

.. code-block:: python

    def wyswietl(a, b, c=0, *args):
        print(locals())

    dane = (1, 2, 3, 4)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4,)}

    dane = (1, 2, 3, 4, 5, 6, 7)
    wyswietl(*dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6, 7)}

    wyswietl(1, 2)
    # {'a': 1, 'b': 2, 'c': 0, 'args': ()}

.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    wyswietl(1, 2, x=77, y=99)
    # {'a': 1, 'b': 2, 'c': 0, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    wyswietl(1, 2, x=77, y=99, c=7)
    # {'a': 1, 'b': 2, 'c': 7, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    dane = {'x': 77, 'y': 99}
    wyswietl(1, 2, 3, **dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    dane = {'x': 77, 'y': 99, 'a': 7}
    wyswietl(1, 2, 3, **dane)
    # Traceback (most recent call last):
    #   ...
    # TypeError: wyswietl() got multiple values for argument 'a'

.. code-block:: python

    def wyswietl(a, b, c=0, *args, **kwargs):
        print(locals())

    wyswietl(1, 2, 3, 4, 5, 6, x=77, y=99)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}

    pozycyjne = (4, 5, 6)
    nazwane = {'x': 77, 'y': 99}
    wyswietl(1, 2, 3, *pozycyjne, **nazwane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}

Przykładowe zastosowanie
========================
.. code-block:: python

    from typing import List

    def celsius_to_fahrenheit(*degrees) -> List[float]:
        return [x * 1.8 + 32 for x in degrees]


    celsius_to_fahrenheit(1)
    # [33.8]

    celsius_to_fahrenheit(1, 2, 3, 4, 5)
    # [33.8, 35.6, 37.4, 39.2, 41.0]



.. code-block:: python

    class Kontakt:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    Kontakt(imie='Max', nazwisko='Peck')

.. code-block:: python

    class Osoba:
        first_name = 'Max'
        last_name = 'Peck'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)
            return '{first_name} {last_name}'.format(first_name='Max', last_name='Peck')
            return f'{self.first_name} {self.last_name}'


Assignments
===========
.. todo:: zrobić zadania do rozwiązania dla parametrów z gwiazdką
