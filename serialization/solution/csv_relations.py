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

output = []

for contact in addressbook:
    addresses = []

    for address in contact.addresses:
        dane = address.__dict__.values()
        address = '|'.join([str(x) for x in dane])
        addresses.append(address)

    contact_data = contact.__dict__
    contact_data['addresses'] = ';'.join(addresses)
    output.append(contact_data)


with open('filename.csv', 'w', encoding='utf-8') as file:
    fieldnames = set()

    for contact in output:
        for field_name in contact.keys():
            fieldnames.add(field_name)

    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writeheader()

    for row in output:
        writer.writerow(row)
