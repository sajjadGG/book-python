.. _Intermediate Comprehensions Nesting:


**********************
Comprehensions Nesting
**********************


Nested Comprehensions
=====================
.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis'},
    ]

    fieldnames = set(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {'born', 'last_name', 'first_name'}

.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis'},
    ]

    fieldnames = set()
    fieldnames.update(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {'born', 'last_name', 'first_name'}

.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis'},
    ]

    fieldnames = set()
    fieldnames.update(key for row in DATA for key in row.keys())

    print(fieldnames)
    # {'born', 'last_name', 'first_name'}


Generator comprehensions
========================
.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis'},
    ]

    fieldnames = set()

    fieldnames.add(key
        for row in DATA
            for key in row.keys()
    )

    print(fieldnames)
    # {<generator object <genexpr> at 0x1179a0a50>}


Assignments
===========
.. todo:: Create assignments
