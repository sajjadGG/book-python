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
* Estimated time of completion: 10 min
* Solution: :download:`solution/oop_attribute_access.py`

:English:
    #. Create ``flowers: list``
    #. Create classes ``Virginica``, ``Versicolor``, ``Setosa`` identical to ``Iris``
    #. Iterate over input data (see below)

        #. Create object of a class based on last element of a tuple (Species column)
        #. Initialize objects with data from measurements
        #. To ``species`` field add class name that you are instantiating
        #. Use ``**kwargs`` notation while passing arguments
        #. Add instances to ``flowers``

    #. Print instance class name (from species field) and then both sum and mean of the measurements
    #. Format output to receive a table as shown in output data (see below)

:Polish:
    #. Stwórz klasy ``Virginica``, ``Versicolor``, ``Setosa``, które będą identyczne do ``Iris``
    #. Iterując po danych wejściowych (patrz niżej)

        #. Twórz obiekty klasy odpowiedniej dla nazwy gatunku (ostatni rekord każdej z krotek)
        #. Obiekt inicjalizuj danymi z pomiarów
        #. Do pola ``species`` w klasie zapisz nazwę klasy, której instancję tworzysz
        #. Wykorzystaj notację ``**kwargs`` przy podawaniu argumentów
        #. Obiekt instancje do ``flowers``

    #. Wypisz nazwę stworzonej klasy (z pola species) oraz sumę i średnią z pomiarów
    #. Wynik sformatuj aby wyglądał jak tabelka z danych wyjściowych (patrz sekcja output)

:Input:
    .. code-block:: python
        :caption: Iris sample dataset
        :name: listing-oop-classes

        INPUT = [
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

:Output:
    .. code-block:: text

        Species    Total   Avg
        ----------------------
         virginica  15.5  3.88
            setosa  10.2  2.55
        versicolor  13.9  3.48
         virginica  16.6  4.15
        versicolor  15.6  3.90
            setosa   9.4  2.35
        versicolor  16.3  4.07
         virginica  19.3  4.83
            setosa   9.5  2.38
            setosa   9.4  2.35

:Hint:
    * ``print(f'{name:>10} {total:>5.1f} {avg:>5.2f}')``
