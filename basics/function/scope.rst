************************
Function Variables Scope
************************


Access Scope
============
.. code-block:: python
    :caption: Functions has access to global values

    DATA = [1, 2, 3]

    def add():
        return sum(DATA)

    print(add())
    # 6

.. code-block:: python
    :caption: Shadowing

    DATA = [1, 2, 3]

    def add():
        DATA = [10, 20, 30]
        return sum(DATA)

    print(add())
    # 60

    print(DATA)
    # [1, 2, 3]

.. code-block:: python
    :caption: Modify global, BAD PRACTICE!!

    DATA = [1, 2, 3]

    def add():
        global DATA
        DATA = [10, 20, 30]
        return sum(DATA)


    print(add())
    # 60

    print(DATA)
    # [10, 20, 30]


Global Scope
============
.. highlights::
    * All variables in main program
    * Variables are available inside all functions

.. code-block:: python

    print(globals())
    # {...}


Local Scope
===========
.. highlights::
    * Variables defined inside function
    * Variables are not available from outside
    * If outside the function, will return the same as ``globals()``

.. code-block:: python

    print(locals())
    # {...}

.. code-block:: python

    def add(a, b, c=3):
        d = 4
        print(locals())

    add(1, 2)
    # {'a':1, 'b':2, 'c':3, 'd':4}


Assignments
===========

Wanted
------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/scope_wanted.py`

:English:
    #. For given input data (see below)
    #. Define ``wanted: Set[str]`` with 'setosa' and 'versicolor'
    #. Iterate over data and split row into ``features`` and ``label`` (last)
    #. Define function which sums ``features``, only when ``label`` is in ``wanted``
    #. When ``label`` is not in ``wanted`` return ``0`` (zero)
    #. Print sum

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zdefiniuj ``wanted: Set[str]`` z 'setosa' oraz 'versicolor'
    #. Iterując po danych rozdziel wiersz na ``features`` i ``label`` (ostatni)
    #. Zdefiniuj funkcję sumującą ``features``, tylko gdy ``label`` jest w ``wanted``
    #. Gdy ``label`` nie występuje w ``wanted`` zwróć ``0`` (zero)
    #. Wypisz sumę

:Input:
    .. code-block:: python

        INPUT = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        OUTPUT: float
        # 74.9

Roman numbers
-------------
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/scope_roman.py`

:English:
    #. Define function converting roman numerals to integer
    #. Define function converting integer to roman numerals

:Polish:
    #. Zdefiniuj funkcję przeliczającą liczbę rzymską na całkowitą
    #. Zdefiniuj funkcję przeliczającą liczbę całkowitą na rzymską

:Input:
    .. code-block:: python

        CONVERSION_TABLE = {
            'I': 1,
            'II': 2,
            'III': 3,
            'IV': 4,
            'V': 5,
            'VI': 6,
            'VII': 7,
            'VIII': 8,
            'IX': 9,
            'X': 10,
            'XX': 20,
            'XXX': 30,
            'XL': 40,
            'L': 50,
            'LX': 60,
            'LXX': 70,
            'LXXX': 80,
            'XC': 90,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

:The whys and wherefores:
    * Defining and calling functions
    * Checking for corner cases
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups
