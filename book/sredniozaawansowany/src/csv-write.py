import csv

DATA = [
    {'first_name': 'José', 'last_name': 'Jiménez'},
    {'first_name': 'Max', 'last_name': 'Peck'},
    {'first_name': 'Ivan', 'last_name': 'Ivanovic'},
]

with open('filename.csv', 'w', encoding='utf-8') as file:
    fieldnames = DATA[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writeheader()

    for row in DATA:
        writer.writerow(row)