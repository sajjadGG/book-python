.. _Sequence Getitem:

*****************
Sequence Get Item
*****************


Rationale
=========
.. highlights::
    * Index must ``int`` (positive, negative or zero)
    * Index must be less or equal to length of object
    * Negative index starts from the end and go right to left


Positive Index
==============
.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'


Negative Index
==============
.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[-0]            # 'a'
    data[-1]            # 'd'
    data[-2]            # 'c'


Out of Range
============
.. code-block:: python
    :caption: Accessing not existing element

    data = ['a', 'b', 'c', 'd']

    data[100]           # IndexError: string index out of range
    data[-100]          # IndexError: string index out of range


Ordered Sequence
================
.. code-block:: python
    :caption: Get item from ``str``

    data = 'abcd'

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'

    data[-0]            # 'a'
    data[-1]            # 'd'
    data[-2]            # 'c'

.. code-block:: python
    :caption: Get item from ``list``

    data = ['a', 'b', 'c', 'd']

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'

    data[-0]            # 'a'
    data[-1]            # 'd'
    data[-2]            # 'c'

.. code-block:: python
    :caption: Get item from ``tuple``

    data = ('a', 'b', 'c', 'd')

    data[0]             # 'a'
    data[1]             # 'b'
    data[2]             # 'c'

    data[-0]            # 'a'
    data[-1]            # 'd'
    data[-2]            # 'c'


Unordered Sequence
==================
.. code-block:: python
    :caption: Get item from ``set`` is impossible. ``set`` is unordered data structure.

    data = {'a', 'b', 'c', 'd'}

    data[0]             # TypeError: 'set' object is not subscriptable
    data[1]             # TypeError: 'set' object is not subscriptable
    data[2]             # TypeError: 'set' object is not subscriptable

    data[-0]            # TypeError: 'set' object is not subscriptable
    data[-1]            # TypeError: 'set' object is not subscriptable
    data[-2]            # TypeError: 'set' object is not subscriptable

.. code-block:: python
    :caption: Get item from ``frozenset`` is impossible. ``frozenset`` is unordered data structure.

    data = frozenset({'a', 'b', 'c', 'd'})

    data[0]             # TypeError: 'frozenset' object is not subscriptable
    data[1]             # TypeError: 'frozenset' object is not subscriptable
    data[2]             # TypeError: 'frozenset' object is not subscriptable

    data[-0]            # TypeError: 'frozenset' object is not subscriptable
    data[-1]            # TypeError: 'frozenset' object is not subscriptable
    data[-2]            # TypeError: 'frozenset' object is not subscriptable


Assignments
===========

Sequence Getitem Select
------------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/sequence_getitem_select.py`

:English:
    #. Use data from "Input" section (see below)
    #. Write header (first line) to ``header: tuple`` variable
    #. Create ``result: list``
    #. Add to ``result`` converted to ``list`` values from row at index 2, 6, 9 (each row is a separate list)
    #. Add to ``result`` converted to ``tuple`` values from row at index 12, 15, 16 (each row is a separate tuple)
    #. Append to ``result``: empty ``list``, empty ``tuple``, empty ``set`` and empty ``frozenset``
    #. Use only indexes
    #. Do not use ``for``, ``while`` or ``slice()``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zapisz nagłówek (pierwsza linia) do zmiennej ``header: tuple``
    #. Stwórz ``result: list``
    #. Dodaj do ``result`` przekonwertowane do ``list`` wartości z wierszy o indeksach 2, 6, 9 (każdy wiersz to osobna lista)
    #. Dodaj do ``result`` przekonwertowane do ``tuple`` wartości z wierszy o indeksach 12, 15, 16  (każdy wiersz to osobna krotka)
    #. Dodaj na koniec ``result``: pustą ``list``, pustą ``tuple``, pusty ``set``, pusty ``frozenset``
    #. Użyj tylko indeksów
    #. Nie używaj ``for``, ``while`` lub ``slice()``
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

        header: tuple
        # ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

        result: list
        # [[5.1, 3.5, 1.4, 0.2, 'setosa'],
        #  [4.7, 3.2, 1.3, 0.2, 'setosa'],
        #  [4.9, 3.0, 1.4, 0.2, 'setosa'],
        #  (4.6, 3.4, 1.4, 0.3, 'setosa'),
        #  (5.0, 3.6, 1.4, 0.3, 'setosa'),
        #  (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        #  [],
        #  (),
        #  set(),
        #  frozenset()]

:The whys and wherefores:
    * Using nested data structures
    * Using indexes
    * Type casting

:Hint:
    * To pretty print use ``pprint(result)`` (requires ``from pprint import pprint``)
