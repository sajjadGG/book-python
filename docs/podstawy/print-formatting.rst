****************
Print formatting
****************

Konkatanacja stringów
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
