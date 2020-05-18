.. _Basic Files Access Modes:

*****************
File Access Modes
*****************


Write
=====
* ``mode='wt'`` - write in text mode
* ``mode='wb'`` - write in binary mode
* ``mode='w'`` - write in text mode (alias to "wt")
* ``mode='wt+'`` - open for updating (reading and writing)
* ``mode='wb+'`` - open for updating (reading and writing)
* ``mode='w+'`` - open for updating (reading and writing) (alias to "wt+")

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    data = 'We choose to go to the Moon...'

    with open(FILE, mode='w'):
        file.write(data)


Append
======
* ``mode='at'`` - append in text mode
* ``mode='ab'`` - append in binary mode
* ``mode='a'`` - append in text mode (alias to "at")
* ``mode='at+'`` - open for updating (reading and writing)
* ``mode='ab+'`` - open for updating (reading and writing)
* ``mode='a+'`` - open for updating (reading and writing) (alias to "at+")

.. code-block:: python

    FILE = r'/tmp/myfile.txt'
    data = 'We choose to go to the Moon...'

    with open(FILE, mode='a'):
        file.write(data)


Read
====
* ``mode='rt'`` - read in text mode (default)
* ``mode='rb'`` - read in binary mode
* ``mode='r'`` - read in text mode (alias to "wt")
* ``mode='rt+'`` - open for updating (reading and writing)
* ``mode='rb+'`` - open for updating (reading and writing)
* ``mode='r+'`` - open for updating (reading and writing) (alias to "rt+")
* If no mode is specified, the default mode is "rt"

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE):
        data = file.read()

.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    with open(FILE, mode='r'):
        data = file.read()


Exception handling
==================
.. code-block:: python

    FILE = r'/tmp/myfile.txt'

    try:
        with open(FILE) as file:
            print(file.read())

    except FileNotFoundError:
        print('File does not exist')

    except PermissionError:
        print('Permission denied')


Assignments
===========

File Access Error
-----------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/file_access_error.py`

:English:
    #. Using ``input()`` ask user for a file path
    #. Print file content
    #. Handle exception for not existing file
    #. Handle exception for not having sufficient permissions

:Polish:
    #. Używając ``input()`` zapytaj użytkownika o ścieżkę do pliku
    #. Wypisz zawartość pliku
    #. Obsłuż wyjątek dla nieistniejącego pliku
    #. Obsłuż wyjątek dla braku wystarczających uprawnień

