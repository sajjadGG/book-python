*****************
Sequence ``list``
*****************


.. highlights::
    * Can store elements of any types
    * Mutable - can add, remove, and modify items


Type Definition
===============
.. highlights::
    * ``[]`` is used more often
    * ``list()`` is more readable
    * Comma after last element is optional
    * Brackets are required

.. code-block:: python
    :caption: ``list`` type definition

    data = list()
    data = []

    data = [1]
    data = [1,]

    data = [1, 2.0, None, False, 'Iris']
    data = [1, 2.0, None, False, 'Iris',]

.. code-block:: python

    alphabet = list('ABCDE')
    # ['A', 'B', 'C', 'D', 'E']


Adding Elements
===============
* ``list + list``
* ``list.extend()``
* ``list.append()``

.. code-block:: python
    :caption: Adding two lists

    data = [1, 2]

    data + [3, 4]
    # [1, 2, 3, 4]

.. code-block:: python
    :caption: Extending lists

    data = [1, 2]

    data.extend([3, 4])
    # [1, 2, 3, 4]

.. code-block:: python
    :caption: Appending single item

    data = [1, 2]

    data.append(3)
    # [1, 2, 3]

.. code-block:: python
    :caption: Appending multiple items

    data = [1, 2]

    data.append([3, 4])
    # [1, 2, [3, 4]]

Inserting Elements at Specific Position
---------------------------------------
.. code-block:: python

    data = [1, 2]

    data.insert(0, 'a')
    # ['a', 1, 2]

.. code-block:: python

    data = [1, 2]

    data.insert(1, 'a')
    # [1, 'a', 2]


Modification
============

Getting Items
-------------
.. highlights::
    * More in :ref:`Sequence Indexing` and :ref:`Sequence Slicing`

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[0]         # 'a'
    data[1]         # 'b'
    data[2]         # 'c'
    data[3]         # 'd'

Setting Items
-------------
.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[0] = 'x'

    print(data)
    # ['x', 'b', 'c', 'd']

Deleting Items
--------------
.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    del data[3]

    print(data)
    # ['a', 'b', 'c']

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    value = data.pop()

    print(data)
    # ['a', 'b', 'c']

    print(value)
    # 'd'


Sorting
=======
.. epigraph::
    Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data. It was invented by Tim Peters in 2002 for use in the Python programming language. The algorithm finds subsets of the data that are already ordered, and uses the subsets to sort the data more efficiently. This is done by merging an identified subset, called a run, with existing runs until certain criteria are fulfilled. Timsort has been Python's standard sorting algorithm since version 2.3. It is now also used to sort arrays in Java SE 7, and on the Android platform.

.. highlights::
    * ``sorted()`` - Returns sorted list, do not modify the original
    * ``list.sort()`` - Changes object permanently, returns None

.. code-block:: python

    a = [3, 1, 2]
    b = sorted(a)

    print(a)
    # [3, 1, 2]

    print(b)
    # [1, 2, 3]

.. code-block:: python

    a = [3, 1, 2]
    b = a.sort()

    print(a)
    # [1, 2, 3]

    print(b)
    # None


Multiple Statements in One Line
===============================
.. code-block:: python

    data = [3, 1, 2]

    data.sort().append(4)
    # AttributeError: 'NoneType' object has no attribute 'append'

.. code-block:: python

    data = [3, 1, 2]
    data.sort()
    data.append(4)

    print(data)
    # [1, 2, 3, 4]


Built-in Functions on Sequences
===============================
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``sum()`` - Sum of elements
* ``len()`` - Length of a list

.. code-block:: python

    a = [1, 2, 3, 4, 5]

    min(a)      # 1
    max(a)      # 5
    sum(a)      # 15
    len(a)      # 5


Assignments
===========

List Create
-----------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 3 min
* Solution: :download:`solution/sequence_list_create.py`

:English:
    #. Create list ``result`` with elements:

        * 1
        * 1.1
        * 'Mark Watney'

    #. Print ``result``
    #. Print number of elements in ``result``

:Polish:
    #. Stwórz listę ``result`` z elementami:

        * 1
        * 1.1
        * 'Mark Watney'

    #. Wypisz ``result``
    #. Wypisz liczbę elementów ``result``

List Many
---------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/sequence_list_many.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create lists ``a``, ``b``, ``c`` representing each row

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz listy ``a``, ``b``, ``c`` reprezentujące każdy wierszy

:Input:
    .. csv-table:: Input data
        :header: "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"

        "5.8", "2.7", "5.1", "1.9", "virginica"
        "5.1", "3.5", "1.4", "0.2", "setosa"
        "5.7", "2.8", "4.1", "1.3", "versicolor"

:The whys and wherefores:
    * Defining ``list``
    * Learning IDE features

Modify
------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/sequence_list_modify.py`

:English:
    #. Use data from "Input" section (see below)
    #. Insert at index zero of ``a`` list species name from ``b`` (setosa)
    #. Append to the ``b`` list species name popped from ``a`` (virginica)
    #. From list ``c`` delete species

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Na listę ``a`` na pozycję o indeksie 0 wstaw gatunek pobrany z listy ``b`` (setosa)
    #. Na koniec listy ``b`` wstaw gatunek pobrany z listy ``a`` (virginica)
    #. Z listy ``c`` usuń gatunek

:Input:
    .. code-block:: python

        a = [5.8, 2.7, 5.1, 1.9, 'virginica']
        b = [5.1, 3.5, 1.4, 0.2, 'setosa']
        c = [5.7, 2.8, 4.1, 1.3, 'versicolor']

:The whys and wherefores:
    * Defining ``list``
    * Learning IDE features
