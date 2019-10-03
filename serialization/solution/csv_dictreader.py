from csv import DictReader, QUOTE_NONE


FILE = r'../data/iris.csv'
FIELDNAMES = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species',
]


with open(FILE) as file:
    header, *data = DictReader(file,
        f=file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quoting=QUOTE_NONE)

    for row in data:
        print(dict(row))
