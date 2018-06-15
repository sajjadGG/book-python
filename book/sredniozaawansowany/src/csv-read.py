import csv

FILENAME = r'filename.csv'
# "first_name", "last_name"
# "Jose", "Jimenez"
# "Max", "Peck"
# "Ivan", "Ivanovic"


with open(FILENAME) as file:
    data = csv.DictReader(file, delimiter=',', quotechar='"')

    for row in data:
        print(row['first_name'], row['last_name'])
