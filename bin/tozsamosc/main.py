import logging
import pesel2 as pesel

logging.basicConfig(level=logging.CRITICAL)
logging.getLogger('pesel2').setLevel(level=logging.DEBUG)
log = logging.getLogger(__name__)


wprowadzony = input('Podaj pesel: ')

if pesel.poprawny_pesel(wprowadzony):
    log.info('Pesel jest poprawny')
else:
    log.error('Pesel nie jest poprawny')


if pesel.czy_kobieta(wprowadzony):
    log.info('Kobieta')
else:
    log.info('Mężczyzna')