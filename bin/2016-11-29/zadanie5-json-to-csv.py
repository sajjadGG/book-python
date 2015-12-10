#!/usr/bin/env python3

import csv
import json

flat_data = []
fieldnames = {'source'}


def make_key(key, k):
    if 'timestamp' in k:
        return 'timestamp'
    elif key in k:
        return k
    else:
        return '{}_{}'.format(key, k)


with open('../../tmp/fixtures-flat.json') as file:
    content = file.read()


for key, value in json.loads(content).items():
    for element in value:
        slownik = {}
        for k, wartosc in element.items():
            klucz = make_key(key, k)
            fieldnames.add(klucz)
            slownik['source'] = key
            slownik[klucz] = wartosc

        flat_data.append(slownik)


with open('../tmp/fixtures-flat.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames, quoting=csv.QUOTE_ALL, delimiter=';', quotechar='"')
    writer.writeheader()

    for row in flat_data:
        writer.writerow(row)


with open('../tmp/fixtures-flat.csv') as file:
    print(file.read())
