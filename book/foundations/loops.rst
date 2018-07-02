*****
Loops
*****

Pętle służą do wykonywania tego samego fragmentu kodu wielokrotnie.
W Pythonie, pętle wykonywane są na obiektach wieloelementowych, albo iteratorach.


``while``
=========
* Pętla ``while`` wykonuje się dopóki argument jest prawdą.

.. code-block:: python

    while True:
        pass


.. code-block:: python

    x = 0

    while x <= 10:
        print(x)
        x += 1


``for``
=======

Iterating simple types
----------------------
Pętla ``for`` wykonuje się na zestawie elementów. Dosłownie można tę instrukcję przeczytać jako "Dla iksów będących wartościami listy, wykonaj instrukcję:"

.. code-block:: python

    for x in [1, 3, 4]:
        print(x)
        # 1
        # 3
        # 4

.. code-block:: python

    for x in 'Hello':
        print(x)
        # H
        # e
        # l
        # l
        # o

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

Iterating over ``dict`` items
-----------------------------
.. code-block:: python

    DATA = [('a', 0), ('b', 1), ('c', 2)]

    for element in DATA:
        print(element)
        # ('a', 0)
        # ('b', 1)
        # ('c', 2)

.. code-block:: python

    a, b = 1, 2
    a, b = (1, 2)
    key, value = (1, 2)

.. code-block:: python

    DATA = [('a', 0), ('b', 1), ('c', 2)]

    for key, value in DATA:
        print(f'{key} -> {value}')
        # a -> 0
        # b -> 1
        # c -> 2

.. code-block:: python

    DATA = [
        (0, 1),
        ('name', 'José'),
        ('locations', ['CapeCanaveral', 'Houston']),
    ]

    for key, value in DATA:
        print(f'{key} -> {value}')
        # 0 -> 1
        # name -> José
        # locations -> ['CapeCanaveral', 'Houston']

.. code-block:: python

    DATA = {'x': 1, 'y': 2}

    for element in DATA.values():
        print(element)
        # 1
        # 2

    for element in DATA.keys():
        print(element)
        # 'x'
        # 'y'

    # for domyślnie iteruje po kluczach w ``dict``
    for element in DATA:
        print(element)
        # 'x'
        # 'y'

    for key, value in DATA.items():
        print(key, value)
        # 'x', 1
        # 'y', 2

.. code-block:: python

    DATA = {'x': 1, 'y': 2}

    # accessing ``dict`` items with key
    for element in DATA:
        DATA.get(element))
        DATA[element]
        # '1'
        # '2'

Iterating complex types
-----------------------
.. code-block:: python

    DATA = ['Max', 3, 2.8, ['1.0', 'José']]

    for x in DATA:
        print(f'Value is: {x}')

    # Value is: Max
    # Value is: 3
    # Value is: 2.8
    # Value is: ['1.0', 'José']

.. code-block:: python

    DATA = ['Max', 3, 2.8, ['1.0', 'José']]

    for first_level_element in DATA:
        for second_level_element in first_level_element:
            print(f'Value is: {second_level_element}')

    # Value is: M
    # Value is: a
    # Value is: x
    # TypeError: 'int' object is not iterable


.. code-block:: python

    DATA = ['Max', 3, 2.8, ['1.0', 'José']]

    for first_level_element in DATA:
        if isinstance(first_level_element, (list, set, tuple)):
            for second_level_element in first_level_element:
                print(f'Value is: {second_level_element}')
        else:
            print(f'Value is: {first_level_element}')

    # Value is: Max
    # Value is: 3
    # Value is: Peck
    # Value is: 2.8
    # Value is: 1.0
    # Value is: José

Inline ``for``
==============
* Pętla ``for`` może być także napisana jako jednoliniowy generator
* List comprehension :numref:`Generators`

Simple usage
------------
.. code-block:: python

    cyfry = [x for x in range(0, 10)]
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

.. code-block:: python

    cyfry = []

    for x in range(0, 10):
        cyfry.append(x)

    print(cyfry)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Conditional loop
----------------
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

Applying function to element
----------------------------
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

``for`` vs. ``inline for``
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

Inline ``for`` not only for ``list``
------------------------------------
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


Keywords in loops
=================
* ``break`` - powoduje przerwanie pętli.
* ``continue`` - powoduje przerwanie aktualnie wykonywanej iteracji.

.. code-block:: python

    while True:
        number = input('Type number: ')

        if number:
            break


Assignments
===========

Report card
-----------
#. Przekonwertuj skalę ocen ``(2, 3, 3.5, 4, 4.5, 5)`` na listę ``float`` za pomocą inline ``for``
#. Użytkownik podaje oceny jako ``int`` lub ``float``
#. Program ma sprawdzać czy ocena znajduje się w skali ocen
#. Jeżeli ocena jest na liście dopuszczalnych ocen, dodaje ją do dzienniczka
#. Jeżeli wpisano cyfrę nie znajdującą się na liście dopuszczalnych ocen, wyświetl informację "Grade is not allowed" i dalej kontynuuj wpisywanie
#. Jeżeli wciśnięto sam Enter, oznacza to koniec wpisywania do dzienniczka
#. Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną z ocen

:Założenia:
    * Nazwa pliku: ``loops_report_card.py``
    * Szacunkowa długość kodu: około 15 linii
    * Maksymalny czas na zadanie: 10 min

:Co zadanie sprawdza?:
    * wczytywanie ciągu znaków od użytkownika
    * weryfikacja ciągu wprowadzonego od użytkownika
    * korzystanie z pętli oraz instrukcji wychodzących
    * konwersja typów i rzutowanie
    * sprawdzanie czy obiekt jest instancją klasy

:Podpowiedź:
    * ``len()``, ``sum()``

Label encoder
-------------
#. Mając do dyspozycji zbiór danych Irysów z :numref:`listing-data-structures-iris-sample`
#. Stwórz słownik gatunków, gdzie kolejnym liczbom naturalnym zaczynając od zera przyporządkuj gatunek irysów
#. Przygotuj listę cech (``labels``) z kluczami ze słownika gatunków

.. code-block:: python

    print(species)
    # {0: 'I. versicolor', 1: 'I. virginica', 2: 'I. setosa'}

    print(labels)
    # [0, 1, 2, 1, 1, 0, ...]

:Założenia:
    * Nazwa pliku: ``loops_label_encoder.py``
    * Szacunkowa długość kodu: około 13 linii
    * Maksymalny czas na zadanie: 15 min

:Podpowiedź:
    - ``from random import shuffle``

.. literalinclude:: src/data-structures-iris-sample.py
    :name: listing-data-structures-iris-sample
    :language: python
    :caption: Sample Iris databases
