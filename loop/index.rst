.. _Loops:

*****
Loops
*****


``while``
=========
* Continue execution when argument is ``True``

.. code-block:: python

    while True:
        pass

.. code-block:: python

    i = 0

    while i <= 10:
        print(x)
        i += 1


``for``
=======

Iterating simple types
----------------------
.. code-block:: python

    for number in range(0, 5):
        print(f'Value is: {number}')

    # Value is: 0
    # Value is: 1
    # Value is: 2
    # Value is: 3
    # Value is: 4

.. code-block:: python

    for number in range(0, 10, 2):
        print(number)

    # 0
    # 2
    # 4
    # 6
    # 8

.. code-block:: python

    for character in 'Hello':
        print(character)

    # H
    # e
    # l
    # l
    # o

.. code-block:: python

    for element in [1, 3, 4]:
        print(element)

    # 1
    # 3
    # 4

Iterating over nested ``list`` items
------------------------------------
.. code-block:: python

    DATA = [
        ('a', 0),
        ('b', 1),
        ('c', 2),
    ]

    for element in DATA:
        print(element)

    # ('a', 0)
    # ('b', 1)
    # ('c', 2)

.. code-block:: python

    a, b = 'a', 0
    a, b = ('a', 0)
    key, value = ('a', 0)

.. code-block:: python

    DATA = [
        ('a', 0),
        ('b', 1),
        ('c', 2),
    ]

    for key, value in DATA:
        print(f'key: "{key}", value: "{value}"')

    # key: "a", value: "0"
    # key: "b", value: "1"
    # key: "c", value: "2"

.. code-block:: python

    DATA = [
        (0, 1),
        ('name', 'José'),
        ('locations', ['CapeCanaveral', 'Houston']),
    ]

    for key, value in DATA:
        print(f'key: "{key}", value: "{value}"')

    # key: "0",         value: "1"
    # key: "name",      value: "José"
    # key: "locations", value: "['CapeCanaveral', 'Houston']"

``enumerate()``
---------------
.. code-block:: python

    DATA = [
        ('a', 0),
        ('b', 1),
        ('c', 2),
    ]

    for index, element in enumerate(DATA):
        print(f'index: "{index}", element: "{element}"')

    # index: "0", element: "('a', 0)"
    # index: "1", element: "('b', 1)"
    # index: "2", element: "('c', 2)"


Iterating over ``dict`` items
-----------------------------
.. code-block:: python

    DATA = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
    }

    for element in DATA.values():
        print(element)

    # 'José'
    # 'Jiménez'
    # 42

.. code-block:: python

    DATA = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
    }

    for element in DATA.keys():
        print(element)

    # 'first_name'
    # 'last_name'
    # 'age'

.. code-block:: python

    DATA = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
    }

    # for domyślnie iteruje po kluczach w ``dict``
    for element in DATA:
        print(element)

    # 'first_name'
    # 'last_name'
    # 'age'

.. code-block:: python

    DATA = {
        'first_name': 'José',
        'last_name': 'Jiménez',
        'age': 42,
    }

    for key, value in DATA.items():
        print(f'key: "{key}", value: "{value}"')

    # key: "first_name", value: "José"
    # key: "last_name",  value: "Jiménez"
    # key: "age",        value: "42"

Iterating complex types
-----------------------
* flatmap

.. code-block:: python

    DATA = ['Max', ('1.0', 'José'), 3, 2.8, {True, None, False}]

    for element in DATA:
        print(f'value: "{element}"')

    # value: "Max"
    # value: "('1.0', 'José')"
    # value: "3"
    # value: "2.8"
    # value: "{False, True, None}"

.. code-block:: python

    DATA = ['Max', ('1.0', 'José'), 3, 2.8, {True, None, False}]

    for element in DATA:
        for sub in element:
            print(f'value: "{sub}"')

    # value: "M"
    # value: "a"
    # value: "x"
    # value: "1.0"
    # value: "José"
    # TypeError: 'int' object is not iterable


.. code-block:: python

    DATA = ['Max', ('1.0', 'José'), 3, 2.8, {True, None, False}]

    for element in DATA:

        if isinstance(element, (list, set, tuple)):
            for sub in element:
                print(f'value: "{sub}"')
        else:
            print(f'value: "{element}"')

    # value: "Max"
    # value: "1.0"
    # value: "José"
    # value: "3"
    # value: "2.8"
    # value: "False"
    # value: "True"
    # value: "None"


Inline ``for``
==============
* Pętla ``for`` może być także napisana jako jednoliniowy generator
* List comprehension :numref:`Generators`

Simple usage
------------
.. code-block:: python

    numbers = [x for x in range(0, 10)]
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

.. code-block:: python

    numbers = []

    for x in range(0, 10):
        numbers.append(x)

    print(numbers)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Conditional loop
----------------
Do takiego iteratora można także dodać instrukcję warunkową.

.. code-block:: python

    even_numbers = [x for x in range(0, 10) if x % 2 == 0]
    # [0, 2, 4, 6, 8]

.. code-block:: python

    even_numbers = []

    for x in range(0, 10):
        if x % 2 == 0:
            even_numbers.append(x)

    print(even_numbers)
    # [0, 2, 4, 6, 8]

Applying function to element
----------------------------
Najczęściej wykorzystuje się tą konstrukcję aby zaaplikować funkcję dla każdego elementu nowej listy

.. code-block:: python

    [float(x) for x in range(0, 10)]
    [float(x) for x in range(0, 10) if x % 2 == 0]

.. code-block:: python

    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    parzyste = [float(x) for x in range(0, 10) if is_even(x)]
    # [0.0, 2.0, 4.0, 6.0, 8.0]

.. code-block:: python

    def describe(number):
        if number % 2 == 0:
            return {'number': number, 'status': 'even'}
        else:
            return {'number': number, 'status': 'odd'}

    [describe(x) for x in range(0, 5)]
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

    [x for x in line.split(':') if x.startswith('/')]
    # ['/home/jose', '/bin/bash']

Inline ``for`` not only for ``list``
------------------------------------
.. code-block:: python

    {x**2 for x in range(0, 5)}
    # set {0, 1, 4, 9, 16}

    {x: x**2 for x in range(0, 5)}
    # dict {0:0, 1:1, 2:4, 3:9, 4:16}

    {x**2: x for x in range(0, 5)}
    # dict {0:0, 1:1, 4:2, 9:3, 16:4}

    {x**2: x**3 for x in range(0, 5)}
    # dict {0:0, 1:1, 4:8, 9:27, 16:64}

.. code-block:: python

    my_dict = {'x': 1, 'y': 2}

    {value: key for key, value in my_dict.items()}
    # dict {1:'x', 2:'y'}

    {v:k for k,v in my_dict.items()}
    # dict {1:'x', 2:'y'}


Keywords in loops
=================

``break`` - exits loop
----------------------
.. code-block:: python

    while True:
        number = input('Type number: ')

        # if user hit enter, without typing number
        if not number:
            break

``continue`` - skips iteration
------------------------------
.. code-block:: python

    for i in range(0, 10):
        if i % 2 == 0:
            continue

        print(i)

    # 1
    # 3
    # 5
    # 7
    # 9


Assignments
===========

Text manipulation
-----------------
#. Dany jest tekst "Lorem Ipsum"
#. Dla każdego zdania (zdania oddzielone są kropkami)
#. Za pomocą funkcji ``len()`` policz ile jest wyrazów::

    We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win

:About:
    * Filename: ``loop_sentences.py``
    * Lines of code to write: 4 lines
    * Estimated time of completion: 5 min

:Co zadanie sprawdza:
    * Dzielenie stringów
    * Sprawdzanie długości ciągów znaków
    * Iterowanie po elementach listy

Unique keys from schema-less database
-------------------------------------
#. Mając bazę danych z listingu poniżej
#. Wygeneruj listę unikalnych kluczy dictów

.. code-block:: python

    DATABASE = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Max', 'last_name': 'Peck'},
        {'first_name': 'Иван', 'age': 42},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
        {'first_name': 'José', 'born': 1961, 'agency': 'NASA'},
    ]

:Algorithm:
    #. Iteruj po rekordach w bazie danych
    #. Z rekordu wyciągnij klucze
    #. Dodaj klucze do zbioru
    #. Usuń duplikaty w zbiorze

:About:
    * Filename: ``loop_unique_keys.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Generowanie zbiorów
    * Usuwanie powtarzających się elementów
    * Wyciąganie elementów ze słownika
    * Iterowanie po słowniku
    * Aktualizacja zbiorów

Report card
-----------
#. Przekonwertuj skalę ocen ``(2, 3, 3.5, 4, 4.5, 5)`` na listę ``float`` za pomocą inline ``for``
#. Użytkownik podaje oceny jako ``int`` lub ``float``
#. Jeżeli ocena jest na liście dopuszczalnych ocen, dodaje ją do dzienniczka
#. Jeżeli wciśnięto sam Enter, oznacza to koniec wpisywania do dzienniczka
#. Jeżeli wpisano cyfrę nie znajdującą się na liście dopuszczalnych ocen, wyświetl informację "Grade is not allowed" i dalej kontynuuj wpisywanie
#. Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną z ocen

:About:
    * Filename: ``loop_report_card.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Wczytywanie ciągu znaków od użytkownika
    * Generowanie struktur danych i konwersja typów
    * Weryfikacja ciągu wprowadzonego od użytkownika
    * Korzystanie z pętli oraz instrukcji wychodzących
    * Konwersja typów i rzutowanie
    * Sprawdzanie czy obiekt jest instancją klasy
    * Wykorzystanie funkcji wbudowanych

:Hints:
    * ``average = sum(...) / len(...)``

Label encoder
-------------
#. Mając do dyspozycji zbiór danych Irysów z :numref:`listing-loops-iris-sample`
#. Ze zbioru wyodrębnij dane odrzucając nagłówek.
#. Przemieszaj elementy zbioru danych
#. Stwórz słownik gatunków ``species``, gdzie kolejnym liczbom naturalnym zaczynając od zera przyporządkuj gatunek irysów.
#. Klucze muszą być wygenerowane na podstawie kolejności występowania gatunków w przemieszanym zbiorze danych:

    .. code-block:: python

        species = {
            0: 'versicolor',
            1: 'virginica',
            2: 'setosa'
        }

#. Przygotuj listę cech (``labels``) z kluczami ze słownika gatunków.
#. Etykiety muszą być wygenerowane na podstawie kolejności w przemieszanym zbiorze danych:

    .. code-block:: python

        print(labels)
        # [0, 1, 2, 1, 1, 0, ...]

#. Wyświetl na ekranie ``species`` oraz ``labels``

:Algorithm:
    #. Wyodrębnij dane odrzucając nagłówek
    #. Przemieszaj elementy zbioru danych
    #. Stwórz słownik gatunków ``species``
    #. Iteruj po elementach zbioru danych
    #. Gatunek to ostatni element rekordu
    #. Jeżeli w słowniku nie ma gatunku, to dodaj go z kolejnym numerem
    #. Do listy label dodawaj wartość słownika gatunków dla gatunku w tym rekordzie
    #. Odwróć słownik gatunków
    #. Wyświetl na ekranie ``species`` oraz ``labels``

:About:
    * Filename: ``loop_label_encoder.py``
    * Lines of code to write: 13 lines
    * Estimated time of completion: 15 min

:The whys and wherefores:
    * Sprawdzanie występowania elementów w słowniku
    * Generowanie słownika i listy na podstawie innych danych
    * Odwracanie słownika

:Hints:
    * ``from random import shuffle``

.. literalinclude:: src/loops-iris-sample.py
    :name: listing-loops-iris-sample
    :language: python
    :caption: Sample Iris databases
