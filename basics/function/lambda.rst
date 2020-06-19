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
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_lambda_chain.py`

:English:
    #. Use data from "Input" section (see below)
    #. Inline functions ``odd()`` and ``cube()`` with ``lambda`` expressions
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Wciel kod ``odd()`` i ``cube()`` wykorzystując wyrażenia ``lambda``
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        def odd(x):
            return x % 2 != 0

        def cube(x):
            return x ** 3


        numbers = (x for x in range(1, 34) if x % 3 == 0)
        numbers = filter(odd, numbers)
        numbers = map(cube, numbers)
        numbers = list(numbers)
        result = sum(numbers) / len(numbers)

        print(result)

:Output:
    .. code-block:: python

        result: float
        # 11502.0

:Hint:
    * ``mean = sum(...) / len(...)``
    * type cast to ``list()`` before calculating mean to expand generator
