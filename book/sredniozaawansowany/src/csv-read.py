import csv

with open('filename.csv') as file:
    data = csv.DictReader(file, delimiter=',', quotechar='"')

    for row in data:
        print(row['first_name'], row['last_name'])
