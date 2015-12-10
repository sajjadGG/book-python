import csv

zawartosc = []

with open('/etc/passwd') as file:
    for linia in file.readlines():
        if not linia.startswith('#'):
            zawartosc.append(linia)

with open('/tmp/tymczasowy.csv', 'w') as file:
    plik = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for linia in zawartosc:
        plik.writerow(linia.split(':'))

with open('/tmp/tymczasowy.csv') as file:
    print(file.read())
