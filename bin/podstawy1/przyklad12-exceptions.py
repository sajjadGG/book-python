import logging

FILENAME = '/etc/hosts'
#FILENAME = 'C:/Windows/System32/drivers/etc/hosts'


logging.basicConfig(
    level=logging.DEBUG,
    filename='/tmp/%s.log' % __name__,
    format='[%(asctime).19s] [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)



class DoesNotExistsError(ArithmeticError):
    strerror = 'asdasdasd'
    errno = 10


def ctg(deg):

    if deg == 90:
        raise DoesNotExistsError

    return None



log.info('Rozpoczynam program')

try:

    log.debug('Próbuję odczytać plik')

    with open(FILENAME, 'w') as file:
        content = file.read()
        print(content)

    log.debug('Plik odczytany i zamknięty')

except PermissionError as e:
    log.error(e)
    print(e.strerror)

except OSError as e:
    log.error(e)
    print(e.strerror)

except Exception as e:
    log.error(e)
    print(e.strerror)

else:
    print('Operacje na pliku zakończyły się powodzeniem')

finally:
    log.debug('Zakończenie pracy nad plikiem')

log.info('Kończymy program')


student = {'imie': 'Matt', 'nazwisko': 'H'}
print(student)

for ocena in student['oceny']:
    print(ocena)

for ocena in student.get('oceny'):
    print(ocena)

for ocena in student.get('oceny', []):
    print(ocena)

try:
    oceny = student['oceny']
except KeyError:
    student['oceny'] = []
    oceny = []

print(oceny)
print(student)