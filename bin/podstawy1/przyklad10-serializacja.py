from datetime import datetime
import json

now = datetime.now()

def make_datetime(dt):
    return str(dt).replace(' ', 'T')[:23]


class Osoba:
    imie = 'Mattół'
    nazwisko = 'Harasymczuk'


PYTHON = [
    Osoba,
    make_datetime(now),
    str(now),
    now.__str__(),
    '%s' % now,
    '{}'.format(now),
    {'imię': 'Mattół', 'nazwisko': 'Harasymczuk'},
    (10, 20, 30),
    (1,)
]

JSON = '["2016-10-26T14:41:51.020", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", {"nazwisko": "Harasymczuk", "imi\u0119": "Matt\u00f3ł"}, [10, 20, 30], [1]]'





#js = json.dumps(PYTHON)
#print(js)
#python = json.loads(JSON)
#print(python)


import pickle
p = pickle.dumps(PYTHON)
print('Z Python do Pickle:', p)

pp = pickle.loads(p)
print('Z Pickle do Python:', pp)

osoba = pp[0]
print('Obiekt po konwersji:', osoba.nazwisko)