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

    print(bool(lambda x: x % 2 == 0))

.. code-block:: python

    is_even = lambda x: x % 2 == 0
    is_even(4)

.. code-block:: python

    def is_even(x):
        return x % 2 == 0

    is_even(4)

Example 2
---------
.. code-block:: python

    DATA = [1, 2, 3, 4]


    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False


    result = filter(is_even, DATA)
    print(list(result))
    # [2, 4]

.. code-block:: python

    DATA = [1, 2, 3, 4]


    def is_even(x):
        return x % 2 == 0


    result = filter(is_even, DATA)
    print(list(result))
    # [2, 4]

.. code-block:: python

    DATA = [1, 2, 3, 4]

    result = filter(lambda x: x % 2 == 0, DATA)
    print(list(result))
    # [2, 4]

Example 3
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

    result = []

    for user in DATA:
        if is_system_user(user):
            result.append(user)

    print(result)
    # [{'user': 'root', 'uid': 0}]


.. code-block:: python

    DATA = [
        {'user': 'twardowski', 'uid': 1000},
        {'user': 'root', 'uid': 0},
    ]


    result = filter(lambda x: x['uid'] < 1000, DATA)

    print(list(result))
    # [{'user': 'root', 'uid': 0}]

Assignments
===========

Built-in Generators
-------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/function_lambda_task.py`

:English:
    #. Using generator expression to create ``result: List[int]`` with numbers from 1 to 33 which are divisible by 3
    #. Filter ``result`` to contain only odd numbers
    #. Cube all numbers in ``result``
    #. Calculate arithmetic mean from ``result``
    #. Użyj funkcji ``lambda``

:Polish:
    #. Używając wyrażenia generatorowego stwórz ``result: List[int]`` z liczbami z zakresu 1 do 33 podzielnymi przez 3
    #. Przefiltruj ``result`` aby zawierał tylko liczby nieparzyste
    #. Podnieś wszystkie liczby w ``result`` do sześcianu
    #. Oblicz średnią arytmetyczną z ``result``
    #. Użyj funkcji ``lambda``

:Hint:
    * ``mean = sum(...) / len(...)``
    * type cast to ``list()`` before calculating mean to expand generator
