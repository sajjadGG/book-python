*******
``set``
*******


* Only unique values
* Mutable - can add, remove, and modify items


Initializing
============
* Do not record element position
* Do not record order of insertion
* Do not support indexing
* Do not support slicing

Initialize empty
----------------
* Defining only with ``set()``

.. code-block:: python

    my_set = set()

Initialize with one element
---------------------------
* Comma after last element is optional
* Brackets are required

.. code-block:: python

    my_set = {1}
    my_set = {1,}

Initialize with many elements
-----------------------------
* Brackets are required
* Only unique values
* Can store elements of any **hashable** types

.. code-block:: python

    my_set = {1, 3, 1}
    # {1, 3}

.. code-block:: python

    my_set = {1, 2.0, 'Jan'}
    # {1, 2.0, 'Jan'}

    my_set = {1, 2.0, (3, 4)}
    # {1, 2.0, (3, 4)}

.. code-block:: python

    my_set = {1, 2.0, [3, 4]}
    # TypeError: unhashable type: 'list'

    my_set = {1, 2.0, {3, 4}}
    # TypeError: unhashable type: 'set'

.. code-block:: python

    {1}
    # {1}

    {1.0}
    # {1.0}

    {1, 1.0}
    # {1}


Adding items
============

Adding one element
------------------
.. code-block:: python

    my_set = {1, 2}

    my_set.add(3)
    # {1, 2, 3}

    my_set.add(3)
    # {1, 2, 3}

    my_set.add(4)
    # {1, 2, 3, 4}

Adding many items
-----------------
.. code-block:: python

    my_set = {1, 2}
    # {1, 2}

    my_set.update({3, 4})
    # {1, 2, 3, 4}

    my_set.update([5, 6])
    # {1, 2, 3, 4, 5, 6}

    my_set.update((7, 8))
    # {1, 2, 3, 4, 5, 6, 7, 8}


Popping items
=============
* Gets and remove items

.. code-block:: python

    my_set = {1, 2, 3}

    value = my_set.pop()

    my_set  # {1, 2}
    value   # 3


Converting to ``set`` deduplicate items
=======================================

Converting ``list`` to ``set``
------------------------------
.. code-block:: python
    :caption: Converting ``list`` to ``set`` deduplicate items

    names = [
        'Twardowski',
        'Иванович',
        'Jiménez',
        'Twardowski'
    ]

    unique_names = set(names)
    # {'Twardowski', 'Иванович', 'Jiménez'}

Converting ``tuple`` to ``set``
-------------------------------
.. code-block:: python
    :caption: Converting ``tuple`` to ``set`` deduplicate items

    names = (
        'Twardowski',
        'Иванович',
        'Jiménez',
        'Twardowski'
    )

    unique_names = set(names)
    # {'Twardowski', 'Иванович', 'Jiménez'}


Length of a ``set``
===================
.. code-block:: python

    my_set = {1, 2, 3}

    len(my_set)
    # 3


Assignments
===========

Create
------
* Complexity level: easy
* Lines of code to write: 13 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/set_create.py`

:English:
    #. For given data input (see below)
    #. Create ``set`` representing first row
    #. Values from second row add to ``set`` using ``.add()``
    #. From third row create ``set`` and add it with ``.update()``
    #. From fourth row create ``tuple`` and add it with ``.update()``
    #. From fifth row create ``list`` and add it with ``.update()``

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Stwórz ``set`` reprezentujący pierwszy wiersz
    #. Wartości z drugiego wiersza dodawaj do ``set`` za pomocą ``.add()``
    #. Na podstawie trzeciego wiersza stwórz ``set`` i dodaj go za pomocą ``.update()``
    #. Na podstawie czwartego wiersza stwórz ``tuple`` i dodaj go za pomocą ``.update()``
    #. Na podstawie piątego wiersza stwórz ``list`` i dodaj go za pomocą ``.update()``

:Input:
    .. csv-table:: Input data
        :header: "Row", "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"

        "1", "5.8", "2.7", "5.1", "1.9", "virginica"
        "2", "5.1", "3.5", "1.4", "0.2", "setosa"
        "3", "5.7", "2.8", "4.1", "1.3", "versicolor"
        "4", "6.3", "2.9", "5.6", "1.8", "virginica"
        "5", "6.4", "3.2", "4.5", "1.5", "versicolor"

:The whys and wherefores:
    * Defining ``set``
    * Basic ``set`` methods
