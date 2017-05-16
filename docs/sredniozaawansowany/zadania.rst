*******
Zadania
*******


Parsowanie ``/etc/hosts``
=========================

Z twojego systemu operacyjnego wyciągnij plik ``/etc/hosts`` i przedstaw go w formie listy dictów jak w przykładzie poniżej:

.. code-block:: python

    {'ip': '127.0.0.1', 'hostnames': ['localhost'], 'protocol': 'ipv4'},
    {'ip': '255.255.255.255', 'hostnames': ['broadcasthost'], 'protocol': 'ipv4'},
    {'ip': '::1', 'hostnames': ['localhost'], 'protocol': 'ipv6'},

:Uwaga:
    * Zwróć uwagę na uprawnienia do odczytu pliku
    * System Windows również posiada ten plik (``C:/Windows/System32/drivers/etc/hosts``)
    * Gdyby w Twoim systemie nie było pliku, skorzystaj z szablonu poniżej:

.. code-block:: text

    ##
    # Host Database
    ##
    127.0.0.1	    localhost
    127.0.0.1	    localhost
    10.13.37.1	    facebook.com google.com microsoft.com
    255.255.255.255	broadcasthost
    ::1             localhost

Parsowanie ``/etc/passwd``
==========================
The ``/etc/passwd`` file is a colon-separated file that contains the following information:

- User name
- Encrypted password
- User ID number (UID)
- User's group ID number (GID)
- Full name of the user (GECOS)
- User home directory
- Login shell

Gdyby w Twoim systemie nie było pliku, skorzystaj z szablonu poniżej:

.. code-block:: text

    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
    sync:x:5:0:sync:/sbin:/bin/sync
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
    news:x:9:13:news:/etc/news:
    uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin
    operator:x:11:0:operator:/root:/sbin/nologin
    games:x:12:100:games:/usr/games:/sbin/nologin
    gopher:x:13:30:gopher:/var/gopher:/sbin/nologin
    ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
    nobody:x:99:99:Nobody:/:/sbin/nologin
    nscd:x:28:28:NSCD Daemon:/:/sbin/nologin
    vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin
    ntp:x:38:38::/etc/ntp:/sbin/nologin
    pcap:x:77:77::/var/arpwatch:/sbin/nologin
    dbus:x:81:81:System message bus:/:/sbin/nologin
    avahi:x:70:70:Avahi daemon:/:/sbin/nologin
    rpc:x:32:32:Portmapper RPC user:/:/sbin/nologin
    mailnull:x:47:47::/var/spool/mqueue:/sbin/nologin
    smmsp:x:51:51::/var/spool/mqueue:/sbin/nologin
    apache:x:48:48:Apache:/var/www:/sbin/nologin
    sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
    dovecot:x:97:97:dovecot:/usr/libexec/dovecot:/sbin/nologin
    oprofile:x:16:16:Special user account to be used by OProfile:/home/oprofile:/sbin/nologin
    rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
    nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
    xfs:x:43:43:X Font Server:/etc/X11/fs:/sbin/nologin
    haldaemon:x:68:68:HAL daemon:/:/sbin/nologin
    avahi-autoipd:x:100:156:avahi-autoipd:/var/lib/avahi-autoipd:/sbin/nologin
    gdm:x:42:42::/var/gdm:/sbin/nologin
    sabayon:x:86:86:Sabayon user:/home/sabayon:/sbin/nologin


Książka adresowa
================

:Nazwa skryptu: ``bin/ksiazka-adresowa.py``
:Uruchamianie: ``python bin/ksiazka-adresowa.py``

:Zadanie:
    Napisz książkę adresową, która będzie zapisywała dane do pliku w formacie json.
    Każdy z użytkowników jest reprezentowany przez:

    * imię
    * nazwisko
    * telefon
    * adres

     * ulica
     * miasto
     * kod_pocztowy
     * wojewodztwo
     * panstwo

    Wszystkie dane w książce muszą być reprezentowane przez typy proste.

:Zadanie 2:
    Bardzo często wykorzystywanym typem pliku jest CSV, czyli wartości oddzielone przecinkami. Zamień format pliku na ten typ. Zrób tak, aby dane trafiły do odpowiednich kolumn nawet po przesortowaniu. Użyj ``csv.DictWriter()``. Wszystkie pola muszą być zawsze w cudzysłowiach i oddzielone średnikami.

:Zadanie 3:
    Zmodyfikuj aby można było wpisywać wiele adresów.

:Zadanie 4:
    Zmodyfikuj program aby wykorzystywał klasy do reprezentowania wpisów w książce. Które podejście jest lepsze?

:Zadanie 5:
    Teraz wykorzystaj plik bazy danych sqlite aby trzymać informacje w tabeli. Które podejście jest lepsze?

:Zadanie 6:
    Wykorzystaj Django do stworzenia takiego modelu i wygeneruj panel administracyjny. Trudne?

:Pytanie:
    * Które podejście było najłatwiejsze?
    * W jakim formacie najlepiej przechowywać dane?
    * Które podejście jest najlepsze dla innych programistów, a które dla użytkowników?

Walidacja PESEL
===============

Za pomocą wyrażeń regularnych sprawdź:

* czy pesel jest poprawny
* jaka jest data urodzenia? (podaj obiekt ``datetime.date``
* płeć użytkownika który podał PESEL

:Z gwiazdką:
    * sprawdź walidację numerów PESEL dla osób urodzonych po 2000 roku.
    * sprawdź sumę kontrolną

Zbalansowanie nawiasów
======================

:Nazwa skryptu: ``bin/zbalansowanie-nawiasow.py``
:Uruchamianie: ``python bin/zbalansowanie-nawiasow.py``

:Zadanie 1:
    Napisz kod który sprawdzi zbalansowanie nawiasów, tzn. czy ilość otwieranych nawiasów jest równa ilości nawiasów zamykanych. Zwórć uwagę, że mogą być cztery typy nawiasów:

    * okrągłe: ``(`` i ``)``
    * kwadratowe: ``[`` i ``]``
    * klamrowe ``{`` i ``}``
    * trójkątne ``<`` i ``>``

:Zadanie 2:
    Rozbuduj poniższy zestaw testów i napisz funkcjonalność.

    .. code-block:: python

        >>> dane = "() [] () ([]()[])"
        >>> zbalansowanie_nawiasow(a)
        True
        >>> dane = "( (] ([)]"
        >>> zbalansowanie_nawiasow(a)
        False

:Zadanie 3:
    Spróbuj użyć rekurencji.
