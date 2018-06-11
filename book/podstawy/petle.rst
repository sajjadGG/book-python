.. _Pętle:

*****
Pętle
*****

Pętle służą do wykonywania tego samego fragmentu kodu wielokrotnie. W Pythonie, pętle wykonywane są na obiektach wieloelementowych, albo iteratorach.

Pętla ``for``
=============

Pętla ``for`` wykonuje się na zestawie elementów. Dosłownie można tę instrukcję przeczytać jako "Dla iksów będących wartościami listy, wykonaj instrukcję:"

.. code-block:: python

    for x in [1, 3, 4, 2]:
        print(f'Value is: {x}')


.. code-block:: python

    >>> for x in ['Max', 3, 'Peck', 2.8, [1, 'José', 'Jiménez']]:
    ...    print(f'Value is: {x}')
    Value is: Max
    Value is: 3
    Value is: Peck
    Value is: 2.8
    Value is: [1, 'José', 'Jiménez']

.. code-block:: python

    >>> for element in ['Max', '3', 'Peck', '2.8', [1, 'José', 'Jiménez']]:
    ...    for e in element:
    ...        print(f'Value is: {e}')
    Value is: M
    Value is: a
    Value is: x
    Value is: 3
    Value is: P
    Value is: e
    Value is: c
    Value is: k
    Value is: 2
    Value is: .
    Value is: 8
    Value is: 1
    Value is: José
    Value is: Jiménez

.. code-block:: python

    >>> for x in ['Max', 3, 'Peck', 2.8, [1, 'José', 'Jiménez']]:
    ...    if isinstance(x, list):
    ...        for element in x:
    ...            print(f'Value is: {element}')
    ...    else:
    ...        print(f'Value is: {x}')
    Value is: Max
    Value is: 3
    Value is: Peck
    Value is: 2.8
    Value is: 1
    Value is: José
    Value is: Jiménez

.. code-block:: python

    >>> for x in range(0, 5):
    >>>     print(f'Value is: {x}')
    Value is: 0
    Value is: 1
    Value is: 2
    Value is: 3
    Value is: 4

.. code-block:: python

    >>> for x in range(0, 30, 5):
    ...    print(f'Value is: {x}')

    Value is: 0
    Value is: 5
    Value is: 10
    Value is: 15
    Value is: 20
    Value is: 25

.. code-block:: python

    for key, value in [(0, 0), (1, 1), (1, 2)]:
        print(f'{key} -> {value}')

.. code-block:: python

    slownik = {'x': 1, 'y': 2}

    for element in slownik.keys():
        print(element)

    for element in slownik.values():
        print(element)

    for element in slownik:
        # for domyślnie iteruje po kluczach
        print(element)

    for key, value in slownik.items():
        print(key, value)

.. code-block:: python

    slownik = {'x': 1, 'y': 2}
    for element in slownik:

        # dobieranie sie do wartosci slownika za pomoca klucza
        print(slownik.get(element))
        print(slownik[element])

        # get zwraca wartość w słowniku dla klucza
        {'x': 1, 'y': 2}[element]
        {'x': 1, 'y': 2}.get(element)

Pętla ``while``
===============
Pętla while wykonuje się dopóki argument jest prawdą.

.. code-block:: python

    x = 0

    while x <= 10:
        print(f'Value is: {x}')
        x = x + 1

.. code-block:: python

    while True:
        number = input('Type number: ')

        if number:
            break


Słowa kluczowe w pętlach
========================
* ``break`` - powoduje przerwanie pętli.
* ``continue`` - powoduje przerwanie aktualnie wykonywanej iteracji.


Inline ``for``
==============
Pętla ``for`` może być także napisana jako jednoliniowy generator.

Prosty przykład
---------------
.. code-block:: python

    cyfry = [x for x in range(0, 10)]
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

.. code-block:: python

    cyfry = []
    for x in range(0, 10):
        cyfry.append(x)

    print(cyfry)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Instrukcja warunkowa
--------------------
Do takiego iteratora można także dodać instrukcję warunkową.

.. code-block:: python

    parzyste = [x for x in range(0, 10) if x % 2 == 0]
    parzyste = [x for x in range(0, 10) if not x % 2]
    # [0, 2, 4, 6, 8]

.. code-block:: python

    cyfry = []
    for x in range(0, 10):
        if x % 2 == 0:
            cyfry.append(x)

    print(cyfry)
    # [0, 2, 4, 6, 8]

Aplikowanie funkcji dla elementu
--------------------------------
Najczęściej wykorzystuje się tą konstrukcję aby zaaplikować funkcję dla każdego elementu nowej listy

.. code-block:: python

    floaty = [float(x) for x in range(0, 10)]
    parzyste = [float(x) for x in range(0, 10) if x % 2 == 0]

.. code-block:: python

    def czy_parzysta(cyfra):
        if cyfra % 2 == 0:
            czy_parzysta = True
        else:
            czy_parzysta = False
        return {'cyfra': cyfra, 'czy_parzysta': czy_parzysta}

    parzyste = [czy_parzysta(x) for x in range(0, 10)]

    [
        {'cyfra': 0, 'czy_parzysta': True},
        {'cyfra': 1, 'czy_parzysta': False},
        {'cyfra': 2, 'czy_parzysta': True},
        {'cyfra': 3, 'czy_parzysta': False},
        {'cyfra': 4, 'czy_parzysta': True},
        {'cyfra': 5, 'czy_parzysta': False},
        {'cyfra': 6, 'czy_parzysta': True},
        {'cyfra': 7, 'czy_parzysta': False},
        {'cyfra': 8, 'czy_parzysta': True},
        {'cyfra': 9, 'czy_parzysta': False}
     ]

Porównanie z pętlą ``for``
--------------------------
Przykład praktyczny z życia

.. code-block:: python

    line = 'jose:x:1000:1000:José Jiménez:/home/jose:/bin/bash'

    paths = []
    for record in line.split(':'):
        if record.startswith('/'):
            paths.append()
    print(paths)
    # ['/home/jose', '/bin/bash']

.. code-block:: python

    paths = [record for record in line.split(':') if record.startswith('/')]
    print(paths)
    # ['/home/jose', '/bin/bash']

.. code-block:: python

    # this is how you might find this in real world
    paths = [x for x in line.split(':') if x.startswith('/')]
    print(paths)
    # ['/home/jose', '/bin/bash']


Inline ``for`` to nie tylko lista
---------------------------------
.. code-block:: python

    {float(x) for x in range(0, 5)}
    # set {1.0, 2.0, 3.0, 4.0}

    {x: float(x) for x in range(0, 5)}
    # dict {1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0}

Zadania kontrolne
=================

Dzienniczek ucznia
------------------
#. Użytkownik podaje oceny jako ``int`` lub ``float``
#. Program ma sprawdzać czy ocena znajduje się w skali ocen ``(2, 3, 3.5, 4, 4.5, 5)``
#. Jeżeli ocena jest na liście dopuszczalnych ocen, dodaje ją do dzienniczka
#. Jeżeli wpisano cyfrę nie znjadującą się na liście dopuszczalnych ocen, wyświetl informację "Niepoprawna ocena" i dalej kontunuuj wpisywanie
#. Wyświetla wyliczoną dla dzienniczka ocen średnią arytmetyczną
#. Jeżeli wciśnięto sam Enter, oznacza to koniec wpisywania do dzienniczka

:Podpowiedź:
    * Czytelny kod powinien mieć około 10 linii
    * dla ułatwienia wszystkie oceny na skali mogą być typu ``float``
    * ``len()``, ``sum()``

:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * korzystanie z pętli oraz instrukcji wychodzących
    * konwersja typów i rzutowanie
    * sprawdzanie czy obiekt jest instancją klasy
