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

Składnia
========

Klasy
-----
.. literalinclude:: src/oop-class.py
    :language: python
    :caption: Class

Pola Statyczne
--------------
.. literalinclude:: src/oop-static-field.py
    :language: python
    :caption: Class

.. code-block:: python

    class Astronaut:
        agency = 'NASA'

    # Objects - Instances
    ivan = Astronaut()
    jose = Astronaut()
    max = Astronaut()

    ivan.agency  # NASA
    jose.agency  # NASA
    max.agency   # NASA
    Astronaut.agency  # NASA

    ivan.agency = 'Roscosmos'

    ivan.agency  # Roscosmos
    jose.agency  # NASA
    max.agency   # NASA
    Astronaut.agency  # NASA

    Astronaut.agency = 'ESA'

    ivan.agency  # Roscosmos
    jose.agency  # ESA
    max.agency   # ESA
    Astronaut.agency  # ESA

Pola dynamiczne
---------------
.. code-block:: python

    class Pojazd:
        def __init__(self, marka, kola=4):
            self.marka = marka
            self.kola = kola
            self.kierowca = 'Max Peck'  # tak się raczej nie robi


    mercedes = Pojazd(marka='mercedes', kola=6)
    print(mercedes.kola)

    tir = Pojazd(marka='scania', kola=18)
    print(tir.kola)

Metody
------
.. code-block:: python

    class Pojazd:
        marka = None
        kierowca = None
        kola = 4

        def zatrab(self):
            print('piiip')

        def kto_kieruje(self):
            print(self.kierowca)


    auto = Pojazd()
    auto.zatrab()
    auto.kto_kieruje()

``self``
--------
.. code-block:: python

    class Pojazd:
        def zatrab(self):
            print('piiip')

Wykonywanie operacji na obiekcie
--------------------------------
.. code-block:: python

    >>> text = 'Ehlo,world'

    >>> text.split(',')
    ['Ehlo', 'world']

    >>> str.split(text, ',')
    ['Ehlo', 'world']

    >>> str.split('Ehlo,world', ',')
    ['Ehlo', 'world']


Pola klasy
----------
.. code-block:: python

    import logging


    class Samochod:
        kola = 4
        marka = None

        def set_marka(self, marka):
            logging.warning('Ustawiamy marke')
            self.marka = marka

        def get_marka(self):
            return self.marka


    # Java way
    mercedes = Samochod()
    mercedes.set_marka('Mercedes')
    print(mercedes.get_marka())


    # Python way
    maluch = Samochod()
    maluch.marka = 'Maluch'
    print(maluch.marka)


    maluch = Samochod(marka='Maluch')
    print(maluch.marka)

.. literalinclude:: src/oop-getter.py
    :language: python
    :caption: Case Study uzasadnionego użycia gettera w kodzie


Funkcja inicjalizująca
----------------------
.. code-block:: python

    class Server:

        def __init__(self, host, user, password=None):
            """
            host i user są wymagane
            password jest niewymagany i domyślnie jest None
            """
            self.host = host
            self.user = user
            self.password = password


    localhost = Server(
        host='localhost',
        user='admin',
        password='admin'
    )


``__init__`` jest metodą klasy, która wykonuje się podczas tworzenia nowego obiektu. Nie jest to do końca konstruktor tego obiektu, ale dla większości zastosowań można przyjąć, że metoda ``__init__`` jest konstruktorem klasy.

.. code-block:: python

    import logging

    class Samochod:
        kierowca = None

        def __init__(self, marka, kola=4):
            logging.warning('inicjalizujemy obiekt %s', marka)
            self.marka = marka
            self.kola = kola


    sam1 = Samochod(marka='Maluch')
    print(sam1.marka)
    print(sam1.kola)

    print(dir(sam1))
    print(sam1.__dict__)


    sam2 = Samochod(marka='Merc')
    print(sam2.marka)
    print(sam2.kola)


.. warning:: Nie powinniśmy uruchamiać innych metod na obiekcie. Bo obiekt nie jest jeszcze w pełni zainicjalizowany!! (bo konstruktor się nie wykonał do końca). Dopiero jak się skończy ``__init__`` to możemy uruchamiać metody obiektu.

    .. code-block:: python

        class Server:

            def __init__(self, host, user, password=None):
                self.host = host
                self.user = user
                self.password = password
                self.login()  # Błąd. Obiekt nie jest jeszcze w pełni zainicjalizowany, chociaż Python na to pozwoli (bo jest to funkcja inicjalizująca (Java już nie bo tam jest konstruktor).

           def login(self):
                print('loguję się do systemu')


        localhost = Server(
            host='localhost',
            user='admin',
            password='admin'
        )

        # to jest poprawne wywoałnie
        localhost.login()

Dziedziczenie
-------------
.. literalinclude:: src/oop-inheritance.py
    :name: listing-oop-inheritance
    :language: python
    :caption: Inheritance

Wielodziedziczenie
------------------
.. literalinclude:: src/oop-multiple-inheritance.py
    :name: listing-oop-multiple-inheritance
    :language: python
    :caption: Multiple Inheritance

* gdzie wsadzić metodę ``zatrab()``
* gdzie wsadzić metodę ``ruszaj()``
* gdzie wsadzić metodę ``otworz_dach()``

Kompozycja
----------
Tzw. Klasy Mixin

.. code-block:: python

    class OtwieralneSzyby:
        def otworz_szyby(self):
            raise NotImplementedError

        def zamknij_szyby(self):
            raise NotImplementedError


    class OtwieralnyDach:
        def otorz_dach(self):
            raise NotImplementedError

        def zamknij_dach(self):
            raise NotImplementedError


    class UmieTrabic:
        def zatrab(self):
            print('\bbiip')


    class Pojazd:
        kola = None


    class Samochod(Pojazd, UmieTrabic, OtwieralneSzyby):
        kola = 4

        def wlacz_swiatla(self, *args, **kwargs):
            print('włączam światła')


    class Cabrio(Samochod, OtwieralnyDach):
        def wlacz_swiatla(self, *args, **kwargs):
            print('Podnieś obudowę lamp')
            print('Puść muzyzkę')
            super().wlacz_swiatla(*args, **kwargs)
            print('Zatrąb')


    class Motor(Pojazd, UmieTrabic):
        kola = 2


    c = Cabrio()
    c.wlacz_swiatla()


.. code-block:: python

    class OtwieralnyDach:
        def otworz_dach(self):
            pass

        def zamknij_dach(self):
            pass


    class Trabi:
        def zatrab(self):
            raise NotImplementedError



    class Pojazd:
        kola = None


    class Samochod(Pojazd):
        kola = 4


    class Motor(Pojazd, Trabi):
        kola = 2

        def zatrab(self):
            print('biip')


    class Cabriolet(Samochod, OtwieralnyDach, Trabi):
        def zatrab(self):
            print('tru tu tu tu')


    class Mercedes(Samochod, OtwieralnyDach, Trabi):
        pass


    class Maluch(Samochod, Trabi):
        pass


Dziedziczenie czy kompozycja?
-----------------------------
* Kompozycja ponad dziedziczenie!


``super()``
-----------
Funkcja ``super`` pozwala uzyskać dostęp do obiektu po którym dziedziczymy, do jego parametrów statycznych i metod, które przeciążamy (m.in. funkcji ``__init__``).

.. code-block:: python

    >>> class Samochod:
    ...     def zatrab(self):
    ...         print('biiiip')

    >>> class Maluch(Samochod):
    ...     def zatrab(self):
    ...         print('bip')
    ...
    ...     def jak_robi_samochod(self):
    ...         return super().zatrab()


``__str__()`` i ``__repr__()``
------------------------------
Dwiema dość często używanymi metodami systemowymi są ``__repr__`` i ``__str__``. Obie te funkcje konwertują obiekt klasy do stringa, mają jednak inne przeznaczenie:

Albo jeszcze inaczej:

    * ``__repr__`` jest dla developerów (być jednoznacznym),
    * ``__str__`` dla użytkowników (być czytelnym).

.. code-block:: python

    class Samochod:
        def __init__(self, marka, kola=4):
            self.marka = marka
            self.kola = kola

        def __str__(self):
            return f'Marka: {self.marka} i ma {self.kola} koła'

        def __repr__(self):
            return f'Samochod(marka={self.marka}, kola={self.kola})'


    auto = Samochod(marka='mercedes', kola=3)
    print(auto)
    # Marka: {self.marka} i ma {self.kola} koła

    auta = [
        Samochod(marka='mercedes', kola=3),
        Samochod(marka='maluch', kola=4),
        Samochod(marka='fiat', kola=4),
    ]
    print(auta)
    # Samochod(marka='mercedes', kola=3),
    # Samochod(marka='maluch', kola=4),
    # Samochod(marka='fiat', kola=4),


Przykład praktyczny:

.. code-block:: python

    import datetime

    datetime.datetime.now()  # ``__repr__``
    print(datetime.datetime.now())  # ``__str__``


Dobre praktyki
==============

Tell - don't ask
----------------
"Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data. It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do. This encourages to move behavior into an object to go with the data."

Dobrze:

    .. code-block:: python

        class Samochod:
            szyby = 'zamkniete'

            def otworz_szyby(self):
                self.szyby = 'otwarte'


        auto.otworz_szyby()

Źle:

    .. code-block:: python

        class Samochod:
            szyby = 'zamkniete'

            def otworz_szyby(self):
                self.szyby = 'otwarte'


        auto.szyby = 'zamkniete'


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


Zadania kontrolne
=================

Książka adresowa
----------------
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

.. literalinclude:: src/oop-address-book.py
    :name: listing-oop-address-book
    :language: python
    :caption: Address Book

:Podpowiedź:
    * Powinieneś dopisać około 20 linii

:Zadanie z gwiazdką:
    * Klasa ``Adres`` powinna mieć zmienną liczbę argumentów za pomocą ``**kwargs`` i dynamicznie wpisywane pola ``setattr()`` (jeżeli nie mają wartości ``None``).

:Co zadanie sprawdza?:
    * myślenie obiektowe i odwzorowanie struktury w programie
    * praca z obiektami
    * zagnieżdżanie obiektów
    * rzutowanie obiektu na stringa oraz jego reprezentacja (które i kiedy użyć)
    * korzystanie z operatorów ``*`` i ``**`` (zadanie z gwiazdką)

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
