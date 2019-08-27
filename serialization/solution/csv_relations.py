import csv


class Contact:
    def __init__(self, name, addresses=()):
        self.name = name
        self.addresses = addresses


class Address:
    def __init__(self, center, location):
        self.center = center
        self.location = location


DATA = [
    Contact(name='Jan Twardowski', addresses=(
        Address(center='JSC', location='Houston, TX'),
        Address(center='KSC', location='Merritt Island, FL'),
        Address(center='JPL', location='Pasadena, CA'),
    )),
    Contact(name='Mark Watney'),
    Contact(name='Melissa Lewis', addresses=()),
]

output = []

for contact in DATA:
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
