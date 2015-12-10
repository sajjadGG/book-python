import csv

FILENAME = '/tmp/ksiazka-adresowa.csv'

ADDRESS_BOOK = [
    {'imie': 'Matt',
    'nazwisko': 'Harasymczuk',
    'ulica': 'Westpad',
    'miasto': 'Katwijk aan Zee',
    'kod_pocztowy': '2224',
    'wojewodztwo': 'Zuid-Holland',
    'panstwo': 'Netherlands'},

    {'imie': 'Angelika',
    'nazwisko': 'Jan',
    'ulica': 'Bial',
    'miasto': 'Warszawa',
    'kod_pocztowy': '02-370',
    'wojewodztwo': 'Mazowieckie',
    'panstwo': 'Polska'},
]


with open(FILENAME, 'w') as file:
    fieldnames = sorted(ADDRESS_BOOK[0].keys())
    writer = csv.DictWriter(file, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL, delimiter=';')
    writer.writeheader()

    for kontakt in ADDRESS_BOOK:
        writer.writerow(kontakt)


with open(FILENAME) as file:
    content = file.read()
    print(content)