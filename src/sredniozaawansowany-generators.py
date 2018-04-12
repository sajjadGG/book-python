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

FILENAME = '../data/file-etc-passwd.txt'


def systemowe_lista(lines):
    konta = []

    for linia in lines:

        if not linia.isspace() and not linia.startswith('#'):
            uid = int(linia.split(':')[2])
            username = str(linia.split(':')[0])

            if uid < 1000:
                konta.append(username)

    return konta


def systemowe_generator(lines):
    for linia in lines:

        if not linia.isspace() and not linia.startswith('#'):
            uid = int(linia.split(':')[2])
            username = str(linia.split(':')[0])

            if uid < 1000:
                yield username


if __name__ == '__main__':
    with open(FILENAME) as file:
        lines = file.readlines()
        lista = systemowe_lista(lines)
        generator = systemowe_generator(lines)

    print('Lista:', sys.getsizeof(lista))
    print('Generator:', sys.getsizeof(generator))
