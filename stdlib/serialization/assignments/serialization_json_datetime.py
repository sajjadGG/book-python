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
    >>> from inspect import isclass
    >>> isclass(Encoder)
    True
    >>> isclass(Decoder)
    True
    >>> issubclass(Encoder, json.JSONEncoder)
    True
    >>> issubclass(Decoder, json.JSONDecoder)
    True
    >>> with open(FILE, mode='w') as file:
    ...     json.dump(DATA, file, cls=Encoder)
    >>> with open(FILE, mode='r') as file:
    ...     result = json.load(file, cls=Decoder)
    >>> from os import remove
    >>> remove(FILE)
    >>> type(result)
    <class 'dict'>
    >>> len(result) > 0
    True
    >>> all(type(key) is str
    ...     and type(value) in (str, datetime, list)
    ...     for key, value in result.items())
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'mission': 'Ares 3',
     'launch_date': datetime.datetime(2035, 6, 29, 0, 0, tzinfo=datetime.timezone.utc),
     'destination': 'Mars',
     'destination_landing': datetime.datetime(2035, 11, 7, 0, 0, tzinfo=datetime.timezone.utc),
     'destination_location': 'Acidalia Planitia',
     'crew': [{'astronaut': 'Melissa Lewis', 'date_of_birth': datetime.date(1995, 7, 15)},
              {'astronaut': 'Rick Martinez', 'date_of_birth': datetime.date(1996, 1, 21)},
              {'astronaut': 'Alex Vogel', 'date_of_birth': datetime.date(1994, 11, 15)},
              {'astronaut': 'Chris Beck', 'date_of_birth': datetime.date(1999, 8, 2)},
              {'astronaut': 'Beth Johansen', 'date_of_birth': datetime.date(2006, 5, 9)},
              {'astronaut': 'Mark Watney', 'date_of_birth': datetime.date(1994, 10, 12)}]}
"""


# Given
from datetime import datetime, date, timezone
import json

FILE = '_temporary.json'

DATA = {"mission": "Ares 3",
        "launch_date": datetime(2035, 6, 29, tzinfo=timezone.utc),
        "destination": 'Mars',
        "destination_landing": datetime(2035, 11, 7, tzinfo=timezone.utc),
        "destination_location": "Acidalia Planitia",
        "crew": [{"astronaut": 'Melissa Lewis', "date_of_birth": date(1995, 7, 15)},
                 {"astronaut": 'Rick Martinez', "date_of_birth": date(1996, 1, 21)},
                 {"astronaut": 'Alex Vogel', "date_of_birth": date(1994, 11, 15)},
                 {"astronaut": 'Chris Beck', "date_of_birth": date(1999, 8, 2)},
                 {"astronaut": 'Beth Johansen', "date_of_birth": date(2006, 5, 9)},
                 {"astronaut": 'Mark Watney', "date_of_birth": date(1994, 10, 12)}]}


class Encoder(json.JSONEncoder):
    def default(self, value: datetime) -> str:
        return ...


class Decoder(json.JSONDecoder):
    def __init__(self) -> None:
        super().__init__(object_hook=self.default)

    def default(self, data: dict) -> dict:
        ...


# Solution
class Encoder(json.JSONEncoder):
    def default(self, value: datetime) -> str:
        return value.isoformat()


class Decoder(json.JSONDecoder):
    date_of_birth: date
    launch_date: datetime
    destination_landing: datetime

    def __init__(self) -> None:
        super().__init__(object_hook=lambda data: {
                field: getattr(self, method)(value)
                for field, value in data.items()
                if (method := self.__annotations__.get(field, str).__name__)})

    def datetime(self, value: str) -> date:
        return datetime.fromisoformat(value)

    def date(self, value: str) -> date:
        return datetime.fromisoformat(value).date()

    def str(self, value: str) -> str:
        return value
