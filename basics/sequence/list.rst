*****************
Sequence ``list``
*****************


.. highlights::
    * Can store elements of any types
    * Mutable - can add, remove, and modify items


Initializing
============
.. highlights::
    * ``list()`` is more readable
    * ``[]`` is used more often

Initialize empty
----------------
.. code-block:: python

    my_list = []
    my_list = list()

Initialize with one element
---------------------------
.. highlights::
    * Comma after last element is optional
    * Brackets are required

.. code-block:: python

    my_list = [1]
    my_list = [1,]

Initialize with many elements
-----------------------------
.. highlights::
    * Brackets are required

.. code-block:: python

    my_list = [1, 2.0, None, False, 'Iris']

.. code-block:: python

    alphabet = list('ABCDE')
    # ['A', 'B', 'C', 'D', 'E']

Type Annotation
---------------
.. code-block:: python

    my_list: list = list()
    my_list: list = []

    my_list: list = ['a', 1, 2.2]

.. code-block:: python

    from typing import List

    my_list: List[int] = [1, 2, 3, 4]
    my_list: List[float] = [5.8, 2.7, 5.1, 1.9]
    my_list: List[str] = ['a', 'b', 'c', 'd']


Adding elements
===============

Extending lists
---------------
.. code-block:: python

    my_list = [1, 2]

    my_list.extend([3, 4])
    # [1, 2, 3, 4]

.. code-block:: python

    my_list = [1, 2]

    my_list + [3, 4]
    # [1, 2, 3, 4]

Appending elements
------------------
.. code-block:: python

    my_list = [1, 2]

    my_list.append(3)
    # [1, 2, 3]

.. code-block:: python

    my_list = [1, 2]

    my_list.append([3, 4])
    # [1, 2, [3, 4]]

Inserting elements at specific position
---------------------------------------
.. code-block:: python

    my_list = [1, 2]

    my_list.insert(0, 'a')
    # ['a', 1, 2]

.. code-block:: python

    my_list = [1, 2]

    my_list.insert(1, 'a')
    # [1, 'a', 2]


Accessing elements
==================
.. highlights::
    * More in :ref:`Sequence Indexing` and :ref:`Sequence Slicing`

.. code-block:: python

    my_list = ['a', 'b', 'c', 'd']

    my_list[0]         # 'a'
    my_list[1]         # 'b'
    my_list[3]         # 'd'

.. code-block:: python

    my_list = ['a', 'b', 'c', 'd']

    my_list[-1]        # 'd'
    my_list[-3]        # 'b'


Sorting
=======

``sorted()``
------------
.. highlights::
    * Returns sorted list
    * Do not modify the object

.. code-block:: python

    a = [3, 1, 2]
    b = sorted(a)

    print(a)    # [3, 1, 2]
    print(b)    # [1, 2, 3]

``list.sort()``
---------------
.. highlights::
    * Changes object permanetly

.. code-block:: python

    a = [3, 1, 2]
    b = a.sort()

    print(a)    # [1, 2, 3]
    print(b)    # None


Multiple statements in one line
===============================
.. code-block:: python

    my_list = [3, 1, 2]

    my_list.sort().append(4)
    # AttributeError: 'NoneType' object has no attribute 'append'


Membership Operators
====================
.. csv-table:: Membership operators
    :widths: 15, 25, 60
    :header-rows: 1

    "Operand", "Example", "Description"
    "``x == y``", "``x == 18``", "value of ``x`` is equal to ``y``"
    "``x != y``", "``x != 18``", "value of ``x`` is not equal to ``y``"
    "``x in y``", "``x in [1, 2, 3]``", "``y`` contains ``x``"
    "``x not in y``", "``x not in [1, 2, 3]``", "``y`` not contains ``x``"


Built-in functions on sequences
===============================

``min()``
---------
.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    min(numbers)
    # 1

``max()``
---------
.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    max(numbers)
    # 5

``sum()``
---------
.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    sum(numbers)
    # 15


Length of a ``list``
====================
.. code-block:: python

    my_list = [1, 2, 3]

    len(my_list)
    # 3


Assignments
===========

Create
------
* Complexity level: easy
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/list_create.py`

:English:
    #. For given data input (see below)
    #. Create a ``list`` representing each row
    #. To convert table use multiline select with ``alt`` key in your IDE

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
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

:The whys and wherefores:
    * Defining ``list``
    * Learning IDE features
