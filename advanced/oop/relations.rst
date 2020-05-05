*********
Relations
*********


Relations
=========
.. code-block:: python

    from typing import List


    class Astronaut:
        def __init__(self, name: str, experience: List[Missions] = ()) -> None:
            self.name = name
            self.experience = experience

    class Mission:
        def __init__(self, year: int, name: str) -> None:
            self.year = year
            self.name = name


    CREW = [
        Astronaut('Jan Twardowski', experience=(
            Mission(1969, 'Apollo 11'),
            Mission(2024, 'Artemis 3'))),

        Astronaut('Mark Watney', experience=(
            Mission(2035, 'Ares 3'))),

        Astronaut('Melissa Lewis'),
    ]


Assignments
===========

OOP Relations
-------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/oop_relations.py`

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

OOP Relations Flatten
---------------------
* Complexity level: hard
* Lines of code to write: 60 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/oop_relations_flatten.py`

:English:
    #. Using ``csv.DictWriter()`` save contacts from addressbook to CSV file
    #. How to write relations to CSV file (contact has many addresses)?
    #. Recreate object structure from CSV file

:Polish:
    #. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
    #. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
    #. Odtwórz strukturę obiektów na podstawie danych odczytanych z pliku

:Non functional requirements:
    #. All fields must be enclosed by double quote ``"`` character
    #. Use ``;`` to separate columns
    #. Use ``utf-8`` encoding
    #. Use Unix newline

:Input:
    .. code-block:: python

       class Contact:
            def __init__(self, first_name, last_name, addresses=()):
                self.first_name = first_name
                self.last_name = last_name
                self.addresses = addresses


        class Address:
            def __init__(self, location, city):
                self.location = location
                self.city = city


        DATA = [
            Contact(first_name='Jan', last_name='Twardowski', addresses=(
                Address(location='Johnson Space Center', city='Houston, TX'),
                Address(location='Kennedy Space Center', city='Merritt Island, FL'),
                Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
            )),
            Contact(first_name='Mark', last_name='Watney'),
            Contact(first_name='Melissa', last_name='Lewis', addresses=()),
        ]

OOP Relations Nested
--------------------
* Complexity level: medium
* Lines of code to write: 60 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/oop_relations_nested.py`

:English:
    #. Client can open a bank account
    #. Client can have many accounts
    #. Bank has many clients
    #. Each account has unique number generated when opening an account
    #. Client can ask about number of all of his accounts
    #. Client can add money to the account
    #. Client can withdraw money from the account

:Polish:
    #. Klient może otworzyć konto w banku
    #. Klient może mieć wiele kont
    #. Bank może mieć wielu klientów
    #. Każde konto ma unikalny numer, który jest generowany przy zakładaniu
    #. Klient może odpytać o numery wszystkich swoich kont
    #. Klient może wpłacić pieniądze na swoje konto
    #. Klient może wybrać pieniądze z bankomatu
