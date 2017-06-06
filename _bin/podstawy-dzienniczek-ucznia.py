#!/usr/bin/env python3

import logging
import statistics


LISTA_DOPUSZALNYCH_OCEN = [2, 3, 3.5, 4, 4.5, 5]
dzienniczek = []

log = logging.getLogger(__name__)


while True:
    try:
        wprowadzona_ocena = float(input('Wprowadź ocenę: '))
    except ValueError:
        break

    if wprowadzona_ocena not in LISTA_DOPUSZALNYCH_OCEN:
        log.critical('Wprowadzono nieprawidłową ocenę', wprowadzona_ocena)
        break
    else:
        dzienniczek.append(wprowadzona_ocena)


suma = sum(dzienniczek)
ilosc = len(dzienniczek)
srednia = suma / ilosc

print(dzienniczek)
print(srednia)

srednia = statistics.mean(dzienniczek)
print(srednia)
