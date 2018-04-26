.. _Funkcje:

*******
Funkcje
*******

Funkcje pozwalają na wielokrotne używanie tego samego kodu. Znacznie poprawiają także czytelność kodu i go porządkują.


Definiowanie funkcji
====================

.. code-block:: python

    def hello():
        print('hello world')

Konwencja nazewnicza funkcji
============================

* CamelCase? Nie?! Używanie ``_`` w nazwach (snake_case)
* Funkcje o nazwie zaczynającej się od ``_`` przez konwencję są traktowane jako prywatne (w Pythonie nie ma private/protected/public).
* Funkcje o nazwie zaczynającej się od ``__`` i kończących się na ``__`` przez konwencję są traktowane jako systemowe.
* Nazwy opisowe funkcji
* ``nazwa_funkcji_()``
* ``__nazwa_funkcji()``

Argumenty do funkcji
====================
Argumenty funckji to wartości na których ta funckja wykonuje operacje. W idealnym przypadku wartość wyjściowa funkcji powinna zależeć jedynie od jej argumentów.

.. code-block:: python

    >>> def dodaj(a, b):
    ...    return a + b

    >>> dodaj(1, 2)
    3


Nazwy argumentów
-----------------

Każdy argument ma swoją nazwę przez którą uzyskujemy dostęp do wartości argumentu w ciele funkcji. Ta nazwa może też być używana do przypisania wartości przy wywołaniu funkcji.

.. code-block:: python

    >>> dodaj(a=1, b=2)
    3

    >>> def podziel(a, b):
    ...     return a / b

    >>> podziel(a=1, b=2)
    0.5

    >>> podziel(b=2, a=1)
    0.5


Argumenty z wartością domyślną
------------------------------
Argument funkcji może mieć także wartość domyślną, z której funkcja skorzysta jeżeli użytkownik nie zdefiniuje tego argumentu. Argumenty z wartością domyślną muszą być skrajnie po prawej stronie.

.. code-block:: python

    >>> def hello(tekst='hello world'):
    ...     print(tekst)

    >>> hello(tekst='ehlo')
    ehlo

    >>> hello()
    hello world

    >>> def convert(value, to='bin'):
    ...     if to == 'bin':
    ...         return bin(value)
    ...     elif to == 'hex':
    ...         return hex(value)
    ...     elif to == 'oct':
    ...         return oct(value)
    ...     else:
    ...         raise ValueError('`to` should be either bin, hex or oct!!')

Przykład praktyczny
-------------------
.. code-block:: python

    def server(host, user, password, port=1337):
        print(locals())


    # kolejność ma znaczenie
    # łatwo się pomylić
    server('localhost', 'admin', 'admin')

    # argumenty definiowane są jawnie
    # trudniej się pomylić
    # kod jest bardziej przejrzysty
    server(host='localhost', user='admin', password='admin')

    server(
        host='localhost',
        user='admin',
        password='admin',
        port=31337,
    )

    # dla nazwanych argumentów kolejność nie ma znaczenia
    server(
        port=31337,
        user='admin',
        host='localhost',
        password='admin'
    )

.. code-block:: python

    jira = Jira(
        url='http://localhost:8080',
        username='admin',
        password='admin',
        ssl_verify=False)

    # Zdecydowanie mniej czytelny zapis
    # Szczególnie nie wiadomo co False na koncu znaczy
    jira = Jira('http://localhost:8080', 'admin', 'admin', False)

Zwracanie wartości
==================

Zwracanie wartości prostych
---------------------------

.. code-block:: python

    def zwracanie_stringow():
        return 'bar'

    def zwracanie_bool():
        return True

    def zwracanie_wartosci_pustej():
        return None

    def zwracanie_niejawne():
        # Python always return something, in this case ``return None``
        pass

    def zwracanie_dict():
        return {'imie': 'Ivan', 'nazwisko': 'Ivanovic'}

    def zwracanie_tupli_1():
        return 10, 20.6, 30, 5, 'foobar'

    def zwracanie_tupli_2():
        return (10, 20.6, 30, 5, 'foobar')

    def zwracanie_listy():
        return [10, 20.6, 'foobar']

    def zwracanie_funkcji():
        return zwracanie_listy

Zwracanie typów złożonych
-------------------------
.. code-block:: python

    def zwracanie_zlozone():
        return [
            {'imie': 'Max', 'nazwisko': 'Peck'},
            {'imie': 'Ivan', 'nazwisko': 'Ivanovic'},
            {'imie': 'José', 'nazwisko': 'Jiménez'},
        ]


Operator ``*`` i ``**``
=======================
.. todo:: zrobić zadania do rozwiązania dla parametrów z gwiazdką

Użycie operatora ``*`` przy definicji funkcji powoduje umożliwienie przekazywanie do funkcji dodatkowych parametrów anonimowych. Zazwczaj zmienna, która jest przy tym operatorze nazywa się ``*args`` (arguments).

Użycie operatora ``**`` przy definicji funkcji powoduje umożliwienie przekazywania do niej dodatkowych argumentów nazwanych. Zazwczaj zmienna, która jest przy tym operatorze nazywa się ``**kwargs`` (keyword arguments).

Wykorzystywanie ``args`` i ``kwargs`` przy przyjmowaniu parametrów przez funkcję
--------------------------------------------------------------------------------
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

Wykorzystanie ``args`` i ``kwargs`` przy przekazywaniu parametrów do funkcji
----------------------------------------------------------------------------
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


Przy zwracaniu wartości z funkcji
----------------------------------
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
------------------------
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

Konwersja liczby na zapis słowny
--------------------------------
#. Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową.
#. Konwertujemy cyfry, nie liczby, a zatem:

    .. code-block:: python

        >>> int_to_str(912)
        'dziewięć jeden dwa'

        >>> int_to_str(1100)
        'jeden jeden zero zero'

#. Wersja zaawansowana - odmiana przez przypadki

    .. code-block:: python

        >>> int_to_str(973)
        'dziewiećset siedemdziesiąt trzy'

        >>> int_to_str(127.32)
        'sto dwadzieścia siedem i trzydzieści dwa setne'

:Wymagania:
    * Znaki nie będące cyframi mają być ignorowane
    * Napisz testy sprawdzające przypadki brzegowe.
    * 6 cyfr przed przecinkiem
    * 5 cyfr po przecinku

:Co zadanie sprawdza?:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Przypadek zaawansowany: argumenty pozycyjne i domyślne
    * Rzutowanie i konwersja typów

Rzymskie
--------
#. Napisz program, który przeliczy wprowadzoną liczbę rzymską na jej postać dziesiętną.
#. Napisz drugą funkcję, która dokona procesu odwrotnego.

:Co zadanie sprawdza?:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Sprawdzanie czy element istnieje w ``dict``
    * Rzutowanie i konwersja typów

