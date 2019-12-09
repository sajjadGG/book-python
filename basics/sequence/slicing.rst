.. _Sequence Slicing:

****************
Sequence Slicing
****************


Accessing range of elements
===========================
.. highlights::
    * Slice Index must be positive or negative ``int`` or zero
    * ``my_sequence[start:stop:step]``
    * ``my_sequence[start:stop]``
    * Slice has three indexes:

        - start (inclusive), default: 0
        - stop (exclusive), default: len(...)
        - step, default: 1

.. code-block:: python

    text = 'We choose to go to the Moon!'

    len(text)
    # 28


Accessing slice from start
==========================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0:2]       # 'We'
    text[0:9]       # 'We choose'

    text[16:28]     # 'to the Moon!'
    text[23:28]     # 'Moon!'

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[3:9]       # 'choose'
    text[23:27]     # 'Moon'

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:2]        # 'We'
    text[:9]        # 'We choose'

    text[16:]       # 'to the Moon!'
    text[23:]       # 'Moon!'


Accessing slice from back
=========================
.. highlights::
    * Negative index starts from the end and go right to left

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:-13]      # 'We choose to go'
    text[:-19]      # 'We choose'

    text[-12:]      # 'to the Moon!'
    text[-5:]       # 'Moon!'

    text[-12:-6]    # 'to the'
    text[-5:-1]     # 'Moon'

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[23:-2]     # 'Moo'
    text[13:-2]     # 'go to the Moo'

    text[-1:0]      # ''
    text[-2:0]      # ''
    text[-2:2]      # ''
    text[-5:5]      # ''


Every ``n-th`` element
======================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::2]             # 'W hoet ot h on'

.. code-block:: python
    :caption: Reversing

    text = 'We choose to go to the Moon!'

    text[::-1]            # '!nooM eht ot og ot esoohc eW'
    text[::-2]            # '!oMeto go soce'


Accessing slice not existing elements
=====================================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:100]      # 'We choose to go to the Moon!'
    text[100:]      # ''


Accessing slice from all elements
=================================
* Used in ``numpy``

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:]         # 'We choose to go to the Moon!'


Arithmetic operations on slice indexes
======================================
.. code-block:: python

    text = 'We choose to go to the Moon!'
    first = 23
    last = 28

    text[first:last]       # 'Moon!'
    text[first:last-1]     # 'Moon'

.. code-block:: python

    text = 'We choose to go to the Moon!'
    first = 23
    last = 28
    step = 2

    text[first:last:step]       # 'Mo!'
    text[first:last-1:step]     # 'Mo'

.. code-block:: python

    text = 'We choose to go to the Moon!'
    first = 9
    last = 2
    step = -2

    text[first:last:step]       # ' soc!'
    text[first-1:last:step]     # 'eoh'

.. code-block:: python

    text = 'We choose to go to the Moon!'

    start = text.find('Moon')   # 23
    stop = start + 4

    text[start:stop]
    # Moo


Slicing sequences
=================

Slicing ``str``
---------------
.. code-block:: python

    DATA = 'abcde'

    DATA[:3]            # 'abc'
    DATA[3:]            # 'de'
    DATA[1:4]           # 'bcd'
    DATA[::2]           # 'ace'
    DATA[::-1]          # 'edcba'

Slicing ``tuple``
-----------------
.. code-block:: python

    DATA = ('a', 'b', 'c', 'd', 'e')

    DATA[:3]            # ('a', 'b', 'c')
    DATA[3:]            # ('d', 'e')
    DATA[1:4]           # ('b', 'c', 'd')
    DATA[::2]           # ('a', 'c', 'e')
    DATA[::-1]          # ('e', 'd', 'c', 'b', 'a')

Slicing ``list``
----------------
.. highlights::
    * Slicing works the same as for ``str``

.. code-block:: python

    DATA = ['a', 'b', 'c', 'd', 'e']

    DATA[:3]            # ['a', 'b', 'c']
    DATA[3:]            # ['d', 'e']
    DATA[1:4]           # ['b', 'c', 'd']
    DATA[::2]           # ['a', 'c', 'e']
    DATA[::-1]          # ['e', 'd', 'c', 'b', 'a']

Slice ``set``
-------------
.. highlights::
    * Slicing ``set`` is not possible

.. code-block:: python

    DATA = {'a', 'b', 'c', 'd', 'e'}

    DATA[:3]
    # TypeError: 'set' object is not subscriptable

Slice ``dict``
--------------
.. code-block:: python

    DATA = {'a': 1, 'b': 2}

    DATA[:3]
    # TypeError: unhashable type: 'slice'


Slicing nested sequences
========================
.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    DATA[::2]
    # [
    #   [1, 2, 3],
    #   [7, 8, 9],
    # ]


Slice function
==============
.. highlights::
    * Slice object can be returned from function
    * Function can, for example, calculate starting point of a sub-string

.. code-block:: python

    text = 'We choose to go to the Moon!'

    between = slice(23, 28)
    text[between]
    # 'Moon!'


Assignments
===========

Simple collections
------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/slice_every_nth.py`

:English:
    #. Create tuple ``a`` with digits: 0, 1, 2, 3
    #. Create list ``b`` with digits: 2, 3, 4, 5
    #. Create set ``c`` with every second element from ``a`` and ``b``
    #. Print ``c``

:Polish:
    #. Stwórz tuplę ``a`` z cyframi: 0, 1, 2, 3
    #. Stwórz listę ``b`` z cyframi: 2, 3, 4, 5
    #. Stwórz zbiór ``c`` z co drugim elementem ``a`` i ``b``
    #. Wypisz ``c``

:Output:
    .. code-block:: python

        c: set
        # {0, 2, 4}

:The whys and wherefores:
    * Defining and using ``list``, ``tuple``, ``set``
    * Slice data structures
    * Type casting

Split train/test
----------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/slice_split_train_test.py`

:English:
    #. For input data (see below)
    #. Write header (first line) to ``header`` variable
    #. Write data without header to ``data`` variable
    #. Calculate pivot point: number records in ``data`` multiplied by PERCENT
    #. Divide ``data`` into two lists:

        * ``train``: 60% - training data
        * ``test``: 40% - testing data

    #. From ``data`` write training data from start to pivot
    #. From ``data`` write test data from pivot to end

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zapisz nagłówek (pierwsza linia) do zmiennej ``header``
    #. Zapisz dane bez nagłówka do zmiennej ``data``
    #. Wylicz punkt podziału: ilość rekordów w ``data`` razy PROCENT
    #. Podziel ``data`` na dwie listy:

        * ``train``: 60% - dane do uczenia
        * ``test``: 40% - dane do testów

    #. Z ``data`` zapisz do uczenia rekordy od początku do punktu podziału
    #. Z ``data`` zapisz do testów rekordy od punktu podziału do końca

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

        train: List[tuple]
        # [(5.8, 2.7, 5.1, 1.9, 'virginica'),
        #  (5.1, 3.5, 1.4, 0.2, 'setosa'),
        #  (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        #  (6.3, 2.9, 5.6, 1.8, 'virginica'),
        #  (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        #  (4.7, 3.2, 1.3, 0.2, 'setosa'),
        #  (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        #  (7.6, 3.0, 6.6, 2.1, 'virginica'),
        #  (4.9, 3.0, 1.4, 0.2, 'setosa'),
        #  (4.9, 2.5, 4.5, 1.7, 'virginica'),
        #  (7.1, 3.0, 5.9, 2.1, 'virginica'),
        #  (4.6, 3.4, 1.4, 0.3, 'setosa')]

        test: List[tuple]
        # [(5.4, 3.9, 1.7, 0.4, 'setosa'),
        #  (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        #  (5.0, 3.6, 1.4, 0.3, 'setosa'),
        #  (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        #  (6.5, 3.0, 5.8, 2.2, 'virginica'),
        #  (6.5, 2.8, 4.6, 1.5, 'versicolor'),
        #  (6.3, 3.3, 6.0, 2.5, 'virginica'),
        #  (6.9, 3.1, 4.9, 1.5, 'versicolor'),
        #  (4.6, 3.1, 1.5, 0.2, 'setosa')]

:The whys and wherefores:
    * Using nested sequences
    * Using slices
    * Type casting
    * Magic Number

Slicing text
------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/slice_text.py`

:English:
    #. For input data (see below)
    #. Expected value is ``Jana III Sobieskiego``
    #. Use only ``slice`` to clean each variable
    #. Compare with output data (see below)

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Oczekiwana wartość ``Jana III Sobieskiego``
    #. Wykorzystaj tylko ``slice`` do oczyszczenia każdej zmiennej
    #. Porównaj wyniki z danymi wyjściowymi (patrz sekcja output)

:Input:
    .. code-block:: python

        a = 'lt. Mark Watney'
        b = 'lt. col. Jan Twardowski\t'
        c = 'dr hab. inż. Jan Twardowski, prof. LAW'
        d = 'gen. pil. Jan Twardowski'
        e = 'Mark Watney, PhD'
        f = 'lt. col. ret. Melissa Lewis'
        g = 'dr n. med. Ryan Stone'
        h = 'Ryan Stone, MD-PhD'

:The whys and wherefores:
    * Variable definition
    * Print formatting
    * Slicing strings
    * Cleaning text input
