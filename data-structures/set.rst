*******
``set``
*******

* Only unique values
* Can store elements of any **hashable** types
* Mutable - can add, remove, and modify items
* Brackets are required
* Comma after last element is optional


Defining ``set``
================
* Defining only with ``set()``
* Is an unordered collection
* ``set`` do not record element position or order of insertion
* ``set`` do not support indexing, slicing, or other sequence-like behavior

Empty ``set``
-------------
.. code-block:: python

    my_set = set()

``set`` with one element
------------------------
.. code-block:: python

    my_set = {1}
    my_set = {1,}

``set`` with multiple values
----------------------------
.. code-block:: python

    my_set = {1, 3, 1}          # {1, 3}

``set`` with multiple values in many types
------------------------------------------
.. code-block:: python

    my_set = {1, 2.0, 'Jan'}    # {1, 2.0, 'Jan'}
    my_set = {1, 2.0, (3, 4)}   # {1, 2.0, (3, 4)}
    my_set = {1, 2.0, [3, 4]}   # TypeError: unhashable type: 'list'
    my_set = {1, 2.0, {3, 4}}   # TypeError: unhashable type: 'set'


Adding items
============

Adding one element
------------------
.. code-block:: python

    my_set = {1, 2, 3}          # {1, 2, 3}

    my_set.add(4)               # {1, 2, 3, 4}
    my_set.add(4)               # {1, 2, 3, 4}
    my_set.add(3)               # {1, 2, 3, 4}

Adding many items
-----------------
.. code-block:: python

    my_set = {1, 2, 3}          # {1, 2, 3}

    my_set.update([4, 5])       # {1, 2, 3, 4, 5}


Length of a ``set``
===================
.. code-block:: python

    my_set = {1, 2, 3}

    len(my_set)                 # 3


Converting ``list`` to ``set`` deduplicate items
================================================
.. code-block:: python

    names = ['Twardowski', 'Иван', 'Jiménez', 'Twardowski']

    unique_names = set(names)
    # {'Twardowski', 'Иван', 'Jiménez'}
