**************
Dynamic Typing
**************


Duck typing
===========
* `The Unreasonable Effectiveness of Dynamic Typing for Practical Programs by Robert Smallshire <http://www.infoq.com/presentations/dynamic-static-typing>`_

.. code-block:: python
    :caption: Syntax similarities and Dynamic Typing

    {}              # dict
    {1}             # set
    {1, 2}          # set
    {1: 2}          # dict
    {1: 1, 2: 2}    # dict


    my_data = {1}
    isinstance(my_data, set)   # True
    isinstance(my_data, dict)  # False

    my_data = {1: 1}
    isinstance(my_data, set)   # False
    isinstance(my_data, dict)  # True

    my_data = {}
    isinstance(my_data, (set, dict))  # True

    isinstance(my_data, dict)  # True
    isinstance(my_data, set)   # False


Everything is an object
=======================
* even function is an object!

Object properties
-----------------
.. code-block:: python

    def add_numbers(a: int, b: float) -> float:
        """Function add numbers"""
        return a + b


    print(add_numbers.__doc__)
    # Function add numbers

    print(add_numbers.__name__)
    # add_numbers

    print(add_numbers.__annotations__)
    # {'a': <class 'int'>, 'b': <class 'float'>, 'return': <class 'float'>}

    print(add_numbers.__class__)
    # <class 'function'>

Object methods
--------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b

    add_numbers(1, 2)
    # 3

    add_numbers.__call__(1, 2)
    # 3

    add_numbers()
    # TypeError: function() missing 2 required positional arguments: 'a' and 'b'

    add_numbers.__call__()
    # TypeError: function() missing 2 required positional arguments: 'a' and 'b'

Injecting properties
--------------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b


    add_numbers.my_variable = 10

    print(add_numbers.my_variable)
    # 10

Injecting methods
-----------------
 .. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b


    add_numbers.say_hello = lambda name: print(f'My name... {name}')

    add_numbers.say_hello('Jose Jimenez')
    # My name... Jose Jimenez


