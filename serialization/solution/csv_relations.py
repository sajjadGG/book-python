import csv

OUTPUT = r'../../_tmp/csv_relations.csv'

class Contact:
    def __init__(self, first_name, last_name, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses


class Address:
    def __init__(self, location, city):
        self.location = location
        self.city = city


INPUT = [
    Contact(first_name='Jan', last_name='Twardowski', addresses=(
        Address(location='JSC', city='Houston, TX'),
        Address(location='KSC', city='Merritt Island, FL'),
        Address(location='JPL', city='Pasadena, CA'),
    )),
    Contact(first_name='Mark', last_name='Watney'),
    Contact(first_name='Melissa', last_name='Lewis', addresses=()),
]

output = []

for contact in INPUT:
    addresses = []

    for address in contact.addresses:
        dane = address.__dict__.values()
        address = ', '.join([str(x) for x in dane])
        addresses.append(address)

    contact_data = contact.__dict__
    contact_data['addresses'] = '; '.join(addresses)
    output.append(contact_data)


fieldnames = set()

for contact in output:
    for field_name in contact.keys():
        fieldnames.add(field_name)


with open(OUTPUT, mode='w', encoding='utf-8') as file:

    writer = csv.DictWriter(
        f=file,
        fieldnames=sorted(fieldnames, reverse=True),
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in output:
        writer.writerow(row)
