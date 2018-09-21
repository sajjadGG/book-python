**************
Comprehensions
**************


* Pętla ``for`` może być także napisana jako jednoliniowy generator
* List comprehension :numref:`Generators`

Simple usage
============
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
================
* Do takiego iteratora można także dodać instrukcję warunkową.

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
============================
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
==========================
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
====================================
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


Assignments
===========

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
