**********************************
Funkcje wbudowane i słowa kluczowe
**********************************

Słowa kluczowe
==============

Słowa kluczowe (keywords) to wyrazy zarezerwoane do użytku Pythona. Nie można użyć słowa kluczowego jako nazwy zmiennej, nazwy funkcji czy innego identyfikatora. Każdy ze słów kluczowych odgrywa ważną rolę w tym języku. Lista słów kluczowych może być uzyskana wpisując:

.. code-block:: python

    import keyword
    print(keyword.kwlist)


``import``
----------

Biblioteki w Pythonie są pogrupowane w moduły. Słowo kluczowe ``import`` służy do importowania modułów do naszej przetrzeni nazw. Przestrzeń nazw (namespace) zawiera wszystkie zmienne (również funkcje i klasy), które zadeklarowaliśmy w trakcie działania programu. ```import`` to Pythonowy odpowiednik np. dyrektywy ``#include<nazwa_biblioteki>`` z C++.

.. code-block:: python

    import module

Wykonanie powyższego kodu spowoduje dodanie do aktualnej przestrzeni nazw modułu ``module``. Każdy moduł może zawierać submoduły, funkcje, klasy, itp. Możemy dodatkowo wskazać, którą klasę lub metodę chcemy zaimportować z modułu. Dodatkowo, wykorzystując słowo kluczowe ``as`` możemy nadać zaimportowanemu modułowi czy funkcji nową nazwę.

.. code-block:: python

    from module import submodule
    from module.submodule import function as alias
    from module import submodule as alias

Aby wykorzystać funkcję z danego modułu, musimy najpierw wskazać, z którego modułu chcemy skorzystać a następnie podać nazwę funkcji czy zmiennej do której chcemy się odwołać. Korzystając z przykładu powyżej:

.. code-block:: python

    import keyword
    print(keyword.kwlist)

W pierwszej linijce importujemy moduł ``keyword``. W drugiej linijce wypisujemy zawartość zmiennej ``kwlist`` z modułu ``keyword``. Moglibyśmy uzyskać podobny efekt wykonując:

.. code-block:: python

    from keyword import kwlist
    print(kwlist)

W tym przykładzie, z modułu ``keyword`` importujemy jedynie zmienną ``kwlist``. Przy takiej składni warto wspomnieć, że zmniejsza ona czytelność, nie podnosząc wcale efektywności kodu. Interpreter i tak wczyta najpierw całą zawartość modułu, następnie stworzy nową zmienną ``kwlist``, której przypisze odpowiednią wartość. Taki zapis zmniejsza czytelność kodu i zwiększa prawdopodobieństwo błędu.  Używając zapisu ``import module`` i następnie ``module.variable`` jendoznacznie wskazujemy z jakiego modułu korzystamy.



.. code-block:: python

    from . import module
    from .. import module

    from .module import submodule
    from ..module import submodule


``pass``
--------

Python domyślnie oczekuje wcięcia po dwukropku. Jeżeli chcemy zostawić klasę czy funkcję pustą, korzystamy wtedy ze słowa kluczowego ``pass``.

.. code-block:: python

    class User:
        pass


``continue``
------------
Słowo kluczowe ``continue`` powoduje przerwanie aktualnie wykonywanej pętli i przejście do kolejnej iteracji. Przydatne podczas debugowania i testowania kodu.

.. todo:: lepszy przykład

.. code-block:: python

    >>> for number in range(0, 30):
    ...     # jeżeli nie ma reszty z dzielenia przez 5
    ...     if not number % 5 == 0:
    ...         continue
    ...     print(number)
    0
    5
    10
    15
    20
    25


.. code-block:: python

    for i in range(1, 30):
        print(i)
        continue

        # ten kod się nie wywoła
        # przydatne do zrozumienia działania funkcji
        # gdy chcemy wyprintować ``i`` a nie wykonywać np. requestu API w dalszej części
        if not i % 4:
            print('podzielny przez 4')
        else:
            print('asdasd')


``break``
---------
Słowo kluczowe ``break`` przerywa aktualnie wykonywaną pętlę.

.. todo:: lepszy przykład

.. code-block:: python

    >>> for number in range(0, 30):
    ...     if number % 5:
    ...         break
    ...     print(number)
    0

``return``
----------

Słowo kluczowe ``return`` wskazuje funkcji jaką wartość ma dana funkcja zwrócić. Wykonanie linii ze słowem kluczowym ``return`` kończy wykonywanie funkcji.

.. code-block:: python

    >>> def sum(a, b):
    ...     return a + b
    ...
    >>> sum(2, 3)
    5


.. code-block:: python

    >>> def sum(a, b):
    ...     return a + b
    ...     print('Total is', a + b)  # ten kod się nie wykona
    ...
    >>> sum(2, 3)
    5


``__file__``
------------
.. code-block:: python

    print(__file__)

``__name__``
------------
.. code-block:: python

    print(__name__)

Zmienna ``__name__`` pozwala między innymi ustalić czy dany plik jest wykonywany czy importowany. Jeżeli dany plik jest wykonywany, zmienna ``__name__`` ustawiana jest na ``'__main__'``, jeżeli dany plik jest importowany jako moduł, zmienna ``__name__`` ustawiana jest na nazwę modułu. Jest to przydatne na przykład przy testowaniu modułów. Dodanie do modułu poniższej linijki:

.. code-block:: python

    if __name__ == '__main__':
        print('hello world')

Sprawi, że wypisane na konsoli zostanie ``'hello world!'`` jeżeli dany plik jest wykonywany jako główny. Powyższy kod nie wykona się natomiast jeżeli plik zaimportujemy jako moduł w innym pliku.

Przykład z życia:

.. code-block:: python

    import logging

    log = logging.getLogger(__name__)


.. code-block:: python

    def run():
        ...

    if __name__ == '__main__':
        # Jeżeli skrypt wywoływany jest z konsoli "z ręki" to uruchom funckję ``run()``
        # Jeżeli został zaimportowany, to ten fragment będzie zignorowany
        # I trzeba uruchomić funkcję ``run()`` samodzielnie - kontrolowanie
        run()

Funkcje wbudowane
=================

Funkcje wbudowane to funkcje dostępne domyślnie w języku Python.

``print()``
-----------
.. code-block:: python

    print('ehlo world')
    print('ehlo', 'world')
    print('ehlo', 'world', sep=';')

    imie = 'Max Peck'
    print('ehlo', imie, 'world')

Wyświetla argument jako tekst w wierszu poleceń.

W Pytonie2, print jest słowem kluczowym - nie wymaga użycia nawiasów. Ale dla kompatybilności można je również podawać.

``sorted()`` i ``sort()``
-------------------------
* Sortują elementy listy.
* ``sorted()`` to operator niemutowalny (nie zmienia kolejności elementów w liście).
* ``sorted()`` to funkcja, która jako argument przyjmuje listę.

.. code-block:: python

    >>> numbers = [3, 1, 2]
    >>> sorted(numbers)
    [1, 2, 3]
    >>> print(numbers)
    [3, 1, 2]

* ``.sort()`` to operator zmieniający listę (mutujący).
* ``sort()`` to metoda klasy lista.

.. code-block:: python

    >>> numbers = [3, 1, 2]
    >>> numbers.sort()
    >>> print(numbers)
    [1, 2, 3]

.. code-block:: python

    numbers = [3, 2, 1]
    print(numbers)
    # [3, 2, 1]

    print(numbers.sort())
    # None

    print(numbers)
    # [1, 2, 3]

    print('---------------------')

    numbers = [3, 2, 1]
    print(numbers)
    # [3, 2, 1]

    print(sorted(numbers))
    # [1, 2, 3]

    print(numbers)
    # [3, 2, 1]


``range()``
-----------
Tworzy **iterator**, który zwraca liczby w sekwencji. Jedna z rzeczy, która uległa zmianie od Pythona2, w którym range zwracał sekwencję liczb zamiast iteratora.

.. code-block:: python

    >>> numbers_generator = range(0, 5)
    >>> print(numbers_generator)
    range(0, 5)

    >>> for liczba in range(0, 5):
    ...    print(liczba)

.. code-block:: python

    >>> numbers_generator = range(0, 5)
    >>> numbers = list(numbers_generator)
    >>> print(numbers)
    [0, 1, 2, 3, 4]




``isinstance()``
----------------
Sprawdza czy dany obiekt jest instancją danej klasy.

.. code-block:: python

    >>> isinstance(10, int)
    True

    >>> isinstance(10, float)
    False

    >>> isinstance(10, (int, float))  # to musi być tupla, a nie lista
    True

``min()``
---------
Wartość minimalna z listy.

.. code-block:: python

    >>> numbers = [1, 2, 3, 4, 5]
    >>> min(numbers)
    1
    >>> min(3, 1, 5)
    1

``max()``
---------
Wartość maksymalna z listy.

.. code-block:: python

    >>> numbers = [1, 2, 3, 4, 5]
    >>> max(numbers)
    5
    >>> max(3, 1, 5)
    5

``len()``
---------
Długość listy, tuple, stringa itp.

.. code-block:: python

    >>> numbers = [1, 2, 3, 4, 5]
    >>> len(numbers)
    5
    >>> len('Max')
    3
    >>> len({'id': 3, 'name': 'Max'})
    2

``input()``
-----------

Pozwala użytkownikowi wpisać tekst.

.. code-block:: python

    >>> name = input()
    Ivan
    >>> print(name)
    'Ivan'

Pamiętaj o dodaniu dwukropka i spacji, aby tekst się nie zlewał.

.. code-block:: python

    >>> name = input('Type your name: ')
    Type your name: José
    >>> print(name)
    'José'

Czasami trzeba oczyścić dane, np. usuwając zbędne spacje na początku i końcu ciągu znaków podanego przez użytkownika.

 .. code-block:: python

    >>> name = input('Type your name: ')
    Type your name:         Ivan
    >>> print(name.strip())
    'Ivan'

``bin()``
---------

Konwertuje liczbę na binarną.

.. code-block:: python

    >>> bin(3)
    '0b11'

    >>> bin(-3)
    '-0b11'

``hex()``
---------

Konwertuje liczbę na hex.

.. code-block:: python

    >>> hex(99)
    '0x63'

``oct()``
---------

Konwertuje liczbę na oct.

.. code-block:: python

    >>> oct(23)
    '0o27'

``ord()``
---------
Zwraca kod ASCII jednoznakowego stringa.

.. code-block:: python

    >>> ord('a')
    97

``chr()``
---------
Z pozycji w tablicy ASCII konwertuje kod na znak Unicode.

.. code-block:: python

    >>> chr(97)
    'a'

Wszystkie funkcje wbudowane
===========================

    ===============  ==============  ==================  ============  ================
    ..               ..              Built-in Functions  ..            ..
    ---------------  --------------  ------------------  ------------  ----------------
    `abs()`          `dict()`        `help()`            `min()`       `setattr()`
    `all()`          `dir()`         `hex()`             `next()`      `slice()`
    `any()`          `divmod()`      `id()`              `object()`    `sorted()`
    `ascii()`        `enumerate()`   `input()`           `oct()`       `staticmethod()`
    `bin()`          `eval()`        `int()`             `open()`      `str()`
    `bool()`         `exec()`        `isinstance()`      `ord()`       `sum()`
    `bytearray()`    `filter()`      `issubclass()`      `pow()`       `super()`
    `bytes()`        `float()`       `iter()`            `print()`     `tuple()`
    `callable()`     `format()`      `len()`             `property()`  `type()`
    `chr()`          `frozenset()`   `list()`            `range()`     `vars()`
    `classmethod()`  `getattr()`     `locals()`          `repr()`      `zip()`
    `compile()`      `globals()`     `map()`             `reversed()`  `__import__`
    `complex()`      `hasattr()`     `max()`             `round()`
    `delattr()`      `hash()`        `memoryview()`      `set()`
    ===============  ==============  ==================  ============  ================
