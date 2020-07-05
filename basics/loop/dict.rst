.. _Loop Dict:

**************
Loop over Dict
**************


Rationale
=========
.. highlights::
    * Since Python 3.7 ``dict`` keeps order
    * Before Python 3.7 ``dict`` order is not ensured!!


Iterate
=======
.. code-block:: python
    :caption: By default ``dict`` iterates over keys

    iris = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    for obj in iris:
        print(obj)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'


Iterate Keys
============
.. code-block:: python
    :caption: Iterating over ``dict`` items

    iris = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(iris.keys())
    # ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']

    for obj in iris.keys():
        print(obj)

    # 'Sepal length'
    # 'Sepal width'
    # 'Petal length'
    # 'Petal width'
    # 'Species'


Iterate Values
==============
.. code-block:: python
    :caption: Iterating over ``dict`` items

    iris = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(iris.values())
    # [5.1, 3.5, 1.4, 0.2, 'setosa']

    for obj in iris.values():
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'


Iterate Key-Value Pairs
=======================
.. highlights::
    * list of pairs ``key``, ``value``

.. code-block:: python
    :caption: Getting pair: ``key``, ``value`` from ``dict`` items

    iris = {
        'Sepal length': 5.1,
        'Sepal width': 3.5,
        'Petal length': 1.4,
        'Petal width': 0.2,
        'Species': 'setosa',
    }

    list(iris.items())
    # [
    #   ('Sepal length', 5.1),
    #   ('Sepal width', 3.5),
    #   ('Petal length', 1.4),
    #   ('Petal width', 0.2),
    #   ('Species', 'setosa'),
    # ]


    for key, value in iris.items():
        print(key, '->', value)

    # Sepal length -> 5.1
    # Sepal width -> 3.5
    # Petal length -> 1.4
    # Petal width -> 0.2
    # Species -> setosa


Generate with Range
===================
.. highlights::
    * ``range()``
    * Pythonic way is to use ``zip()``
    * Don't use ``len(range(...))`` - it evaluates generator

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']
    result = {}

    for i in range(len(header)):
        key = header[i]
        value = data[i]
        result[key] = value

    print(result)
    # {
    #   'Sepal length': 5.1,
    #   'Sepal width': 3.5,
    #   'Petal length': 1.4,
    #   'Petal width': 0.2,
    #   'Species': 'setosa',
    # }

Generate with Enumerate
=======================
.. highlights::
    * ``enumerate()``
    * ``_`` regular variable name (not a special syntax)
    * ``_`` by convention is used when variable will not be referenced

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']
    result = {}

    for i, key in enumerate(header):
        result[key] = data[i]

    print(result)
    # {
    #   'Sepal length': 5.1,
    #   'Sepal width': 3.5,
    #   'Petal length': 1.4,
    #   'Petal width': 0.2,
    #   'Species': 'setosa',
    # }


Generate with Zip
=================
.. highlights::
    * ``zip()``
    * The most Pythonic way

.. code-block:: python

    header = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    data = [5.1, 3.5, 1.4, 0.2, 'setosa']

    result = dict(zip(header, data))

    print(result)
    # {
    #   'Sepal length': 5.1,
    #   'Sepal width': 3.5,
    #   'Petal length': 1.4,
    #   'Petal width': 0.2,
    #   'Species': 'setosa',
    # }


Assignments
===========

Loop Dict from Dict to Dict
---------------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/loop_dict_to_dict.py`

:English:
    #. Use data from "Input" section (see below)
    #. Convert to ``result: Dict[str, str]``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Przekonwertuj do ``result: Dict[str, str]``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        DATA = {
            6: ['Doctorate', 'Prof-school'],
            5: ['Masters', 'Bachelor', 'Engineer'],
            4: ['HS-grad'],
            3: ['Junior High'],
            2: ['Primary School'],
            1: ['Kindergarten'],
        }

:Output:
    .. code-block:: python

        result: Dict[str, str]
        # {'Doctorate': '6',
        #  'Prof-school': '6',
        #  'Masters': '5',
        #  'Bachelor': '5',
        #  'Engineer': '5',
        #  'HS-grad': '4',
        #  'Junior High': '3',
        #  'Primary School': '2',
        #  'Kindergarten': '1'}

:The whys and wherefores:
    * Accessing ``dict`` items
    * Iterating over ``dict``
    * Updating ``dict``

Loop Dict from List to Dict
---------------------------
* Complexity level: medium
* Lines of code to write: 6 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/loop_dict_to_list.py`

:English:
    #. Use data from "Input" section (see below)
    #. Separate header and data
    #. Print ``List[dict]``:

        * key - name from the header
        * value - measurement or species

    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Wypisz ``List[dict]``:

        * klucz: nazwa z nagłówka
        * wartość: wyniki pomiarów lub gatunek

    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

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

:Output:
    .. code-block:: python

        result: List[dict]
        # [{'Sepal length': 5.8, 'Sepal width': 2.7, 'Petal length': 5.1, 'Petal width': 1.9, 'Species': 'virginica'},
        #  {'Sepal length': 5.1, 'Sepal width': 3.5, 'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
        #  {'Sepal length': 5.7, 'Sepal width': 2.8, 'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        #  ...]

:The whys and wherefores:
    * Working with nested data structures
    * Iterating over dict and lists

Loop Dict Label Encoder
-----------------------
* Complexity level: hard
* Lines of code to write: 13 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/loop_label_encoder.py`

:English:
    #. Use data from "Input" section (see below)
    #. Define:

        * ``features: List[tuple]`` - measurements
        * ``labels: List[int]`` - species
        * ``label_encoder: Dict[int, str]`` - dictionary with encoded (as numbers) species names

    #. Separate header from data
    #. To encode and decode ``labels`` (species) we need ``label_encoder: Dict[int, str]``:

        * key - id (incremented integer value)
        * value - species name

    #. ``label_encoder`` must be generated from ``DATA``
    #. For each row add appropriate data to ``features``, ``labels`` and ``label_encoder``
    #. Print ``features``, ``labels`` and ``label_encoder``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zdefiniuj:

        * ``features: List[tuple]`` - pomiary
        * ``labels: List[int]`` - gatunki
        * ``label_encoder: Dict[int, str]`` - słownik zakodowanych (jako cyfry) nazw gatunków

    #. Odseparuj nagłówek od danych
    #. Aby móc zakodować i odkodować ``labels`` (gatunki) potrzebny jest ``label_encoder: Dict[int, str]``:

        * key - identyfikator (kolejna liczba rzeczywista)
        * value - nazwa gatunku

    #. ``label_encoder`` musi być wygenerowany z ``DATA``
    #. Dla każdego wiersza dodawaj odpowiednie dane do ``feature``, ``labels`` i ``label_encoder``
    #. Wypisz ``feature``, ``labels`` i ``label_encoder``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

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

:Output:
    .. code-block:: python

        features: List[tuple]
        # [(5.8, 2.7, 5.1, 1.9),
        #  (5.1, 3.5, 1.4, 0.2),
        #  (5.7, 2.8, 4.1, 1.3),
        #  (6.3, 2.9, 5.6, 1.8),
        #  (6.4, 3.2, 4.5, 1.5),
        #  (4.7, 3.2, 1.3, 0.2), ...]

        labels: List[int]
        # [0, 1, 2, 0, 2, 1, 2, 0, 1, 0, 0, 1, 1, 2, 1, 2, 0, 2, 0, 2, 1]

        label_encoder: Dict[int, str]
        # {0: 'virginica',
        #  1: 'setosa',
        #  2: 'versicolor'}

:The whys and wherefores:
    * ``dict`` lookups
    * Dynamic ``dict`` generating
    * ``dict`` reversal
