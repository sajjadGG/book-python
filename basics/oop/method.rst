.. _OOP Methods:

*******
Methods
*******


About
=====
.. highlights::
    * Methods are functions in the class
    * First argument is always instance (``self``)
    * While calling function you never pass ``self``
    * Prevents copy-paste code
    * Improves readability
    * Improves refactoring
    * Decomposes bigger problem into smaller chunks

.. glossary::

    method
        Function inside the class which takes ``self`` as a first argument.


Methods without arguments
=========================
.. code-block:: python
    :caption: Methods without arguments

    class Astronaut:
        def say_hello(self):
            print('My name... Jose Jimenez')


    astro = Astronaut()
    astro.say_hello()
    # My name... Jose Jimenez


Methods with required argument
==============================
.. code-block:: python
    :caption: Methods with required argument

    class Astronaut:
        def say_hello(self, name):
            print(f'My name... {name}')


    astro = Astronaut()

    astro.say_hello(name='Jose Jimenez')
    # My name... Jose Jimenez

    astro.say_hello('Jose Jimenez')
    # My name... Jose Jimenez

    astro.say_hello()
    # TypeError: say_hello() missing 1 required positional argument: 'name'


Methods with optional argument (with default value)
===================================================
.. code-block:: python
    :caption: Methods with arguments with default value

    class Astronaut:
        def say_hello(self, name='Unknown'):
            print(f'My name... {name}')


    astro = Astronaut()

    astro.say_hello(name='Jose Jimenez')
    # My name... Jose Jimenez

    astro.say_hello('Jose Jimenez')
    # My name... Jose Jimenez

    astro.say_hello()
    # My name... Unknown


Methods Accessing Fields
========================
.. code-block:: python
    :caption: Methods Accessing Fields

    class Astronaut:
        def __init__(self, name):
            self.name = name

        def say_hello(self):
            print(f'My name... {self.name}')


    astro = Astronaut('Jose Jimenez')
    astro.say_hello()
    # My name... Jose Jimenez


Methods Calling Other Methods
=============================
.. code-block:: python
    :caption: Methods Calling Other Methods

    class Astronaut:
        def get_name(self):
            return 'Jose Jimenez'

        def say_hello(self):
            name = self.get_name()
            print(f'My name... {name}')


    astro = Astronaut()
    astro.say_hello()
    # My name... Jose Jimenez

.. code-block:: python
    :caption: Methods calling other methods

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2

        def sepal_area(self):
            return self.sepal_length * self.sepal_width

        def petal_area(self):
            return self.petal_length * self.petal_width

        def total_area(self):
            return self.sepal_area() + self.petal_area()


    flower = Iris()
    print(flower.total_area())
    # Total area: 18.13


Assignments
===========

Methods
-------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/syntax_methods.py`

:English:
    #. Define class ``Iris``
    #. Define method ``total()`` which calculates sum of all numerical attributes of an object

        * "Sepal length"
        * "Sepal width"
        * "Petal length"
        * "Petal width"

    #. Define method ``mean()`` which calculates mean of all numerical attributes of an object (assume length equal to 4)
    #. Create ``setosa`` object with attributes set at the initialization (see input data)
    #. Create ``virginica`` object with attributes set at the initialization (see input data)
    #. Print species name, total and mean of each instance

:Polish:
    #. Zdefiniuj klasę ``Iris``
    #. Zdefiniuj metodę ``total()`` klasy ``Iris`` wyliczającą sumę wszystkich atrybutów numerycznych obiektu:

        * "Sepal length"
        * "Sepal width"
        * "Petal length"
        * "Petal width"

    #. Zdefiniuj metodę ``mean()`` klasy ``Iris`` wyliczającą średnią wszystkich atrybutów numerycznych obiektu (przyjmij długość równą 4)
    #. Stwórz obiekt ``setosa`` z pomiarami podawanymi przy inicjalizacji (patrz dane wejściowe)
    #. Stwórz obiekt ``virginica`` z pomiarami podawanymi przy inicjalizacji (patrz dane wejściowe)
    #. Wypisz nazwę gatunku oraz sumę i średnią z pomiarów dla każdej instancji

:Input:
    .. csv-table:: Initial values
        :header: "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"
        :widths: 10, 10, 10, 10, 60

        "5.1", "3.5", "1.4", "0.2", "setosa"
        "5.8", "2.7", "5.1", "1.9", "virginica"
