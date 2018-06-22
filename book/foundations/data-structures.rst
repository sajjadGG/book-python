**********************
Simple Data Structures
**********************

Simple Collections
==================

``tuple``
---------
.. code-block:: python

    my_tuple = ()
    my_tuple = tuple()

    my_tuple = 1,
    my_tuple = (1,)

    my_tuple = 1, 2, None, False, 'hej'
    my_tuple = (1, 2, None, False, 'hej')
    my_tuple = tuple(1, 2, None, False, 'hej')

.. code-block:: python

    >>> def return_arguments(a, b):
    ...    return a, b

    >>> return_arguments(10, 20)
    (10, 20)

.. code-block:: python

    >>> my_tuple = (1, 2, 3, 4, 5)

    >>> my_tuple[:3]  # do 3
    (1, 2, 3)

    >>> my_tuple[1:4]  # od 1 do 4
    (2, 3, 4)

    >>> my_tuple[3:]  # od 3 do końca
    (4, 5)

    >>> my_tuple[::2]  # co 2
    (1, 3, 5)

    >>> my_tuple[-1]  # ostatni i ostatni element
    5

.. code-block:: python

    >>> my_tuple = (1, 2, 3, 4, 5)

    MIN = 1
    MAX = 5

    zmienna = slice(MIN, MAX)
    my_tuple[zmienna]
    # (2, 3, 4)

    my_tuple[MIN:MAX]  # to samo
    # (2, 3, 4)


``list``
--------
.. code-block:: python

    my_list = []
    my_list = list()

    my_list = [1]

    my_list = [1, 2, None, False, 'hej']
    my_list = list(1, 2, None, False, 'hej')

.. code-block:: python

    >>> my_list = [1, 2, None, False, 'hej']
    >>> my_list[1]
    2
    >>> my_list[2:5]
    [None, False, 'hej']

.. code-block:: python

    >>> my_list = [1, 2]
    >>> my_list = my_list.append([3, 4])
    [1, 2, [3, 4]]

    >>> my_list = [1, 2]
    >>> my_list.extend([3, 4])
    [1, 2, 3, 4]


``set``
-------
.. code-block:: python

    my_set = {1}
    # {1}

    {1, 3, 1}
    # {1, 3}

    set([1, 3, 1])
    # {1, 3}

.. code-block:: python

    my_set = {1, 2, 3}
    # {1, 2, 3}

    my_set.add(4)
    my_set.add(4)
    my_set.add(3)
    # {1, 2, 3, 4}

.. code-block:: python

    {1,2} - {2,3}  # Różnica
    # {1}

    {1,2} | {2,3}  # Suma
    # {1, 2, 3}

    {1,2} & {2,3}  # Iloczyn
    # {2}

    {1,2} ^ {2,3}  # Różnica symetryczna
    # {1, 3}

    {1,2} + {3,4}
    # Traceback (most recent call last):
    #    ...
    # TypeError: unsupported operand type(s) for +: 'set' and 'set'

.. code-block:: python

    my_set = {1, 2, 3}
    len(my_set)  # Liczność
    # 3

    1 in my_set  # Przynależność
    # True

    for element in my_set:  # Można po nim iterować
        print(element)

.. code-block:: python

    names = ['Max', 'Ivan', 'Jose', 'Max']
    unique_names = set(imiona)
    # {'Jose', 'Ivan', 'Max'}

``dict``
--------
.. code-block:: python

    my_dict = {
        "first_name": "José",
        "last_name": 'Jiménez',
        'age': 30,
        'locations': ['Cape Canaveral', 'Houston'],
        1: 'value for one',
    }

    my_dict['last_name']
    # 'Jiménez'

    my_dict['locations']
    # ['Cape Canaveral', 'Houston']

    my_dict[1]
    # 'value for one'

.. code-block:: python

    >>> my_dict = {'wiek': 20, 'wiek': 30}
    {'wiek': 30}

.. code-block:: python

    >>> my_dict = {'wiek': 30, 'imie': 'José', 'nazwisko': 'Jiménez'}

    >>> my_dict.keys()
    dict_keys(['wiek', 'imie', 'nazwisko'])

    >>> my_dict.values()
    dict_values([30, 'José', 'Jiménez'])

    >>> my_dict.items()
    dict_items([('wiek', 30), ('imie', 'José'), ('nazwisko', 'Jiménez')])

.. note:: przy wyświetlaniu elementów słownika, kolejność może się zmieniać!

``dict`` vs. ``set``
--------------------
Należy zwrócić uwagę, aby nie pomylić z dictem:

.. code-block:: python

    {}  # dict
    {1}  # set
    {1, 2}  # set
    {1: 2} # dict
    {1:1, 2:2} # dict

.. code-block:: python

    >>> my_data = {}
    >>> isinstance(my_data, (set, dict))
    True
    >>> isinstance(my_data, dict)
    True
    >>> isinstance(my_data, set)
    False

    >>> my_data = {1}
    >>> isinstance(my_data, set)
    True
    >>> isinstance(my_data, dict)
    False

    >>> my_data = {1: 1}
    >>> isinstance(my_data, set)
    False
    >>> isinstance(my_data, dict)
    True

Acessing ``dict`` values with ``[...]`` and ``.get(...)``
---------------------------------------------------------
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

    >>> what = 10, 20
    <class 'tuple'>

    >>> what = (10, 20)
    <class 'tuple'>

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

    >>> what = (10.)
    <class 'float'>

.. code-block:: python

    >>> what = 10, # len(what) = 1
    <class 'tuple'>

    >>> what = (10,) # len(what) = 1
    <class 'tuple'>

    >>> what = 10. # len(what) -> TypeError: object of type 'float' has no len()
    <class 'float'>

    >>> what = (10.) # len(what) -> TypeError: object of type 'float' has no len()
    <class 'float'>

    >>> what = (10) # len(what) -> TypeError: object of type 'int' has no len()
    <class 'int'>


Złożone typy danych
===================

Lista słowników
---------------
.. code-block:: python

    DATA = [
        {'first_name': 'Max'},
        {'first_name': 'José', 'last_name': 'Jiménez'},
        {'first_name': 'Ivan', 'tags': ['astronaut', 'roscosmos', 'space']},
    ]

    DATA[0]['last_name']
    # Traceback (most recent call last):
    #  ...
    # KeyError: 'nazwisko'

    DATA[0].get('last_name', 'n/a')
    # 'n/d'

    ' and '.join(DATA[3].get('tags'))
    # astronaut and roscosmos and space

Multidimensional lists
----------------------
.. code-block:: python

    array = [
        [0, 1, 2],
        [1, 2, 3],
        [1, 2, 3],
    ]

.. code-block:: python

    array2 = [
        [0, None, 'abc'],
        [1, 2, 3],
    ]

Mixed types
-----------
.. code-block:: python

    array = [
        [0, 1, 2],
        (1, 2, 3),
        {1, 3, 1},
        {'imie': 'José', 'nazwisko': 'Jiménez'}
    ]

How to initialize?
==================
* ``list()`` or ``[]``
* ``tuple()`` or ``()``
* ``dict()`` or ``{}``
* ``set()`` or ``{}``

Assignments
===========

Generowanie listy unikalnych kluczy
-----------------------------------
#. Mając bazę danych z listingu poniżej
#. Wygeneruj listę uniklalnych kluczy dictów

.. code-block:: python

    DATABASE = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Max', 'last_name': 'Peck'},
        {'first_name': 'Ivan'},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
        {'first_name': 'Jose', 'born': 1961, 'first_step': 1969},
    ]

:Założenia:
    * Nazwa pliku: ``type-unique.py``
    * Szacunkowa długość kodu: około 3 linie
    * Maksymalny czas na zadanie: 5 min

Podział zbioru
--------------
#. Mając do dyspozycji zbiór danych Irysów z :numref:`listing-data-structures-iris-sample`
#. Pierwsza linia jest nagłówkiem
#. Ustaw dane z kolejnych linii w losowej kolejności
#. Podziel zbiór na dwie listy w proporcji:

    - dane do uczenia - 80%
    - dane testowe - 20%

:Założenia:
    * Nazwa pliku: ``type-split-list.py``
    * Szacunkowa długość kodu: około 6 linie
    * Maksymalny czas na zadanie: 10 min

:Podpowiedź:
    - ``from random import shuffle``

.. literalinclude:: src/data-structures-iris-sample.py
    :name: listing-data-structures-iris-sample
    :language: python
    :caption: Sample Iris databases

Słownik unikalnych cech
-----------------------
#. Mając do dyspozycji zbiór danych Irysów z :numref:`listing-data-structures-iris-sample`
#. Stwórz słownik gatunków.
#. Kolejnym liczbom naturalnym zaczynając od zera przyporządkuj gatunek irysów
#. Przygotuj listę cech z kluczami ze słownika gatunków.

.. code-block:: python

    # 0: I. setosa
    # 1: I. versicolor
    # 2: I. virginica
    labels = [0, 1, 2, 1, 1, 0, ...]

:Założenia:
    * Nazwa pliku: ``type-split-dict.py``
    * Szacunkowa długość kodu: około 6 linie
    * Maksymalny czas na zadanie: 10 min
