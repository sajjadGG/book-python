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


Proxy methods
=============
.. code-block:: python
    :caption: One of the most common use of ``*args``, ``**kwargs`` is for proxy methods.

    class Point2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Point3D(Point2D):
        def __init__(self, *args, **kwargs):
            if 'z' in kwargs:
                z = kwargs.pop('z')
            else:
                *args, z = args

            super().__init__(*args, **kwargs)
            self.z = z

        def __str__(self):
            return f'Point3D(x={self.x}, y={self.y}, z={self.z})'


    p1 = Point3D(x=1, y=2, z=3)
    p2 = Point3D(1, 2, 3)
    p3 = Point3D(1, 2, z=3)

    print(p1)
    # Point3D(x=1, y=2, z=3)

    print(p2)
    # Point3D(x=1, y=2, z=3)

    print(p3)
    # Point3D(x=1, y=2, z=3)


Placeholder class
=================
.. code-block:: python
    :caption: Dynamically creating fields

    class MyClass:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)


    a = MyClass(first_name='Jan', last_name='Twardowski')
    a.first_name          # Jan
    a.last_name           # 'Twardowski'

    b = MyClass(species='Setosa')
    b.species            # 'Setosa'

.. code-block:: python
    :caption: Dynamically creating fields

    class Astronaut:
        def __init__(self, last_name, **kwargs):
            self.last_name = last_name

            for key, value in kwargs.items():
                setattr(self, key, value)


    jan = Astronaut(last_name='Twardowski', addresses=())
    ivan = Astronaut(first_name='Иван', last_name='Иванович', agency='Roscosmos')

    print(jan.last_name)   # Twardowski
    print(ivan.first_name)  # Иван

    print(jan.__dict__)    # {'last_name': 'Twardowski', 'addresses': ()}
    print(ivan.__dict__)    # {'last_name': 'Иванович', 'first_name': 'Иван', 'agency': 'Roscosmos'}

.. code-block:: python

    class MyClass:
        def __init__(self, **kwargs):
            self.__dict__ = kwargs


    a = MyClass(first_name='Jan', last_name='Twardowski')
    print(a.first_name)          # Jan
    print(a.last_name)           # 'Twardowski'

    b = MyClass(species='Setosa')
    print(b.species)             # 'Setosa'
    print(b.first_name)          # AttributeError: 'MyClass' object has no attribute 'first_name'
    print(b.last_name)           # AttributeError: 'MyClass' object has no attribute 'last_name'
