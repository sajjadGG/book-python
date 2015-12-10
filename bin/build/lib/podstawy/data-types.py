#!/usr/bin/env python3

import datetime

db_rows = [
    {"id": 1, "name": "Matt", "last_name": "Harasymczuk", 'xxx': datetime.datetime(2015, 12, 14, 16, 15, 21, 468157)},
    {"id": 2, "name": "Katarzyna", "last_name": "Kurek", 'xxx': datetime.datetime(2015, 12, 14, 16, 15, 21, 468157)},
    {"id": 3, "name": "Jarosław", "last_name": "Senator", 'xxx': datetime.datetime(2015, 12, 14, 16, 15, 21, 468157)}
]


def get_datetime():
    """
    Funkcja ma za zadanie wyciągnąć wartość daty w przypadku gdy nie znamy nazwy kolumny.

    >>> get_datetime()
    [datetime.datetime(2015, 12, 14, 16, 15, 21, 468157), datetime.datetime(2015, 12, 14, 16, 15, 21, 468157), datetime.datetime(2015, 12, 14, 16, 15, 21, 468157)]
    """
    a = list()

    for row in db_rows:
        for key in row.keys():
            if isinstance(row.get(key), datetime.datetime):
                a.append(row.get(key))

    return a
