************
Serializacja
************

``pickle``
==========

.. code-block:: python

    >>> PYTHON = [
    ...     Osoba,
    ...     make_datetime(now),
    ...     str(now),
    ...     now.__str__(),
    ...     '%s' % now,
    ...     '{}'.format(now),
    ...     {'imię': 'Mattół', 'nazwisko': 'Harasymczuk'},
    ...     (10, 20, 30),
    ...     (1,)
    ]

    >>> import pickle

    >>> p = pickle.dumps(PYTHON)
    >>> print('Z Python do Pickle:', p)

    >>> pp = pickle.loads(p)
    >>> print('Z Pickle do Python:', pp)

    >>> osoba = pp[0]
    >>> print('Obiekt po konwersji:', osoba.nazwisko)


``json``
========

Serializacja
------------

.. code-block:: python

    >>> import json
    >>> json.loads()

Problem z rzutowaniem daty na JSON:

.. code-block:: python

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


Deserializacja
--------------

.. code-block:: python


    >>> DATA = '["2016-10-26T14:41:51.020", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", "2016-10-26 14:41:51.020673", {"nazwisko": "Harasymczuk", "imi\u0119": "Matt\u00f3ł"}, [10, 20, 30], [1]]'

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


``csv``
=======

.. code-block:: python

    >>> import csv

    >>> with open('filename.csv') as csvfile:
    ...     data = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    ...
    ...     for row in data:
    ...         print(row['first_name'], row['last_name'])


.. code-block:: python

    >>> import csv

    >>> data = [
    ...    {'first_name': 'Baked', 'last_name': 'Beans'},
    ...    {'first_name': 'Lovely', 'last_name': 'Spam'},
    ...    {'first_name': 'Wonderful', 'last_name': 'Spam'}
    ...]

    >>> with open('filename.csv', 'w') as csvfile:
    ...    fieldnames = data[0].keys()
    ...    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    ...    writer.writeheader()
    ...
    ...    for row in data:
    ...        writer.writerow(row)
    ...


xml
===

.. code:: xml

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

