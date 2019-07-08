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


Adding items
============

Adding one element
------------------
.. code-block:: python

    my_set = {1, 2, 3}

    my_set.add(4)
    # {1, 2, 3, 4}

    my_set.add(4)
    # {1, 2, 3, 4}

    my_set.add(3)
    # {1, 2, 3, 4}

Adding many items
-----------------
.. code-block:: python

    my_set = {1, 2, 3}

    my_set.update([4, 5])
    # {1, 2, 3, 4, 5}


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
* Filename: ``data-structures/set_create.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

.. csv-table:: Pomiary Iris
    :name: sequences-set-create
    :header: "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"

    "5.8", "2.7", "5.1", "1.9", "virginica"
    "5.1", "3.5", "1.4", "0.2", "setosa"
    "5.7", "2.8", "4.1", "1.3", "versicolor"
    "6.3", "2.9", "5.6", "1.8", "virginica"
    "6.4", "3.2", "4.5", "1.5", "versicolor"

#. Dane są pomiary :numref:`sequences-set-create`
#. Stwórz ``set`` na podstawie pierwszego wiersza
#. Wszystkie wartości z dwóch kolejnych wierszy dodawaj do wcześniejszego zbioru za pomocą ``.add()`` (skorzystaj z ``alt`` w Twoim IDE).
#. Ostatnie dwa wiersze dodaj za pomocą ``.update()``

    * czwarty wiersz podaj jako ``tuple``
    * piąty jako ``list``
