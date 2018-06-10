#!/usr/bin/env python3


def konwersja_odleglosci(metry):
    km = int(metry / 1000)
    mile = float(metry / 1608)
    nm = float(metry / 1852)

    return {
        'kilometers': km,
        'miles': mile,
        'nautical miles': nm,
        'all': [km, mile, nm]
    }
