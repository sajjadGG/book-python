****************
Print formatting
****************

Konkatenacja stringów
=====================

Operator ``+``
--------------

.. code-block:: python

    imie = 'Matt'
    print('Cześć ' + imie + '!')

Wykorzystanie parametrów funkcji ``print()``
--------------------------------------------

.. code-block:: python

    imie = 'Matt'
    print('Cześć ', imie, '!')


Interpolacja zmiennych
======================

Operator: ``%s``, ``%d``, ``%f``
--------------------------------

* kolejnościowe
* nazwane
* typy: ``string``, ``int``, ``float``
* operatory na stringu

.. code-block:: python

    imie = 'Piotr'
    wiek = 18

    def get_imie(imie):
        return imie

    print('Cześć %s!' % imie)

    print("%s ma %s lat" % (imie, wiek))
    print('%s ma %s lat' % (wiek, imie))
    print('%s ma %10.1f lat' % (imie, wiek))
    print('%s ma %.1f lat' % (imie, wiek))
    print('%s ma %d lat' % (get_imie(imie), wiek))

    print('%(imie)s ma %(wiek)d lat' % {
        'wiek': wiek,
        'imie': imie,
    })

    print('Hej, mam na imię %(imie)s.' % locals())


Metoda ``.format()``
====================

* ``string``
* ``int``
* ``float``
* operatory na stringu
* jako parametry do ``print("string", **args)``

.. code-block:: python

    imie = 'Piotr'
    wiek = 18

    print('{imie} ma {wiek} lat'.format(
            imie=imie,
            wiek=wiek))

    print('{wiek} ma {imie} lat'.format(**locals()))

    print('Hej mam na imie {} i mam {} lat'.format(imie, wiek))

    >>> print('Hej mam na imie {0} i mam {1} lat'.format(imie, wiek))
    Hej mam na imie Piotr i mam 10 lat

    >>> print('Hej mam na imie {1} i mam {0} lat'.format(imie, wiek))
    Hej mam na imie 10 i mam Piotr lat

    >>> print('Hej mam na imie {1:.3} i mam {0:.3} lat'.format(float(wiek), imie))
    Hej mam na imie Pio i mam 10.0 lat

    >>> print('Hej mam na imie {1:.3} i mam {0:10.3} lat'.format(float(wiek), imie))
    Hej mam na imie Pio i mam       10.0 lat


f-strings - Python >= 3.6
=========================

* ``f'{variable}'``
* ``f'{self.field}'``
* ``f'{datetime:%Y-%m-%d %H:%M}'``

.. code-block:: python

    import datetime

    imie = 'Piotr'
    wiek = 18


    def get_imie(imie):
        return imie

    print(f'Hej {imie}')
    print(f'Hej {get_imie()}, masz: {wiek} lat')


    print(f'dzis jest: {datetime.datetime.now():%Y-%m-%d %H:%M}')

    now = datetime.datetime.now
    print(f'dzis jest: {now():%Y-%m-%d %H:%M}')


Przykład z życia
================

.. warning:: Kod podatny jest na SQL Injection. W praktyce skorzystaj z funkcji ``prepare``.

.. code-block:: python

    sql_query = f"""

        SELECT id, username, email
        FROM users
        WHERE 'username' = '{username}'
        AND 'password' = '{password}'

    """


Więcej informacji
=================

* https://pyformat.info - Formatowanie stringów w Python


``pprint``
==========

.. code-block:: python

    from pprint import pprint

    data = [
       {'first_name': 'Baked', 'last_name': 'Beans'},
       {'first_name': 'Lovely', 'last_name': 'Spam'},
       {'first_name': 'Wonderful', 'last_name': 'Spam'}
    ]

    pprint(data)


Zadania kontrolne
=================

Powielanie napisów
------------------

:Zadanie 1:
    Napisz program, który wczyta od użytkownika pewien napis, a następnie wyświetli 5 kopii tego napisu, każda w osobnej linii.

:Zadanie 2:
    Napisz trzy wersje tego programu:

    * wykorzystując ``range()``
    * wykorzystując pętlę ``while``
    * wykorzystując właściwości mnożenia stringów ``print('ciag znakow' * 5)``

:Zadanie 3:
    Napisz doctest do takiej funkcji.

Przeliczanie temperatury
------------------------

:Zadanie 1:
    Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita. Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni). Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze. Oczywiście napisz testy do rozwiązania.

:Zadanie 2:
    Zrób aby znak plus lub minus był zawsze wyświetlany.

:Zadanie *:
    Zrób aby tabelka była stałej szerokości.

:Podpowiedź:
    * Fahrenheit to Celsius: (°F - 32) / 1.8 = °C
    * Celsius to Fahrenheit: (°C * 1.8) + 32 = °F
    * skorzystaj z funkcji ``range()``
