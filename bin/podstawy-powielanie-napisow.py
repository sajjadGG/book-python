#!/usr/bin/env python3

"""
Zadanie 1:
Napisz program, który wczyta od użytkownika pewien napis,
a następnie wyświetli 30 kopii tego napisu, każda w osobnej linii.

Zadanie 2:
Napisz trzy wersje tego programu:

- wykorzystując range()
- wykorzystując pętlę while
- wykorzystując właściwości mnożenia stringów

Zadanie 3:
- Napisz doctest do takiej funkcji.

Podpowiedź:
- print('ciag znakow' * 30)
"""

#!/usr/bin/env python3

ciag_znakow = input('Podaj ciag znakow: ')


print('Rozwiazanie 1')
for i in range(0, 30):
    print(ciag_znakow)


print('Rozwiazanie 2')
i = 0
while i < 30:
    print(ciag_znakow)
    i = i + 1

print('Rozwiazanie 3')
print((ciag_znakow + '\n') * 30)

print('Alternatywnie')
print('%s\n' % ciag_znakow * 30)

print('Alternatywnie 2')
tekst = '{napis}\n'.format(napis=ciag_znakow)
print(tekst * 30)

