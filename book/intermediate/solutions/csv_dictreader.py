import csv


FILENAME = '../data/csv-iris-dataset.csv'
FIELDNAMES = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species',
]

with open(FILENAME, encoding='utf-8') as file:
    data = csv.DictReader(
        file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quotechar='"')

    for row in list(data)[1:]:
        print(row)
