*********
Decorator
*********

Zastosowanie
============
* Modify arguments
* Modify returned value
* Do things before call
* Do things after call
* Avoid calling
* Modify global state (not a good idea)
* Metadata

Przykład zastosowania
---------------------
- Zagnieżdżone
- wykonywane od góry

.. code-block:: python

    @permission_required(uid=0)
    @modyfikuj_sciezke_w_zaleznosci_od_systemu_operacyjnego
    @timeout(seconds=10, error_message='za dlugo')
    def instaluj_oprogramowanie(sciezka, nazwa_oprogramowania, wersja_paczki):
        pass


Definicja
=========
.. code-block:: python

    def my_decorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper

    # usage

    @my_decorator
    def func(x):
        return x

Class Decorators
================
.. literalinclude:: src/decorators-class-decorator.py
    :name: listing-decorators-case-study-flask
    :language: python
    :caption: Case Study wykorzystania dekotatorów do poprawienia czytelności kodu Flask

.. todo:: classdecorators
.. todo:: https://andrefsp.wordpress.com/2012/08/23/writing-a-class-decorator-in-python/

@staticmethod
-------------
.. code-block:: python

    class Foo:
        def __init__(self, tekst='Jose'):
            self.tekst = tekst

        def hello(self):
            print(f'hello {self.tekst}')

        @staticmethod
        def ehlo():
            print('hello')


    # pryzkładowa implementacja
    def staticmethod(f):
        def wrapper(*args, **kwargs):
            return f()
        return wrapper

@classmethod
------------



Przykład
========

.. code-block:: python

    import os
    import logging


    def if_file_exists(function):

        def check(filename):
            if os.path.exists(filename):
                function(filename)
            else:
                logging.error('File "%(filename)s" does not exists, will not execute!', locals())

        return check


    @if_file_exists
    def print_file(filename):
        with open(filename) as file:
            content = file.read()
            print(content)


    if __name__ == '__main__':
        print_file('/etc/passwd')
        print_file('/tmp/passwd')

Case Study
----------
.. literalinclude:: src/decorators-case-study-flask.py
    :name: listing-decorators-case-study-flask
    :language: python
    :caption: Case Study wykorzystania dekotatorów do poprawienia czytelności kodu Flask

.. literalinclude:: src/decorators-case-study-django.py
    :name: listing-decorators-case-study-django
    :language: python
    :caption: Case Study wykorzystania dekotatorów do poprawienia czytelności kodu Django


Zadania kontrolne
=================

Prosty dekorator
----------------
* Program przechodzi przez pliki i katalogi wykorzystując ``os.walk``.
* Stwórz funkcję, która wypisuje na ekranie nazwę pliku lub katalogu.
* Stwórz dekorator do funkcji, który przed wyświetleniem jej na ekranie podmieni ścieżkę na bezwzględną (``path`` + ``filename``).

