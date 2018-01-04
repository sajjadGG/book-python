#!/usr/bin/env python3.6
"""
Przykład implementacji książki adresowej za pomocą klas.
"""


class Osoba:
    def __init__(self,
                 imie=None,
                 nazwisko=None,
                 wiek=None):

        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

class Kontakt(Osoba):
    def __init__(self,
                 imie=None,
                 nazwisko=None,
                 wiek=None,
                 adres=None):

        super().__init__(imie, nazwisko, wiek)

        if adres is None:
            adres = Adres()

        if isinstance(adres, list):
            self.adres = adres
        else:
            self.adres = [adres]

    def dodaj_adres(self, nowy_adres):
        self.adres.append(nowy_adres)


class Address:
    """
    Klasa Address, która służy do przechowywania adresów
    """
    def __init__(self, **kwargs):
        print(kwargs)
        if 'ulica' in kwargs:
            self.ulica = kwargs['ulica']
        if 'miasto' in kwargs:
            self.miasto = kwargs['miasto']
        pass

    def __str__(self):
        return f"ulica {self.ulica} w {self.miasto}"

    def __repr__(self):
        return f"ulica {self.ulica} w {self.miasto}"


address_of_person = Address(ulica = "Gdańska",
                            miasto='Warszawa')

person = Kontakt('Max', 'Peck', adres = address_of_person)

nowy_adres = Address(ulica = "Warszawska",
                     miasto='Gdańsk')

person.dodaj_adres(nowy_adres)

print(address_of_person.miasto)

print(f"Mam na imie {person.imie},",
      f" mieszkam w {person.adres}")


class KsiazkaAdresowa:
    def __init__(self):
        self.lista = []

    def dodaj_do_listy(self, nowy_kontakt):
        self.lista.append(nowy_kontakt)

    def pokaz_kontakt(self, index):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
