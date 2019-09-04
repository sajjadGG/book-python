*****************
Placeholder class
*****************


Proxy methods
=============
.. code-block:: python
    :caption: One of the most common use of ``*args``, ``**kwargs`` is for proxy methods.

    class Point2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Point3D(Point2D):
        def __init__(self, z, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.z = z


Flat Problem
============
.. code-block:: python

    DATA = {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"},

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

    iris = Iris(**DATA)
    iris.species
    # 'versicolor'


Nested Problem
==============
.. code-block:: python

    DATA = [
        {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"},
        {"sepal_length": 4.9, "sepal_width": 3.1, "petal_length": 1.5, "petal_width": 0.1, "species": "setosa"},
    ]

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

        def __repr__(self):
            return f'{self.species}'

    flowers = []

    for row in DATA:
        iris = Iris(**row)
        flowers.append(iris)

    print(flowers)
    # ['versicolor', 'setosa']


Placeholder class
=================
.. code-block:: python

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
