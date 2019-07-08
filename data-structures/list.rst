********
``list``
********


* Can store elements of any types
* Mutable - can add, remove, and modify items


Initializing
============
* ``list()`` is more readable
* ``[]`` is used more often

Initialize empty
----------------
.. code-block:: python

    my_list = []
    my_list = list()

Initialize with one element
---------------------------
* Comma after last element is optional
* Brackets are required

.. code-block:: python

    my_list = [1]
    my_list = [1,]

Initialize with many elements
-----------------------------
* Brackets are required

.. code-block:: python

    my_list = [1, 2.0, None, False, 'José']

.. code-block:: python

    alphabet = list('ABCDE')
    # ['A', 'B', 'C', 'D', 'E']


Adding elements
===============

Appending elements
------------------
.. code-block:: python

    my_list = [1, 2]

    my_list.append(3)
    # [1, 2, 3]

.. code-block:: python

    my_list = [1, 2]

    my_list.append([4, 5])
    # [1, 2, 3, [4, 5]]

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


Inserting elements at specific position
---------------------------------------
.. code-block:: python

    my_list = [1, 2]

    my_list.insert(0, 'a')
    # ['a', 1, 2]


``sorted()`` vs. ``list.sort()``
================================

``sorted()``
------------
* ``sorted()`` zwraca posortowaną listę, ale nie zapisuje zmienionej kolejności

.. code-block:: python

    numbers = [3, 1, 2]

    sorted(numbers)
    # [1, 2, 3]

    print(numbers)
    # [3, 1, 2]

``list.sort()``
---------------
* ``list.sort()`` zmienia listę na stałe

.. code-block:: python

    numbers = [3, 1, 2]

    numbers.sort()
    # None

    print(numbers)
    # [1, 2, 3]


Multiple statements in one line
===============================
.. code-block:: python

    my_list = [3, 1, 2]

    a = my_list.sort().append(4)
    # AttributeError: 'NoneType' object has no attribute 'append'


Membership Operators
====================
.. csv-table:: Membership operators
    :widths: 15, 25, 60
    :header-rows: 1

    "Operand", "Example", "Description"
    "``x == y``", "``x == 18``", "value of ``x`` is equal to ``y``"
    "``x != y``", "``x != 18``", "value of ``x`` is not equal to ``y``"
    "``x in y``", "``x in [1, 2, 3]``", "``x`` contains ``y``"
    "``x not in y``", "``x not in [1, 2, 3]``", "``x`` not contains ``y``"


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
* Filename: ``data-structures/list_create.py``
* Lines of code to write: 3 lines
* Estimated time of completion: 5 min

.. csv-table:: Pomiary Iris
    :name: sequences-list-iris
    :header: "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"

    "5.8", "2.7", "5.1", "1.9", "virginica"
    "5.1", "3.5", "1.4", "0.2", "setosa"
    "5.7", "2.8", "4.1", "1.3", "versicolor"
    "6.3", "2.9", "5.6", "1.8", "virginica"
    "6.4", "3.2", "4.5", "1.5", "versicolor"

#. Dane są pomiary :numref:`sequences-list-iris`
#. Każdy z wierszy zapisz jako osobny ``list``
#. Do przekonwertowania tabelki, wykorzystaj zaznaczanie wielu linijek za pomocą klawisza ``alt`` w Twoim IDE
