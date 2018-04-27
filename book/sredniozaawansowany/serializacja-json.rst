**********************************
Serializacja i deserializacja JSON
**********************************


Format JSON jest podobny do zapisu dict w Python, ale różni się:

- brak przecinka na końcu ostatniego elementu list
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
.. code-block:: python

    >>> DATA = {'first_name': 'Ivan', 'last_name': 'Ivanovic'}

    >>> import json
    >>> json.dumps(DATA)
    '{"first_name": "Ivan", "last_name": "Ivanovic"}'

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

Encoder Lambda
---------------
.. literalinclude:: src/json-encoder-lambda.py
    :name: listing-json-encoder-lambda
    :language: python
    :caption: Encoder Lambda

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
    :caption: Encoder kalas do formatu JSON


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

Zadania kontrolne
=================

Serializacja dat
----------------
#. Skopiuj do swojego pliku strukturę danych :numref:`listing-json-encoder-datetime`
#. Zapisz ją do pliku json
#. Wczyraj ją z pliku json jako obiekty Pythonowe (ten sam efekt co na listingu)

:Co zadanie sprawdz:
    * Serializacja danych
    * Korzystanie z biblioteki JSON
    * Serializowanie zagnieżdżonych obiektów

.. literalinclude:: src/json-excercise-datetime.py
    :name: listing-json-excercise-datetime
    :language: python
    :caption: Sample Python data JSON

Serializacja obiektów do JSON
-----------------------------
#. Użyj obiektu ``książka_adresowa`` stworzonego w zadaniu z programowaniem obiektowym
#. Zapisz kontakty z książki adresowej w JSON
#. Jak odtworzyć relacje?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

:Podpowiedź: ``self.__dict__``
