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

Zadania kontrolne
=================

Mini Botnet
-----------

Stwórz program, który otworzy socket na porcie na localhoście podanym przez użytkownika z linii poleceń (wykorzystaj ``argparse``) i będzie nasłuchiwał połączeń. Zweryfikuj za pomocą ``telnet`` albo ``netcat`` czy program odpowiada. Następnie napisz w pythonie klienta, który będzie wysyłał polecenia do tamtego programu.

* port na którym nasłuchuje maszyna ofiary powinien być losowo wybierany (od 1025-65535 [dlaczego taki zakres?]) i przesyłany w komunikacie *ping*.
* przychodzące pingi, ich data, host i port źródłowy zapisać w bazie ``sqlite3`` na hoście attackera
* przetwarzanie requestów jest nieblokujące, tzn. otwieraj wątek dla każdego zapytania
* wykonaj polecenie za pomocą ``eval`` w systemie operacyjnym i zwróć klientowi odpowiedź
* dodaj funkcję aby wyświetlał dowolny plik, którego nazwa przyjdzie od atakującego
* dodaj funkcję aby listował dowolny katalog - wykorzystaj ``os.walk`` oraz ``os.path.join`` do łączenia nazw katalogów
* dodaj opcję aby victim przyjmował zapytania w formacie XML, pole command oraz arguments powinny być osobno
* zmodyfikuj program aby zwracał atakującemu wyniki wykonanych poleceń na komputerze ofiary w formacie JSON
* nazwy poleceń, datę ich uruchomienia i ich wyniki zapisuj lokalnie do bazy ``sqlite3`` na komputerze ofiary (w charakterze logów)
* stwórz dekorator ``localhost_only``, który będzie sprawdzał IP źródłowe połączenia i jeżeli nie pochodzi z ``127.0.0.1`` odmówi wykonania polecenia
* stwórz dekorator ``log_request``, który weźmie parametry zapytania (IP, polecenie, argumenty) i zapisze je do pliku ``/tmp/botnet.log`` w formacie ``Request from IP:PORT to execute COMMAND ARGUMENTS``

.. figure:: img/botnet.png
    :scale: 75%
    :align: center

    Architektura programów botnet

:Pliki nazwij:

    * ``victim.py`` - ofiara
    * ``attacker-ping-server.py`` - serwer przyjmujący
    * ``attacker-execute-client.py``

:Uwaga:
    * nigdy nie rób tego na produkcji bez tzw. sanityzacji parametrów, np. lista zaufanych hostów, możliwe polecenia!

:Podpowiedź:
    * użyj ``os.path.join`` do łączenia sciezki i nazwy pliku
    * ``random``
    * ``argparse``
    * ``logging``
    * ``socket``
    * ``socketserver.UDPServer``, ``socketserver.TCPServer``
    * ``subprocess.run()``
    * ``json.dumps()``, ``json.loads()``
    * ``xml.etree.ElementTree``
    * ``sqlite3``

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
