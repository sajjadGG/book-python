Function Arguments
==================


.. testsetup::

    def add(*args, **kwargs):
        pass

    def connect(*args, **kwargs):
        pass

    def read_csv(*args, **kwargs):
        pass


Rationale
---------
.. glossary::

    argument
        Value/variable/reference being passed to the function

    positional argument
        Value passed to function - order is important

    keyword argument
        Value passed to function resolved by name - order is not important


Syntax
------
Function definition with parameters:

.. code-block:: python

    myfunction(<arguments>)

>>> add(1, 2)
>>> add(a=1, b=2)
>>> add(1, b=2)


Positional Arguments
--------------------
* Order of positional arguments has significance

    >>> def subtract(a, b):
    ...     return a - b
    >>>
    >>>
    >>> subtract(2, 1)
    1
    >>> subtract(1, 2)
    -1


Keyword Arguments
-----------------
* Order of keyword arguments has no significance

    >>> def subtract(a, b):
    ...     return a - b
    >>>
    >>>
    >>> subtract(a=2, b=1)
    1
    >>> subtract(b=1, a=2)
    1


Positional and Keyword Arguments
--------------------------------
* Positional arguments must be at the left side
* Keyword arguments must be at the right side

    >>> def subtract(a, b):
    ...     return a - b
    >>>
    >>>
    >>> subtract(2, b=1)
    1
    >>> subtract(a=2, 1)
    Traceback (most recent call last):
    SyntaxError: positional argument follows keyword argument
    >>> subtract(2, a=1)
    Traceback (most recent call last):
    TypeError: subtract() got multiple values for argument 'a'


Examples
--------
Example 1:

    >>> def hello(name='José Jiménez'):
    ...      print(f'My name... {name}')
    >>>
    >>>
    >>> hello('Mark Watney')
    My name... Mark Watney
    >>> hello(name='Mark Watney')
    My name... Mark Watney
    >>> hello()
    My name... José Jiménez

Example 2:

    >>> connect('myusername', 'mypassword')

    >>> connect('myusername', 'mypassword', 'example.com', 443, False, 1, True)

    >>> connect(host='example.com', username='myusername', password='mypassword')

    >>> connect(
    ...     host='example.com',
    ...     username='myusername',
    ...     password='mypassword',
    ...     port=443,
    ...     ssl=True,
    ...     persistent=True)

Example 3:

    >>> read_csv('iris.csv')

    >>> read_csv('iris.csv', encoding='utf-8')

    >>> read_csv('iris.csv', encoding='utf-8', parse_dates=['date_of_birth'])

    >>> read_csv('iris.csv', skiprows=3, delimiter=';')

    >>> read_csv('iris.csv',
    ...     encoding='utf-8',
    ...     skiprows=3,
    ...     delimiter=';',
    ...     usecols=['Sepal Length', 'Species'],
    ...     parse_dates=['date_of_birth'])


Assignments
-----------
.. literalinclude:: assignments/function_args_a.py
    :caption: :download:`Solution <assignments/function_args_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_b.py
    :caption: :download:`Solution <assignments/function_args_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_c.py
    :caption: :download:`Solution <assignments/function_args_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_d.py
    :caption: :download:`Solution <assignments/function_args_d.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_e.py
    :caption: :download:`Solution <assignments/function_args_e.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_f.py
    :caption: :download:`Solution <assignments/function_args_f.py>`
    :end-before: # Solution

.. literalinclude:: assignments/function_args_g.py
    :caption: :download:`Solution <assignments/function_args_g.py>`
    :end-before: # Solution
