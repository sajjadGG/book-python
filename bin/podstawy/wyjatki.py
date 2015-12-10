import sys

"""
def zawartosc_pliku(nazwa_pliku):
    with open(nazwa_pliku) as file:
        return file.readlines()

print(zawartosc_pliku('/etc/passwd'))

try:
    print(zawartosc_pliku('/etc/nieistnijacy_plik'))
except FileNotFoundError:
    print('Nie ma takiego pliku')
"""
"""
ciag_uzytkownika = input('Wpisz cokolwiek: ')


try:
    liczba = int(float(ciag_uzytkownika))
except ValueError:
    print('Wpisałeś ciąg znaków, który nie można zamienić na liczbę')
    sys.exit(1)

print(liczba)
"""


class PlikJestPustyError(Exception):
    def __init__(self, error):
        print('asdasdasdasdasd')


with open('/tmp/tymczasowy', 'w') as file:
    file.write('')


def zawartosc_pliku(nazwa_pliku):
    with open(nazwa_pliku) as file:
        zawatosc = file.readlines()
        if zawatosc:
            return zawatosc
        else:
            raise PlikJestPustyError('Plik jest pusty')

            # print(zawartosc_pliku('/tmp/tymczasowy'))
            # print(siema)
