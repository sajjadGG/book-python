#!/usr/bin/env python3.6
"""
Przykład implementacji funkcji do parsowania rekordów.
"""

def konwertuj(lista_wejsciowa):
    """
    Zwraca zmienną słownikową o następującej strukturze:
    {
        'imie': ...,
        'nazwisko': ...,
        'wiek': ...,
        'adres': {
            'kod pocztowy': ...,
            'miasto': ...,
            'ulica': ...,
            'numer domu': ...,
        }
    }
    Z odpowiednimi wartościami z argumentu list_input.

    argumenty:
        lista_wejsciowa: lista, o poniższej strukturze:
          [imię, nazwisko, wiek, ulica, miasto, kod pocztowy, numer mieszkania]
    """
    zwracany_slownik = {
        'imie': None,
        'nazwisko': None,
        'wiek': None,
        'adres': {
            'kod pocztowy': None,
            'miasto': None,
            'ulica': None,
            'numer domu': None,
        }
    }

    zwracany_slownik['imie'] = lista_wejsciowa[0]
    zwracany_slownik['nazwisko'] = lista_wejsciowa[1]
    zwracany_slownik['wiek'] = lista_wejsciowa[2]
    zwracany_slownik['adres']['kod pocztowy'] = lista_wejsciowa[5]
    zwracany_slownik['adres']['miasto'] = lista_wejsciowa[4]
    zwracany_slownik['adres']['ulica'] = lista_wejsciowa[3]
    zwracany_slownik['adres']['numer domu'] = lista_wejsciowa[6]

    return zwracany_slownik

def wypisz_uzywajac_kluczy(lista_rekordow):
    """
    Wypisz listę rekordów używając klucza słownika.
    """
    for rekord in lista_rekordow:
        for klucz in rekord:
            print(klucz, ':', rekord[klucz])

def wypisz_uproszczony(lista_rekordow):
    """
    Wypisz listę rekordów.
    """
    for rekord in lista_rekordow:
        print("Imie: ", rekord['imie'])
        print("Nazwisko: ", rekord['nazwisko'])
        print("Adres: ul. ", rekord['adres']['ulica'], ' ',
            rekord['adres']['numer domu'],", ",
            rekord['adres']['kod pocztowy'], ' ',
            rekord['adres']['miasto'], sep='')


if __name__ == '__main__':

    uzytkownik1 = ['Mateusz',
                   'Krainski',
                   25,
                   'Strzelecka',
                   'Gdańsk',
                   '76-250',
                   '5/9']

    uzytkownik2 = ['John',
                   'Doe',
                   98,
                   'Gdańska',
                   'Warszawa',
                   '01-111',
                   '1']

    uzytkownik3 = ['Jane',
                   'Doe',
                   11,
                   'Warszawska',
                   'Kraków',
                   '02-222',
                   '2']

    uzytkownik4 = ['Unnamed',
                   'User',
                   1,
                   'Krakowska',
                   'Poznań',
                   '03-444',
                   '3']

    ksiazka_adresowa = []

    ksiazka_adresowa.append(konwertuj(uzytkownik1))
    ksiazka_adresowa.append(konwertuj(uzytkownik2))
    ksiazka_adresowa.append(konwertuj(uzytkownik3))
    ksiazka_adresowa.append(konwertuj(uzytkownik4))

    wypisz_uproszczony(ksiazka_adresowa)
    wypisz_uzywajac_kluczy(ksiazka_adresowa)
