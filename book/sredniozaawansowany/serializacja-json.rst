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
.. code-block:: pycon

    >>> DATA = {'first_name': 'Ivan', 'last_name': 'Ivanovic'}

    >>> import json
    >>> json.dumps(DATA)
    '{"first_name": "Ivan", "last_name": "Ivanovic"}'

Problem z rzutowaniem daty na JSON:

.. code-block:: pycon

    >>> import json
    >>> import datetime

    >>> DATA = {'now': datetime.datetime.now()}

    >>> print(DATA)
    {'now': datetime.datetime(1961, 4, 12, 2, 7, 0, 64511)}

    >>> json.JSONEncoder.default = lambda self,obj: ('{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj) if isinstance(obj, datetime.datetime) else None)

    >>> json.dumps(DATA)
    '{"now": "1961-04-12T02:07:00.064511Z"}'

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
.. literalinclude:: src/json-dumps-datetime.py
    :name: listing-json-dumps-datetime
    :language: python
    :caption: Daty w formacie JSON domyślnie nie są parsowane

Dekodowanie daty
----------------
.. literalinclude:: src/json-decoder-datetime.py
    :name: listing-json-decoder-datetime
    :language: python
    :caption: Decoder dat do formatu JSON

Dekodowanie obiektów
--------------------
.. literalinclude:: src/json-encoder-inject.py
    :name: listing-json-encoder-inject
    :language: python
    :caption: Encoder do formatu JSON

Zadania kontrolne
=================

Serializacja obiektów do JSON
-----------------------------
#. Użyj obiektu ``książka_adresowa`` stworzonego w zadaniu z programowaniem obiektowym
#. Zapisz kontakty z książki adresowej w JSON
#. Jak odtworzyć relacje?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

:Podpowiedź: ``self.__dict__``

.. literalinclude:: src/json-loads.py
    :name: listing-json-loads
    :language: python
    :caption: Odczyt danych z formatu JSON