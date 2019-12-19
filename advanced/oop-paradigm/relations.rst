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
