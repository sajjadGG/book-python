from csv import DictWriter, QUOTE_ALL


FILENAME = r'../../_tmp/dictwriter_fixed.csv'
DATA = [
    {'first_name': 'Jan', 'last_name': 'Twardowski'},
    {'first_name': 'Jose', 'last_name': 'Jimenez'},
    {'first_name': 'Mark', 'last_name': 'Watney'},
    {'first_name': 'Ivan', 'last_name': 'Ivanovic'},
    {'first_name': 'Melissa', 'last_name': 'Lewis'},
]


with open(FILENAME, mode='w', encoding='utf-8') as file:
    writer = DictWriter(
        f=file,
        fieldnames=['first_name', 'last_name'],
        delimiter=';',
        quotechar='"',
        quoting=QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in DATA:
        writer.writerow(row)
