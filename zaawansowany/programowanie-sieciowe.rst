**********************
Programowanie sieciowe
**********************

Socket
======

Otwieranie połączeń
-------------------

Protokoły
---------

Nasłuchiwanie
-------------

Przekazywanie informacji
------------------------

Biblioteki sieciowe
===================

``smtp``
--------

Automatyzacja pracy
===================

``fabric``
----------

* http://www.fabfile.org/
* https://pypi.python.org/pypi/Fabric3

Mini Botnet
-----------

Stwórz program, który otworzy socket na porcie na localhoście podanym przez użytkownika z linii poleceń (wykorzystaj ``argparse``) i będzie nasłuchiwał połączeń. Zweryfikuj za pomocą ``telnet`` albo ``netcat`` czy program odpowiada. Następnie napisz w pythonie klienta, który będzie wysyłał polecenia do tamtego programu.

.. figure:: /_img/botnet.png
    :scale: 50%
    :align: center

    Botnet Schemat Architektoniczny

:Uwaga:
    * nigdy nie rób tego na produkcji bez tzw. sanityzacji parametrów, np. lista zaufanych hostów, możliwe polecenia!
    * pliki nazwij:

        * ``victim.py`` - ofiara
        * ``attacker-ping-server.py`` - serwer przyjmujący
        * ``attacker-execute-client.py``

* zrób aby przetwarzanie requestów było nieblokujące, tzn. otwieraj wątek dla każdego zapytania
* program wykona polecenie za pomocą ``eval``, które przyszło z zapytania
* wykonaj polecenie w systemie operacyjnym i zwróć klientowi odpowiedź
* dodaj funkcję aby wyświetlał dowolny plik
* dodaj funkcję aby listował dowolny katalog - wykorzystaj ``os.walk`` oraz ``os.path.join`` do łączenia nazw katalogów
* zmodyfikuj program aby przyjmował zapytania w formacie XML, pole command oraz arguments powinny być osobno
* zmodyfikuj program aby przyjmował zapytania w formacie JSON, pole command oraz arguments powinny być osobno
* stwórz dekorator ``localhost_only``, który będzie sprawdzał IP źródłowe połączenia i jeżeli nie pochodzi z ``127.0.0.1`` odmówi wykonania polecenia
* stwórz dekorator ``log_request``, który weźmie parametry zapytania (IP, polecenie, argumenty) i zapisze je do pliku ``/tmp/botnet.log`` w formacie ``Request from IP:PORT to execute COMMAND ARGUMENTS``

:Podpowiedź:
    * użyj ``os.path.join`` do łączenia sciezki i nazwy pliku
    * ``argparse``
    * ``logging``
    * ``socket``
    * ``socketserver``
    * ``subprocess.run()``
    * ``json.dumps()``, ``json.loads()``
    * ``xml.etree.ElementTree``

:Zadanie z gwiazdką:
    Za pomocą ``Django`` stwórz panel administracyjny dla botnetu:

    * Wyszukiwanie aktywnych hostów
    * `command`

:Polecenia do wykonania:

    .. code-block:: xml

        <execute>
            <command timeout="2">/bin/ls -la /home</command>
            <command>/bin/ls -l /home/ /tmp/</command>
            <command timeout="1">/bin/sleep 2</command>
            <command timeout="2">/bin/echo 'juz wstalem'</command>
        </execute>
