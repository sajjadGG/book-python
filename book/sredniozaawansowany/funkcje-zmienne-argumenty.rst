********************************
Zmienna ilość argumentów funkcji
********************************

.. todo:: zrobić zadania do rozwiązania dla parametrów z gwiazdką


Operator ``*`` i ``**``
=======================
Użycie operatora ``*`` przy definicji funkcji powoduje umożliwienie przekazywanie do funkcji dodatkowych parametrów anonimowych. Zazwczaj zmienna, która jest przy tym operatorze nazywa się ``*args`` (arguments).

Użycie operatora ``**`` przy definicji funkcji powoduje umożliwienie przekazywania do niej dodatkowych argumentów nazwanych. Zazwczaj zmienna, która jest przy tym operatorze nazywa się ``**kwargs`` (keyword arguments).


Definiowanie funkcji ze zmienną ilością parametrów
==================================================
.. code-block:: python

    def wyswietl_argumenty(dopasowane, *pozycyjne, **nazwane):
        print(f'argumenty dopasowane: {dopasowane}')  # 1
        print(f'argumenty pozycyjne: {pozycyjne}')    # 2, 3, 4
        print(f'argumenty nazwane: {nazwane}')        # c=5, d=6


    wyswietl_argumenty(1, 2, 3, 4, c=5, d=6)

Wewnątrz funkcji będziemy mieli dostępną zmienną ``dopasowane`` o wartości 1, zmeinną ``pozycyjne``, zawierającą listę elementów (2, 3, 4) oraz zmienną słownikową ``nazwane``, która ma klucze 'c' i 'd', które przechowują wartości, odpowiednio, 5 i 6.

Przez konwencję ``pozycyjne`` powinny być nazwane ``args``, a ``nazwane`` - ``kwargs`` (keyword arguments).

.. code-block:: python

    def wyswietl_argumenty(dopasowane, *args, **kwargs):
        print(f'argumenty dopasowane: {dopasowane}')  # 1
        print(f'argumenty pozycyjne: {args}')         # 2, 3, 4
        print(f'argumenty nazwane: {kwargs}')         # c=5, d=6


    wyswietl_argumenty(1, 2, 3, 4, c=5, d=6)

Przykładowe zastosownaie operatorów ``*`` i ``**`` polega na wykorzystaniu ich przy wywołaniu funkcji. Wtedy, wykorzystując operator ``*``, kolejne elementy listy albo krotki będą przekazane jako kolejne argumenty funkcji, a wykorzystując operator ``**`` kolejne elementy zmiennej słownikowej będą przekazane jako nazwane argumenty. Oznacza to, że na przykład argument ``x`` funkcji, przyjmie wartość ``vector['x']``.

.. code-block:: python

    >>> def my_function(x, y, z):
    ...    print(x, y, z)

    >>> vector = (1, 0, 1)
    >>>  my_function(*vector)
    1, 0, 1

    >>> vector = {'y': 1, 'x': 0, 'z': 1}
    >>> my_function(**vector)
    0, 1, 1

.. warning:: Nie przywiązuj się do nazewnictwa ``*args`` i ``**kwargs``, chociaż jest to konwencja!!

    .. code-block:: python

        def wyswietl_argumenty(dopasowane, *pozycyjne, **nazwane):
            print(f'argumenty dopasowane: {dopasowane}')  # 1
            print(f'argumenty pozycyjne: {pozycyjne}')    # 2, 3, 4
            print(f'argumenty nazwane: {nazwane}')        # c=5, d=6


        wyswietl_argumenty(1, 2, 3, 4, c=5, d=6)

    Taki zapis jest również możliwy, chociaż bardzo mylący

    .. code-block:: python

        def wyswietl_argumenty(dopasowane, *kwargs, **args):
            print(f'argumenty dopasowane: {dopasowane}')  # 1
            print(f'argumenty pozycyjne: {kwargs}')       # 2, 3, 4
            print(f'argumenty nazwane: {args}')           # c=5, d=6


        wyswietl_argumenty(1, 2, 3, 4, c=5, d=6)


Przekazywanie do funkcji zmiennej ilości parametrów
===================================================
.. code-block:: python

    >>> def wyswietl(a, b, c=0):
    ...    print(locals())

    >>> wyswietl(1, 2, 3)
    {'a': 1, 'b': 2, 'c': 3}

    >>> dane = (1, 2, 3)
    >>> wyswietl(*dane)
    {'a': 1, 'b': 2, 'c': 3}

    >>> dane = (1, 2)
    >>> wyswietl(*dane)
    {'a': 1, 'b': 2, 'c': 0}

.. code-block:: python

    >>> def wyswietl(a, b, c=0, *args):
    ...    print(locals())

    >>> dane = (1, 2, 3, 4)
    >>> wyswietl(*dane)
    {'a': 1, 'b': 2, 'c': 3, 'args': (4,)}

    >>> dane = (1, 2, 3, 4, 5, 6, 7)
    >>> wyswietl(*dane)
    {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6, 7)}

    >>> wyswietl(1, 2)
    {'a': 1, 'b': 2, 'c': 0, 'args': ()}

.. code-block:: python

    >>> def wyswietl(a, b, c=0, *args, **kwargs):
    ...     print(locals())

    >>> wyswietl(1, 2, x=77, y=99)
    {'a': 1, 'b': 2, 'c': 0, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    >>> wyswietl(1, 2, x=77, y=99, c=7)
    {'a': 1, 'b': 2, 'c': 7, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

    >>> dane = {'x': 77, 'y': 99}
    >>> wyswietl(1, 2, 3, **dane)
    {'a': 1, 'b': 2, 'c': 3, 'args': (), 'kwargs': {'x': 77, 'y': 99}}

.. code-block:: python

    >>> def wyswietl(a, b, c=0, *args, **kwargs):
    ...     print(locals())

    >>> wyswietl(1, 2, 3, 4, 5, 6, x=77, y=99)
    {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}

    >>> pozycyjne = (4, 5, 6)
    >>> nazwane = {'x': 77, 'y': 99}
    >>> wyswietl(1, 2, 3, *pozycyjne, **nazwane)
    {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}


Przyjmowanie z funkcji zmiennej ilości argumentów
=================================================
.. code-block:: python

    >>> value, _ = function()
    >>> value, *args = function()

.. code-block:: python

    def liczby_0_do_5():
        return range(0, 5)

    pierwsza, druga, *pozostale = liczby_0_do_5()
    # pierwsza == 0
    # druga == 1
    # pozostale == (2, 3, 4)

.. code-block:: python

    def create_or_update():
        return True, [
            {'id': 1, 'imie': 'Ivan', 'nazwisko': 'Ivanovic'},
            {'id': 2, 'imie': 'José', 'nazwisko': 'Jiménez'},
        ], 2, str('No Error')

    # czy_utworzone, objects, count, error = create_or_update()
    bylo_utworzone, *_  = create_or_update()

    if bylo_utworzone:
        print('utworzone')
    else:
        print('zmodyfikowane')


.. code-block:: python

    def sensor_temperatury():
        # ładniej byłoby gdyby programista napisał
        # {'napiecie': 10, 'natezenie': 20, 'rezystancja': 30, 'czas': 5, 'location': 'laboratorium'}
        # ale programiści niskopoziomowi zwykle zwracają jako list...
        return (10, 20.6, 30, 5, 'laboratorium')

    # z funkcji dopasuje nam dwa pierwsze elementy, a kolejne umieści w ``tuple`` o nazwie ``_``
    # Przez konwencję, jeżeli nie korzystamy później z argumentów, to możemy przypisać je do ``_``
    napiecie, natezenie, *_ = sensor_temperatury()


Przykładowe zastosowanie
========================
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

Zadania kontrolne
=================
