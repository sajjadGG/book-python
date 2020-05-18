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
    data = [1, 2, 3]
    data = [1.1, 2.2, 3.3]
    data = [True, False]
    data = ['a', 'b', 'c']
    data = ['a', 1, 2.2, True, None]

.. code-block:: python

    list('hello')
    # ['h', 'e', 'l', 'l', 'o']

    list('ABCD')
    # ['A', 'B', 'C', 'D']


Type Casting
============
* ``list()`` converts argument to ``list``

.. code-block:: python

    data = [1, 2, 3]
    list(data)
    # [1, 2, 3]

.. code-block:: python

    data = (1, 2, 3)
    list(data)
    # [1, 2, 3]

.. code-block:: python

    data = {1, 2, 3}
    list(data)
    # [1, 2, 3]

.. code-block:: python

    data = frozenset({1, 2, 3})
    list(data)
    # [1, 2, 3]


Getting Items
=============
.. highlights::
    * More about indexing in chapter :ref:`Sequence Indexing`
    * More about slicing in chapter :ref:`Sequence Slicing`

.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[0]         # 'a'
    data[1]         # 'b'
    data[2]         # 'c'
    data[3]         # 'd'


Setting Items
=============
.. code-block:: python

    data = ['a', 'b', 'c', 'd']

    data[0] = 'x'
    print(data)
    # ['x', 'b', 'c', 'd']

    data[4] = 'x'
    # IndexError: list assignment index out of range

Deleting Items
==============
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


Inserting Elements
==================
* Insert at specific position

.. code-block:: python

    data = [1, 2]

    data.insert(0, 'a')
    # ['a', 1, 2]

.. code-block:: python

    data = [1, 2]

    data.insert(1, 'a')
    # [1, 'a', 2]


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

    data.append(4).sort()
    # AttributeError: 'NoneType' object has no attribute 'sort'

.. code-block:: python

    data = [3, 1, 2]
    data.append(4)
    data.sort()

    print(data)
    # [1, 2, 3, 4]


Built-in Functions on Sequences
===============================
* ``min()`` - Minimal value
* ``max()`` - Maximal value
* ``sum()`` - Sum of elements
* ``len()`` - Length of a list
* ``all()`` - All values are ``True``
* ``any()`` - Any values is ``True``
* ``isinstance(a, b)`` - If ``a`` is instance of ``b``
* ``isinstance(a, (b,c))`` - If ``a`` is instance of ``b`` or ``c``

.. code-block:: python

    data = [2, 0, 1]

    min(data)       # 0
    max(data)       # 2
    sum(data)       # 3
    len(data)       # 3
    any(data)       # True
    all(data)       # False

.. code-block:: python

    data = [True, False, True]

    min(data)       # False
    max(data)       # True
    sum(data)       # 2
    len(data)       # 3
    any(data)       # True
    all(data)       # False


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

        * 'a'
        * 1
        * 2.2

    #. Print ``result``
    #. Print number of elements in ``result``

:Polish:
    #. Stwórz listę ``result`` z elementami:

        * 'a'
        * 1
        * 2.2

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
    #. ``a`` with data from row 1
    #. ``b`` with data from row 2
    #. ``c`` with data from row 3

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz listy ``a``, ``b``, ``c`` reprezentujące każdy wierszy
    #. ``a`` z danymi z wiersza 1
    #. ``b`` z danymi z wiersza 2
    #. ``c`` z danymi z wiersza 3

:Input:
    .. csv-table:: Input data
        :header: "Row", "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"
        :stub-columns: 1

        "1", "5.8", "2.7", "5.1", "1.9", "virginica"
        "2", "5.1", "3.5", "1.4", "0.2", "setosa"
        "3", "5.7", "2.8", "4.1", "1.3", "versicolor"

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
    #. Insert at the begin of ``a`` last element popped from ``b``
    #. Append to the ``b`` last element popped from ``a``
    #. For getting elements use ``list.pop()``
    #. From list ``c`` using ``del`` delete last element
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Na początek ``a`` wstaw ostatni element wyciągnięty z ``b``
    #. Na koniec ``b`` wstaw ostatni element wyciągnięty z ``a``
    #. Do wyciągnięcia używaj ``list.pop()``
    #. Z listy ``c`` za pomocą ``del`` usuń last element
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        a = [4.7, 3.2, 1.3, 0.2, 'setosa']
        b = [7.0, 3.2, 4.7, 1.4, 'versicolor']
        c = [7.6, 3.0, 6.6, 2.1, 'virginica']

:Output:
    .. code-block:: python

        a = ['versicolor', 4.7, 3.2, 1.3, 0.2]
        b = [7.0, 3.2, 4.7, 1.4, 'setosa']
        c = [7.6, 3.0, 6.6, 2.1]


:The whys and wherefores:
    * Defining ``list``
    * Learning IDE features
