#!/usr/bin/env python3

studenci = {
    "imie": "Mateusz",
    "nazwisko": 'Harasymczuk',
    'wiek': 10,
}

#print(studenci['nazwisko'])


studenci = [
    {'imie': 'Mateusz'},
    {'imie': 'Angelika', 'nazwisko': 'Janaszkiewicz'},
    {'imie': 'Dawid', 'nazwisko': 'Dorynek'},
    {'imie': 'Piotr', 'nazwisko': None},
    {'imie': 'Grzegorz', 'programuje w': ['python', 'java', 'c/c++']},
]


#dane = studenci[0]['nazwisko']

dane = studenci[0].get('nazwisko', 'n/d')

dane = '\n'.join(studenci[4].get('programuje w'))

print(dane)





