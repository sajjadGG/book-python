#!/usr/bin/env python3

from pprint import pprint
import sys


def czytaj_passwd():
    with open('/etc/passwd') as file:

        for linia_w_pliku_passwd in file.readlines():
            if not linia_w_pliku_passwd.startswith('#'):

                element_linii = linia_w_pliku_passwd.split(':')
                login = element_linii[0]
                uid = int(element_linii[2])

                if uid < 1000:
                    yield login


# zawartosc = czytaj_passwd()
# print(sys.getsizeof(zawartosc))
# pprint(list(zawartosc))
# sys.exit()


def czytaj_passwd_tradycyjnie():
    with open('/etc/passwd') as file:
        tresc_pliku = []

        for linia in file.readlines():
            if not linia.startswith('#'):
                return linia
                tresc_pliku.append(linia)

        return tresc_pliku


# zawartosc_tradycyjna = czytaj_passwd_tradycyjnie()
# print(zawartosc_tradycyjna)
# print(sys.getsizeof(zawartosc_tradycyjna))


"""
def czytaj_passwd_rozwijanie_list():
    with open('/etc/passwd') as file:

        for linia_w_pliku_passwd in file.readlines():
            if not linia_w_pliku_passwd.startswith('#'):

                element_linii = linia_w_pliku_passwd.split(':')
                login = element_linii[0]
                uid = int(element_linii[2])

                if uid < 1000:
                    yield login


zawartosc_rozwinieta = list(czytaj_passwd_rozwijanie_list())
#print(sys.getsizeof(zawartosc))
print(zawartosc_rozwinieta)
"""

"""
a = range(0, 30)

with open('/etc/passwd') as file:
    nasz_passwd = file.readlines()

shelle = [
        linia.split(':')[-1]

        for linia in nasz_passwd
            if not linia.startswith('#') and int(linia.split(':')[2]) < 1000
]

print(shelle)
"""

osoby_w_klasie = [
    {'username': 'mharasymczuk', 'czy_wykladowca': True},
    {'username': 'pkuzmiak', 'czy_wykladowca': False},
    {'username': 'awojtaszek', 'czy_wykladowca': False},
    {'username': 'jsenator', 'czy_wykladowca': False},
]


def uczestnicy_kursu(osoby):
    def jest_wykladowca(user):
        if user['czy_wykladowca']:
            return True
        else:
            return False

    for osoba in osoby:
        if not osoba['czy_wykladowca']:
            yield {
                'wykladowcy': jest_wykladowca,
                'uczestnicy': [x for x in osoby if not x['czy_wykladowca']],
                'wszystkie_username': [x['username'] for x in osoby]

            }


uczestnicy_kursu = [osoba.get('username') for osoba in osoby_w_klasie if not osoba['czy_wykladowca']]
pprint(uczestnicy_kursu)
