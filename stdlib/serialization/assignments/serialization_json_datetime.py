"""
* Assignment: Serialization JSON Datetime
* Filename: serialization_json_datetime.py
* Complexity: easy
* Lines of code: 15 lines
* Time: 13 min

English:
    1. Use data from "Given" section (see below)
    2. Save data to file in JSON format
    3. Read data from file
    4. Recreate data structure
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zapisz dane do pliku w formacie JSON
    3. Odczytaj dane z pliku
    4. Odtwórz strukturę danych
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(result)
    <class 'list'>
    >>> len(result) > 0
    True
    >>> all(type(row) is dict
    ...     for row in result)
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'astronaut': {'date': datetime.date(1961, 4, 12), 'person': 'mark.watney@nasa.gov'},
     'flight': [{'datetime': datetime.datetime(1969, 7, 21, 2, 56, 15), 'action': 'landing'}]}
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
from datetime import datetime, date
import json

FILE = '_temporary.json'

DATA = {"mission": "Ares 3",
        "launch_date": date(2035, 6, 29),
        "destination": 'Mars',
        "destination_landing": date(2035, 11, 7),
        "destination_location": "Acidalia Planitia",
        "crew": [{"astronaut": 'Melissa Lewis', "date_of_birth": date(1995, 7, 15)},
                 {"astronaut": 'Rick Martinez', "date_of_birth": date(1996, 1, 21)},
                 {"astronaut": 'Alex Vogel', "date_of_birth": date(1994, 11, 15)},
                 {"astronaut": 'Chris Beck', "date_of_birth": date(1999, 8, 2)},
                 {"astronaut": 'Beth Johansen', "date_of_birth": date(2006, 5, 9)},
                 {"astronaut": 'Mark Watney', "date_of_birth": date(1994, 10, 12)}]}


# Solution
class JSONDatetimeEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, datetime):
            return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        elif isinstance(value, date):
            return value.strftime('%Y-%m-%d')


class JSONDatetimeDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.default)

    def default(self, obj):
        for key, value in obj.items():
            if key == 'datetime':
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
            elif key == 'date':
                value = datetime.strptime(value, '%Y-%m-%d').date()
            obj[key] = value
        return obj


with open(FILE, mode='w') as file:
    json.dump(DATA, file, cls=JSONDatetimeEncoder)


with open(FILE) as file:
    result = json.load(file, cls=JSONDatetimeDecoder)
