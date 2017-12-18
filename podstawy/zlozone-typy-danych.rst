.. _Zbiory i operacje na nich:

*******************
Złożone typy danych
*******************

Zbiory i operacje na nich
=========================

``tuple`` - Krotka
------------------
.. code-block:: python

    a = (1, 2, 3)
    a = tuple(1, 2, 3)

.. code-block:: python

    >>> def return_arguments(a, b):
    ...    return (a, b)

    >>> out = return_arguments(10, 20)
    >>> print(out)
    (10, 20)


``list`` - Lista
----------------
.. code-block:: python

    my_list = []
    my_list = list()
    my_list = [1, 2, None, False, 'hej']

.. code-block:: python

    >>> my_list = [1, 2, None, False, 'hej']
    >>> my_list[2]
    None

.. code-block:: python

    def make_html1(lista):
        """
        Performance - Method concatenates strings using + in a loop
        """
        html = '<table>'

        for element in lista:
            html += f'\r\n<tr><td>{element}</td></tr>'
        html += '\r\n</table>'

        return html


    def make_html2(lista):
        """
        Problem solved
        """
        html = ['<table>']

        for element in lista:
            html.append(f'<tr><td>{element}</td></tr>')

        html.append('</table>')

        return '\r\n'.join(html)


``set`` - Zbiór
---------------
.. code-block:: python

    >>> a = set([1, 3, 1])
    >>> a
    {1, 3}

Przykład trochę bardziej zaawansowany:

.. code-block:: python

    class Adres:
        def __init__(self, miasto):
            self.miasto = miasto


    Adres(miasto='...')
    print({Adres(miasto='...'), Adres(miasto='...')})

    a = Adres(miasto='...')
    print({a, a})

.. code-block:: python

    {}  # dict
    {'klucz': 'wartość'}  # dict
    {'klucz', 'wartość'}  # set
    {'klucz'}  # set


``dict`` - Słownik
------------------
.. code-block:: python

    my_data = {
        "imie": "José",
        "nazwisko": 'Jiménez',
        'wiek': 10,
    }

    print(my_data['nazwisko'])


Dobieranie się do wartości elementów za pomocą ``[...]`` i ``.get(...)``
------------------------------------------------------------------------
Do zawartości zmiennej słownikowej możemy uzyskać dostęp używając nawiasów kwadratowych wraz z kluczem, albo funkcji ``.get(klucz)``. Różnica między tymi podejściami polega na tym, że jeżeli dana zmienna słownikowa nie zawiera pewnego klucza, używanie nawiasów kwadratowych wygeneruje wyjątek KeyError, natomiast użycie funkcji ``.get(klucz)`` nie zwróci nic. Do funkcji ``.get(klucz)`` możemy dodatkowo dopisać wartość domyślną która zostanie zwrócona, jeżeli słownik nie posiada danego klucza.

.. code-block:: python

    >>> dane = {'imie': 'José', 'nazwisko': 'Jiménez'}

    >>> dane['nazwisko']
    'Jiménez'

    >>> dane.get('nazwisko')
    'Jiménez'

    >>> dane['wiek']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'wiek'

    >>> dane.get('wiek')

    >>> dane.get('wiek', 'n/d')
    'n/d'


Jak Python rozróżnia typy
-------------------------
Dla każdego z poniższych przykładów wykonano funkcję ``type(what)`` i wynik pokazano poniżej. Dla czytelności przykładu pominięto tę linijkę.

.. code-block:: python

    >>> what = 'foo'
    <class 'str'>

    >>> what = 'foo',
    <class 'tuple'>

    >>> what = ('foo')
    <class 'str'>

    >>> what = ('foo',)
    <class 'tuple'>

.. code-block:: python

    >>> what = 10
    <class 'int'>

    >>> what = 10.5
    <class 'float'>

    >>> what = .5
    <class 'float'>

    >>> what = 10.
    <class 'float'>

    >>> what = 10,
    <class 'tuple'>

    >>> what = 10, 20
    <class 'tuple'>

    >>> what = (10, 20)
    <class 'tuple'>

    >>> what = (10,)
    <class 'tuple'>

    >>> what = (10.)
    <class 'float'>

.. code-block:: python

    >>> what = {}
    <class 'dict'>

    >>> what = {'id'}
    <class 'set'>

    >>> what = {'id': 1}
    <class 'dict'>


    >>> a = {}

    >>> isinstance(a, dict)
    True

    >>> isinstance(a, set)
    False

    >>> isinstance(a, (set, dict))
    True


Złożone typy danych
===================

Lista słowników
---------------
.. code-block:: python

    studenci = [
        {'imie': 'Max'},
        {'imie': 'José', 'nazwisko': 'Jiménez'},
        {'imie': 'Ivan', 'nazwisko': None},
        {'imie': 'Buster', 'programuje w': ['python', 'java', 'c/c++']},
    ]

    dane = studenci[0]['nazwisko']
    dane = studenci[0].get('nazwisko', 'n/d')
    dane = '\n'.join(studenci[4].get('programuje w'))
    print(dane)

Listy wielowymiarowe
--------------------
.. code-block:: python

    array = [
        [0, 1, 2],
        [1, 2, 3],
    ]


Mieszane typy
-------------
.. code-block:: python

    array = [
        [0, 1, 2],
        (1, 2, 3),
        set([1, 3, 1]),
        {'imie': 'José', 'nazwisko': 'Jiménez'}
    ]


Jak inicjować poszczególne typy?
================================
- ``list()`` czy ``[]``
- ``tuple()`` czy ``()``
- ``dict()`` czy ``{}``
- ``set()`` czy ``{}``


Zadania kontrolne
=================

Wyrazy
------
Napisz program, który na podstawie paragrafu tekstu "Lorem Ipsum" podzieli go na zdania () i dla każdego zdania wyświetli ile jest w nim wyrazów::

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

:Założenia:
    * kropka rozdziela zdania
    * spacja oddziela wyrazy w zdaniu

:Podpowiedź:
    * ``str.split()``
    * ``len()``
    * ``for wyraz in zdanie:``

Przeliczanie odległości
-----------------------
Napisz program który przekonwertuje odległości (podane w metrach) i zwróci ``dict``, zgodnie z szablonem:

.. code-block:: python

    {
        'kilometers': int,
        'miles': float,
        'nautical miles': float,
        'all': [int, float, float]
    }

:Podpowiedź:
    * 1000 m = 1 km
    * 1608 m = 1 mila
    * 1852 m = 1 mila morska
    * ``def konwersja_odleglosci():`` oraz ``return {...}``