"""
Napisz program, który wczyta od użytkownika pewien napis, a następnie wyświetli 30 kopii tego napisu, każda w osobnej linii.

Napisz trzy wersje tego programu:

* wykorzystując range()
* wykorzystując pętlę while
* wykorzystując właściwości mnożenia stringów

Napisz doctest do takiej funkcji.
"""


def kopie_napisu_1(napis):
    """
    >>> kopie_napisu_1('Hello World')
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    Hello World
    """
    for _ in range(30):
        print(napis)


def kopie_napisu_2(napis):
    i = 0
    while i < 30:
        print(napis)
        i += 1


def kopie_napisu_3(napis):
    print(('\n' + napis) * 30)


def kopie_napisu_4(napis):
    ciag_znakow = '\n%s' % napis
    print(ciag_znakow * 30)


def kopie_napisu_5(napis):
    ciag_znakow = '\n{}'.format(napis)
    print(ciag_znakow * 30)


def kopie_napisu_6(napis):
    ciag_znakow = '\n' + napis
    print(ciag_znakow * 30)


# kopie_napisu_1('Hello World')
# kopie_napisu_2('Hello World')
# kopie_napisu_3('Hello World')
# kopie_napisu_4('Hello World')
# kopie_napisu_5('Hello World')
kopie_napisu_6('Hello World')
