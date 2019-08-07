**************************
Iterating nested sequences
**************************


Iterating over nested ``list`` items
====================================
.. code-block:: python
    :caption: Iterating over nested ``list`` items

    DATA = [1, 2, 3]

    for digit in DATA:
        print(digit)

    # 1
    # 2
    # 3

.. code-block:: python
    :caption: Iterating over nested ``list`` items

    DATA = [(...), (...), (...)]

    for obj in DATA:
        print(obj)

    # (...)
    # (...)
    # (...)

.. code-block:: python
    :caption: Iterating over nested ``list`` items

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for row in DATA:
        print(row)

    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # (6.3, 2.9, 5.6, 1.8, 'virginica')


Unpacking values in loop
========================

Recap information about unpacking
---------------------------------
.. code-block:: python
    :caption: Unpacking values

    a, b = 'a', 0
    a, b = ('a', 0)
    k, v = ('a', 0)
    key, value = ('a', 0)

Unpacking ``list`` of pairs
---------------------------
.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        ('a', 0),
        ('b', 1),
        ('c', 2),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')

    # a -> 0
    # b -> 1
    # c -> 2

.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        (0, 1),
        ('name', 'Jan Twardowski'),
        ('locations', ['CapeCanaveral', 'Houston']),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')

    # 0 -> 1
    # name -> Jan Twardowski
    # locations -> ['CapeCanaveral', 'Houston']

Unpacking ``list`` of sequences
-------------------------------
.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    # sepal_len, sepal_wid, petal_len, petal_wid, species = (5.1, 3.5, 1.4, 0.2, 'setosa')

    for sepal_len, sepal_wid, petal_len, petal_wid, species in DATA:
        print(f'{species} -> {sepal_len}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3

.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for sepal_len, *_, species in DATA:
        print(f'{species} -> {sepal_len}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3

.. code-block:: python
    :caption: Unpacking values in loop

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for *measurements, species in DATA:
        print(f'{species} -> {measurements}')

    # setosa -> [5.1, 3.5, 1.4, 0.2]
    # versicolor -> [5.7, 2.8, 4.1, 1.3]
    # virginica -> [6.3, 2.9, 5.6, 1.8]


Enumerating and item index
==========================
.. code-block:: python
    :caption: Enumerating and item index

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
    ]

    for i, row in enumerate(DATA):
        print(f'{i} -> {row}')

    # 0 -> (5.1, 3.5, 1.4, 0.2, 'setosa')
    # 1 -> (5.7, 2.8, 4.1, 1.3, 'versicolor')
    # 2 -> (6.3, 2.9, 5.6, 1.8, 'virginica')


Iterating over ``dict`` items
=============================
* Since Python 3.7 ``dict`` has of adding elements
* Before Python 3.7 ``dict`` order is not ensured!!

Iterating over ``dict`` values
------------------------------
.. code-block:: python
    :caption: Iterating over ``dict`` items

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    DATA.values()
    # [5.1, 3.5, 1.4, 0.2, 'setosa']

    for element in DATA.values():
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Iterating over ``dict`` keys
----------------------------
.. code-block:: python
    :caption: Iterating over ``dict`` items

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    DATA.keys()
    # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']

    for element in DATA.keys():
        print(element)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'

By default ``dict`` iterates over keys
--------------------------------------
.. code-block:: python
    :caption: By default ``dict`` iterates over keys

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    for element in DATA:
        print(element)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'

Getting pair: ``key``, ``value`` from ``dict`` items
----------------------------------------------------
.. code-block:: python
    :caption: Getting pair: ``key``, ``value`` from ``dict`` items

    DATA = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    DATA.items()
    # [
    #   ('Sepal length', 5.1),
    #   ('Sepal width', 3.5),
    #   ('Petal length', 1.4),
    #   ('Petal width', 0.2),
    #   ('Species', 'setosa')
    # ]


    for key, value in DATA.items():
        print(f'{key} -> {value}')

    # Sepal length -> 5.1
    # Sepal width -> 3.5
    # Petal length -> 1.4
    # Petal width -> 0.2
    # Species -> setosa

``list`` of ``dict``
--------------------
.. code-block:: python
    :caption: ``list`` of ``dict``

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Sepal width': 2.9, 'Petal length': 5.6, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

    for row in DATA:
        sepal_length = row['Sepal length']
        species = row['Species']
        print(f'{species} -> {sepal_length}')

    # setosa -> 5.1
    # versicolor -> 5.7
    # virginica -> 6.3


Iterating complex types
=======================
.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - simple loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]

    for element in DATA:
        print(element})

    # ('Jan', 'Twardowski')
    # Watney
    # 42
    # 13.37
    # {False, True, None}

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - nested loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]

    for outer in DATA:
        for inner in outer:
            print(inner)

    # Jan
    # Twardowski
    # W
    # a
    # t
    # n
    # e
    # y
    # Traceback (most recent call last):
    #   File "<input>", line 4, in <module>
    # TypeError: 'int' object is not iterable

.. code-block:: python
    :caption: Iterating over ``list`` with scalar and vector values - smart loop

    DATA = [('Jan', 'Twardowski'), 'Watney', 42, 13.37, {True, None, False}]


    for outer in DATA:
        if not isinstance(outer, (list, set, tuple))
            print(outer)
        else:
            for inner in outer:
                print(inner)

    # Jan
    # Twardowski
    # Watney
    # 42
    # 13.37
    # False
    # True
    # None


Assignments
===========

Get elements from nested data structure
---------------------------------------
* Level: Easy
* Lines of code to write: 3 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/for_nested.py`

#. Na podstawie ``DATA`` z :numref:`listing-for-elements-fom-nested`
#. Po odrzuceniu nagłówka iteruj po danych
#. Wyświetl na ekranie nazwy gatunków zaczynające się na "v".

.. code-block:: python
    :caption: Iris sample dataset
    :name: listing-for-elements-fom-nested

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, {'species': 'virginica'}),
        (5.1, 3.5, 1.4, 0.2, {'species': 'setosa'}),
        (5.7, 2.8, 4.1, 1.3, {'species': 'versicolor'}),
        (6.3, 2.9, 5.6, 1.8, {'species': 'virginica'}),
        (6.4, 3.2, 4.5, 1.5, {'species': 'versicolor'}),
        (4.7, 3.2, 1.3, 0.2, {'species': 'setosa'}),
        (7.0, 3.2, 4.7, 1.4, {'species': 'versicolor'}),
        (7.6, 3.0, 6.6, 2.1, {'species': 'virginica'}),
        (4.6, 3.1, 1.5, 0.2, {'species': 'setosa'}),
    ]

``dict`` to ``dict``
--------------------
* Level: Easy
* Lines of code to write: 4 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/for_dict_to_dict.py`

#. Dany jest ``dict`` w formacie:

    .. code-block:: python

        DATA = {
            6: ['Doctorate', 'Prof-school'],
            5: ['Masters', 'Bachelor', 'Engineer'],
            4: ['HS-grad'],
            3: ['Junior High'],
            2: ['Primary School'],
            1: ['Kindergarten'],
        }

#. Przekonwertuj go aby uzyskać format:

    .. code-block:: python

        output = {
            'Doctorate': '6',
            'Prof-school': '6',
            'Masters': '5',
            'Bachelor': '5',
            'Engineer': '5',
            'HS-grad': '4',
            'Junior High': '3',
            'Primary School': '2',
            'Kindergarten': '1'
        }

:The whys and wherefores:
    * Wyciąganie elementów ze słownika
    * Iterowanie po słowniku
    * Aktualizacja słownika

Unique keys from schema-less database
-------------------------------------
* Level: Easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/loop_unique_keys.py`
* Input data: :numref:`listing-loops-unique-keys`

.. code-block:: python
    :name: listing-loops-unique-keys
    :caption: Unique keys from schema-less database

    DATA = [
        {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
    ]

#. Mając bazę danych z listingu :numref:`listing-loops-unique-keys`
#. Iteruj po rekordach w bazie danych
#. Z rekordu wyciągnij klucze
#. Wypisz unikalne klucze

:The whys and wherefores:
    * Generowanie zbiorów
    * Usuwanie powtarzających się elementów
    * Wyciąganie elementów ze słownika
    * Iterowanie po słowniku
    * Aktualizacja zbiorów

:Hint:
    * Compare solutions with :numref:`Micro-benchmarking use case`

Label encoder
-------------
* Level: Medium
* Lines of code to write: 13 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/loop_label_encoder.py`
* Input data: :numref:`listing-loops-iris-sample`

.. code-block:: python
    :name: listing-loops-iris-sample
    :caption: Sample Iris databases

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
        (7.1, 3.0, 5.9, 2.1, 'virginica'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.0, 3.6, 1.4, 0.3, 'setosa'),
        (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        (6.5, 3.0, 5.8, 2.2, 'virginica'),
        (6.5, 2.8, 4.6, 1.5, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (6.9, 3.1, 4.9, 1.5, 'versicolor'),
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]

#. Ze zbioru :numref:`listing-loops-iris-sample` wyodrębnij dane
#. Zdefiniuj:

    * ``X: List[Tuple[float]]`` - features - pomiary
    * ``y: List[int]`` - labels - gatunki
    * ``label_encoder: Dict[int, str]`` - słownik podmiany nazw gatunków

#. Aby móc odszyfrować ``labels`` i zamienić wartości ``int`` na nazwy gatunków (``str``), potrzebny jest słownik podmiany "liczba -> nazwa gatunku". Na podstawie danych (nie zapisuj go na sztywno w kodzie) wygeneruj taki słownik
#. Dla każdego rekordu wyodrębnij pomiary i nazwę gatunku
#. Zaktualizuj odpowiednie listy
#. Wyświetl na ekranie ``X``, ``y`` i ``label_encoder``:
#. Efekt końcowy:

    .. code-block:: python
        :caption: Przykład danych wyodrębnionych

        X = [
            (5.8, 2.7, 5.1, 1.9),
            (5.1, 3.5, 1.4, 0.2),
            (5.7, 2.8, 4.1, 1.3),
            (6.3, 2.9, 5.6, 1.8),
            (6.4, 3.2, 4.5, 1.5),
            (4.7, 3.2, 1.3, 0.2), ...]

        y = [0, 1, 2, 1, 2, 0, ...]

        label_encoder = {
            0: 'virginica',
            1: 'setosa',
            2: 'versicolor'}

:The whys and wherefores:
    * Sprawdzanie występowania elementów w słowniku
    * Generowanie słownika i listy na podstawie innych danych
    * Odwracanie słownika
