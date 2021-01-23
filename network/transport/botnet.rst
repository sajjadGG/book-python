Mini Botnet
***********


Assignments
===========
.. todo:: Convert assignments to literalinclude

Mini Botnet
^^^^^^^^^^^
* Assignment: Mini Botnet
* Complexity: medium
* Lines of code: 45 lines
* Time: 21 min

1. Stwórz mini botnet o architekturze podanej na obrazku. Mini botnet składa się z trzech części:

    a. Heartbeat Receiver - server przyjmujący informacje o ofiarach (czy wciąż żyją i jakie mają backdoory),
    b. Victim - ofiara,
    c. Attacker - atakujący.

.. figure:: img/botnet.png

    Architektura botnet

Hints:
    * Do weryfikacji czy port jest otwarty możesz użyć ``telnet`` albo ``netcat``

Heartbeat Receiver
^^^^^^^^^^^^^^^^^^
* Assignment: Heartbeat Receiver
* Complexity: medium
* Lines of code: 45 lines
* Time: 21 min

English:
    TODO: English Translation

Polish:
    1. Server ma przyjmować komunikaty UDP na porcie 1337
    2. Datę UTC przyjścia pakietu, IP i port backdoora zapisuje do bazy danych ``sqlite3`` jako pola:

        a. ``datetime DATETIME``,
        b. ``host TEXT``,
        c. ``port INTEGER``.

Hints:
    * ``socketserver.UDPServer``

Victim
^^^^^^
* Assignment: Victim
* Complexity: medium
* Lines of code: 150 lines
* Time: 34 min

English:
    TODO: English Translation

Polish:
    1. Po zainfekowaniu otwiera randomowy port TCP (backdoor) z przedziału 1025-65535 na którym nasłuchuje komunikatów
    2. Dlaczego taki zakres portów?
    3. Co 5 sekund wysyła informację ze swoim numerem portu backdoor oraz swoim adresem IP do Heartbeat Receiver
    4. Po otrzymaniu komunikatu XML na port backdoora wykonuje operację w nim zawarte
    5. Ofiara ma przesyłać JSON atakującemu w formacie:

        a. ``date: datetime`` (UTC),
        b. ``host: str``,
        c. ``port: int``,
        d. ``stdout: str``,
        e. ``stderr: str``.

    6. Stwórz dekorator ``is_valid_xml``, który sprawdzi czy XML się waliduje (czy ma poprawną strukturę) i tylko wtedy wykona polecenia
    7. Stwórz dekorator ``log_incoming_requests``, który zapisze do pliku ``botnet.log`` logi w formacie ``Request from IP:PORT to execute COMMAND ARGUMENTS`` dla każdego polecenia wykonywanego na systemie ofiary

Hints:
    * ``random``
    * ``logging``
    * ``socket``
    * ``socketserver.TCPServer``
    * ``subprocess.run()``
    * ``json.dumps()``, ``json.loads()``
    * ``xml.etree.ElementTree``

Attacker
^^^^^^^^
* Assignment: Attacker
* Complexity: medium
* Lines of code: 150 lines
* Time: 34 min

English:
    TODO: English Translation

Polish:
    1. Skopiuj zawartość listingu z sekcji "Given" do pliku ``botnet-commands.xml``
    2. Skrypt można wywoływać z parametrami linii poleceń:

        a. ``--xml FILENAME``, domyślnie ``botnet-commands.xml``, opcjonalny (jeżeli podano inne parametry),
        b. ``--exec COMMAND`` - opcjonalny,
        c. ``--cat FILENAME`` - opcjonalny,
        d. ``--ls PATH`` - opcjonalny,
        e. ``--eval CODE`` - opcjonalny.

    3. Skrypt ma do wszystkich botów (ofiar), które pingnęły serwer heartbeat w ciągu godziny wysyłać (IP ofiary, port backdoor) polecenia do wykonania
    4. Polecenia są:

        a. w pliku XML podanym jako parametr (jeżeli podano flagę ``--xml``),
        b. podane jako parametr do ``--exec``,
        c. wyświetlanie zawartości pliku podanego jako parametr ``--cat``,
        d. listowanie zawartości katalogu podanego jako parametr ``--ls``,
        e. wykonywanie kodu Python i zwracanie wyników, jeżeli podano ``--eval``.

    5. Polecenia do wykonania bez względu na flagę muszą być przesłane za pomocą komunikatów XML
    6. Datę, komunikat XML, oraz listę hostów do których poszło zapytanie zapisuj w bazie ``sqlite3`` w charakterze logów
    7. Wyniki, które przyjdą od ofiar zapisuj w bazie danych ``sqlite3`` wraz z datą otrzymania, adresem IP ofiary, portem (backdoor), stdout i stderr
    8. Do obsługi parametrów z linii poleceń wykorzystaj ``argparse``
    9. Przetwarzanie requestów jest nieblokujące, tzn. otwieraj wątek dla każdego zapytania
    10. Wykorzystaj ``os.path.join`` (łączenie ścieżki) oraz ``os.walk`` (wyświetlanie zawartości).

Given:
    .. literalinclude:: src/botnet-commands.xml
        :language: python
        :caption: Komunikat XML z listą poleceń do wykonania na komputerze ofiary

Hints:
    * ``argparse``
    * ``socket``
    * ``json.dumps()``, ``json.loads()``

:Extra task:
    Za pomocą ``Django`` stwórz panel administracyjny dla botnet:

        * Wyszukiwanie aktywnych hostów
        * ``command``
