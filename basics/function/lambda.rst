.. _Function Lambda:

***************
Function Lambda
***************


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


Convention
==========
.. highlights::
    * Usually parameters are named ``x`` and ``y``
    * Use shortest code possible
    * Do not assign ``lambda`` to variable
    * Usually there are no spaces in lambda expressions (to make code shorter)

.. code-block:: python

    lambda x,y: x+y

.. code-block:: python
    :caption: Lambda is anonymous function and it should stay anonymous. Do not name it.

    square = lambda x: x**2
    square(4)
    # 16

Use Case
========
.. code-block:: python

    DATA = [1, 2, 3, 4]

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    list(filter(is_even, DATA))
    # [2, 4]

.. code-block:: python

    DATA = [1, 2, 3, 4]

    def is_even(x):
        return x % 2 == 0

    list(filter(is_even, DATA))
    # [2, 4]

.. code-block:: python

    DATA = [1, 2, 3, 4]

    list(filter(lambda x: x%2==0, DATA))
    # [2, 4]


Examples
========
.. code-block:: python
    :caption: Example 1

    data = [1, 2, 3, 4]

    def increment(x):
        return x + 1


    list(map(increment, data))
    # [2, 3, 4, 5]

    list(map(lambda x: x+1, data))
    # [2, 3, 4, 5]

.. code-block:: python
    :caption: Example 2

    people = [
        {'age': 21, 'name': 'Jan Twardowski'},
        {'age': 25, 'name': 'Mark Watney'},
        {'age': 18, 'name': 'Melissa Lewis'}]

    def adult(person):
        if person['age'] >= 21:
            return True
        else:
            return False


    list(filter(lambda x: x['age'] >= 21, people))
    # [{'age': 21, 'name': 'Jan Twardowski'},
    #  {'age': 25, 'name': 'Mark Watney'}]

.. code-block:: python
    :caption: ``filter()`` example

    people = [
        {'is_astronaut': False, 'name': 'Jan Twardowski'},
        {'is_astronaut': True, 'name': 'Mark Watney'},
        {'is_astronaut': True, 'name': 'Melissa Lewis'}]

    def astronaut(person):
        return person['is_astronaut']

    list(filter(lambda x: x['is_astronaut'], people))
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
