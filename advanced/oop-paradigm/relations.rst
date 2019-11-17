*********
Relations
*********


Relations
=========
.. code-block:: python

    class Astronaut:
        def __init__(self, name, locations=()):
            self.name = name
            self.locations = locations


    class Location:
        def __init__(self, name):
            self.name = name


    INPUT = [
        Astronaut('Jan Twardowski', locations=(
            Location('Johnson Space Center'),
            Location('Kennedy Space Center'),
            Location('Jet Propulsion Laboratory'),
        )),
        Astronaut('Mark Watney'),
        Astronaut('Melissa Lewis', locations=()),
    ]


Assignments
===========

Defining Classes
----------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/intermediate_iris.py`

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
    #. Wynik sformatuj aby wyglądał jak tabelka z danych wyjściowych (patrz poniżej)

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

Basic Address Book
------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/intermediate_addressbook.py`

:English:
    #. Create Address Book based on input data (see below)
    #. Model data using classes and relations
    #. We should have three classes, name it

:Polish:
    #. Dla danych z listingu poniżej napisz książkę adresową
    #. W zadaniu mamy do czynienia z trzema klasami, wymień je.
    #. Zamodeluj problem wykorzystując trzy klasy i relacje między nimi

:The whys and wherefores:
    * OOP modeling
    * working with objects
    * nesting objects and relations
    * casting objects to ``str``

:Input:
    .. code-block:: json
        :caption: Address Book

        [
            {"first_name": "Jan", "last_name": "Twardowski", "addresses": [
                {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "post_code": "31-008", "region": "Małopolskie", "country": "Poland"}]},

            {"first_name": "José", "last_name": "Jiménez", "addresses": [
                {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
                {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

            {"first_name": "Mark", "last_name": "Watney", "addresses": [
                {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
                {"street": "2825 E Ave P", "city": "Palmdale", "post_code": 93550, "region": "California", "country": "USA"}]},

            {"first_name": "Иван", "last_name": "Иванович", "addresses": [
                {"street": "", "city": "Космодро́м Байкону́р", "post_code": "", "region": "Кызылординская область", "country": "Қазақстан"},
                {"street": "", "city": "Звёздный городо́к", "post_code": 141160, "region": "Московская область", "country": "Россия"}]},

            {"first_name": "Melissa", "last_name": "Lewis", "addresses": []},

            {"first_name": "Alex", "last_name": "Vogel", "addresses": [
                {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
        ]
