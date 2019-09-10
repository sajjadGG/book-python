*****************
Looping over dict
*****************


* Since Python 3.7 ``dict`` keeps order
* Before Python 3.7 ``dict`` order is not ensured!!

Looping over ``dict``
=====================

Values iterator
---------------
.. code-block:: python
    :caption: Iterating over ``dict`` items

    INPUT = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    INPUT.values()
    # [5.1, 3.5, 1.4, 0.2, 'setosa']

    for element in INPUT.values():
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Keys iterator
-------------
.. code-block:: python
    :caption: Iterating over ``dict`` items

    INPUT = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    INPUT.keys()
    # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']

    for element in INPUT.keys():
        print(element)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'

Default iterator
----------------
.. code-block:: python
    :caption: By default ``dict`` iterates over keys

    INPUT = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    for element in INPUT:
        print(element)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'

Items iterator
--------------
* list of pairs ``key``, ``value``

.. code-block:: python
    :caption: Getting pair: ``key``, ``value`` from ``dict`` items

    INPUT = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    INPUT.items()
    # [
    #   ('Sepal length', 5.1),
    #   ('Sepal width', 3.5),
    #   ('Petal length', 1.4),
    #   ('Petal width', 0.2),
    #   ('Species', 'setosa')
    # ]


    for key, value in INPUT.items():
        print(f'{key} -> {value}')

    # Sepal length -> 5.1
    # Sepal width -> 3.5
    # Petal length -> 1.4
    # Petal width -> 0.2
    # Species -> setosa


Create ``dict`` from two sequences
==================================

``range()``
-----------
* Pythonic way is to use ``zip()``
* Don't use ``len(range(...))`` - it evaluates generator

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    output = {}

    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        output[key] = value

    print(output)
    # {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    # }

enumerate()
-----------
* ``_`` regular variable name (not a special syntax)
* ``_`` by convention is used when variable will not be referenced

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    output = {}

    for i, _ in enumerate(keys):
        key = keys[i]
        value = values[i]
        output[key] = value

    print(output)
    # {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    # }

``zip()``
---------
.. code-block:: python

    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]

    output = dict(zip(keys, values))

    print(output)
    # {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    # }


Assignments
===========

``dict`` to ``dict``
--------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/loop_dict_to_dict.py`

:English:
    #. For input data (see below)
    #. Convert to ``Dict[str, str]``
    #. Results should be identical to output (see below)

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Przekonwertuj do ``Dict[str, str]``
    #. Rezultat powinien być identyczny do wyjściowego (patrz poniżej)

:Input:
    .. code-block:: python

        INPUT = {
            6: ['Doctorate', 'Prof-school'],
            5: ['Masters', 'Bachelor', 'Engineer'],
            4: ['HS-grad'],
            3: ['Junior High'],
            2: ['Primary School'],
            1: ['Kindergarten'],
        }

:Output:
    .. code-block:: python

        OUTPUT: Dict[str, str] = {
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
    * Accessing ``dict`` items
    * Iterating over ``dict``
    * Updating ``dict``

``List[tuple]`` to ``List[dict]``
---------------------------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/loop_dict_to_list.py`

:English:
    #. For input data (see below)
    #. Separate header and data
    #. Print ``List[dict]``

        - key - name from the header
        - value - measurement or species

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Odseparuj nagłówek i dane
    #. Wypisz ``List[dict]``

        - klucz: nazwa z nagłówka
        - wartość: wyniki pomiarów lub gatunek

:Input:
    .. code-block:: python

        INPUT = [
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

:Output:
    .. code-block:: python

        OUTPUT: List[dict] = [
            {'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
            {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
            {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
            ...
        ]

:The whys and wherefores:
    * Working with nested data structures
    * Iterating over dict and lists
