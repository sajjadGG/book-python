Serializacja i deserializacja danych w JSON
===========================================
Format JSON jest podobny do zapisu dict w Python, ale różni się:

- brak przecinka na końcu ostatniego elementu list
- zawsze są stosowane podwójne cudzysłowia
- ``true`` i ``false`` jest pisane małymi literami
- zamiast ``None`` jest ``null``

Zapis danych do formatu JSON
----------------------------
.. literalinclude:: src/json-dumps.py
    :name: listing-json-dumps
    :language: python
    :caption: Zapis danych do formatu JSON

Odczyt danych z formatu JSON
----------------------------
.. literalinclude:: src/json-loads.py
    :name: listing-json-loads
    :language: python
    :caption: Odczyt danych z formatu JSON

Problemy z serializacją i deserializacją
----------------------------------------
* Serializacja i deserializacja dat
* Serializacja i deserializacja obiektów

Serializacja i pisanie własnych encoderów
-----------------------------------------
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
    {'now': datetime.datetime(2017, 4, 15, 20, 5, 18, 64511)}

    >>> json.JSONEncoder.default = lambda self,obj: ('{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj) if isinstance(obj, datetime.datetime) else None)

    >>> json.dumps(DATA)
    '{"now": "2017-04-15T20:05:18.064511Z"}'

.. code-block:: python

    import datetime
    import json

    class DatetimeEncoder(json.JSONEncoder):
        def default(self, obj):
            try:
                return super(DatetimeEncoder, obj).default(obj)
            except TypeError:
                return '{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj)


    json.dumps(data, cls=DatetimeEncoder)

.. code-block:: python

    import json

    class Adress:
        def __init__(self, miasto):
            self.miasto = miasto

        def __str__(self):
            return f'{self.miasto}'


    class Osoba:
        def __init__(self, imie, nazwisko):
            self.imie = imie
            self.nazwisko = nazwisko
            self.adres = [Adress('Bajkonur')]

        def __str__(self):
            return f'{self.imie}'


    class OsobaEncoder(json.JSONEncoder):
        def default(self, obj):
            try:
                return super().default(obj)
            except TypeError:
                print(obj)
                return obj.__dict__




    matt = Osoba(imie='José', nazwisko='...')


    lista = [
        matt,
    ]

    out = json.dumps(lista, cls=OsobaEncoder)


Deserializacja i pisanie własnych decoderów
-------------------------------------------
.. code-block:: python

    >>> DATA = '["2016-10-26T14:41:51.020", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", {"nazwisko": "Ivanovic", "imie": "Ivan"}, [10, 20, 30], [1]]'

    >>> import json
    >>> json.loads(DATA)


.. code-block:: python

    import datetime
    import json

    DATA = '{"survey":{"datetime":"2016-12-27T16:46:02.640Z", "email":"asd@asd.pl"}, "events":[{"datetime":"2016-12-27T16:46:02.640Z", "action":"click"}], "datetime":"2016-12-27T16:46:02.640Z"}'

    class DatetimeDecoder(json.JSONDecoder):
        def __init__(self):
                json.JSONDecoder.__init__(self, object_hook=self.convert_datetime)

        def convert_datetime(slef, args):
            for key, value in args.items():
                if key == 'datetime':
                    args[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
            return args


    out = json.loads(DATA, cls=DatetimeDecoder)
    print(out)

.. code-block:: python

    import datetime
    import json

    DATA = '{"survey":{"datetime":"2016-12-27T16:46:02.640Z", "email":"asd@asd.pl"}, "events":[{"datetime":"2016-12-27T16:46:02.640Z", "action":"click"}], "datetime":"2016-12-27T16:46:02.640Z"}'

    def datetime_decoder(obj):
        for key, value in obj.items():
            if key == 'datetime':
               obj[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
        return obj


    out = json.loads(DATA, object_hook=datetime_decoder)
    print(out)


.. code-block:: python

    import datetime
    import json

    DATA = '{"survey":{"datetime":"2016-12-27T16:46:02.640Z", "email":"asd@asd.pl"}, "events":[{"datetime":"2016-12-27T16:46:02.640Z", "action":"click"}], "datetime":"2016-12-27T16:46:02.640Z"}'

    json.JSONEncoder.default = lambda self,obj: ('{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj) if isinstance(obj, datetime.datetime) else None)


    def _(obj):
        if isinstance(obj, datetime.datetime):
            # return '{:%Y-%m-%dT%H:%M:%S.%fZ}'.format(obj)
            return obj.isoformat()
        else:
            return None



    d = json.dumps(DATA)
    print(d)


.. code-block:: python

    import datetime
    import json

    DATA = '{"survey":{"datetime":"2016-12-27T16:46:02.640Z", "email":"asd@asd.pl"}, "events":[{"datetime":"2016-12-27T16:46:02.640Z", "action":"click"}], "datetime":"2016-12-27T16:46:02.640Z"}'


    def make_datetime(string):
        """
        >>> make_datetime('2013-10-21T13:28:06.419Z')
        datetime.datetime(2013, 10, 21, 13, 28, 6, 419000, tzinfo=datetime.timezone.utc)
        """
        return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%fZ').replace(
            tzinfo=datetime.timezone.utc)


    data = json.loads(DATA)

    for key, value in data.items():
        for element in value:
            element['timestamp'] = make_datetime(element['timestamp'])

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