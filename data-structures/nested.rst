******************
Nested Collections
******************


``list`` of ``tuple``
=====================

Getting elements
----------------
.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    DATA[2]
    # (7.6, 3.0, 6.6, 2.1, 'virginica')

    DATA[2][1]
    # 3.0

Appending elements
------------------
.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    element = (4.9, 2.5, 4.5, 1.7, 'virginica')
    DATA.append(element)

.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    DATA.append((4.9, 3.0, 1.4, 0.2, 'setosa'))

Length
------
.. code-block:: python

    DATA = [
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
    ]

    len(DATA)
    # 3

    len(DATA[2])
    # 5


``list`` of ``dict``
====================

Getting elements
----------------
.. code-block:: python

    DATA = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

    DATA[0]
    # {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa')

    DATA[0]['measurements']
    # [4.7, 3.2, 1.3, 0.2]

    DATA[0]['species']
    # 'setosa'

.. code-block:: python

    DATA = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

    DATA[0].get('kind')
    # KeyError: 'kind'

    DATA[0].get('kind', 'n/a')
    # 'n/a'

    DATA[2].get('measurements')
    # [7.6, 3.0, 6.6, 2.1]

    DATA[2].get('measurements')[1]
    # 3.0

Length
------
.. code-block:: python

    DATA = [
        {'measurements': [4.7, 3.2, 1.3, 0.2], 'species': 'setosa'},
        {'measurements': [7.0, 3.2, 4.7, 1.4], 'species': 'versicolor'},
        {'measurements': [7.6, 3.0, 6.6, 2.1], 'species': 'virginica'},
    ]

    len(DATA)
    # 3

    len(DATA[0])
    # 2

    len(DATA[1])
    # 2

    len(DATA[1]['species'])
    # 10

    len(DATA[1]['measurements'])
    # 4


``list`` of ``list``
====================
* Multidimensional lists

.. code-block:: python

    DATA = [[1,2,3],[4,5,6],[7,8,9]]

.. code-block:: python

    DATA = [[1,2,3], [4,5,6], [7,8,9]]

.. code-block:: python

    DATA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

Getting elements
----------------
.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    array[0][0]
    # 1

    array[0][2]
    # 3

    array[2][1]
    # 8

Length
------
.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    len(DATA)
    # 3

    len(DATA[2])
    # 3


Mixed types
===========

Getting elements
----------------
.. code-block:: python

    DATA = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
        {'species': 'virginica', 'measurements': [7.6, 3.0, 6.6, 2.1]}
    ]

    DATA[1][2]
    # 6

    DATA[3]['species']
    # 'virginica'

    DATA[3].get('species')
    # 'virginica'

Length
------
.. code-block:: python

    DATA = [
        [1, 2, 3],
        (4, 5, 6),
        {7, 8, 9},
        {'species': 'virginica', 'measurements': [7.6, 3.0, 6.6, 2.1]}
    ]

    len(DATA)
    # 4

    len(DATA[0])
    # 3

    len(DATA[3])
    # 2

    len(DATA[3]['measurements'])
    # 4


Assignments
===========

Select
------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/nested_select.py`

:English:
    #. For given data input (see below)
    #. Write header (first line) to ``header`` variable
    #. Write to ``output`` list, data from records:

        * 2, 6, 9 as ``list``
        * 12, 15, 16 as ``tuple``
        * 18, 21 as ``dict``:

            * key -> index number
            * value -> species

    #. Add empty ``set`` to ``output``
    #. Use only indexes
    #. Do not use ``for``, ``while`` or ``slice()``

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Zapisz nagłówek (pierwsza linia) do zmiennej ``header``
    #. Zapisz do listy ``output``, dane z rekordów:

        * 2, 6, 9 jako ``list``
        * 12, 15, 16 jako ``tuple``
        * 18, 21 jako ``dict``:

            * klucz -> numer indeksu
            * wartość -> nazwa gatunku

     #. Dodaj pusty ``set`` do ``output``
     #. Użyj tylko indeksów
     #. Nie używaj ``for``, ``while`` lub ``slice()``

:Input:
    .. code-block:: python
        :caption: Iris Dataset

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


:The whys and wherefores:
    * Umiejętność przetwarzania złożonych typów danych
    * Korzystanie z przecięć danych
    * Konwersja typów
    * Magic Number

