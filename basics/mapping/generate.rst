****************
Mapping Generate
****************


List of pairs
=============
.. code-block:: python

    pairs = [
        ('a', 1)
    ]

    dict(pairs)
    # {'a': 1}

.. code-block:: python

    pairs = [
        ('a', 1),
        ('b', 2)
    ]

    dict(pairs)
    # {'a': 1, 'b': 2}

.. code-block:: python

    pairs = [
        ('first_name', 'Jan'),
        ('last_name', 'Twardowski'),
    ]

    dict(pairs)
    # {
    #   'first_name': 'Jan',
    #   'last_name': 'Twardowski'
    # }

.. code-block:: python

    pairs = [
         {'a', 1},
         {'b', 2},
    ]

    pairs
    # [{1, 'a'}, {'b', 2}]

    dict(pairs)
    # {1: 'a', 'b': 2}

.. code-block:: python

    pairs = [
        ('Sepal length', 5.8),
        ('Sepal width', 2.7),
        ('Petal length', 5.1),
        ('Petal width', 1.9),
        ('Species', 'virginica')
    ]

    dict(pairs)
    # {
    #     'Sepal length': 5.8,
    #     'Sepal width': 2.7,
    #     'Petal length': 5.1,
    #     'Petal width': 1.9,
    #     'Species': 'virginica'
    # }


Zip
===
.. highlights::
    * ``zip`` is a generator
    * ``zip`` will create a list of pairs (like ``dict.items()``)

.. code-block:: python

    keys =  ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species']
    values = [5.8, 2.7, 5.1, 1.9, 'virginica']

    dict(zip(keys, values))
    # {
    #   'Sepal length': 5.8,
    #   'Sepal width': 2.7,
    #   'Petal length': 5.1,
    #   'Petal width': 1.9,
    #   'Species': 'virginica'
    # }


Enumerate
=========
.. code-block:: python

    labels = ['setosa', 'versicolor', 'virginica']

    dict(enumerate(labels))
    # {
    #   0: 'setosa',
    #   1: 'versicolor',
    #   2: 'virginica'
    # }


Assignments
===========
.. todo:: Create assignments
