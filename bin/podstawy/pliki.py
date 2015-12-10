#!/usr/bin/env python3

with open('/tmp/tymczasowy', 'w') as file:
    file.write('adsasdas')


with open('/etc/passwd') as file:
    zawartosc = file.readlines()


for linia in zawartosc:
    if linia.startswith('root'):
        opis = linia.split(':')
        print(opis[4])


print(zawartosc[11:13])
