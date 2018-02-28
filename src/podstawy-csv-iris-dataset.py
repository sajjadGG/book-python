import csv


FILENAME = 'ml-iris-dataset.csv'

with open(FILENAME) as file:
    fieldnames = [
        'sepal_length',
        'sepal_width',
        'petal_length',
        'petal_width',
        'species',
    ]
    dane = csv.DictReader(file, fieldnames=fieldnames)

    for row in dane:
        print(row)