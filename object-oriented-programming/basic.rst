.. _OOP Basic:

*********
OOP Basic
*********


Object Paradigm
===============
* Model world as objects that interacts with each other

.. glossary::

    class
        Templates for objects.

    instance
    object
        Object created from class.

    method
        Function inside the class.

    property
    attribute
    field
        Variable inside the class.


Classes
=======
* Capitalized ``CamelCase`` name convention
* Classes are templates for objects

.. code-block:: python
    :caption: Defining class. Classes should have capitalized name

    class Iris:
        pass

.. code-block:: python
    :caption: Classes should have ``CamelCase`` names

    class IrisSetosa:
        pass

Classes vs Instances
--------------------
* Instances are also known as Objects
* Two newlines between class and code
* ``snake_case`` names

.. figure:: img/blueprint.png
    :scale: 8%
    :align: center

    Intuition definition: Class is a blueprint, instances are homes made from this plan. Image source: :cite:`FigureBlueprintHouse`

.. code-block:: python
    :caption: One class and one instance

    class Iris:
        pass


    flower = Iris()

.. code-block:: python
    :caption: One class and three instances

    class Iris:
        pass


    setosa = Iris()
    versicolor = Iris()
    virginica = Iris()

.. code-block:: python
    :caption: Three classes and three instances

    class IrisSetosa:
        pass

    class IrisVersicolor:
        pass

    class IrisVirginica:
        pass


    iris_setosa = IrisSetosa()
    iris_versicolor = IrisVersicolor()
    iris_virginica = IrisVirginica()


Fields
======
* Fields are also known as "Properties" or "Attributes"
* ``snake_case`` name convention
* Fields are defined in ``__init__()`` method
* Fields store information for instances

.. code-block:: python
    :caption: Classes can have multiple fields. All fields should be initialized in ``__init__()`` method.

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2
            self.species = 'setosa'


    flower = Iris()

    print(flower.sepal_length)  # 5.1
    print(flower.sepal_width)   # 3.5
    print(flower.species)       # 'setosa'


Initializer Method
==================
* ``__init__()`` is not a constructor!
* It's a first method run after object is initiated
* All classes has default ``__init__()``
* Initialize all fields only in ``__init__``

.. code-block:: python
    :caption: Class initialization

    class Iris:
        def __init__(self, species):
            self.species = species


    setosa = Iris(species='setosa')
    print(setosa.species)
    # setosa

    virginica = Iris('virginica')
    print(virginica.species)
    # virginica

    versicolor = Iris()
    # TypeError: __init__() missing 1 required positional argument: 'species'

.. code-block:: python
    :caption: Method argument with default value

    class Iris:
        def __init__(self, species=None):
            self.species = species


    setosa = Iris(species='setosa')
    print(setosa.species)
    # setosa

    virginica = Iris('virginica')
    print(virginica.species)
    # virginica

    versicolor = Iris()
    # None


Methods
=======
* Methods are functions in the class
* First argument is always instance (``self``)
* While calling function you never pass ``self``

Simple Methods
--------------
.. code-block:: python
    :caption: Simple Methods

    class Iris:
        def __init__(self):
            self.species = 'setosa'

        def latin_name(self):
            print(f'Latin name is: Iris setosa')


    flower = Iris()
    flower.latin_name()
    # Latin name is: Iris setosa

Methods accessing fields
------------------------
.. code-block:: python
    :caption: Methods accessing fields

    class Iris:
        def __init__(self):
            self.species = 'setosa'

        def latin_name(self):
            print(f'Latin name is: Iris {self.species}')


    flower = Iris()
    flower.latin_name()
    # Latin name is: Iris setosa

Methods with argument
---------------------
.. code-block:: python
    :caption: Methods with arguments

    class Iris:
        def latin_name(self, species):
            print(f'Iris {species}')


    flower = Iris()

    flower.latin_name(species='setosa')  # Iris setosa
    flower.latin_name('setosa')          # Iris setosa
    flower.latin_name()                  # TypeError: latin_name() missing 1 required positional argument: 'species'

Methods with arguments with default value
-----------------------------------------
.. code-block:: python
    :caption: Methods with default arguments

    class Iris:
        def latin_name(self, species='unknown'):
            print(f'Iris {species}')


    flower = Iris()

    flower.latin_name(species='setosa')  # Iris setosa
    flower.latin_name('setosa')          # Iris setosa
    flower.latin_name()                  # Iris unknown

Methods calling other methods
-----------------------------
.. code-block:: python
    :caption: Methods call other methods

    class Iris:
        def __init__(self):
            self.sepal_length = 5.1
            self.sepal_width = 3.5
            self.petal_length = 1.4
            self.petal_width = 0.2
            self.species = 'setosa'

        def sepal_area(self):
            return self.sepal_length * self.sepal_width

        def petal_area(self):
            return self.petal_length * self.petal_width

        def total_area(self):
            area = self.sepal_area() + self.petal_area()
            print(f'Total area is: {area:.1f}')


    flower = Iris()
    flower.total_area()
    # Total area is: 18.1


One class per file?
===================
* Osobne pliki - gdy klasy są duże
* Jeden plik - gdy klasy są małe i czytelne

.. code-block:: python
    :caption: Classes and Objects

    class IrisSetosa:
        pass

    class IrisVersicolor:
        pass

    class IrisVirginica:
        pass


    setosa = IrisSetosa()
    versicolor = IrisVersicolor()
    virginica = IrisVirginica()


Assignments
===========

Defining Classes
----------------
* Filename: :download:`solution/basic_iris.py`
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min

#. Stwórz klasę ``Iris`` z polami:

    - ``sepal_length: float``,
    - ``sepal_width: float``,
    - ``petal_length: float``,
    - ``petal_width: float``,
    - ``species: str``.

#. Napisz metodę ``total()`` wyliczającą sumę dla pól numerycznych obiektu (``sepal_length``, ``sepal_width``, ``petal_length``, ``petal_width``)
#. Napisz metodę ``average()`` wyliczającą średnią dla powyższych pól
#. Stwórz obiekt ``setosa`` z pomiarami:

    * sepal_length: 5.4
    * sepal_width: 3.9
    * petal_length: 1.3
    * petal_width: 0.4

#. Wyświetl na ekranie nazwę gatunku oraz sumę i średnią z pomiarów.

Dragon (version alpha)
----------------------
* Filename: :download:`solution/basic_dragon.py`
* Lines of code to write: 120 lines
* Estimated time of completion: 60 min (±10 min), then 30 min live coding with instructor
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

#. Zadanie jest specyfikacją wymagań biznesowych, a nie dokumentacją techniczną. tj. "co Smok ma robić, a nie jak to ma robić"
#. Smok ma:

    * nazwę
    * pozycję ``x`` na ekranie
    * pozycję ``y`` na ekranie
    * nazwę pliku tekstury, domyślnie ``img/dragon/alive.png``
    * punkty życia, domyślnie losowy ``int`` z zakresu od 50 do 100

#. Smok może:

    * być ustawiony w dowolne miejsce ekranu
    * zadawać komuś losowe obrażenia z przedziału od 5 do 20
    * otrzymywać obrażenia
    * być przesuwany o zadaną liczbę punktów w którymś z kierunków

#. Przyjmij górny lewy róg ekranu za punkt początkowy:

    * idąc w prawo dodajesz ``x``
    * idąc w lewo odejmujesz ``x``
    * idąc w górę odejmujesz ``y``
    * idąc w dół dodajesz ``y``

#. Jest to wersja ``alpha`` więc bez dodatkowych funkcjonalności
#. Przy każdym obrażeniu wypisz na ekranie nazwę Smoka, ilość obrażeń i pozostałe punkty życia
#. Kiedy punkty życia Smoka spadną do, lub poniżej zera:

    * Smok jest martwy
    * ustaw status obiektu na ``dead``
    * na ekranie ma pojawić się napis ``XXX is dead`` gdzie XXX to nazwa smoka
    * zmień nazwę pliku tekstury na ``img/dragon/dead.png``
    * na ekranie pojawi się informacja ile złota smok wyrzucił (losowa 1-100)
    * na ekranie pojawi się informacja o pozycji gdzie smok zginął
    * Nie można zadawać mu obrażeń
    * Smok nie może zadawać obrażeń
    * Smok nie może się poruszać

#. Przeprowadź grę:

    * Stwórz smoka w pozycji x=50, y=120 i nazwij go Wawelski
    * Ustaw nową pozycję na x=10, y=20
    * Przesuń smoka o 10 w lewo i 20 w dół
    * Przesuń smoka o 10 w lewo i 15 w prawo
    * Przesuń smoka o 15 w prawo i 5 w górę
    * Przesuń smoka o 5 w dół
    * Zadaj 10 obrażeń smokowi
    * Zadaj 5 obrażeń smokowi
    * Zadaj 3 obrażeń smokowi
    * Zadaj 2 obrażeń smokowi
    * Zadaj 15 obrażeń smokowi
    * Zadaj 25 obrażeń smokowi
    * Zadaj 75 obrażeń smokowi

#. Pozycja Smoka na końcu powinna być x=20, y=40
#. Możesz wprowadzać dodatkowe pola, metody, funkcje, zmienne, stały, klasy, obiekty, co tylko chcesz
#. Nie musisz trzymać się kolejności punktów i podpunktów w zadaniu
#. Nie przeglądaj kolejnych (przyszłych) części zadania. Zadanie jest symulacją pewnego procesu. Jeżeli zaglądniesz w przód, to zepsujesz sobie zabawę.

:The whys and wherefores:
    * "Smok" jest tylko narracją do demonstracji praktyk
    * myślenie obiektowe i odwzorowanie struktury w programie
    * tworzenie i praca z obiektami
    * zagnieżdżanie obiektów
    * specyfikacja interfejsów klas
    * interakcja między obiektami
    * podział aplikacji na warstwy
    * dobre praktyki programistyczne
