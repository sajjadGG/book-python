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
    :caption: Initialize empty

    my_list = []
    my_list = list()

.. code-block:: python
    :caption: Initialize with one element

    my_list = [1]
    my_list = [1,]

.. code-block:: python
    :caption: Initialize with many elements

    my_list = [1, 2.0, None, False, 'Iris']
    my_list = [1, 2.0, None, False, 'Iris',]

.. code-block:: python

    alphabet = list('ABCDE')
    # ['A', 'B', 'C', 'D', 'E']


Type Annotation
===============
.. code-block:: python

    my_list: list = list()
    my_list: list = []

.. code-block:: python

    my_list: list = ['a', 1, 2.2]

.. code-block:: python

    from typing import List

    my_list: List[int] = [1, 2, 3, 4]
    my_list: List[float] = [5.8, 2.7, 5.1, 1.9]
    my_list: List[str] = ['a', 'b', 'c', 'd']


Adding Elements
===============
* ``list + list``
* ``list.extend()``
* ``list.append()``

.. code-block:: python

    my_list = [1, 2]

    my_list + [3, 4]
    # [1, 2, 3, 4]

.. code-block:: python
    :caption: Extending lists

    my_list = [1, 2]

    my_list.extend([3, 4])
    # [1, 2, 3, 4]

.. code-block:: python
    :caption: Appending single item

    my_list = [1, 2]

    my_list.append(3)
    # [1, 2, 3]

.. code-block:: python
    :caption: Appending multiple items

    my_list = [1, 2]

    my_list.append([3, 4])
    # [1, 2, [3, 4]]

Inserting Elements at Specific Position
---------------------------------------
.. code-block:: python

    my_list = [1, 2]

    my_list.insert(0, 'a')
    # ['a', 1, 2]

.. code-block:: python

    my_list = [1, 2]

    my_list.insert(1, 'a')
    # [1, 'a', 2]


Modification
============

Getting Items
-------------
.. highlights::
    * More in :ref:`Sequence Indexing` and :ref:`Sequence Slicing`

.. code-block:: python

    my_list = ['a', 'b', 'c', 'd']

    my_list[0]         # 'a'
    my_list[1]         # 'b'
    my_list[2]         # 'c'
    my_list[3]         # 'd'

Setting Items
-------------
.. code-block:: python

    my_list = ['a', 'b', 'c', 'd']

    my_list[0] = 'x'

    print(my_list)
    # ['x', 'b', 'c', 'd']

Deleting Items
--------------
.. code-block:: python

    my_list = ['a', 'b', 'c', 'd']

    del my_list[3]

    print(my_list)
    # ['a', 'b', 'c']

.. code-block:: python

    my_list = ['a', 'b', 'c', 'd']

    my_list.pop()
    # 'd'

    print(my_list)
    # ['a', 'b', 'c']


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

    my_list = [3, 1, 2]

    my_list.sort().append(4)
    # AttributeError: 'NoneType' object has no attribute 'append'

.. code-block:: python

    my_list = [3, 1, 2]
    my_list.sort()
    my_list.append(4)

    print(my_list)
    # [1, 2, 3, 4]


Membership Operators
====================
* ``==`` - Eq (equals)
* ``!=`` - Ne (not-equals)
* ``in`` - Contains
* ``not in`` - Missing

.. code-block:: python

    [1, 2] == [1, 2]        # True
    [1, 2] == [2, 1]        # False

    [1, 2, 3] != [1, 2]     # True
    [1, 2] != [1, 2]        # False

    1 in [1, 2]             # True
    3 in [1, 2]             # False

    [2] in [1, 2]           # False
    [1, 2] in [1, 2]        # False

    [2] in [1, [2]]         # False
    [1, 2] in [[1,2], 3]    # True

    4 not in [1, 2]         # True
    1 not in [1, 2]         # False

    [2] not in [1, 2]       # True
    [1, 2] not in [1, 2]    # True


Built-in Functions on Sequences
===============================
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``sum()`` - Sum of elements
* ``len()`` - Length of a list

.. code-block:: python

    min([1, 2, 3, 4, 5])
    # 1

    max([1, 2, 3, 4, 5])
    # 5

    sum([1, 2, 3, 4, 5])
    # 15

    len([1, 2, 3])
    # 3


Assignments
===========

Create
------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/list_create.py`

:English:
    #. For given data input (see below)
    #. Create a ``list`` representing each row
    #. To convert table use multiline select with ``alt`` key in your IDE

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Stwórz ``list`` reprezentujący każdy wiersz
    #. Do przekonwertowania tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE

:Input:
    .. csv-table:: Input data
        :header: "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"

        "5.8", "2.7", "5.1", "1.9", "virginica"
        "5.1", "3.5", "1.4", "0.2", "setosa"
        "5.7", "2.8", "4.1", "1.3", "versicolor"
        "6.3", "2.9", "5.6", "1.8", "virginica"
        "6.4", "3.2", "4.5", "1.5", "versicolor"

:Output:
    .. code-block:: python

        a = [5.8, 2.7, 5.1, 1.9, 'virginica']
        b = [5.1, 3.5, 1.4, 0.2, 'setosa']
        c = [5.7, 2.8, 4.1, 1.3, 'versicolor']
        d = [6.3, 2.9, 5.6, 1.8, 'virginica']
        e = [6.4, 3.2, 4.5, 1.5, 'versicolor']

:The whys and wherefores:
    * Defining ``list``
    * Learning IDE features
