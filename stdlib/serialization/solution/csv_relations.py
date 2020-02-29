import csv

output = r'../../_tmp/csv_relations.csv'


class Astronaut:
    def __init__(self, first_name, last_name, experience=()):
        self.name = first_name
        self.last_name = last_name
        self.experience = list(experience)

class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


CREW = [
    Astronaut('Jan Twardowski', experience=(
        Mission(1969, 'Apollo 11'),
        Mission(2024, 'Artemis 3'))),

    Astronaut('Mark Watney', experience=(
        Mission(2035, 'Ares 3'))),

    Astronaut('Melissa Lewis'),
]

output = []

for contact in CREW:
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


with open(output, mode='w', encoding='utf-8') as file:

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
