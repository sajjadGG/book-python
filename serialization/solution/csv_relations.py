import csv


class Contact:
    def __init__(self, first_name, last_name, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.addresses}'

    def __repr__(self):
        return self.__str__()


class Address:
    def __init__(self, **kwargs):
        self.street = kwargs.get('street', None)
        self.city = kwargs.get('city', None)

    def __str__(self):
        return f'{self.street} {self.city}'

    def __repr__(self):
        return self.__str__()


addressbook = [
    Contact(first_name='Jan', last_name='Twardowski', addresses=[
        Address(street='2101 E NASA Pkwy', city='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Address(street=None, city='Kennedy Space Center', kod='32899', panstwo='USA'),
        Address(street='4800 Oak Grove Dr', city='Pasadena', kod='91109', panstwo='USA'),
        Address(street='2825 E Ave P', city='Palmdale', stan='California', kod='93550', panstwo='USA', data_urodzenia=None),
    ]),
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
]

do_zapisu = []

for kontakt in ksiazka_adresowa:
    adresy = []

    for adres in kontakt.adresy:
        dane = adres.__dict__.values()
        adres = '|'.join([str(x) for x in dane])
        adresy.append(adres)

    dane_kontaktu = kontakt.__dict__
    dane_kontaktu['adresy'] = ';'.join(adresy)
    do_zapisu.append(dane_kontaktu)


with open('filename.csv', 'w', encoding='utf-8') as file:
    fieldnames = set()
    for kontakt in do_zapisu:
        for fieldname in kontakt.keys():
            fieldnames.add(fieldname)


    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL,
                            lineterminator='\n')
    writer.writeheader()

    for row in do_zapisu:
        writer.writerow(row)
