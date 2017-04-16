#tekst = input('Wprowadź tekst: ')
tekst = 'Hej Matt. Mam nadzieję, że wszystko u Ciebie dobrze. Co tam.'

tekst_podzielony = tekst.split('.')
print(tekst_podzielony)

for zdanie in tekst_podzielony:
    wyrazy = zdanie.split()
    if wyrazy:
        ile = len(wyrazy)
        print(ile, wyrazy)


import sys
sys.exit()





tekst_podzielony = str.split(tekst, '.')
print(tekst_podzielony)


class Osoba:
    imie = 'Matt'
    nazwisko = 'Harasymczuk'

    def przedstaw_sie(self):
        print(self.nazwisko)


matt = Osoba()
matt.przedstaw_sie()

angie = Osoba()
angie.nazwisko = 'Jan'


Osoba.przedstaw_sie(angie)