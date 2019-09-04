**************
Dynamic Typing
**************


Duck typing
===========
* `The Unreasonable Effectiveness of Dynamic Typing for Practical Programs by Robert Smallshire <http://www.infoq.com/presentations/dynamic-static-typing>`_

.. code-block:: python
    :caption: Duck typing

    {}  # dict
    {1}  # set
    {1, 2}  # set
    {1: 2}  # dict
    {1: 1, 2: 2}  # dict

    my_data = {}
    isinstance(my_data, (set, dict))  # True

    isinstance(my_data, dict)  # True
    isinstance(my_data, set)  # False

    my_data = {1}
    isinstance(my_data, set)  # True
    isinstance(my_data, dict)  # False

    my_data = {1: 1}
    isinstance(my_data, set)  # False
    isinstance(my_data, dict)  # True


Everything is an object
=======================
* even function is an object!

Object properties
-----------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b

    add_numbers.__doc__             # 'Function add numbers'
    add_numbers.__name__            # 'add_numbers'
    add_numbers.__annotations__     # {}
    add_numbers.__class__           # <class 'function'>

Object methods
--------------
.. code-block:: python

    def add_numbers(a, b):
        """Function add numbers"""
        return a + b

    add_numbers.__call__()          # TypeError: function() missing 2 required positional arguments: 'a' and 'b'
    add_numbers.__call__(1, 2)      # 3

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


    add_numbers.say_hello = lambda name: print(f'Hello {name}')

    add_numbers.say_hello('Jan Twardowski')
    # Hello Jan Twardowski


Monkey Patching
===============

Recap information about classes and objects
-------------------------------------------
.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jose Jimenez'

        def hello(self):
            print(f'My name... {self.name}')

    u = User()
    u.hello()
    # My name... Jose Jimenez

.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jose Jimenez'

        def hello(self):
            print(f'My name... {self.name}')

    User.hello()
    # TypeError: hello() missing 1 required positional argument: 'self'

Injecting fields
----------------
.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jose Jimenez'

        def hello(self):
            print(f'My name... {self.name}')


    User.agency = 'NASA'    # Injecting static field

    print(User.agency)
    # NASA


Injecting methods
-----------------
.. code-block:: python

    class User:
        def hello(self):
            print('Hello from User')


    def my_function():
        print('New Version')


    User.hello = my_function
    User.hello()
    # 'New Version'

.. code-block:: python

    class User:
        pass


    User.hello = lambda name: print(f'Hello {name}')

    User.hello('Jan Twardowski')
    # Hello Jan Twardowski

.. code-block:: python

    class User:
        pass

    u = User()
    u.hello = lambda name: print(f'Hello {name}')

    u.hello('Jan Twardowski')
    # Hello Jan Twardowski

.. code-block:: python

    class User:
        def __init__(self):
            self.name = 'Jan Twardowski'
        pass

    u = User()
    u.hello = lambda self: print(f'Hello {self.name}')

    u.hello()
    # TypeError: <lambda>() missing 1 required positional argument: 'self'

.. code-block:: python

    class User:
        pass

    User.hello = lambda self: print(f'Hello {self.name}')

    u = User()
    u.name = 'Jan Twardowski'

    u.hello()
    # Hello Jan Twardowski

Use case
--------
.. code-block:: python

    import datetime
    import json


    def datetime_encoder(self, obj):
        if isinstance(obj, datetime.date):
            return f'{obj:%Y-%m-%d}'
        else:
            return str(obj)

    json.JSONEncoder.default = datetime_encoder

    output = {"datetime": datetime.date(1961, 4, 12)}
    json.dumps(output)
    # {"datetime": "1961-04-12"}
