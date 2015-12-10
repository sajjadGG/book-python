import sys

"""
9.2. Generatory vs. Przetwarzanie Listy

Napisz program, który wczyta plik /etc/passwd, a następnie:

* przefiltruje linie, tak aby nie zawierały komentarzy (zaczynające się od #)
* przefiltruje linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
* zwróci listę loginów takich użytkowników
* Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję.
* Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe yield.
* Porównaj wyniki jednego i drugiego rozwiązania przez użycie sys.getsizeof()

"""

def konta_systemowe(filename):
    konta = []

    with open(filename) as file:
        for linia in file.readlines():

            if not linia.startswith('#'):
                uid = int(linia.split(':')[2])
                username = str(linia.split(':')[0])

                if uid < 1000:
                    konta.append(username)

    return konta


def system_accounts1(filename):
    with open(filename) as file:

        for linia in file.readlines():

            if not linia.startswith('#'):
                uid = int(linia.split(':')[2])
                username = str(linia.split(':')[0])

                if uid < 1000:
                    yield username


def system_accounts2(filename):
    with open(filename) as file:
        #content = (line.split(':') for line in file.readlines() if not line.startswith('#'))

        for line in (line for line in file.readlines() if not line.startswith('#')):
            fields = line.split(':')
            uid = int(fields[2])
            username = fields[0]

            if uid < 1000:
                yield username


if __name__ == '__main__':
    z_returna = konta_systemowe('/etc/passwd')
    z_yielda1 = system_accounts1('/etc/passwd')
    z_yielda2 = system_accounts2('/etc/passwd')

    print('Z Returna:', sys.getsizeof(z_returna))
    print('Z Yielda:', sys.getsizeof(z_yielda1))
    print('Z Yielda:', sys.getsizeof(z_yielda2))
