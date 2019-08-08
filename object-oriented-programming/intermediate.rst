.. _OOP Intermediate:

****************
OOP Intermediate
****************


Initial arguments mutability and shared state
=============================================

.. _Initial arguments mutability and shared state:

Bad
---
.. literalinclude:: src/oop-init-shared-state-bad.py
    :language: python
    :caption: Initial arguments mutability and shared state

Good
----
.. literalinclude:: src/oop-init-shared-state-good.py
    :language: python
    :caption: Initial arguments mutability and shared state


Relations
=========
.. code-block:: python

    class Address:
        def __init__(self, street=None, city=None, country=None):
            self.street = street
            self.city = city
            self.country = country


    class Contact:
        def __init__(self, first_name, last_name, addresses=()):
            self.first_name = first_name
            self.last_name = last_name
            self.address = addresses


    twardowski = Contact(first_name='Jan', last_name='Twardowski', address=[
        Address(street='Kamienica Pod św. Janem Kapistranem', city='Kraków', country='Poland'),
        Address(street='2101 E NASA Pkwy', city='Houston', country='USA'),
        Address(city='Kennedy Space Center', country='USA'),
    ])


Assignments
===========

Defining Classes
----------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/intermediate_iris.py`
* Input data: :numref:`listing-oop-classes`

.. code-block:: python
    :caption: Iris sample dataset
    :name: listing-oop-classes

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
        (7.1, 3.0, 5.9, 2.1, 'virginica'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.0, 3.6, 1.4, 0.3, 'setosa'),
        (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        (6.5, 3.0, 5.8, 2.2, 'virginica'),
        (6.5, 2.8, 4.6, 1.5, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (6.9, 3.1, 4.9, 1.5, 'versicolor'),
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]

#. Stwórz ``flowers: list``
#. Stwórz klasy ``Virginica``, ``Versicolor``, ``Setosa``, które będą identyczne do ``Iris``
#. Iterując po ``DATA`` z :numref:`listing-oop-classes`:

    #. Twórz obiekty klasy odpowiedniej dla nazwy gatunku (ostatni rekord każdej z krotek)
    #. Obiekt inicjalizuj danymi z pomiarów
    #. Obiekt dodaj do listy ``flowers``

#. Na ekranie wyświetlaj nazwę gatunku oraz sumę i średnią z pomiarów.

:Dla chętnych:
    #. Wynik sformatuj aby wyglądał jak tabelka:

        .. code-block:: text

            Species    Total   Avg
            ----------------------
             virginica  15.5  3.88
                setosa  10.2  2.55
            versicolor  13.9  3.48
             virginica  16.6  4.15
            versicolor  15.6  3.90
                setosa   9.4  2.35
            versicolor  16.3  4.07
             virginica  19.3  4.83
                setosa   9.5  2.38
                setosa   9.4  2.35

Basic Address Book
------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/intermediate_addressbook.py`

#. Dla danych z listingu poniżej napisz książkę adresową

    .. literalinclude:: assignment/oop_addressbook.json
        :language: json
        :caption: Address Book

#. W zadaniu mamy do czynienia z trzema klasami, wymień je.
#. Zamodeluj problem wykorzystując trzy klasy i relacje między nimi
#. Użytkownik może mieć wiele adresów
#. Użytkownik może nie mieć żadnego adresu

:The whys and wherefores:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na ``str`` oraz jego reprezentacja (które i kiedy użyć)

Address Book from API
---------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/intermediate_addressbook_api.py`

#. API programu powinno być tak jak na :numref:`listing-oop-addressbook-py`
#. Zrób tak, aby się ładnie wyświetlało zarówno dla jednego wyniku jak i dla wszystkich w książce
#. ``Address`` ma mieć zmienną liczbę argumentów

:The whys and wherefores:
    * Korzystanie z ``.__str__()``

.. literalinclude:: assignment/oop_addressbook.py
    :name: listing-oop-addressbook-py
    :language: python
    :caption: Address Book

Dragon (version beta)
---------------------
* Complexity level: medium
* Lines of code to write: 120 lines
* Estimated time of completion: 30 min (±10 min), then 30 min live coding with instructor
* Filename: :download:`solution/intermediate_dragon.py`
* Warning: Don't delete code, assignment will be continued

.. figure:: img/dragon.gif
    :scale: 100%
    :align: center

    Firkraag dragon from game Baldur's Gate II: Shadows of Amn

#. Zaimportuj smoka z poprzedniej części zadania ("Part 1")
#. Wykorzystaj mechanizm dziedziczenia dla Smoka
#. Nie modyfikuj klasy smoka z poprzedniej części
#. Smok nie może wyjść poza obszar ekranu (1024x768) + napisz ``doctest``
#. Jeżeli dojdzie do granicy ekranu, to przesuwając dalej, pozycja będzie ustawiona na maks
#. Zmień smokowi punkty życia na losowy ``int`` z zakresu 100 do 150
#. Stwórz bohatera "Jan Twardowski":

    * losowe punkty życia (200-250)
    * zadaje losowe obrażenia (1-15)
    * klasa postaci (domyślnie "Warrior")
    * Bohater może przyjmować obrażenia
    * Bohater może zginąć
    * Bohater może poruszać się po planszy

#. Wszystkie istoty mają statusy:

    * "Full Health" - gdy punkty życia 100% (zastąp status "alive")
    * "Injured" - gdy punkty życia 99% - 75%
    * "Badly Wounded" - gdy punkty życia 74% - 25%
    * "Near Death" - gdy punkty życia 24% - 1%
    * "Dead" - gdy punkty życia poniżej lub równe 0%

#. Bohater przejmuje złoto smoka, jeżeli go zabije
#. Przeprowadź walkę, tak długo aż ktoś pierwszy nie zginie
#. Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić

:Hint:
    * Aby zaimportować trzeba najpierw w katalogu stworzyć pusty plik ``__init__.py``
