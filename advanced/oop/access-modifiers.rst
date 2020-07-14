****************
Attribute Access
****************


.. highlights::
    * Fields are always public
    * No protected and private
    * ``_name`` - protected field (by convention)
    * ``__name__`` - system field
    * ``name_`` - used while name collision

.. code-block:: python
    :caption: Access modifiers

    class Temperature:
        pass


    temp = Temperature()
    temp._value = 10

    print(temp._value)  # IDE should warn, that you access protected member
    # 10

.. code-block:: python
    :caption: Access modifiers

    class Iris:
        pass


    flower = Iris()
    flower._sepal_length = 5.1
    flower._sepal_width = 3.5
    flower._petal_length = 1.4
    flower._petal_width = 0.2
    flower.species = 'setosa'

    print(flower._sepal_length)     # 5.1       # IDE should warn, that you access protected member
    print(flower._sepal_width)      # 3.5       # IDE should warn, that you access protected member
    print(flower._petal_length)     # 1.4       # IDE should warn, that you access protected member
    print(flower._petal_width)      # 0.2       # IDE should warn, that you access protected member
    print(flower.species)           # setosa


Assignments
===========

OOP Attribute Access
--------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/oop_attribute_access.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create classes ``Virginica``, ``Versicolor``, ``Setosa`` identical to ``Iris``
    #. Create ``result: list[Iris]``
    #. Iterate over input data

        #. Create object of a class based on last element of a tuple (Species column)
        #. Initialize objects with data from measurements
        #. To ``species`` field add class name that you are instantiating
        #. Use ``*args`` notation while passing arguments
        #. Add instances to ``result``

    #. Print instance class name (from species field) and then both sum and mean of the measurements
    #. Format output to receive a table as shown in output data
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz klasy ``Virginica``, ``Versicolor``, ``Setosa``, które będą identyczne do ``Iris``
    #. Stwórz ``result: list[Iris]``
    #. Iterując po danych wejściowych

        #. Twórz obiekty klasy odpowiedniej dla nazwy gatunku (ostatni rekord każdej z krotek)
        #. Obiekt inicjalizuj danymi z pomiarów
        #. Do pola ``species`` w klasie zapisz nazwę klasy, której instancję tworzysz
        #. Wykorzystaj notację ``*args`` przy podawaniu argumentów
        #. Dodaj instancje do ``result``

    #. Wypisz nazwę stworzonej klasy (z pola species) oraz sumę i średnią z pomiarów
    #. Wynik sformatuj aby wyglądał jak tabelka z danych wyjściowych
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python
        :caption: Iris sample dataset
        :name: listing-oop-classes

        DATA = [
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
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

        class Iris:
            def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
                self.sepal_length = sepal_length
                self.sepal_width = sepal_width
                self.petal_length = petal_length
                self.petal_width = petal_width

            def __repr__(self):
                raise NotImplementedError

            def length(self):
                raise NotImplementedError

            def sum(self):
                raise NotImplementedError

            def mean(self):
                raise NotImplementedError


:Output:
    .. code-block:: text

        Species    Total   Avg
        ----------------------
        [
         Virginica  15.5  3.88,
            Setosa  10.2  2.55,
        Versicolor  13.9  3.48,
         Virginica  16.6  4.15,
        Versicolor  15.6  3.90,
            Setosa   9.4  2.35,
        Versicolor  16.3  4.07,
         Virginica  19.3  4.83,
            Setosa   9.5  2.38,
         Virginica  13.6  3.40,
         Virginica  18.1  4.53,
            Setosa   9.7  2.43,
            Setosa  11.4  2.85,
        Versicolor  14.3  3.58,
            Setosa  10.3  2.58,
        Versicolor  13.1  3.28,
         Virginica  17.5  4.38,
        Versicolor  15.4  3.85,
         Virginica  18.1  4.53,
        Versicolor  16.4  4.10,
            Setosa   9.4  2.35]


:Hint:
    * ``self.__class__.__name__``
    * ``self.__dict__.values()``
    * ``f'\n{name:>10} {total:>5.1f} {avg:>5.2f}'``
