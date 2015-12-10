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

