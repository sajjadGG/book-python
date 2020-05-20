.. _Function Return:

***************
Function Return
***************


Syntax
======
.. code-block:: python

    def my_function():
        return <expression>

.. code-block:: python

    def add_numbers(a, b):
        return a + b

.. code-block:: python

    def mean(a, b):
        c = (a+b) / 2
        return c


Return Keyword
==============
.. highlights::
    * ``return`` keyword indicates outcome of the function
    * Code after ``return`` will not execute

.. code-block:: python

    def hello():
        return 'ehlo world'

    print(hello())
    # 'ehlo world'

.. code-block:: python

    def hello():
        return 'ehlo world'
        print('This will not be executed')

    print(hello())
    # 'ehlo world'


Return Basic Type
=================
.. code-block:: python

    def my_function():
        return 42

.. code-block:: python

    def my_function():
        return 13.37

.. code-block:: python

    def my_function():
        return 'Mark Watney'

.. code-block:: python

    def my_function():
        return True


Return Sequence
===============
.. code-block:: python

    def my_function():
        return list(42, 13.37, 'Mark Watney')

    def my_function():
        return [42, 13.37, 'Mark Watney']

.. code-block:: python

    def my_function():
        return tuple(42, 13.37, 'Mark Watney')

    def my_function():
        return (42, 13.37, 'Mark Watney')

    def my_function():
        return 42, 13.37, 'Mark Watney'

.. code-block:: python

    def my_function():
        return set({42, 13.37, 'Mark Watney'})

    def my_function():
        return {42, 13.37, 'Mark Watney'}

.. code-block:: python

    def my_function():
        return frozenset({42, 13.37, 'Mark Watney'})

Return Mapping
==============
.. code-block:: python

    def my_function():
        return dict(first_name='Mark', last_name='Watney')

    def my_function():
        return {'first_name': 'Mark', 'last_name': 'Watney'}


Return Nested Sequence
======================
.. code-block:: python

    def my_function():
        return [
            ('Mark', 'Watney'),
            {'Jan Twardowski', 'Melissa Lewis'},
            {'astro': 'Иванович', 'agency': {'name': 'Roscosmos'}},
            {'astro': 'Jiménez', 'missions': ('Mercury', 'Gemini', 'Apollo')},
            {'astro': 'Vogel', 'missions': (set(), tuple(), list())},
        ]


Return None
===========
.. highlights::
    * Python will ``return None`` if no explicit return is specified

.. code-block:: python

    def my_function():
        return None

.. code-block:: python

    def my_function():
        print('ehlo world')

.. code-block:: python

    def my_function():
        pass

.. code-block:: python

    def my_function():
        """My function"""


Assignments
===========

Return Numbers
--------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_return_numbers.py`

:English:
    #. Define function ``add`` without parameters
    #. Function should return sum of ``42`` and ``13.37``
    #. Call function and intercept returned value
    #. Print value

:Polish:
    #. Zdefiniuj funkcję ``add`` bez parametrów
    #. Funkcja powinna zwracać sumę ``42`` and ``13.37``
    #. Wywołaj funkcję i przechwyć zwracaną wartość
    #. Wyświetl wartość
