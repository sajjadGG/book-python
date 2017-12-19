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
    ...     return a/b

    >>> podziel(a=1, b=2)
    0.5

    >>> podziel(b=2, a=1)
    0.5

Argumenty z wartością domyślną
------------------------------

Argument funkcji może mieć także wartość domyślną, z której funkcja skorzysta jeżeli użytkownik nie zdefiniuje tego argumentu.

.. code-block:: python

    >>> def hello(tekst='hello world'):
    ...     print(tekst)

    >>> hello(tekst='ehlo')
    ehlo

    >>> hello()
    hello world

    >>> def convert(value, to='bin'):
    ...     if to=='bin':
    ...         return bin(value)
    ...     elif to=='hex':
    ...         return hex(value)
    ...     elif to=='oct':
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



Zwracanie wartości
==================

Zwracanie wartości prostych
---------------------------

.. code-block:: python

    def foo1():
        return True

    def foo2():
        return None

    def foo3():
        return 'bar'

    def foo4():
        return [10, 20]

    def foo5():
        return foo1

    def foo6():
        # Python always return something, in this case ``return None``
        pass

    def foo7():
        return 10, 20, 30, 5, 'a'

    def foo8():
        return {'imie': 'Ivan', 'nazwisko': 'Ivanovic'}


Zwracanie typów złożonych
-------------------------

.. code-block:: python

    def foo9():
        return [
            {'imie': 'Max', 'nazwisko': 'Peck'},
            {'imie': 'Ivan', 'nazwisko': 'Ivanovic'},
            {'imie': 'José', 'nazwisko': 'Jiménez'}]


Operator ``*`` i ``**``
=======================
.. todo:: zrobić lepsze przykłady wykorzystania parametrów z gwiazdką
.. todo:: zrobić zadania do rozwiązania dla parametrów z gwiazdką

Argumenty ``*args``, ``**kwargs``
---------------------------------
Użycie operatora * przy definicji funkcji powoduje umożliwienie przekazywanie do funkcji dodatkowych parametrów anonimowych. Zazwczaj zmienna, która jest przy tym operatorze nazywa się ``*args`` (arguments)

Użycie operatora ``**`` przy definicji funkcji powoduje umożliwienie przekazywania do niej dodatkowych argumentów nazwanych. Zazwczaj zmienna, która jest przy tym operatorze nazywa się ``**kwargs`` (keyword arguments)

Przy wywołaniu funkcji
----------------------
Wywołując powyższą funkcję z argumentami:

.. code-block:: python

    >>> def foo(my_var, *args, **kwargs):
    ...    print(f"zmienna my_var: {my_var}")  # pierwsze dopasowanie
    ...    print(f"zmienna args: {args}")  # argumenty pozycyjne 2, 3, 4
    ...    print(f"zmienna kwargs: {kwargs}")  # argumenty nazwane c=5, d=6
    ...
    ...
    ... foo(1, 2, 3, 4, c=5, d=6)
    zmienna my_var: 1
    zmienna args: (2, 3, 4)
    zmienna kwargs: {'c': 5, 'd': 6}

Sprawi, że wewnątrz funkcji będziemy mieli dostępną zmienną ``my_var`` o wartości 1, zmeinną ``args``, zawierającą listę elementów (2, 3, 4) oraz zmienną słownikową ``kwargs``, która ma klucze 'c' i 'd', które przechowują wartości, odpowiednio, 5 i 6.

Przy zwracaniu wartości z funkcji
----------------------------------
.. code-block:: python

    >>> value, _ = function()
    >>> value, *args = function()

.. code-block:: python

    def sensor_temperatury():
        # ładniej byłoby gdyby programista napisał
        # {'napiecie': 10, 'natezenie': 20, 'rezystancja': 30, 'czas': 5, 'location': 'laboratorium'}
        # ale programiści niskopoziomowi zwykle zwracają jako list...
        return (10, 20, 30, 5, 'laboratorium')

    # z funkcji dopasuje nam dwa pierwsze elementy, a kolejne umieści w ``tuple`` o nazwie args
    napiece, natezenie, *args = sensor_temperatury()

    # Przez konwencję, jeżeli nie korzystamy później z argumentów, to możemy przypisać je do ``_``
    napiecie, natezenie, *_ = sensor_temperatury()


.. code-block:: python

    def bar():
        return range(0, 5)

    jeden, dwa, *reszta = bar()

    print(jeden, dwa, reszta)


    def foobar(a, b, *args):
        print(locals())

    foobar(1, 2, 5, 7)


    def foobar(a, b, **kwargs):
        print(locals())

    foobar(1, 2, c=5, d=7)


Inne przykładowe zastosownaie operatorów ``*`` i ``**`` polega na wykorzystaniu ich przy wywołaniu funkcji. Wtedy, wykorzystując operator ``*``, kolejne elementy listy albo krotki będą przekazane jako kolejne argumenty funkcji, a wykorzystując operator ``**`` kolejne elementy zmiennej słownikowej będą przekazane jako nazwane argumenty. Oznacza to, że na przykład argument ``x`` funkcji, przyjmie wartość ``dict_vec['x']``.

.. code-block:: python

    >>> def my_function(x, y, z):
    ...    print(x, y, z)

    >>> tuple_vec = (1, 0, 1)
    >>>  my_function(*tuple_vec)
    1, 0, 1

    >>> dict_vec = {'y': 1, 'x': 0, 'z': 1}
    >>> my_function(**dict_vec)
    0, 1, 1

.. warning:: Nie przywiązuj się do nazewnictwa ``*args`` i ``**kwargs``, chociaż jest to konwencja!!

    .. code-block:: python

        def foo(dopasowane, *pozycyjne, **nazwane):
            print(f"argumenty dopasowane: {dopasowane}")  # 1
            print(f"argumenty pozycyjne: {pozycyjne}")    # 2, 3, 4
            print(f"argumenty nazwane: {nazwane}")        # c=5, d=6


        foo(1, 2, 3, 4, c=5, d=6)

    Taki zapis jest również możliwy, chociaż bardzo mylący

    .. code-block:: python

        def foo(dopasowane, *kwargs, **args):
            print(f"argumenty dopasowane: {dopasowane}")  # 1
            print(f"argumenty pozycyjne: {kwargs}")       # 2, 3, 4
            print(f"argumenty nazwane: {args}")           # c=5, d=6


        foo(1, 2, 3, 4, c=5, d=6)


Przykładowe zastosowanie
------------------------
.. code-block:: python

    class Osoba:
        first_name = 'Max'
        last_name = 'Peck'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)

.. code-block:: python

    def create_or_update():
        return True, [
            {'id': 1, 'imie': 'Ivan', 'nazwisko': 'Ivanovic'},
            {'id': 2, 'imie': 'José', 'nazwisko': 'Jiménez'},
        ], 10, str('asd')


    czy_utworzone, *args  = create_or_update()

    print(czy_utworzone)


Zadania kontrolne
=================

Konwersja liczby na zapis słowny
--------------------------------
#. Napisz program ``numer.py``, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową.
#. Konwertujemy cyfry, nie liczby, a zatem:

    .. code-block:: python

        >>> int_to_str(999)
        'dziewięć jeden jeden'

        >>> int_to_str(1100)
        'jeden jeden zero zero'

#. Wersja zaawansowana - odmiana przez przypadki

    .. code-block:: python

        >>> int_to_str(999)
        'dziewiećset dziewięćdziesiąt dziewięć'

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

