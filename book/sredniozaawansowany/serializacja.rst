*****************************
Serializacja i deserializacja
*****************************

.. _Serializacja i deserializacja danych w CSV:

Serializacja i deserializacja danych w CSV
==========================================

Odczytywanie danych z plików CSV
--------------------------------
.. literalinclude:: src/csv-read.py
    :name: listing-csv-read
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictReader()``

Zapis do plików CSV
-------------------
.. literalinclude:: src/csv-write.py
    :name: listing-csv-write
    :language: python
    :caption: Zapis do plików csv używając ``csv.DictWriter()``

Parsowanie innych plików za pomocą ``csv.DictReader()``
-------------------------------------------------------
.. literalinclude:: src/csv-passwd.py
    :name: listing-csv-passwd
    :language: python
    :caption: Parsing ``/etc/passwd`` file with ``csv.DictReader()``


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


xml
===

.. code-block:: xml

    <execute>
        <command timeout="2">/bin/ls -la /etc/</command>
        <command>/bin/ls -l /home/ /tmp/</command>
        <command timeout="1">/bin/sleep 2</command>
        <command timeout="2">/bin/echo 'juz wstalem'</command>
    </execute>

.. code-block:: python

    import logging
    import xml.etree.ElementTree
    import subprocess

    FILENAME = 'xml-execute-commands.xml'
    LOG_FORMAT = '[%(levelname)-5s] %(filename)s:%(lineno)s - %(msg).110s'


    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    log = logging.getLogger('code-execution')
    root = xml.etree.ElementTree.parse(FILENAME).getroot()


    def run(command, timeout=1):
        log.info('Executing command: %s' % command)

        with subprocess.Popen(command, stdout=subprocess.PIPE) as proc:

            try:
                output, errors = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                log.error('Timeout %s exceeded for command: %s' % (timeout, command))
                return proc.kill()

            if errors:
                log.error(errors)

            if output:
                # red = '\033[00;31m'
                # green = '\033[00;32m'
                # blue = '\033[00;36m'
                # white = '\033[00;39m'
                message = output.decode()

                log.debug('Output: {message}'.format(**locals()))
                return message


    for command in root.findall('./command'):
        cmd = command.text.split()
        timeout = float(command.get('timeout', 1))
        run(cmd, timeout)



xslt
====

.. code-block:: python

    import io
    from lxml import etree


    XSLT = '''
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/">
        <foo><xsl:value-of select="/a/b/text()" /></foo>
        </xsl:template>
    </xsl:stylesheet>
    '''

    xslt_root = etree.XML(XSLT)
    transform = etree.XSLT(xslt_root)

    f = io.StringIO('<a><b>Text</b></a>')
    doc = etree.parse(f)
    result_tree = transform(doc)

    print(result_tree)



Zadania kontrolne
=================

Wczytywanie pliku ``csv``
-------------------------
* https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv
#. ściągnij plik z URL podanego powyżej i zapisz na dysku w miejscu gdzie masz skrypty
#. Wczytaj dane z pliku ``csv``
#. Pierwsza linijka stanowi header

Serializacja ``csv``
--------------------
* Za pomocą ``csv.DictWriter()`` zapisz do pliku dane o zmiennej strukturze.
* ``fieldnames`` nie może być zahardkodowane w skrypcie.

.. code-block:: python

    DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Max', 'last_name': 'Peck'},
        {'first_name': 'Ivan'},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
        {'first_name': 'Jose', 'born': 1961, 'first_step': 1969},
    ]

:Podpowiedź:
    * Kod powinien mieć około 5 linii
    * To jest bardzo często występujący i użyteczny przykład

:Co zadanie sprawdza?:
    * Umiejętność korzystania z modułu ``csv``
    * Umiejętność iteracji po złożonych strukturach danych
    * Dynamiczne generowanie struktur danych na podstawie innych

Serializacja obiektów do Pickle
-------------------------------
#. Użyj obiektu ``książka_adresowa`` stworzonego w zadaniu z serializacją
#. Za pomocą ``pickle`` zapisz kontakty z książki adresowej w pliku
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

Serializacja obiektów do JSON
-----------------------------
#. Użyj obiektu ``książka_adresowa`` stworzonego w zadaniu z serializacją
#. Zapisz kontakty z książki adresowej w JSON
#. Jak odtworzyć relacje?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

:Podpowiedź: ``self.__dict__``

Serializacja obiektów do CSV
----------------------------
#. Użyj obiektu ``książka_adresowa`` stworzonego w zadaniu z serializacją
#. Za pomocą ``csv.DictWriter()`` zapisz kontakty z książki adresowej w pliku
#. Wszystkie pola muszą być zawsze w cudzysłowiach i oddzielone średnikami, kodowanie UTF-8.
#. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku

:Podpowiedź:
    - powtarzanie rekordów (user pozostaje ten sam) z innymi danymi adresowymi
    - dodawanie kolumn (ulica_1, miasto_1, panstwo_1, ulica_2, miasto_2, panstwo_2) i automatyczne generowanie fieldnames
    - wrzucenie danych jako string do jednego pola adres_1, adres_2, adres_3 i ustalenie separatora (np: średnik - ';')
    - jedno pole adres (w ramach niego wszystkie adresy rozdzielone ";" a dane przecinkami ",")
