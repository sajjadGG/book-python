import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

#lista = [3, 1, 2]
#lista.sort()
#sorted(lista)
#print(lista)


def _foo():
    """
    >>> _foo()
    10
    """
    return 10


def foo(a, b=None, *args, **kwargs):
    print(locals())


def run():
    print(__name__)


#if __name__ == '__main__':
#    foo(10, b=12, c=30)


a = range(0, 30)
liczby = list(a)

#print(__file__)


#ciag = input('Podaj wartosc: ')

#log.info('Ciag znakow usera: "%s"', ciag)
#print(ciag, ciag)


pow(2, 10)
2 ** 10

print(divmod(10, 6))