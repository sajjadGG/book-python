*****************************
Serializacja i deserializacja
*****************************


Serializacja i deserializacja danych Pythona
============================================
Python posiada bibliotekę ``pickle``, która służy do serializacji danych i zmiennych Pythona. Ta biblioteka ma także metody do zapisu i odczytu danych z plików ``pkl``.

Przykład demonstrujący jak działa pickle:

.. code-block:: python

    PYTHON = [
         Osoba,
         make_datetime(now),
         str(now),
         now.__str__(),
         '%s' % now,
         '{}'.format(now),
         {'imie': 'Ivan', 'nazwisko': 'Ivanovic'},
         (10, 20, 30),
         (1,)
    ]

    import pickle

    p = pickle.dumps(PYTHON)
    print('Z Python do Pickle:', p)

    pp = pickle.loads(p)
    print('Z Pickle do Python:', pp)

    osoba = pp[0]
    print('Obiekt po konwersji:', osoba.nazwisko)


Zapis i odczyt danych z pliku:

.. code-block:: python

    PYTHON = [
         Osoba,
         make_datetime(now),
         str(now),
         now.__str__(),
         '%s' % now,
         '{}'.format(now),
         {'imie': 'Ivan', 'nazwisko': 'Ivanovic'},
         (10, 20, 30),
         (1,)
    ]

    import pickle

    with open(FILE, 'wb') as pickle_file:
        pickle.dump(PYTHON, pickle_file)

    with open(FILE, 'rb') as pickle_file:
        pp = pickle.load(pickle_file)
    print('Przeczytany obiekt:', pp)


Zadania kontrolne
=================

Serializacja obiektów do Pickle
-------------------------------
#. Użyj obiektu ``książka_adresowa`` stworzonego w zadaniu z serializacją
#. Za pomocą ``pickle`` zapisz kontakty z książki adresowej w pliku
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku
