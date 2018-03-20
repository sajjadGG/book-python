class Osoba:
    imie = 'statycznie'

    def __init__(self, nazwisko='dynamicznie'):
        self.nazwisko = nazwisko


def say_hello():
    print('hello')


def say_ehlo():
    print('ehlo')


osoba = Osoba()
osoba.data_urodzenia = 'dynamicznie w locie'
osoba.hello = say_hello
osoba.imie = 'moge to zmienic'

Osoba.adres = 'pole klasy modyfikowane dynamicznie'
Osoba.ehlo = say_ehlo
Osoba.imie = 'jeszcze inne imie'