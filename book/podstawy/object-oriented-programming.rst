.. _Object Oriented Programming:

***********************
Programowanie obiektowe
***********************

Paradygmat Obiektowy
====================
W programowaniu istnieje kilka popularnych paradygmatów (idei programowania), są to między innymi:

    * imperatywny,
    * deklaratywny,
    * funkcjonalny,
    * proceduralny,
    * obiektowy.

Paradygm imperatywny oznacza, że używane są instrukcje, które zmieniają stan programu. Lista poleceń do wypełnienia przez komputer. Przykładami języków imperatywnych są C++, Python, Java i wiele innych. Paradygm deklaratwny pozwala budować programy opisując pożądany efekt zamiast kolejnych procedur, przykładem takiego języka jest HTML, w którym opisujemy jak ma strona wyglądać, nie wgłębiając się w to jak ten efekt zostanie osiągnięty. Paradygmat funcjonalny oznacza, że wykorzystywane są jedynie funkcje, które zawsze zwracają tą samą wartość dla tych samych argumentów. Nacisk jest wtedy kładziony na matematyczny opis funkcji. Jedną z istotnych zalet tego paradygmatu jest możliwość matematycznego udowodnienia skuteczności programu. Paradygmat proceduralny polega na tym, że program wykonuje listę procedur, które to procedury są zgrupowane w byty, które można nazwać funkcjami. W tym przypadku nie jest to jendak funkcja matematyczna (jak w przypadku paradygmatu funkcjonalnego), a lista poleceń i komend.

Paradygmat obiektowy polega na tym, że program manipuluje złożonymi obiektami, z których każdy ma swój własny stan i ten stan można modyfikować metodami przypisanymi do tego obiektu. Paradygmat obiektówy pozwala pisać bardzo przejrzysty kod i zrozumiały kod.

Syntax
======

Classes and Objects
-------------------
.. literalinclude:: src/oop-class.py
    :language: python
    :caption: Classes and Objects

Static Fields
-------------
.. literalinclude:: src/oop-fields-static.py
    :language: python
    :caption: Static Fields

Dynamic Fields
--------------
.. literalinclude:: src/oop-fields-static.py
    :language: python
    :caption: Dynamic fields

Static vs. Dynamic Fields
-------------------------
.. literalinclude:: src/oop-fields-static-vs-dynamic.py
    :language: python
    :caption: Static vs. Dynamic fields

Methods
-------
.. literalinclude:: src/oop-methods-noarg.py
    :language: python
    :caption: Methods

.. literalinclude:: src/oop-methods-arg.py
    :language: python
    :caption: Methods

``self``
--------
.. literalinclude:: src/oop-methods-self.py
    :language: python
    :caption: Methods

``__init__()`` - Initalizer Method
----------------------------------
* Domyślny init gdy niezdefiniowaliśmy własnego
* ``__init__()`` to nie konstruktor

.. literalinclude:: src/oop-methods-self.py
    :language: python
    :caption: ``__init__()`` - Initalizer Method

Callable
--------
.. code-block:: python

    int()
    10()

Inferencja typów
----------------
* Static Typing (Java, C++, Swift)

.. code-block:: java

    String name = new String("Jose Jimenez")
    name = new String()  # type inferece

* Dynamic Typing (Python, PHP, Ruby)

.. code-block:: python

    name: str = str('Jose Jimenez')  # Type annotations
    name = str()

    # Type annotations (type hinting not forcing)
    name: str = 10

.. code-block:: python

    {}  # dict
    {1}  # set
    {1, 2}  # set
    {1: 2}  # dict
    {1:1, 2:2}  # dict

    my_data = {}
    isinstance(my_data, (set, dict))  # True

    isinstance(my_data, dict)  # True
    isinstance(my_data, set)  # False

    my_data = {1}
    isinstance(my_data, set)  # True
    isinstance(my_data, dict)  # False

    my_data = {1: 1}
    isinstance(my_data, set)  # False
    isinstance(my_data, dict)  # True

Inheritance
-----------
.. literalinclude:: src/oop-inheritance.py
    :name: listing-oop-inheritance
    :language: python
    :caption: Inheritance

Multiple Inheritance
------------------
.. literalinclude:: src/oop-multiple-inheritance.py
    :name: listing-oop-multiple-inheritance
    :language: python
    :caption: Multiple Inheritance

* gdzie wsadzić metodę ``zatrab()``
* gdzie wsadzić metodę ``ruszaj()``
* gdzie wsadzić metodę ``otworz_dach()``

Composition (Mixin Classes)
---------------------------
.. literalinclude:: src/oop-composition.py
    :language: python
    :caption: Composition (Mixin Classes)

Dziedziczenie czy kompozycja?
-----------------------------
* Kompozycja ponad dziedziczenie!

``super()``
-----------
Funkcja ``super`` pozwala uzyskać dostęp do obiektu po którym dziedziczymy, do jego parametrów statycznych i metod, które przeciążamy (m.in. funkcji ``__init__``).

.. code-block:: python

    class Samochod:
        def zatrab(self):
            print('biiiip')

    class Maluch(Samochod):
        def zatrab(self):
            print('bip')

        def jak_trabi_samochod(self):
            return super().zatrab()

``__str__()``
-------------
.. literalinclude:: src/oop-str.py
    :language: python
    :caption: Using ``__str__()`` on a class


``__str__()`` i ``__repr__()``
------------------------------
Dwiema dość często używanymi metodami systemowymi są ``__repr__`` i ``__str__``. Obie te funkcje konwertują obiekt klasy do stringa, mają jednak inne przeznaczenie:

Albo jeszcze inaczej:

    * ``__repr__`` jest dla developerów (być jednoznacznym),
    * ``__str__`` dla użytkowników (być czytelnym).

.. literalinclude:: src/oop-repr.py
    :language: python
    :caption: Using ``__repr__()`` on a class

Przykład praktyczny:

.. code-block:: python

    >>> import datetime
    >>> datetime.datetime.now()  # ``__repr__``
    >>> print(datetime.datetime.now())  # ``__str__``


Inicjalizacja parametrów
------------------------
Wszystkie parametry lokalne dla danej instancji klasy powinny być zainicjalizowane w funkcji ``__init__``.

.. literalinclude:: src/oop-dynamic-fields.py
    :language: python
    :caption: Fields added dynamicly

.. literalinclude:: src/class-init-dynamic.py
    :name: listing-class-init-dynamic
    :language: python
    :caption: Funkcja inicjalizująca, która automatycznie dodaje pola do naszej klasy w zależności od tego co zostanie podane przy tworzeniu obiektu


Private, public? konwencja ``_`` i ``__``
-----------------------------------------
W Pythonie nie ma czegoś takiego jak prywatne pole klasy. Czy prywatna metoda klasy. Wszystkie obiekty zdefiniowane wewnątrz klasy są publiczne. Istnieje jednak ogólnie przyjęta konwencja, że obiekty poprzedzone ``_`` są prywatne dla tej klasy i nie powinny być bezpośrednio wywoływane przez użytkownika. Podobnie z funkcjami rozpoczynającymi się od ``__`` (m.in. metody magiczne wspomniane powyżej). Są tu funkcje systemowe, które są używane przez interpreter Pythona i raczej nie powinny być używane bezpośrednio.

.. code-block:: python

    __author__ = 'Matt Harasymczuk'

    class Person:
        imie = ''  # publiczna
        data_urodzenia = ''  #publiczna
        _wiek =  # prywanta


Co powinno być w klasie a co nie?
---------------------------------
* Jeżeli metoda w swoim ciele ma ``self`` i z niego korzysta to powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` to nie powinna być w klasie
* Jeżeli metoda nie ma w swoim ciele ``self`` ale wybitnie pasuje do klasy, to można ją tam zamieścić oraz dodać dekorator ``@staticmethod``

.. literalinclude:: src/oop-staticmethod.py
    :language: python
    :caption: Case Study uzasadnionego użcycia ``@staticmethod``

Klasa per plik?
---------------
Patrz przykład powyżej


Assignments
===========

Address Book
------------
#. Napisz książkę adresową:

        * imię
        * nazwisko
        * telefon
        * adresy:

            * ulica
            * miasto
            * kod_pocztowy
            * stan
            * panstwo

#. Wszystkie dane w książce muszą być reprezentowane przez klasy.
#. Klasa ``Kontakt`` powinna wykorzystywać domyślne argumenty w ``__init__``.
#. Użytkownik może mieć wiele adresów.
#. Zrób tak, aby się ładnie wyświetlało zarówno dla jednego wyniku (``print(adres)``, ``print(osoba)`` jak i dla wszystkich w książce ``print(ksiazka_adresowa)``.
#. API programu powinno być tak jak na :numref:`listing-oop-address-book`

:Zadanie z gwiazdką:
    * Klasa ``Adres`` powinna mieć zmienną liczbę argumentów za pomocą ``**kwargs`` i dynamicznie wpisywane pola ``setattr()`` (jeżeli nie mają wartości ``None``).

:Założenia:
    * Nazwa pliku: ``oop-addressbook.py``
    * Linii kodu do napisania: około 20 linii
    * Maksymalny czas na zadanie: 30 min

:Co zadanie sprawdza?:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na stringa oraz jego reprezentacja (które i kiedy użyć)
    * korzystanie z operatorów ``*`` i ``**`` (zadanie z gwiazdką)

.. literalinclude:: src/oop-address-book.py
    :name: listing-oop-address-book
    :language: python
    :caption: Address Book

Punkty i wektory
----------------
Przekształć swój kod z przykładu z modułu "Matematyka" tak żeby wykorzytywał klasy.

:Zadanie 0:
    Napisz klasę ``ObiektGraficzny``, która implemtuje "wirtualną" funkcję ``plot()``. Niech domyślnie ta funkcja podnosi ``NotImplementedError`` (podpowiedź: ``raise NotImplementedError``).

:Zadanie 1:
    Napisz klasę ``Punkt``, która dziedziczy po ``ObiektGraficzny``, która będzie miała "ukryte" pola ``_x``, ``_y``. Konstruktor tej klasy ma przyjmować współrzędne ``x`` oraz ``y`` jako argumenty. Napisz obsługę pól ukrytych ``_x`` oraz ``_y`` jako ``@property`` tej klasy (obsługiwane jako ``x`` oraz ``y``). Dopisz implementacje metod ``__str__`` oraz ``__repr__``. Zaimplementuj metodę ``plot(kolor)``, która wyrysuje ten punkt na aktualnie aktywnym wykresie. Kolor domyślnie powinien przyjmować wartość ``'black'``.

    Dopisz do tej klasy metodę statyczną, która zwróci losowy punkt w podobny sposób jak funkcja ``random_point(center, std)`` zwracała obiekt dwuelementowy.

:Zadanie 2:
    Dopisz do tej klasy dwie metody, które pozwolą obliczyć odległość między dwoma punktami. Jedna z tych metod niech będzie metodą statyczną, która przyjmuje dwa punkty jako argumenty, a zwraca odległość między nimi (przykładowe wywołanie tej metody: ``Punkt.oblicz_odleglosc_miedzy_punktami(punkt_A, punkt_B)``). Druga z tych metod niech będzie zwykłą metodą klasy, która przyjmie jeden punkt jako argument oraz obliczy odległość od tego punktud opunktu na którym jest wykonywana (``punkt_A.oblicz_odleglosc_do(punkt_B)``).

:Zadanie 3:
    Napisz kod, który wykorzystując klasę zaimplementowaną w przykładzie powyżej, wygeneruje listę losowych punktów wokół punktów A i B. Wyrysuj te punkty na wykresie, podobnie jak w przykładzie z modułu "Matematyka".

:Zadanie 4:
    Napisz kod, który zaklasyfikuje te losowo wygenerowane punkty do punktów A oraz B na podstawie odległości. W tym celu wykorzystaj napisane metody do obliczania odległości między punktami. Po klasyfikacji wyrysuj te punkty na wykresie, podobnie jak w przykładzie z modułu "Matematyka".

:Założenia:
    * Nazwa pliku: ``oop-vector.py``
    * Linii kodu do napisania: około 20 linii
    * Maksymalny czas na zadanie: 30 min