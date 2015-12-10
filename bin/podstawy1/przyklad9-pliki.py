
FILENAME = '/tmp/plik-tymczasowy-read-write.txt'
#FILENAME = '/etc/hosts'
#FILENAME = 'C:/Windows/System32/drivers/etc/hosts'


with open(FILENAME) as file:
    tekst = file.read()
    print(tekst)


with open(FILENAME, 'a') as file:
    file.write('Ehlo World!')


with open(FILENAME) as file:
    tekst = file.readlines()
    print(tekst)

