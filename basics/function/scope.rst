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
