*****
Pliki
*****

Konstrukcja ``with``
====================

* Context manager

Czytanie
========

.. code-block:: python

    with open(FILENAME) as file:
        content = file.read()

.. code-block:: python

    with open(FILENAME) as file:
        content = file.readlines()

.. code-block:: python

    with open(FILENAME) as file:
        for line in file:
            print(line)

Zapis
=====

.. code-block:: python

    with open(FILENAME, 'w') as file:
        file.write('foobar')

.. code-block:: python

    with open(FILENAME, 'a') as file:
        file.write('foobar')


Tryby odczytu i zapisu
======================

   ========= ===============================================================
   Character Meaning
   ========= ===============================================================
   ``'r'``   open for reading (default)
   ``'w'``   open for writing, truncating the file first
   ``'x'``   open for exclusive creation, failing if the file already exists
   ``'a'``   open for writing, appending to the end of the file if it exists
   ``'b'``   binary mode
   ``'t'``   text mode (default)
   ``'+'``   open a disk file for updating (reading and writing)
   ``'U'``   universal newlines mode (deprecated)
   ========= ===============================================================

Obsługa wyjątków
================

.. code-block:: python

    FILENAME = input('Podaj nazwę pliku: ')

    try:
        with open(FILENAME, 'w') as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
        print('File does not exists')

    except PermissionError:
        print('Brak uprawnien')
