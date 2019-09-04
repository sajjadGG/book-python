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

:Polish:
    #. Stwórz ``flowers: list``
    #. Stwórz klasy ``Virginica``, ``Versicolor``, ``Setosa``, które będą identyczne do ``Iris``
    #. Iterując po ``DATA`` z :numref:`listing-oop-classes`:

        #. Twórz obiekty klasy odpowiedniej dla nazwy gatunku (ostatni rekord każdej z krotek)
        #. Obiekt inicjalizuj danymi z pomiarów
        #. Obiekt dodaj do listy ``flowers``

    #. Na ekranie wyświetlaj nazwę gatunku oraz sumę i średnią z pomiarów.

:Extra Task:
    #. Wynik sformatuj aby wyglądał jak tabelka:

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

Basic Address Book
------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/intermediate_addressbook.py`

:Polish:
    #. Dla danych z listingu poniżej napisz książkę adresową
    #. W zadaniu mamy do czynienia z trzema klasami, wymień je.
    #. Zamodeluj problem wykorzystując trzy klasy i relacje między nimi
    #. Użytkownik może mieć wiele adresów
    #. Użytkownik może nie mieć żadnego adresu

:The whys and wherefores:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na ``str`` oraz jego reprezentacja (które i kiedy użyć)

:Input:
    .. code-block:: json
        :caption: Address Book

        [
            {"first_name": "Jan", "last_name": "Twardowski", "addresses": [
                {"street": "Kamienica Pod św. Janem Kapistranem", "city": "Kraków", "post_code": "31-008", "region": "Malopołskie", "country": "Poland"}]},

            {"first_name": "José", "last_name": "Jiménez", "addresses": [
                {"street": "2101 E NASA Pkwy", "city": "Houston", "post_code": 77058, "region": "Texas", "country": "USA"},
                {"street": "", "city": "Kennedy Space Center", "post_code": 32899, "region": "Florida", "country": "USA"}]},

            {"first_name": "Mark", "last_name": "Watney", "addresses": [
                {"street": "4800 Oak Grove Dr", "city": "Pasadena", "post_code": 91109, "region": "California", "country": "USA"},
                {"street": "2825 E Ave P", "city": "Palmdale", "post_code": "93550", "region": "California", "country": "USA"}]},

            {"first_name": "Иван", "last_name": "Иванович", "addresses": [
                {"street": "", "city": "Космодро́м Байкону́р", "post_code": "", "region": "Кызылординская область", "country": "Қазақстан"},
                {"street": "", "city": "Звёздный городо́к", "post_code": 141160, "region": "Московская область", "country": "Россия"}]},

            {"first_name": "Melissa", "last_name": "Lewis", "addresses": []},

            {"first_name": "Alex", "last_name": "Vogel", "addresses": [
                {"street": "Linder Hoehe", "city": "Köln", "post_code": 51147, "region": "North Rhine-Westphalia", "country": "Germany"}]}
        ]

Address Book from API
---------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/intermediate_addressbook_api.py`

:Polish:
    #. API programu powinno być tak jak na listingu poniżej
    #. Zrób tak, aby się ładnie wyświetlało zarówno dla jednego wyniku jak i dla wszystkich w książce
    #. ``Address`` ma mieć zmienną liczbę argumentów

:The whys and wherefores:
    * Korzystanie z ``.__str__()``

:Input:
    .. code-block:: python
        :caption: Address Book

        class AddressBook:
        pass

        class Contact:
            pass

        class Address:
            pass


        melissa = Contact(imie='Melissa', nazwisko='Lewis')
        print(melissa)
        # Melissa Lewis

        mark = Contact(imie='Mark', nazwisko='Watney', adresy=[Address(miasto='Houston'), Address(miasto='Cocoa Beach')])
        print(mark)
        # Mark Watney [Houston, Cocoa Beach]

        addressbook = AddressBook([
            Contact(imie='Jan', nazwisko='Twardowski', adresy=[
                Address(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
                Address(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
                Address(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
                Address(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
            ]),
            Contact(imie='José', nazwisko='Jiménez'),
            Contact(imie='Иван', nazwisko='Иванович', adresy=[]),
        ])


        print(addressbook)
        # [Jan Twardowski [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]

