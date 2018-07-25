.. _CSV Serialization:

*****************
CSV Serialization
*****************


Odczytywanie danych z plików CSV
================================
* dobra praktyka: zawsze podawać encoding
* dobra praktyka: zawsze podawać quotechar
* dobra praktyka: zawsze podawać delimiter

.. literalinclude:: src/csv-read.py
    :name: listing-csv-read
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictReader()``


Zapis do plików CSV
===================
* dobra praktyka: zawsze podawać encoding
* dobra praktyka: zawsze podawać quotechar
* dobra praktyka: zawsze podawać delimiter
* dobra praktyka: zawsze podawać lineterminator
* dobra praktyka: zawsze podawać quotechar
* dobra praktyka: zawsze podawać delimeter

.. literalinclude:: src/csv-write.py
    :name: listing-csv-write
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictWriter()``


Parsowanie innych plików za pomocą ``csv.DictReader()``
=======================================================

Parsing ``/etc/passwd``
-----------------------
.. literalinclude:: src/csv-passwd.py
    :name: listing-csv-passwd
    :language: python
    :caption: Parsing ``/etc/passwd`` file with ``csv.DictReader()``

Parsing Java properties file
----------------------------
.. literalinclude:: src/csv-properties.py
    :language: python
    :caption: Parsing ``sonar-project.properties`` file with  ``csv.DictReader()``


Assignments
===========

Wczytywanie pliku ``csv``
-------------------------
* https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv

#. Otwórz w przeglądarce podany powyżej URL
#. Zapisz jego zawartość na dysku w miejscu gdzie masz skrypty w pliku ``csv-iris.csv``
#. Korzystając z ``csv.DictReader`` wczytaj zawartość pliku
#. Podaj jawnie ``encoding``, ``delimiter`` oraz ``quotechar``
#. Pierwsza linijka stanowi metadane (nie wyświetlaj jej)
#. Nazwy poszczególnych kolumn:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Kolumna species ma mieć wartość nazwy gatunku a nie cyfry 0, 1, 2 jak to jest w pliku
#. Wypisz wiersze na ekranie

:Założenia:
    * Nazwa pliku: ``csv_dictreader.py``
    * Linii kodu do napisania: około 6 linie
    * Maksymalny czas na zadanie: 15 min

Serializacja ``csv``
--------------------
#. Za pomocą ``csv.DictWriter()`` zapisz do pliku dane o zmiennej strukturze
#. Podaj jawnie ``encoding``, ``delimiter``, ``quotechar`` ``quoting``, ``lineterminator``
#. ``fieldnames`` nie może być wymienione wprost w skrypcie (zahardkodowane)

.. code-block:: python

    DATA = [
        {'first_name': 'José'},
        {'last_name': 'Jiménez'},
        {'first_name': 'Иван', 'last_name': 'Иванович'},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
        {'first_name': 'José', 'born': 1961, 'first_step': 1969},
    ]

:Założenia:
    * Nazwa pliku: ``csv_dictwriter.py``
    * Linii kodu do napisania: około 8 linii
    * Maksymalny czas na zadanie: 15 min

:Podpowiedź:
    * To jest bardzo często występujący i użyteczny przykład

:Co zadanie sprawdza?:
    * Umiejętność korzystania z modułu ``csv``
    * Umiejętność iteracji po złożonych strukturach danych
    * Dynamiczne generowanie struktur danych na podstawie innych

Serializacja obiektów do CSV
----------------------------
#. Użyj obiektu ``książka_adresowa`` z listingu :numref:`listing-address-book`
#. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
#. Wszystkie pola muszą być zawsze w cudzysłowiach i oddzielone średnikami, kodowanie UTF-8.
#. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

:Podpowiedź:
    - powtarzanie rekordów (user pozostaje ten sam) z innymi danymi adresowymi
    - dodawanie kolumn (ulica_1, miasto_1, panstwo_1, ulica_2, miasto_2, panstwo_2) i automatyczne generowanie fieldnames
    - wrzucenie danych jako string do jednego pola adres_1, adres_2, adres_3 i ustalenie separatora (np: średnik - ';')
    - jedno pole adres (w ramach niego wszystkie adresy rozdzielone ";" a dane przecinkami ",")

.. literalinclude:: src/csv-addressbook.py
    :name: listing-address-book
    :language: python
    :caption: Address book

:Założenia:
    * Nazwa pliku: ``csv_addressbook.py``
    * Linii kodu do napisania: około 10 linii
    * Maksymalny czas na zadanie: 20 min
