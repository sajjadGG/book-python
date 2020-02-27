******
Lambda
******

* Lambda - Anonymous functions

Syntax
======
.. code-block:: python

    lambda <arguments>: <expression>

Definition
==========
.. code-block:: python

    lambda x: x**2

.. code-block:: python

    lambda x: x % 2 == 0

.. code-block:: python

    lambda x,y: x+y


Examples
========

Example 1
---------
.. code-block:: python

    DATA = [1, 2, 3, 4]


    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False


    output = filter(is_even, DATA)
    print(list(output))
    # [2, 4]

.. code-block:: python

    DATA = [1, 2, 3, 4]

    output = filter(lambda x: x % 2 == 0, DATA)
    print(list(output))
    # [2, 4]

Example 2
---------
.. code-block:: python

    DATA = [
        {'user': 'twardowski', 'uid': 1000},
        {'user': 'root', 'uid': 0},
    ]

    def is_system_user(data):
        if data['uid'] < 1000:
            return True
        else:
            return False

    system_users = []

    for user in DATA:
        if is_system_user(user):
            system_users.append(user)

    print(system_users)
    # [{'user': 'root', 'uid': 0}]


.. code-block:: python

    DATA = [
        {'user': 'twardowski', 'uid': 1000},
        {'user': 'root', 'uid': 0},
    ]


    system_users = filter(lambda x: x['uid'] < 1000, DATA)

    print(list(system_users))
    # [{'user': 'root', 'uid': 0}]

