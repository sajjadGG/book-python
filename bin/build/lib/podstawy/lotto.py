#!/usr/bin/env python3

import random


MAKSYMALNA = 49
MINIMALNA = 1
ILOSC_LOSOWAN = 6

wylosowane = []


while len(wylosowane) <= ILOSC_LOSOWAN:
    liczba = random.randrange(MINIMALNA, MAKSYMALNA)

    if liczba not in wylosowane:
        wylosowane.append(liczba)

print(sorted(wylosowane))




wylosowane = random.sample(range(MINIMALNA, MAKSYMALNA), ILOSC_LOSOWAN)
print(wylosowane)