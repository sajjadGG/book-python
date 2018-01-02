*********
Decorator
*********

.. todo::
    - przyklad z flaska z app.route na wykorzystywanie dekoratorów
    - decorator decydujący czy odpalić funkcję czy nie na przykładzie @login_required czy @permission_required z django
    - Ansible decorator @timeout(seconds=10, error_message='timeout occured')
    - class decorators

Zastosowanie
============

* Modify arguments
* Modify returned value
* Do things before call
* Do things after call
* Avoid calling
* Modify global state
* Metadata

Przykład zastosowania
---------------------

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

Zadania kontrolne
=================

Prosty dekorator
----------------
* Program przechodzi przez pliki i katalogi wykorzystując ``os.walk``.
* Stwórz funkcję, która wypisuje na ekranie nazwę pliku lub katalogu.
* Stwórz dekorator do funkcji, który przed wyświetleniem jej na ekranie podmieni ścieżkę na bezwzględną (``path`` + ``filename``).

