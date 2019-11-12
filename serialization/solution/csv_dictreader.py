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
    header = file.readline()
    data = DictReader(
        f=file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quoting=QUOTE_NONE)

    for row in data:
        print(dict(row))


# with open(FILE) as file:
#     header, *data = DictReader(
#         f=file,
#         fieldnames=FIELDNAMES,
#         delimiter=',',
#         quoting=QUOTE_NONE)
#
#     for row in data:
#         print(dict(row))
