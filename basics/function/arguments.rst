******************
Function Arguments
******************


Arguments vs Parameters
=======================
* argument is the value/variable/reference being passed to the function
* parameter is the receiving variable used within the function/block


Syntax
======
.. code-block:: python
    :caption: Function definition with parameters

    my_function(<arguments>)

.. code-block:: python

    say_hello(name)

    add(a, b)


Positional Arguments
====================
.. highlights::
    * Order of positional arguments has significance

.. code-block:: python

    def add(a, b):
        return a - b


    subtract(2, 1)          # 1
    subtract(1, 2)          # -1


Keyword Arguments
=================
.. highlights::
    * Order of keyword arguments has no significance

.. code-block:: python

    def subtract(a, b):
        return a - b


    subtract(a=2, b=1)      # 1
    subtract(b=1, a=2)      # 1


Positional and Keyword Arguments
================================
.. highlight::
    * Positional arguments must be at the left side
    * Keyword arguments must be at the right side

.. code-block:: python

    def subtract(a, b):
        return a - b


    subtract(2, b=1)        # 1
    subtract(a=2, 1)        # SyntaxError: positional argument follows keyword argument
    subtract(2, a=1)        # TypeError: subtract() got multiple values for argument 'a'


Examples
========

Example 1
---------
.. code-block:: python

    def hello(name='José Jiménez'):
         print(f'My name... {name}')


    hello('Mark Watney')          # My name... Mark Watney
    hello(name='Mark Watney')     # My name... Mark Watney
    hello()                       # My name... José Jiménez

Example 2
---------
.. code-block:: python

    connect('admin', 'admin')

.. code-block:: python

    connect('admin', 'admin', 'localhost', 22, False, 1, True)

.. code-block:: python

    connect(host='localhost', username='admin', password='admin')

.. code-block:: python

    connect(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        ssl=True,
        persistent=True,
    )

Example 3
---------
.. code-block:: python

    read_csv('iris.csv')

.. code-block:: python

    read_csv('iris.csv', encoding='utf-8')

.. code-block:: python

    read_csv('iris.csv', encoding='utf-8', parse_dates=['date_of_birth'])

.. code-block:: python

    read_csv('iris.csv', skiprows=3, delimiter=';')

.. code-block:: python

    read_csv('iris.csv',
        encoding='utf-8',
        skiprows=3,
        delimiter=';',
        usecols=['Sepal Length', 'Species'],
        parse_dates=['date_of_birth']
    )


Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_args_example.py`

:English:
    #. Define function which takes sequence of integers as an argument
    #. Sum only even numbers
    #. Print returned value

:Polish:
    #. Zdefiniuj funkcję biorącą sekwencję liczb całkowitych jako argument
    #. Zsumuj tylko parzyste liczby
    #. Wypisz zwróconą wartość

:Solution:
    .. literalinclude:: solution/function_args_example.py
        :language: python

Divide
------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_args_divide.py`

:English:
    #. Define function ``divide``
    #. Function takes two arguments
    #. Function divides its arguments and returns the result
    #. Call function with ``divide(10, 3)``
    #. Call function with ``divide(10, 0)``
    #. Print returned values
    #. What to do in case of error?

:Polish:
    #. Zdefiniuj funkcję ``divide``
    #. Funkcja przyjmuje dwa argumenty
    #. Funkcja dzieli oba argumenty przez siebie i zwraca wynik dzielenia
    #. Wywołaj funkcję z ``divide(4, 2)``
    #. Wywołaj funkcję z ``divide(4, 0)``
    #. Wypisz zwracane wartości
    #. Co zrobić w przypadku błędu?

Power
-----
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_args_power.py`

:English:
    #. Define function ``power``
    #. Function takes two arguments
    #. Second argument is optional
    #. Function returns power of the first argument to the second
    #. If only one argument was passed, consider second equal to the first one
    #. Print returned values
    #. Compare result with "Output" section (see below)

:Polish:
    #. Zdefiniuj funkcję ``power``
    #. Funkcja przyjmuje dwa argumenty
    #. Drugi argument jest opcjonalny
    #. Funkcja zwraca wynik pierwszego argumentu do potęgi drugiego
    #. Jeżeli tylko jeden argument był podany, przyjmij drugi równy pierwszemu
    #. Wypisz zwracane wartości
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Output:
    .. code-block:: python

        power(4, 3)
        # 64

        power(3)
        # 27
