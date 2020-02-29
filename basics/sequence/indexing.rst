.. _Sequence Indexing:

*****************
Sequence Indexing
*****************


Accessing element with index
============================
.. highlights::
    * Index must be positive or negative ``int`` or zero
    * Index must be less or equal to length of object
    * Negative index starts from the end and go right to left

.. code-block:: python
    :caption: Indexing from start

    text = 'We choose to go to the Moon!'

    text[0]         # 'W'
    text[1]         # 'e'
    text[23]        # 'M'

.. code-block:: python
    :caption: Indexing from the end

    text = 'We choose to go to the Moon!'

    text[-1]        # '!'
    text[-5]        # 'M'

.. code-block:: python
    :caption: Accessing not existing element

    text = 'We choose to go to the Moon!'

    text[100]
    # IndexError: string index out of range

    text[-100]
    # IndexError: string index out of range


Indexing sequences
==================
* Indexes on ``set`` are not possible

.. code-block:: python
    :caption: Indexing ``str``

    DATA = 'abcde'

    DATA[0]             # 'a'
    DATA[1]             # 'b'
    DATA[2]             # 'c'

    DATA[-0]            # 'a'
    DATA[-1]            # 'e'
    DATA[-2]            # 'd'

.. code-block:: python
    :caption: Indexing ``list``

    DATA = ['a', 'b', 'c', 'd', 'e']

    DATA[0]             # 'a'
    DATA[1]             # 'b'
    DATA[2]             # 'c'

    DATA[-0]            # 'a'
    DATA[-1]            # 'e'
    DATA[-2]            # 'd'

.. code-block:: python
    :caption: Indexing ``tuple``

    DATA = ('a', 'b', 'c', 'd', 'e')

    DATA[0]             # 'a'
    DATA[1]             # 'b'
    DATA[2]             # 'c'

    DATA[-0]            # 'a'
    DATA[-1]            # 'e'
    DATA[-2]            # 'd'

.. code-block:: python
    :caption: Indexing ``set``. Indexes on ``set`` are not possible

    DATA = {'a', 'b', 'c', 'd', 'e'}

    DATA[0]             # TypeError: 'set' object is not subscriptable
    DATA[1]             # TypeError: 'set' object is not subscriptable
    DATA[2]             # TypeError: 'set' object is not subscriptable

    DATA[-0]            # TypeError: 'set' object is not subscriptable
    DATA[-1]            # TypeError: 'set' object is not subscriptable
    DATA[-2]            # TypeError: 'set' object is not subscriptable


Assignments
===========

Select
------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/indexing_select.py`

:English:
    #. For given data input (see below)
    #. Write header (first line) to ``header: tuple`` variable
    #. Create ``output: list``
    #. Convert to ``list`` data from row at index 2, 6, 9 and add to ``output``
    #. Convert to ``tuple`` data from row at index 12, 15, 16 and add to ``output``
    #. Add empty ``set``, ``list`` and ``tuple`` to ``output``
    #. Use only indexes
    #. Do not use ``for``, ``while`` or ``slice()``

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zapisz nagłówek (pierwsza linia) do zmiennej ``header: tuple``
    #. Stwórz ``data: list``
    #. Przekonwertuj do ``list`` dane z wierszy o indeksach 2, 6, 9 i dodaj do ``data``
    #. Przekonwertuj do ``tuple`` dane z wierszy o indeksach 12, 15, 16 i dodaj do ``data``
    #. Dodaj pusty ``set``, ``list`` oraz ``tuple`` do ``data``
    #. Użyj tylko indeksów
    #. Nie używaj ``for``, ``while`` lub ``slice()``

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

        header: tuple
        # ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

        data: list
        # [[5.1, 3.5, 1.4, 0.2, 'setosa'],
        #  [4.7, 3.2, 1.3, 0.2, 'setosa'],
        #  [4.9, 3.0, 1.4, 0.2, 'setosa'],
        #  (4.6, 3.4, 1.4, 0.3, 'setosa'),
        #  (5.0, 3.6, 1.4, 0.3, 'setosa'),
        #  (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        #  set(), [], ()]

:The whys and wherefores:
    * Using nested data structures
    * Using indexes
    * Type casting

