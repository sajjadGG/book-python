*******
Methods
*******


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
    #. Create class ``Iris`` with fields from input data
    #. Create method ``total()`` which sums all the numerical attributes values
    #. Create method ``mean()`` which calculates mean of numerical attributes values
    #. Create ``setosa`` object with attributes set at the initialization (see input data)
    #. Create ``virginica`` object with attributes set at the initialization (see input data)
    #. Print on the screen species name, total and mean of each instance

:Polish:
    #. Stwórz klasę ``Iris`` z polami z danych wejściowych
    #. Napisz metodę ``total()`` wyliczającą sumę atrybutów numerycznych obiektu
    #. Napisz metodę ``mean()`` wyliczającą średnią atrybutów numerycznych obiektu
    #. Stwórz obiekt ``setosa`` z pomiarami podawanymi przy inicjalizacji (patrz dane wejściowe)
    #. Stwórz obiekt ``virginica`` z pomiarami podawanymi przy inicjalizacji (patrz dane wejściowe)
    #. Wyświetl na ekranie nazwę gatunku oraz sumę i średnią z pomiarów dla każdej instancji

:Input:
    .. code-block:: python
        :caption: Iris parameters

        sepal_length: float
        sepal_width: float
        petal_length: float
        petal_width: float
        species: str

    .. code-block:: python
        :caption: Setosa initial values

        sepal_length = 5.4
        sepal_width = 3.9
        petal_length = 1.3
        petal_width = 0.4

    .. code-block:: python
        :caption: Virginica initial values

        sepal_length = 5.8
        sepal_width = 2.7
        petal_length = 5.1
        petal_width = 1.9
