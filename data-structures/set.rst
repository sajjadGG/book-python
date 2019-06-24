*******
``set``
*******

* Only unique values
* Can store elements of any **hashable** types
* Mutable - can add, remove, and modify items


Defining ``set``
================
* Do not record element position
* Do not record order of insertion
* Do not support indexing
* Dot support slicing

Empty ``set``
-------------
* Defining only with ``set()``

.. code-block:: python

    my_set = set()

``set`` with one element
------------------------
* Comma after last element is optional
* Brackets are required

.. code-block:: python

    my_set = {1}
    my_set = {1,}

``set`` with multiple values
----------------------------
* Brackets are required

.. code-block:: python

    my_set = {1, 3, 1}          # {1, 3}

``set`` with multiple values in many types
------------------------------------------
* Brackets are required

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


Converting ``list`` to ``set`` deduplicate items
================================================
.. code-block:: python

    names = [
        'Twardowski',
        'Иванович',
        'Jiménez',
        'Twardowski'
    ]

    unique_names = set(names)
    # {'Twardowski', 'Иванович', 'Jiménez'}


Length of a ``set``
===================
.. code-block:: python

    my_set = {1, 2, 3}

    len(my_set)                 # 3

