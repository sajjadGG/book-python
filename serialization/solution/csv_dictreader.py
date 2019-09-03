import csv


FILE = r'../data/iris-clean.csv'
FIELDNAMES = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species',
]


with open(FILE) as file:
    data = csv.DictReader(
        f=file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quoting=csv.QUOTE_NONE)

    next(data)

    for row in data:
        print(dict(row))
