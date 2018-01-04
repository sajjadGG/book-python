import csv
import json
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger('ksiazka-adresowa')


log.debug('Tworzymy książkę adresową')
ADDRESS_BOOK = [{
    'imie': 'Matt',
    'nazwisko': 'Harasymczuk',
    'telefon': '+48 781 111 743',
    'ulica': 'Białobrzeska',
    'miasto': 'Warszawa',
    'kod_pocztowy': '02-370',
    'wojewodztwo': 'Mazowieckie',
    'panstwo': 'Polska',
}]


with open('/_tmp/ksiazka-adresowa.json', 'w') as file:
    log.debug('Zapisujemy ksiażkę w formacie JSON')
    file.write(json.dumps(ADDRESS_BOOK))


with open('/_tmp/ksiazka-adresowa.csv', 'w') as file:
    log.debug('Zapisujemy książkę w formacie CSV')
    writer = csv.DictWriter(file, quoting=csv.QUOTE_ALL, fieldnames=sorted(ADDRESS_BOOK[0].keys()))
    writer.writeheader()

    for row in ADDRESS_BOOK:
        writer.writerow(row)
