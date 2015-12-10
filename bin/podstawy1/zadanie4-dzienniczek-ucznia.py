#!/usr/bin/env python3

import statistics


LISTA_DOPUSZCZALNYCH_OCEN = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]

dzienniczek_ucznia = []


while True:
    wpis = input('Podaj co dostał uczeń: ')

    if not wpis or not float(wpis) in LISTA_DOPUSZCZALNYCH_OCEN:
        break
    else:
        dzienniczek_ucznia.append(float(wpis))


print('Lista uzyskanych ocen: ')
print(dzienniczek_ucznia)

srednia1 = sum(dzienniczek_ucznia) / len(dzienniczek_ucznia)
srednia2 = statistics.mean(dzienniczek_ucznia)

print(srednia1)
print(srednia2)