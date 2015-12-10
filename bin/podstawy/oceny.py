"""
Napisz program, który wczytuje od użytkownika kolejne oceny i:

* sprawdza czy wprowadzona ocena jest na liście dopuszczalnych na wydziale ocen
* jeżeli ocena jest na liście dopuszczalnych na wydziale ocen, dodaje ją na listę otrzymanych ocen
* jeżeli wciśnięto sam Enter, oznacza to koniec listy otrzymanych ocen
* wyświetla wyliczoną dla listy otrzymanych ocen średnią arytmetyczną.
"""

DOPUSZCZALNE_OCENY = [1, 2, 3, 4, 5, 6]
otrzymane_oceny = list()


while True:
    wpisana_ocena = input('Wpisz ocenę: ')

    try:
        wpisana_ocena = int(wpisana_ocena)
    except ValueError:
        if wpisana_ocena:
            print('Wpisana ocena "{}" nie jest cyfrą całkowitą.'.format(wpisana_ocena))
            continue
        else:
            break

    if wpisana_ocena in DOPUSZCZALNE_OCENY:
        otrzymane_oceny.append(wpisana_ocena)
    else:
        print('Ocena nie znajduje się na liście dopuszczalnych ocen: ', DOPUSZCZALNE_OCENY)
        continue


suma = sum(otrzymane_oceny)
ilosc_ocen = len(otrzymane_oceny)
srednia = suma / ilosc_ocen


print(srednia)
