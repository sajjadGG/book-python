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
        def say_hello(self)
            print('My name... Jose Jimenez')


    astro = Astronaut()

    astro.say_hello()
    # My name... Jose Jimenez

.. code-block:: python
    :caption: Methods without arguments

    class Iris:
        def latin_name(self):
            print(f'Latin name: Iris Setosa')


    flower = Iris()

    flower.latin_name()
    # Latin name: Iris Setosa


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


.. code-block:: python
    :caption: Methods with required argument

    class Iris:
        def latin_name(self, species):
            print(f'Latin name: {species}')


    flower = Iris()

    flower.latin_name(species='Iris Setosa')
    # Latin name: Iris Setosa

    flower.latin_name('Iris Setosa')
    # Latin name: Iris Setosa

    flower.latin_name()
    # TypeError: latin_name() missing 1 required positional argument: 'species'


Methods with optional argument (with default value)
===================================================
.. code-block:: python
    :caption: Methods with arguments with default value

    class Iris:
        def latin_name(self, species='Unknown'):
            print(f'Latin name: {species}')


    flower = Iris()

    flower.latin_name(species='Iris Setosa')
    # Latin name: Iris Setosa

    flower.latin_name('Iris Setosa')
    # Latin name: Iris Setosa

    flower.latin_name()
    # Latin name: Unknown


Methods Accessing Fields
========================
.. code-block:: python
    :caption: Methods Accessing Fields

    class Iris:
        def __init__(self, species):
            self.species = species

        def latin_name(self):
            print(f'Latin name is: {self.species}')


    flower = Iris('Iris Setosa')
    flower.latin_name()
    # Latin name is: Iris Setosa


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
            sepal_area = self.sepal_area()
            petal_area = self.petal_area()
            return sepal_area + petal_area


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
* Filename: :download:`solution/syntax_methods.py`

:English:
    #. Create class ``Iris``
    #. Create method ``total()`` which calculates sum of all numerical attributes of an object
    #. Create method ``mean()`` which calculates mean of all numerical attributes of an object (assume length equal to 4)
    #. Create ``setosa`` object with attributes set at the initialization (see input data)
    #. Create ``virginica`` object with attributes set at the initialization (see input data)
    #. Print species name, total and mean of each instance

:Polish:
    #. Stwórz klasę ``Iris``
    #. Napisz metodę ``total()`` wyliczającą sumę wszystkich atrybutów numerycznych obiektu
    #. Napisz metodę ``mean()`` wyliczającą średnią wszystkich atrybutów numerycznych obiektu (przyjmij długość równą 4)
    #. Stwórz obiekt ``setosa`` z pomiarami podawanymi przy inicjalizacji (patrz dane wejściowe)
    #. Stwórz obiekt ``virginica`` z pomiarami podawanymi przy inicjalizacji (patrz dane wejściowe)
    #. Wypisz nazwę gatunku oraz sumę i średnią z pomiarów dla każdej instancji

:Input:
    .. csv-table:: Initial values
        :header: "Sepal length", "Sepal width", "Petal length", "Petal width", "Species"
        :widths: 10, 10, 10, 10, 60

        "5.8", "2.7", "5.1", "1.9", "virginica"
        "5.1", "3.5", "1.4", "0.2", "setosa"
