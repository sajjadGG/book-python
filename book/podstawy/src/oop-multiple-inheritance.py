class Pojazd:
    marka = None
    kola = 4


class Samochod(Pojazd):
    marka = None
    kierowca = {'imie': 'José', 'nazwisko': 'Jiménez'}
    kola = 6


class Jeep(Samochod):
    marka = 'jeep'
    kola = 10


class Star(Samochod):
    marka = 'star'


class Furmanka(Pojazd):
    marka = 'kon'


class CabrioBezDachu(Samochod):
    marka = 'cabrio'


auto = Star()
print(auto.kola)
# 6

inne = Jeep()
print(inne.kola)
# 10