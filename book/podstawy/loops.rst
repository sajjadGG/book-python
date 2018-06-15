*****
Pętle
*****

Pętle służą do wykonywania tego samego fragmentu kodu wielokrotnie. W Pythonie, pętle wykonywane są na obiektach wieloelementowych, albo iteratorach.

Pętla ``for``
=============

Iterowanie po wartościach prostych
----------------------------------
Pętla ``for`` wykonuje się na zestawie elementów. Dosłownie można tę instrukcję przeczytać jako "Dla iksów będących wartościami listy, wykonaj instrukcję:"

.. code-block:: python

    for x in [1, 3, 4]:
        print(x)
        # 1
        # 3
        # 4

.. code-block:: python

    for x in 'Max Peck':
        print(x)
        # M
        # a
        # x
        #
        # P
        # e
        # c
        # k

Iterowanie po wartościach złożonych
-----------------------------------
.. code-block:: python

    >>> for x in ['Max', 3, 'Peck', 2.8, ['1.0', 'José', 'Jiménez']]:
    ...    print(f'Value is: {x}')
    Value is: Max
    Value is: 3
    Value is: Peck
    Value is: 2.8
    Value is: ['1.0', 'José', 'Jiménez']

.. code-block:: python

    >>> for element in ['Max', 3, 'Peck',  ['1.0', 'José', 'Jiménez']]:
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
    Value is: 2.8
    Value is: 1
    Value is: .
    Value is
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

    for x in range(start=0, stop=10, step=2):
        print(x)
        # 0
        # 2
        # 4
        # 6
        # 8

.. code-block:: python

    for element in [(0,0), (1,1), (2,2)]:
        print(element)
        # (0, 0)
        # (1, 1)
        # (2, 2)

.. code-block:: python

    a, b = 1, 2
    a, b = (1, 2)
    key, value = (1, 2)

    for key, value in [(0,0), (1,1), (2,2)]:
        print(f'{key} -> {value}')
        # 0 -> 0
        # 1 -> 1
        # 2 -> 2

.. code-block:: python

    DATABASE = [
        (0, 1),
        ('name', 'José'),
        ('locations', ['CapeCanaveral', 'Houston']),
    ]

    for key, value in DATABASE:
        print(f'{key} -> {value}')
        # 0 -> 1
        # 'name' -> 'José'
        # 'locations' -> ['CapeCanaveral', 'Houston']


.. code-block:: python

    my_dict = {'x': 1, 'y': 2}

    for element in my_dict.values():
        print(element)
        # 1
        # 2

    for element in my_dict.keys():
        print(element)
        # 'x'
        # 'y'

    # for domyślnie iteruje po kluczach w ``dict``
    for element in my_dict:
        print(element)
        # 'x'
        # 'y'

    for key, value in my_dict.items():
        print(key, value)
        # 'x', 1
        # 'y', 2

.. code-block:: python

    slownik = {'x': 1, 'y': 2}

    # dobieranie sie do wartosci ``dict`` za pomoca klucza
    for element in slownik:
        slownik.get(element))
        slownik[element]
        # '1'
        # '2'


Pętla ``while``
===============
Pętla while wykonuje się dopóki argument jest prawdą.

.. code-block:: python

    x = 0

    while x <= 10:
        print(x)
        x += 1

.. code-block:: python

    while True:
        pass

Słowa kluczowe w pętlach
========================
* ``break`` - powoduje przerwanie pętli.
* ``continue`` - powoduje przerwanie aktualnie wykonywanej iteracji.

.. code-block:: python

    while True:
        number = input('Type number: ')

        if number:
            break

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

    float_list = [float(x) for x in range(0, 10)]
    even_list = [float(x) for x in range(0, 10) if x % 2 == 0]

.. code-block:: python

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    parzyste = [float(x) for x in range(0, 10) if is_even(x)]

.. code-block:: python

    def is_even(number):
        if cyfra % 2 == 0:
            return {'number': number, 'status': 'even'}
        else:
            return {'number': number, 'status': 'odd'}

    [is_even(x) for x in range(0, 5)]
    # [
    #    {'number': 0, 'status': 'even'},
    #    {'number': 1, 'status': 'odd'},
    #    {'number': 2, 'status': 'even'},
    #    {'number': 3, 'status': 'odd'},
    #    {'number': 4, 'status': 'even'},
    # ]

Porównanie z pętlą ``for``
--------------------------
Przykład praktyczny z życia

.. code-block:: python

    line = 'jose:x:1000:1000:José Jiménez:/home/jose:/bin/bash'

    paths = []
    for record in line.split(':'):
        if record.startswith('/'):
            paths.append(record)
    print(paths)
    # ['/home/jose', '/bin/bash']

.. code-block:: python

    [record for record in line.split(':') if record.startswith('/')]
    # ['/home/jose', '/bin/bash']

.. code-block:: python

    # this is how you might find this in real world
    [x for x in line.split(':') if x.startswith('/')]
    # ['/home/jose', '/bin/bash']

Inline ``for`` to nie tylko lista
---------------------------------
.. code-block:: python

    {pow(x) for x in range(0, 5)}
    # set {1, 2, 4, 9, 16}

    {x: pow(x) for x in range(0, 5)}
    # dict {1:1, 2:4, 3:9, 4:16}

    {pow(x): x for x in range(0, 5)}
    # dict {1:1, 4:2, 9:3, 16:4}

.. code-block:: python

    my_dict = {'x': 1, 'y': 2}

    {value: key for key, value in my_dict.items()}
    # dict {1:'x', 2:'y'}

    {v:k for k,v in my_dict.items()}
    # dict {1:'x', 2:'y'}

Zadania kontrolne
=================

Dzienniczek ucznia
------------------
#. Przekonwertuj skalę ocen ``(2, 3, 3.5, 4, 4.5, 5)`` na listę ``float`` za pomocą inline ``for`
#. Użytkownik podaje oceny jako ``int`` lub ``float``
#. Program ma sprawdzać czy ocena znajduje się w skali ocen
#. Jeżeli ocena jest na liście dopuszczalnych ocen, dodaje ją do dzienniczka
#. Jeżeli wpisano cyfrę nie znjadującą się na liście dopuszczalnych ocen, wyświetl informację "Grade is not allowed" i dalej kontunuuj wpisywanie
#. Wyświetla wyliczoną dla dzienniczka ocen średnią arytmetyczną
#. Jeżeli wciśnięto sam Enter, oznacza to koniec wpisywania do dzienniczka

:Założenia:
    * Nazwa pliku: ``loops-report-card.py``
    * Linii kodu do napisania: około 10 linie
    * Maksymalny czas na zadanie: 15 min

:Podpowiedź:
    * Czytelny kod powinien mieć około 10 linii
    * ``len()``, ``sum()``

:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * korzystanie z pętli oraz instrukcji wychodzących
    * konwersja typów i rzutowanie
    * sprawdzanie czy obiekt jest instancją klasy
