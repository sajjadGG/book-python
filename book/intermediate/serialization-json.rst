**********************************
Serializacja i deserializacja JSON
**********************************


Format JSON jest podobny do zapisu dict w Python, ale różni się:

- nie może być przecinka po ostatnim elemencie list
- zawsze są stosowane podwójne cudzysłowia
- ``true`` i ``false`` jest pisane małymi literami
- zamiast ``None`` jest ``null``

Zapis danych do formatu JSON
============================
.. literalinclude:: src/json-dumps.py
    :name: listing-json-dumps
    :language: python
    :caption: Zapis danych do formatu JSON

Odczyt danych z formatu JSON
============================
.. literalinclude:: src/json-loads.py
    :name: listing-json-loads
    :language: python
    :caption: Odczyt danych z formatu JSON


Problemy z serializacją i deserializacją
========================================
* Serializacja i deserializacja dat
* Serializacja i deserializacja obiektów


Serializacja i pisanie własnych encoderów
=========================================
Problem z rzutowaniem daty na JSON:

.. literalinclude:: src/json-encoder-exception.py
    :name: listing-json-encoder-exception
    :language: python
    :caption: Exception during encoding datetime

Encoder Klasowy
---------------
.. literalinclude:: src/json-encoder-class.py
    :name: listing-json-encoder-class
    :language: python
    :caption: Encoder Klasowy

Encoder Function
----------------
.. literalinclude:: src/json-encoder-function.py
    :name: listing-json-encoder-function
    :language: python
    :caption: Encoder Function

Encodowanie daty
----------------
.. literalinclude:: src/json-encoder-datetime.py
    :name: listing-json-encoder-datetime
    :language: python
    :caption: Encoder dat do formatu JSON

Encodowanie obiektów
--------------------
.. literalinclude:: src/json-encoder-object.py
    :name: listing-json-encoder-object
    :language: python
    :caption: Encoder klas do formatu JSON


Deserializacja i pisanie własnych decoderów
===========================================
.. literalinclude:: src/json-decoder-datetime.py
    :name: listing-json-dumps-datetime
    :language: python
    :caption: Daty w formacie JSON domyślnie nie są parsowane

Class decoder
-------------
.. literalinclude:: src/json-decoder-class.py
    :name: listing-json-decoder-class
    :language: python
    :caption: Decoder dat do formatu JSON

Function decoder
----------------
.. literalinclude:: src/json-decoder-function.py
    :name: listing-json-decoder-function
    :language: python
    :caption: Decoder dat do formatu JSON

Object decoder
--------------
.. literalinclude:: src/json-decoder-object.py
    :name: listing-json-decoder-object
    :language: python
    :caption: Encoder do formatu JSON


Assignments
===========

Serializacja dat
----------------
#. Skopiuj do swojego pliku strukturę danych :numref:`listing-json-encoder-datetime`
#. Zapisz ją do pliku json
#. Wczytaj ją z pliku json jako obiekty Pythona (ten sam efekt co na listingu)

:Założenia:
    * Nazwa pliku: ``json_datetimes.py``
    * Linii kodu do napisania: około 10 linii
    * Maksymalny czas na zadanie: 15 min

:Co zadanie sprawdza:
    * Serializacja danych
    * Korzystanie z biblioteki JSON
    * Serializowanie zagnieżdżonych obiektów

.. literalinclude:: src/json-excercise-datetime.py
    :name: listing-json-excercise-datetime
    :language: python
    :caption: Sample Python data JSON

Serializacja obiektów do JSON
-----------------------------
#. Użyj obiektu ``ksiazka_adresowa`` stworzonego w zadaniu z programowaniem obiektowym
#. Zapisz kontakty z książki adresowej w JSON
#. Jak odtworzyć relacje?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

:Założenia:
    * Nazwa pliku: ``csv_dictwriter.py``
    * Linii kodu do napisania: około 8 linii
    * Maksymalny czas na zadanie: 15 min

:Podpowiedź: ``self.__dict__``
