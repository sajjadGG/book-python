import csv

FILE = r'../../_tmp/csv_relations.csv'


class Astronaut:
    def __init__(self, firstname, lastname, experience=()):
        self.name = firstname
        self.lastname = lastname
        self.experience = list(experience)

class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


CREW = [
    Astronaut('Jan', 'Twardowski', experience=(
        Mission(1969, 'Apollo 11'),
        Mission(2024, 'Artemis 3'))),

    Astronaut('Mark', 'Watney', experience=(
        Mission(2035, 'Ares 3'))),

    Astronaut('Melissa', 'Lewis'),
]

result = []

for astronaut in CREW:
    experience = []

    for mission in astronaut.experience:
        exp = ', '.join([str(x) for x in astro.__dict__.values()])
        experience.append(exp)

    astro = astronaut.__dict__
    astro['experience'] = '; '.join(experience)
    result.append(astro)


fieldnames = set()

for contact in result:
    for field_name in contact.keys():
        fieldnames.add(field_name)


with open(FILE, mode='w', encoding='utf-8') as file:

    writer = csv.DictWriter(
        f=file,
        fieldnames=sorted(fieldnames, reverse=True),
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in result:
        writer.writerow(row)
