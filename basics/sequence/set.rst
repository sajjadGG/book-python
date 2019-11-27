****************
Sequence ``set``
****************


.. highlights::
    * Only unique values
    * Mutable - can add, remove, and modify items


Initializing
============
.. highlights::
    * Do not record element position
    * Do not record order of insertion
    * Do not support indexing
    * Do not support slicing

Initialize empty
----------------
.. highlights::
    * Defining only with ``set()``

.. code-block:: python

    my_set = set()

Initialize with one element
---------------------------
.. highlights::
    * Comma after last element is optional
    * Brackets are required

.. code-block:: python

    my_set = {1}
    my_set = {1,}

Initialize with many elements
-----------------------------
.. highlights::
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

Type Annotation
---------------
.. code-block:: python

    my_set: set = set()

.. code-block:: python

    from typing import Set

    my_set: Set[int] = {1, 2, 3}
    my_set: Set[float] = {0.0, 1.1, 2.2}
    my_set: Set[str] = {'a', 'b', 'c'}


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


Membership Operators
====================

Equals
------
.. code-block:: python

    {1, 2} == {1, 2}        # True
    {1, 2} == {2, 1}        # True

Not equals
----------
.. code-block:: python

    {1, 2, 3} != {1, 2}     # True
    {1, 2} != {1, 2}        # False

Contains
--------
.. code-block:: python

    1 in {1, 2}             # True
    3 in {1, 2}             # False

    {2} in {1, 2}           # False
    {1, 2} in {1, 2}        # False

Missing
-------
.. code-block:: python

    4 not in {1, 2}         # True
    1 not in {1, 2}         # False

    {2} not in {1, 2}       # True
    {1, 2} not in {1, 2}    # True


``set`` Methods
===============

``set.isdisjoint()``
--------------------
.. highlights::
    * No common elements

.. code-block:: python

    {1,2}.isdisjoint({3,4})     # True

``set.issubset()``
------------------
.. highlights::
    * All elements in both

.. code-block:: python

    {1,2} <= {3,4}              # False

.. code-block:: python

    {1,2} <= {1,2}              # True
    {1,2} <= {1,2,3}            # True

.. code-block:: python

    {1,2} < {1,2,3}             # True
    {1,2} < {1,2}               # False

``set.issuperset()``
--------------------
.. highlights::
    * All elements of ``b`` are in ``a``

.. code-block:: python

    {1,2} > {1,2,3}             # False
    {1,2} > {1,2}               # False
    {1,2,3} > {1,2}             # True

.. code-block:: python

    {1,2} >= {1,2}              # True
    {1,2,3} >= {1,2}            # True

``set.union()``
---------------
.. highlights::
    * add

.. code-block:: python

    {1,2} | {1,2}               # {1, 2}
    {1,2,3} | {1,2}             # {1, 2, 3}
    {1,2,3} | {1,2,4}           # {1, 2, 3, 4}
    {1,2} | {1,3} | {2,4}       # {1, 2, 3, 4}

``set.difference()``
--------------------
.. highlights::
    * subtract

.. code-block:: python

    {1,2} - {2,3}               # {1}
    {1,2} - {2,3} - {3}         # {1}
    {1,2} - {1,2,3}             # set()

``set.symmetric_difference()``
------------------------------
.. highlights::
    * not common elements from each

.. code-block:: python

    {1,2} ^ {1,2}               # set()
    {1,2} ^ {2,3}               # {1, 3}
    {1,2} ^ {1,3}               # {2, 3}

``set.intersection()``
----------------------
.. highlights::
    * common element from each

.. code-block:: python

    {1,2} & {2,3}               # {2}
    {1,2} & {2,3} & {2,4}       # {2}
    {1,2} & {2,3} & {3}         # set()


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
    #. Dla danych wejściowych (por. sekcja input)
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
