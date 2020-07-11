from csv import DictReader, QUOTE_NONE


FILE = r'/tmp/iris.csv'

FIELDNAMES = [
    'Sepal Length',
    'Sepal Width',
    'Petal Length',
    'Petal Width',
    'Species',
]

with open(FILE) as file:
    header = file.readline()

    data = DictReader(
        f=file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quoting=QUOTE_NONE)

    for row in data:
        print(row)
