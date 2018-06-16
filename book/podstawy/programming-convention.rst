.. _Dobre praktyki:

**************
Dobre praktyki
**************

PEP8
====

Tabulacje i czy spacje?
-----------------------
* 4 spacje
* IDE zamienia tab na 4 spacje

Długość linii
-------------
* 79 znaków
* soft wrap
* co z monitorami 4k?
* najbardziej kontrowersyjna klauzula

Kodowanie plików
----------------
Przy Pythonie 3 kodownaie plików powinno być w UTF-8.

Pojedynczy czy podwójny cudzysłów
---------------------------------
* Python nie rozróżnia czy stosujemy pojedyncze znaki cudzysłowiu czy podwójne.
* Ważne jest aby wybrać jedną konwencję i się jej konsekwentnie trzymać.
* Interpreter Pythona domyślnie stosuje pojedyncze znaki cudzysłowia.
* Z tego powodu w tej książce będziemy trzymać się powyższej konwencji.
* Ma to znaczenie przy ``doctest``, który zawsze korzysta z pojedynczych i rzuca errorem jak są podwójne

.. code-block:: python

    print('it\'s José\'s book')
    print("it's José's book")

.. code-block:: python

    print('<a href="http://python.astrotech.io">Python and Machine Learning</a>')

Wcięcia
-------
:Good:
    .. code-block:: python

    # Aligned with opening delimiter.
    server = Server(host='localhost', port=443, secure=True,
                    username='admin', password='admin')

    # More indentation included to distinguish this from the rest.
    def Server(
            host='localhost', port=443, secure=True
            username='admin', password='admin'):
        print(host, port)

    # Hanging indents should add a level.
    server = Server(
        host='localhost', port=443, secure=True,
        username='admin', password='admin')

    # The best
    server = Server(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        secure=True,
    )

:Not Good:
    .. code-block:: python

        # Arguments on first line forbidden when not using vertical alignment.
        server = Server(host='localhost', port=1337,
            username='admin', password='admin')

        # Further indentation required as indentation is not distinguishable.
        def Server(
            host='localhost', port=1337,
            username='admin', password='admin'):
            print(host, port)

Zamykanie nawiasów
------------------
:Good:
    .. code-block:: python

        vector = [
            1, 2, 3,
            4, 5, 6,
        ]

        result = some_function_that_takes_arguments(
            'a', 'b', 'c',
            'd', 'e', 'f',
        )

        vector = [
            1, 2, 3,
            4, 5, 6]

        result = some_function_that_takes_arguments(
            'a', 'b', 'c',
            'd', 'e', 'f')

Łamanie linii
-------------
Linie możemy łamać poprzez stawianie znaku ukośnika ``\`` na końcu:

.. code-block:: python

    with open('/path/to/some/file/you/want/to/read') as file1, \
            open('/path/to/some/file/being/written', mode='w') as file2:
        content = file1.read()
        file2.write(content)

.. code-block:: python

    class Server:
        def __init__(self, username, password, host='localhost'
                     port=80, secure=False):

            if not instance(username, str) or not instance(password, str) or
                    not instance(host, str) or not instance(secure, bool) or
                    (not instance(port, int) and 0 < port <= 65535):
                raise TypeError(f'One of your parameters is incorrect type')
                
         def __str__(self):
            if secure:
                protocol = 'https'
            else:
                protocol = 'http'

            return f'{protocol}://{self.username}:{self.password}@{self.host}:{self.port}/'

    server = Server(
        host='localhost',
        username='admin',
        password='admin',
        port=443,
        secure=True,
    )

Puste linie
-----------
.. code-block:: python

    class Server:
        def __init__(self, username, password, host='localhost'
                     port=80, secure=False):

            if not instance(username, str):
                raise TypeError(f'Username must be str')

            if not instance(password, str):
                raise TypeError(f'Password must be str')

            if not instance(port, int):
                raise TypeError(f'Port must be int')
            elif: 0 < port <= 65535
                raise ValueError(f'Port must be 0-65535')

         def __str__(self):
            if secure:
                protocol = 'https'
            else:
                protocol = 'http'

            return f'{protocol}://{self.username}:{self.password}@{self.host}:{self.port}/'

Importy
-------
* Każdy z importów powinien być w osobnej linii
* importy systemowe na górze
* importy bibliotek zewnętrznych poniżej systemowych
* importy własnych modułów poniżej bibliotek zewnętrznych
* jeżeli jest dużo importów, pomiędzy grupami powinna być linia przerwy

:Good:
    .. code-block:: python

        import os
        import sys
        import requests
        import numpy as np
        from subprocess import Popen
        from subprocess import PIPE

    .. code-block:: python

        import os
        import sys
        import requests
        import numpy as np
        from random import shuffle
        from subprocess import Popen, PIPE

:Not Good:
    .. code-block:: python

        import sys, os, requests, numpy

    .. code-block:: python

        import sys, os
        import requests, numpy

Białe spacje w wyrażeniach
--------------------------
Tak:

.. code-block:: python

    spam(ham[1], {eggs: 2})

    ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
    ham[lower:upper], ham[lower:upper:], ham[lower::step]
    ham[lower+offset : upper+offset]
    ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
    ham[lower + offset : upper + offset]

    spam(1)

    dct['key'] = lst[index]

    x = 1
    y = 2
    long_variable = 3

    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)

    def complex(real, imag=0.0):
        return magic(r=real, i=imag)

    def munge(input: AnyStr):
    def munge(sep: AnyStr = None):
    def munge() -> AnyStr:
    def munge(input: AnyStr, sep: AnyStr = None, limit=1000):

    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three()

Nie:

.. code-block:: python

    spam( ham[ 1 ], { eggs: 2 } )

    ham[lower + offset:upper + offset]
    ham[1: 9], ham[1 :9], ham[1:9 :3]
    ham[lower : : upper]
    ham[ : upper]

    spam (1)

    dct ['key'] = lst [index]

    x             = 1
    y             = 2
    long_variable = 3

    i=i+1
    submitted +=1
    x = x * 2 - 1
    hypot2 = x * x + y * y
    c = (a + b) * (a - b)

    def complex(real, imag = 0.0):
        return magic(r = real, i = imag)

    def munge(input: AnyStr=None):
    def munge(input:AnyStr):
    def munge(input: AnyStr)->PosInt:

    if foo == 'blah': do_blah_thing()
    do_one(); do_two(); do_three()

    if foo == 'blah': do_blah_thing()
    else: do_non_blah_thing()

    try: something()
    finally: cleanup()

    do_one(); do_two(); do_three(long, argument,
                                 list, like, this)

    if foo == 'blah': one(); two(); three()


Komentarze
----------

Google style comments
~~~~~~~~~~~~~~~~~~~~~

Konwencje nazewnicze
--------------------

* ``zmienne``
* ``STALE``
* ``NazwyKlas``
* ``nazwy_metod()`` i ``nazwy_funkcji()``
* ``nazwymodulow``, ``nazwy_modulow``
* ``self``
* ``cls``

Używanie ``__`` i ``_`` w nazwach
---------------------------------

Konstrukcje warunkowe
---------------------
:Good:
    .. code-block:: python

        if foo is not None:
            pass

        if foo:
            pass

:Not Good:
    .. code-block:: python

        # if (! foo == null) {}
        if not foo is None:

Zwracanie z funkcji
-------------------

Tak:

.. code-block:: python

    def foo(x):
        if x >= 0:
            return math.sqrt(x)
        else:
            return None

    def bar(x):
        if x < 0:
            return None
        return math.sqrt(x)

Nie:

.. code-block:: python

    def foo(x):
        if x >= 0:
            return math.sqrt(x)

    def bar(x):
        if x < 0:
            return
        return math.sqrt(x)

Sprawdzanie warunków
--------------------

Tak:

.. code-block:: python

    if not seq:
    if seq:

    if greeting:

Nie:

.. code-block:: python

    if len(seq)
    if not len(seq)

    if greeting == True:
    if greeting is True:

PEP20 - Zen of Python
=====================
.. code-block:: python

    import this

The Zen of Python
-----------------
* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.
* Errors should never pass silently.
* Unless explicitly silenced.
* In the face of ambiguity, refuse the temptation to guess.
* There should be one-- and preferably only one --obvious way to do it.
* Although that way may not be obvious at first unless you're Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* If the implementation is hard to explain, it's a bad idea.
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!

Zen Pythona
-----------
* Piękne jest lepsze niż brzydkie.
* Wyrażone wprost jest lepsze niż domniemane.
* Proste jest lepsze niż złożone.
* Złożone jest lepsze niż skomplikowane.
* Płaskie jest lepsze niż wielopoziomowe.
* Rzadkie jest lepsze niż gęste.
* Czytelność się liczy.
* Sytuacje wyjątkowe nie są na tyle wyjątkowe, aby łamać reguły.
* Choć praktyczność przeważa nad konsekwencją.
* Błędy zawsze powinny być sygnalizowane.
* Chyba że zostaną celowo ukryte.
* W razie niejasności powstrzymaj pokusę zgadywania.
* Powinien być jeden -- i najlepiej tylko jeden -- oczywisty sposób na zrobienie danej rzeczy.
* Choć ten sposób może nie być oczywisty jeśli nie jest się Holendrem.
* Teraz jest lepsze niż nigdy.
* Chociaż nigdy jest często lepsze niż natychmiast.
* Jeśli rozwiązanie jest trudno wyjaśnić, to jest ono złym pomysłem.
* Jeśli rozwiązanie jest łatwo wyjaśnić, to może ono być dobrym pomysłem.
* Przestrzenie nazw to jeden z niesamowicie genialnych pomysłów -- miejmy ich więcej!


Korzystanie z ``help()``, ``dir()`` i ``object.__dict__``
=========================================================


Magic number i Magic string
===========================


Passwords and secrets
=====================
* UMASK
* Sticky bit
* setuid
* configparser


Wczytywanie konfiguracji programów
==================================
* configparser


Wersjonowanie API
=================

.. code-block:: text

    Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding:gzip, deflate, sdch
    Accept-Language:en-US,en;q=0.8,pl;q=0.6

``pycodestyle`` previously known as ``PEP8``
============================================

:About:
    Python style guide checker. ``pycodestyle`` is a tool to check your Python code
    against some of the style conventions in PEP 8.

    * Plugin architecture: Adding new checks is easy.
    * Parseable output: Jump to error location in your editor.
    * Small: Just one Python file, requires only stdlib. You can use just the
    * pep8.py file for this purpose.
    * Comes with a comprehensive test suite.

:Installation:
    .. code-block:: console

        $ pip install pycodestyle
        $ pip install --upgrade pycodestyle
        $ pip uninstall pycodestyle

:Usage:
    .. code-block:: console

        $ pycodestyle FILENAME.py
        $ pycodestyle DIRECTORY/
        $ pycodestyle --statistics -qq DIRECTORY/
        $ pycodestyle --show-source --show-pep8 FILENAME.py

:Config:
    ``setup.cfg``

    .. code-block:: ini

        [pycodestyle]
        max-line-length = 939
        ignore = E402,W391