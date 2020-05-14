******
Lambda
******


Rationale
=========
.. highlights::
    * Lambda - Anonymous functions
    * When function is used once
    * When function is short


Syntax
======
.. code-block:: python

    lambda <arguments>: <expression>


Definition
==========
.. code-block:: python

    lambda x: x**2

.. code-block:: python

    lambda x: x%2==0

.. code-block:: python

    lambda x,y: x+y


Naming Convention
=================
* Usually parameters are named ``x`` and ``y``
* Use shortest code possible
* Do not assign ``lambda`` to variable
* Usually there are no spaces in lambda expressions (to make code shorter)

.. code-block:: python

    lambda x,y: x+y

.. code-block:: python
    :caption: Lambda is anonymous function and it should stay anonymous. Do not name it.

    squre = lambda x: x**2
    squre(4)
    # 16


Examples
========

Example 1
---------
.. code-block:: python

    def increment(x):
        return x + 1


    data = [1, 2, 3, 4]
    result = map(increment, data)

    print(list(result))
    # [2, 4]

.. code-block:: python

    data = [1, 2, 3, 4]
    result = map(lambda x: x+1, data)

    print(list(result))
    # [2, 3, 4, 5]

Example 2
---------
.. code-block:: python

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False


    data = [1, 2, 3, 4]
    result = filter(is_even, data)

    print(list(result))
    # [2, 4]

.. code-block:: python

    def is_even(x):
        return x % 2 == 0


    data = [1, 2, 3, 4]
    result = filter(is_even, data)

    print(list(result))
    # [2, 4]

.. code-block:: python

    data = [1, 2, 3, 4]
    result = filter(lambda x: x%2==0, data)

    print(list(result))
    # [2, 4]

Example 3
---------
.. code-block:: python
    :caption: ``filter()`` example

    def adult(person):
        if person['age'] >= 21:
            return True
        else:
            return False


    people = [
        {'age': 21, 'name': 'Jan Twardowski'},
        {'age': 25, 'name': 'Mark Watney'},
        {'age': 18, 'name': 'Melissa Lewis'}]

    result = filter(lambda x: x['age'] >= 21, people)

    print(list(result))
    # [{'age': 21, 'name': 'Jan Twardowski'},
    #  {'age': 25, 'name': 'Mark Watney'}]

.. code-block:: python
    :caption: ``filter()`` example

    def astronaut(person):
        return person['is_astronaut']

    people = [
        {'is_astronaut': False, 'name': 'Jan Twardowski'},
        {'is_astronaut': True, 'name': 'Mark Watney'},
        {'is_astronaut': True, 'name': 'Melissa Lewis'}]

    result = filter(lambda x: x['is_astronaut'], people)

    print(list(result))
    # [{'is_astronaut': True, 'name': 'Mark Watney'},
    #  {'is_astronaut': True, 'name': 'Melissa Lewis'}]


Assignments
===========

Function Lambda Chain
---------------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 10 min
* Solution: :download:`solution/function_lambda_chain.py`

:English:
    #. Use generator expression to create ``numbers: List[int]``
    #. In generator use ``range()`` to get numbers from 1 to 33 (inclusive) divisible by 3
    #. Use ``filter()`` to get odd numbers from ``numbers``
    #. Use ``map()`` to cube all numbers in ``numbers``
    #. Use only ``lambda`` function in ``map()`` and ``filter()``
    #. Create ``result: float`` with arithmetic mean of ``numbers``
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj wyrażenia generatorowego do stworzenia ``numbers: List[int]``
    #. W generatorze użyj ``range()`` aby otrzymać liczby od 1 do 33 (włącznie) podzielne przez 3
    #. Użyj ``filter()`` aby otrzymać liczby nieparzyste z ``numbers``
    #. Użyj ``map()`` aby podnieść wszystkie liczby w ``numbers`` do sześcianu
    #. Użyj tylko funkcji ``lambda`` w ``map()`` i ``filter()``
    #. Stwórz ``result: float`` ze średnią arytmetyczną z ``numbers``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        result: float
        # 11502.0

:Hint:
    * ``mean = sum(...) / len(...)``
    * type cast to ``list()`` before calculating mean to expand generator
