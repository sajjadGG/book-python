****************
Access Modifiers
****************


Rationale
=========
.. highlights::
    * Attributes and methods are always public
    * No protected and private keywords
    * ``_name()`` - protected attribute or method (by convention)
    * ``__name`` - private attribute or method (by convention)
    * ``__name__`` - system attribute or method
    * ``name_`` - used while name collision


Protected Attribute
===================
* ``_name`` - protected attribute (by convention)

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

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')

    print(mark.firstname)
    # Traceback (most recent call last):
    #    ...
    # AttributeError: 'Astronaut' object has no attribute 'firstname'

    print(mark.lastname)
    # Traceback (most recent call last):
    #    ...
    # AttributeError: 'Astronaut' object has no attribute 'lastname'

    print(mark._firstname)      # IDE should warn: "Access to a protected member _firstname of a class "
    # Mark

    print(mark._lastname)       # IDE should warn: "Access to a protected member _lastname of a class "
    # Watney

    print(mark.publicname)
    # Mark W.


Private Attribute
=================
* ``__name`` - private attribute

.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.__firstname = firstname
            self.__lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')

    print(mark.publicname)
    # Mark W.

    print(mark.__firstname)
    # Traceback (most recent call last):
    #    ...
    # AttributeError: 'Astronaut' object has no attribute '__firstname'

    print(mark.__lastname)
    # Traceback (most recent call last):
    #    ...
    # AttributeError: 'Astronaut' object has no attribute '__firstname'


System Attributes
=================
* ``__name__`` - system attribute

.. code-block:: python
    :caption: ``obj.__dict__`` - Getting dynamic fields and values

    class Astronaut:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname


    mark = Astronaut('Mark', 'Watney')

    print(mark.__dict__)
    # {'firstname': 'Mark',
    #  'lastname': 'Watney'}

.. code-block:: python
    :caption: ``obj.__dict__`` - Getting dynamic fields and values

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname
            self.publicname = f'{firstname} {lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')


    print(mark.__dict__)
    # {'_firstname': 'Mark',
    #  '_lastname': 'Watney',
    #  'publicname': 'Mark W.'}

    public_attrs = {k:v for k,v in mark.__dict__.items() if not k.startswith('_')}
    print(public_attrs)
    # {'publicname': 'Mark W.'}


Protected Method
================
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def _get_fullname(self):
            return f'{self._firstname} {self._lastname}'

        def get_publicname(self):
            return f'{self._firstname} {self._lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')

    print(dir(mark))
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    # '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
    # '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_firstname',
    # '_get_fullname', '_lastname', 'get_publicname']

    public_methods = [mth for mth in dir(mark) if not mth.startswith('_')]
    print(public_methods)
    # ['get_publicname']


Private Method
==============
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __get_fullname(self):
            return f'{self._firstname} {self._lastname}'

        def get_publicname(self):
            return f'{self._firstname} {self._lastname[0]}.'


    mark = Astronaut('Mark', 'Watney')

    print(dir(mark))
    # ['_Astronaut__get_fullname', '__class__', '__delattr__', '__dict__',
    #  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    #  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
    #  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    #  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    #  '__weakref__', '_firstname', '_lastname', 'get_publicname']

    public_methods = [mth for mth in dir(mark) if not mth.startswith('_')]
    print(public_methods)
    # ['get_publicname']

    mark.__get_fullname()
    # Traceback (most recent call last):
    #   ...
    # AttributeError: 'Astronaut' object has no attribute '__get_fullname'


System Method
=============
.. code-block:: python

    class Astronaut:
        def __init__(self, firstname, lastname):
            self._firstname = firstname
            self._lastname = lastname

        def __str__(self):
            return 'stringification'

        def __repr__(self):
            return 'representation'


    mark = Astronaut('Mark', 'Watney')

    print(str(mark))
    # stringification

    print(repr(mark))
    # representation


Assignments
===========

OOP Attribute Access Modifiers
------------------------------
* Complexity level: easy
* Lines of code to write: 20 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/oop_attribute_access_modifiers.py`

:English:
    #. Use data from "Input" section (see below)
    #. Create class ``Iris``
    #. In ``Iris._init__()`` add protected attributes ``sepal_length``, ``sepal_width``, ``petal_length``, ``petal_width``
    #. In ``Iris._init__()`` add public attribute ``species``
    #. Create class ``Setosa``, ``Versicolor``, ``Virginica`` inheriting from ``Iris``
    #. Iterate over ``result`` and print all public fields of each element
    #. Compare result with "Output" section (see below)

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Stwórz klasę ``Iris``
    #. W ``Iris._init__()`` dodaj chronione atrybuty ``sepal_length``, ``sepal_width``, ``petal_length``, ``petal_width``
    #. W ``Iris._init__()`` dodaj publiczny atrybut ``species``
    #. Stwórz klasy ``Setosa``, ``Versicolor``, ``Virginica`` dziedziczące po ``Iris``
    #. Iteruj po ``result`` i wypisz wszystkie publiczne pola każdego elementu
    #. Porównaj wyniki z sekcją "Output" (patrz poniżej)

:Input:
    .. code-block:: python

        result = [
            Virginica(5.8, 2.7, 5.1, 1.9, 'virginica'),
            Setosa(5.1, 3.5, 1.4, 0.2, 'setosa'),
            Versicolor(5.7, 2.8, 4.1, 1.3, 'versicolor'),
        ]

:Output:
    .. code-block:: python

        {'species': 'virginica'}
        {'species': 'setosa'}
        {'species': 'versicolor'}

OOP Attribute Access Dict
-------------------------
* Complexity level: medium
* Lines of code to write: 35 lines
* Estimated time of completion: 21 min
* Solution: :download:`solution/oop_attribute_access_dict.py`

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
                self._sepal_length = sepal_length
                self._sepal_width = sepal_width
                self._petal_length = petal_length
                self._petal_width = petal_width

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
