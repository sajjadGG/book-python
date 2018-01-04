#!/usr/bin/env python3


def odleglosci(metry):
    return {
        'kilometry': int(metry / 1000),
        'mile lądowe': float(metry / 1608),
        'mile morskie': float(metry / 1852),
    }

wynik = odleglosci(1000)
print(wynik)
