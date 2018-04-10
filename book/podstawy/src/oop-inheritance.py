class Pojazd:
    marka = None
    kierowca = None
    kola = 4


class Samochod(Pojazd):
    marka = None
    kierowca = {'imie': 'José', 'nazwisko': 'Jiménez'}


class Motor(Pojazd):
    marka = 'honda'
    kola = 2


class Tir(Pojazd):
    pass