import csv

FILENAME = r'filename.csv'
DATA = [
    {'first_name': 'José', 'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Ivan', 'last_name': 'Ivanovic'},
]


with open(FILENAME, mode='w', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=['first_name', 'last_name'],
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in DATA:
        writer.writerow(row)
