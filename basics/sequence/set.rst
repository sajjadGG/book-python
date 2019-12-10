****************
Sequence ``set``
****************


.. highlights::
    * Only unique values
    * Mutable - can add, remove, and modify items
    * Can store elements of any **hashable** types


Type Definition
===============
.. highlights::
    * Do not record element position
    * Do not record order of insertion
    * Do not support indexing
    * Do not support slicing
    * Defining only with ``set()`` - no short syntax
    * Comma after last element is optional
    * Brackets are required

.. code-block:: python
    :caption: Initialize empty

    my_set = set()

.. code-block:: python
    :caption: Initialize with one element

    my_set = {1}
    my_set = {1,}

.. code-block:: python
    :caption: Initialize with many elements. Stores only unique values.

    my_set = {1, 3, 1}
    # {1, 3}

    my_set = {1, 2.0, 'Jan'}
    # {1, 2.0, 'Jan'}

    my_set = {1, 2.0, (3, 4)}
    # {1, 2.0, (3, 4)}

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
===============
.. code-block:: python

    my_set: set = set()

.. code-block:: python

    from typing import Set

    my_set: Set[int] = {1, 2, 3}
    my_set: Set[float] = {0.0, 1.1, 2.2}
    my_set: Set[str] = {'a', 'b', 'c'}


Adding Items
============

Adding Single Item
------------------
.. code-block:: python

    my_set = {1, 2}

    my_set.add(3)
    # {1, 2, 3}

    my_set.add(3)
    # {1, 2, 3}

    my_set.add(4)
    # {1, 2, 3, 4}

Adding Many Items
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


Popping Items
=============
* Gets and remove items

.. code-block:: python

    my_set = {1, 2, 3}

    value = my_set.pop()

    my_set  # {1, 2}
    value   # 3


Deduplicate Items
=================
.. code-block:: python
    :caption: Converting ``list`` to ``set`` deduplicate items

    names = [
        'Twardowski',
        'Twardowski',
        'Jiménez',
        'Twardowski'
    ]

    unique_names = set(names)
    # {'Twardowski', 'Jiménez'}

.. code-block:: python
    :caption: Converting ``tuple`` to ``set`` deduplicate items

    names = (
        'Twardowski',
        'Twardowski',
        'Jiménez',
        'Twardowski'
    )

    unique_names = set(names)
    # {'Twardowski', 'Jiménez'}


Membership Operators
====================
.. code-block:: python
    :caption: Equals

    {1, 2} == {1, 2}        # True
    {1, 2} == {2, 1}        # True

.. code-block:: python
    :caption: Not equals

    {1, 2} != {1, 2}        # False
    {1, 2, 3} != {1, 2}     # True

.. code-block:: python
    :caption: Contains

    1 in {1, 2}             # True
    3 in {1, 2}             # False

    {2} in {1, 2}           # False
    {1, 2} in {1, 2}        # False

.. code-block:: python
    :caption: Missing

    4 not in {1, 2}         # True
    1 not in {1, 2}         # False

    {2} not in {1, 2}       # True
    {1, 2} not in {1, 2}    # True


Membership
==========

Disjoint
--------
.. highlights::
    * ``set.isdisjoint()``
    * No common elements

.. code-block:: python

    {1,2}.isdisjoint({3,4})     # True

Subset
------
.. highlights::
    * ``set.issubset()``
    * All elements in both

.. code-block:: python

    {1,2} <= {3,4}              # False
    {1,2} < {3,4}               # False

.. code-block:: python

    {1,2} <= {1,2}              # True
    {1,2} <= {1,2,3}            # True
    {1,2,3} <= {1,2}            # False

.. code-block:: python

    {1,2} < {1,2}               # False
    {1,2} < {1,2,3}             # True
    {1,2,3} < {1,2}             # False

Superset
--------
.. highlights::
    * ``set.issuperset()``
    * All elements of ``b`` are in ``a``

.. code-block:: python

    {1,2} > {1,2}               # False
    {1,2} > {1,2,3}             # False
    {1,2,3} > {1,2}             # True

.. code-block:: python

    {1,2} >= {1,2}              # True
    {1,2} >= {1,2,3}            # False
    {1,2,3} >= {1,2}            # True


Basic Operations
================

Union
-----
.. highlights::
    * ``set.union()``
    * add

.. code-block:: python

    {1,2} | {1,2}               # {1, 2}
    {1,2,3} | {1,2}             # {1, 2, 3}
    {1,2,3} | {1,2,4}           # {1, 2, 3, 4}
    {1,2} | {1,3} | {2,4}       # {1, 2, 3, 4}

Difference
----------
.. highlights::
    * ``set.difference()``
    * subtract

.. code-block:: python

    {1,2} - {2,3}               # {1}
    {1,2} - {2,3} - {3}         # {1}
    {1,2} - {1,2,3}             # set()

Symmetric Difference
--------------------
.. highlights::
    * ``set.symmetric_difference()``
    * not common elements from each

.. code-block:: python

    {1,2} ^ {1,2}               # set()
    {1,2} ^ {2,3}               # {1, 3}
    {1,2} ^ {1,3}               # {2, 3}

Intersection
------------
.. highlights::
    * ``set.intersection()``
    * common element from each

.. code-block:: python

    {1,2} & {2,3}               # {2}
    {1,2} & {2,3} & {2,4}       # {2}
    {1,2} & {2,3} & {3}         # set()


Cardinality
===========
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
    #. Dla danych wejściowych (patrz sekcja input)
    #. Stwórz ``my_set: set`` reprezentujący pierwszy wiersz
    #. Wartości z drugiego wiersza dodawaj do ``my_set`` za pomocą ``.add()``
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
