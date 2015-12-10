OSOBY = [
    {'imie': 'Matt', 'wiek': 10},
    {'imie': 'Angelika', 'wiek': 18},
    {'imie': 'Mateusz', 'wiek': 21},
    {'imie': 'Tadeusz', 'wiek': 35},
]

def osoba_pelnoletnia(osoba):
    print('\nSpawdzamy pelnoletnosc:', osoba)

    if osoba['wiek'] >= 18:
        print('Pelnoletnia:', osoba)
        return True
    else:
        print('Niepelnoletnia:', osoba)
        return False


dorosli = filter(osoba_pelnoletnia, OSOBY)
print(list(dorosli))





import sys
sys.exit()



dorosli = [osoba for osoba in OSOBY if osoba_pelnoletnia(osoba)]

print('\n\n')
print(dorosli)

















import sys
sys.exit()





def jest_pelnoletni(wiek):
    if wiek >= 18:
        return 'tak'
    else:
        return 'nie'


if jest_pelnoletnia(17):
    print('pelnoletni')
else:
    print('niepelnoletni')





def jest_pelnoletni(wiek):
    if wiek >= 18:
        return True
    else:
        return False


if jest_pelnoletnia(17):
    print('pelnoletni')
else:
    print('niepelnoletni')









a = float(1)
b = float(2)

#print(b)

liczby = [-2, -1, 0, 1, 2, 3]



print('Przy zastosowaniu funkcji ``map()``')

for wynik in map(float, liczby):
     print(wynik)


print('\n\n')


print('Przy zastosowaniu funkcji ``filter()``')

for wynik in filter(float, liczby):
    print(wynik)

















def parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


dane = range(0, 30)

parzyste1 = filter(parzysta, dane)
parzyste2 = filter(lambda x: x % 2 == 0, dane)
parzyste3 = filter(lambda x: not x % 2, dane)

#print(list(parzyste3))


def kwadrat(x):
    return pow(x, 2)


potegi1 = map(kwadrat, dane)
potegi2 = map(lambda x: pow(x, 2), dane)

#print(list(potegi1))


def opoznienie(przesuniecie):
    import datetime
    delay = pow(przesuniecie, 2)
    return datetime.datetime.now() + datetime.timedelta(seconds=delay)

czasy = map(opoznienie, dane)

#print(list(czasy))

from pprint import pprint
pprint(list(czasy))
