import logging

logging.basicConfig(
        level=logging.WARNING,
        format='[%(asctime).19s] [%(levelname)s] %(message)s',
)

log = logging.getLogger(__name__)

# logging.critical('Błąd Krytyczny')
# logging.error('Bład')
# logging.warning('Uwaga')
# logging.info('Informacja')
# logging.debug('Debug')


logging.warning('Rozpoczynam program')

logging.info('Teraz będzie sekcja odnośnie wyświeltnia napisów')


def wyswietlanie_napisow(tekst):
    wynik = (tekst + ', ') * 5
    logging.debug('Zmienne lokalne: %s' % locals())
    logging.info('wynik: %s' % wynik)
    logging.debug('Wychodzę z funkcji')
    return wynik


wyswietlanie_napisow('Hello Wold')

logging.warning('Kończę program')


def asd():
    import warnings
    warnings.warn('Uważaj, z tego już nie korzystaj', PendingDeprecationWarning)


asd()
