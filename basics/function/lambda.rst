Function Lambda
===============


Rationale
---------
* Lambda - Anonymous functions
* When function is used once
* When function is short
* You don't need to name it (hence it is anonymous)

.. glossary::

    lambda
        Anonymous function


Syntax
------
.. code-block:: python

    lambda <arguments>: <expression>

Lambda Expressions:

>>> f = lambda x: x+1
>>> f = lambda x,y: x+y

Equivalent functions:

>>> def f(x):
...     return x+1

>>> def f(x,y):
...     return x+y


Convention
----------
* Usually parameters are named ``x`` and ``y``
* Use shortest code possible
* Do not assign ``lambda`` to variable
* Lambda is anonymous function and it should stay anonymous. Do not name it
* :pep:`8` -- Style Guide for Python Code: "Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier". Lambda is anonymous function and it should stay anonymous. Do not name it.
* Usually there are no spaces in lambda expressions (to make code shorter)

Bad:

    >>> square = lambda x: x**2
    >>> square(4)
    16

Good:

    >>> def square(x):
    ...    return x**2
    ...
    >>> square(4)
    16

:pep:`8` -- Style Guide for Python Code: "Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier":


Lambda with Map
---------------
Increment:

    >>> data = [1, 2, 3, 4]
    >>>
    >>> result = map(lambda x: x+1, data)
    >>> list(result)
    [2, 3, 4, 5]

Square:

    >>> data = [1, 2, 3, 4]
    >>>
    >>> result = map(lambda x: x**2, data)
    >>> list(result)
    [1, 4, 9, 16]

Translate:

    >>> PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
    ...      'ł': 'l', 'ń': 'n', 'ó': 'o',
    ...      'ś': 's', 'ż': 'z', 'ź': 'z'}
    >>>
    >>> text = 'zażółć gęślą jaźń'
    >>>
    >>> result = map(lambda x: PL.get(x,x), text)
    >>> ''.join(result)
    'zazolc gesla jazn'

Lambda with Filter
------------------
Even numbers:

    >>> DATA = [1, 2, 3, 4]
    >>>
    >>> result = filter(lambda x: x%2==0, DATA)
    >>> list(result)
    [2, 4]

Adult people:

    >>> people = [
    ...     {'age': 21, 'name': 'Jan Twardowski'},
    ...     {'age': 25, 'name': 'Mark Watney'},
    ...     {'age': 18, 'name': 'Melissa Lewis'}]
    >>>
    >>> result = filter(lambda x: x['age'] >= 21, people)
    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    [{'age': 21, 'name': 'Jan Twardowski'},
     {'age': 25, 'name': 'Mark Watney'}]

Astronauts:

    >>> people = [
    ...     {'is_astronaut': False, 'name': 'Jan Twardowski'},
    ...     {'is_astronaut': True, 'name': 'Mark Watney'},
    ...     {'is_astronaut': True, 'name': 'Melissa Lewis'}]
    >>>
    >>> result = filter(lambda x: x['is_astronaut'], people)
    >>> list(result)  # doctest: +NORMALIZE_WHITESPACE
    [{'is_astronaut': True, 'name': 'Mark Watney'},
     {'is_astronaut': True, 'name': 'Melissa Lewis'}]

    >>> astronauts = ['Mark Watney', 'Melissa Lewis']
    >>>
    >>> people = ['Jan Twardowski', 'Mark Watney',
    ...           'Melissa Lewis', 'Jose Jimenez']
    >>>
    >>> result = filter(lambda x: x in astronauts, people)
    >>> list(result)
    ['Mark Watney', 'Melissa Lewis']


Assignments
-----------
.. literalinclude:: assignments/function_lambda_chain.py
    :caption: :download:`Solution <assignments/function_lambda_chain.py>`
    :end-before: # Solution
