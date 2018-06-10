#!/usr/bin/env python3


def konwersja_odleglosci(metry: int) -> dict:
    km = int(metry / 1000)
    mile = float(metry / 1608)
    nm = float(metry / 1852)

    return {
        'kilometers': km,
        'miles': mile,
        'nautical miles': nm,
        'all': [km, mile, nm]
    }


print(konwersja_odleglosci(100))
print(konwersja_odleglosci(6000))