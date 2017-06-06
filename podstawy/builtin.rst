**********************************
Funkcje wbudowane i słowa kluczowe
**********************************

Słowa kluczowe
==============

``pass``
--------
.. code-block:: python

    class User:
        pass


``continue``
------------

.. code-block:: python

    >>> for number in range(0, 30):
    ...     if number % 5:
    ...         continue
    ...     print(number)
    0
    5
    10
    15
    20
    25

Kod po słowie ``continue`` nie zostanie wykonany. Przydatne podczas debugowania i testowania kodu.

.. code-block:: python

    for i in range(1, 30):
        print(i)
        continue

        if not i % 4:
            print('podzielny przez 4')
        else:
            print('asdasd')


``break``
---------

.. code-block:: python

    >>> for number in range(0, 30):
    ...     if number % 5:
    ...         break
    ...     print(number)
    0

``return``
----------

.. code-block:: python

    >>> def sum(a, b):
    ...     return a + b
    ...
    >>> sum(2, 3)
    5

Kod funkcji po słowie kluczowym ``return`` nie będzie wykonywany!

.. code-block:: python

    >>> def sum(a, b):
    ...     return a + b
    ...     print('Total is', a + b)
    ...
    >>> sum(2, 3)
    5


``__file__``
------------

.. code-block:: python

    >>> print(__file__)

``__name__``
------------

.. code-block:: python

    if __name__ == '__main__':
        print('hello world')

.. code-block:: python

    import logging

    log = logging.getLogger(__name__)


Funkcje wbudowane
=================


``print()``
-----------

.. code-block:: python

    print('ehlo world')
    print('ehlo', 'world')
    print('ehlo', 'world', sep=';')

``sorted()``
------------
``sorted()`` to operator niemutowalny (nie zmienia kolejności elementów w liście).

.. code-block:: python

    >>> numbers = [3, 1, 2]
    >>> sorted(numbers)
    [1, 2, 3]
    >>> print(numbers)
    [3, 1, 2]

``.sort()`` to operator zmieniający listę (mutujący).

.. code-block:: python

    >>> numbers = [3, 1, 2]
    >>> numbers.sort()
    >>> print(numbers)
    [1, 2, 3]


``range()``
-----------

.. code-block:: python

    >>> numbers_generator = range(0, 5)
    >>> print(numbers_generator)
    range(0, 5)

    >>> numbers = list(numbers_generator)
    >>> print(numbers)
    [0, 1, 2, 3, 4]


``isinstance()``
----------------

.. code-block:: python

    >>> isinstance(10, int)
    True

    >>> isinstance(10, float)
    False

    >>> isinstance(10, (int, float))
    True

``min()``
---------

.. code-block:: python

    >>> numbers = [1, 2, 3, 4, 5]
    >>> min(numbers)
    1
    >>> min(3, 1, 5)
    1

``max()``
---------

.. code-block:: python

    >>> numbers = [1, 2, 3, 4, 5]
    >>> max(numbers)
    5
    >>> max(3, 1, 5)
    5

``len()``
---------

.. code-block:: python

    >>> numbers = [1, 2, 3, 4, 5]
    >>> len(numbers)
    5

``input()``
-----------

.. code-block:: python

    >>> name = input()
    Matt
    >>> print(name)
    'Matt'

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
Argument must be integer.

.. code-block:: python

    >>> bin(3)
    '0b11'

    >>> bin(-3)
    '-0b11'

``hex()``
---------

.. code-block:: python

    >>> hex(99)
    '0x63'

``oct()``
---------

.. code-block:: python

    >>> oct(23)
    '0o27'

``ord()``
---------
.. code-block:: python

    >>> ord('a')
    97

``chr()``
---------

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
