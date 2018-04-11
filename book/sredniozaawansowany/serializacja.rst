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

Serializacja obiektów do Pickle
-------------------------------
#. Użyj obiektu ``książka_adresowa`` stworzonego w zadaniu z serializacją
#. Za pomocą ``pickle`` zapisz kontakty z książki adresowej w pliku
#. Stwórz obiekty książki adresowej na podstawie danych odczytanych z pliku
