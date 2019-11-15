.. _OOP Methods:

***********
OOP Methods
***********


* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``


Methods without arguments
=========================
.. code-block:: python
    :caption: Methods without arguments

    class Iris:
        def latin_name(self):
            print(f'Latin name: Iris Setosa')


    flower = Iris()

    flower.latin_name()
    # Latin name: Iris Setosa


Methods with argument
=====================
.. code-block:: python
    :caption: Methods with arguments

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


Methods with arguments with default value
=========================================
.. code-block:: python
    :caption: Methods with arguments with default value

    class Iris:
        def latin_name(self, species='unknown'):
            print(f'Latin name: Iris {species}')


    flower = Iris()

    flower.latin_name(species='Iris Setosa')
    # Latin name: Iris Setosa

    flower.latin_name('setosa')
    # Latin name: Iris Setosa

    flower.latin_name()
    # Latin name: unknown


Methods calling other methods
=============================
.. code-block:: python
    :caption: Methods calling other methods

    class Iris:
        def get_name(self):
            return 'Iris Setosa'

        def latin_name(self):
            name = self.get_name()
            return f'Latin name: {name}'


    flower = Iris()

    flower.latin_name()
    # Latin name: Iris Setosa

Methods accessing fields
========================
.. code-block:: python
    :caption: Methods accessing fields

    class Iris:
        def __init__(self, species='unknown'):
            self.species = species

        def latin_name(self):
            print(f'Latin name is: {self.species}')


    setosa = Iris('Iris Setosa')
    setosa.latin_name()
    # Latin name is: Iris Setosa

    iris = Iris()
    iris.latin_name()
    # Latin name is: unknown


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
