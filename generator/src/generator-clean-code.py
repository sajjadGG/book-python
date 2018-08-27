osoba = {'username': 'Ivan Иванович', 'czy_wykladowca': True}


def asd(x):
    return x.replace('a', 'b')


out = {
    wartosc: asd()
    for klucz, wartosc in osoba.items()
    if klucz == 'username'
}
