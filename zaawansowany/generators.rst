*******************************
Generatory i list comprehension
*******************************

Lazy evaluation
===============

.. code-block:: python

    import datetime

    now = datetime.datetime.now

    print(now())

    for i in range(0, 9999999):
        pow(i, 10)

    print(now())


List comprehension
==================

* wykonywane natychmiast

.. code-block:: python

    [x*x for x in range(0, 30) if x % 2]

Generator expressions
=====================

* lazy evaluation

.. code-block:: python

    (x*x for x in range(0, 30) if x % 2)

List comprehension vs. Generator expressions
============================================

.. code-block:: python

    nieparzyste_list_comp = [x*x for x in range(0, 30) if x % 2]
    print(nieparzyste_list_comp)
    print(nieparzyste_list_comp)

    print('------')

    nieparzyste_generator = (x*x for x in range(0, 30) if x % 2)
    print(list(nieparzyste_generator))
    print(list(nieparzyste_generator))

Operator ``yield``
==================

.. code-block:: python

    osoby_w_klasie = [
        {'username': 'ivan-ivanovic', 'czy_wykladowca': True},
        {'username': 'max-peck', 'czy_wykladowca': False},
        {'username': 'jose-jimenez', 'czy_wykladowca': False},
    ]


    def uczestnicy_kursu_lista():
        uczniowie = []

        for osoba in osoby_w_klasie:
            if not osoba.get('czy_wykladowca'):
                uczen = osoba.get('username')
                uczniowie.append(uczen)

        return uczniowie


    for uczestnik in uczestnicy_kursu_lista():
        print('certyfikat dla', uczestnik)

.. code-block:: python

    osoby_w_klasie = [
        {'username': 'ivan-ivanovic', 'czy_wykladowca': True},
        {'username': 'max-peck', 'czy_wykladowca': False},
        {'username': 'jose-jimenez', 'czy_wykladowca': False},
    ]

    def uczestnicy_kursu_yield():
        for osoba in osoby_w_klasie:
            if not osoba.get('czy_wykladowca'):
                yield osoba.get('username')


    for uczestnik in uczestnicy_kursu_yield():
        print('certyfikat dla', uczestnik)


.. code-block:: python

    osoby_w_klasie = [
        {'username': 'ivan-ivanovic', 'czy_wykladowca': True},
        {'username': 'max-peck', 'czy_wykladowca': False},
        {'username': 'jose-jimenez', 'czy_wykladowca': False},
    ]


    def uczestnicy_kursu(osoby):
        def jest_wykladowca(user):
            if user['czy_wykladowca']:
                return True
            else:
                return False

        for osoba in osoby:
            if not osoba['czy_wykladowca']:
                yield {
                    'wykladowcy': jest_wykladowca,
                    'uczestnicy': [x for x in osoby if not x['czy_wykladowca']],
                    'wszystkie_username': [x['username'] for x in osoby]
                }


    uczestnicy_kursu = [osoba.get('username') for osoba in osoby_w_klasie if not osoba['czy_wykladowca']]
    pprint(uczestnicy_kursu)

Przykłady
=========

Przykładowe inicjalizacje generatorów
-------------------------------------

.. code-block:: python

    a = [x for x in range(0, 30)]
    b = (x for x in range(0, 30))
    c = {x for x in range(0, 30)}
    d = list(x for x in range(0, 30))
    e = tuple(x for x in range(0, 30))
    f = set(x for x in range(0, 30))

    print(x for x in range(0, 30))

Zamiana klucz wartość oraz generowanie ``dict`` i ``set``
---------------------------------------------------------

.. code-block:: python

    >>> osoba = {'username': 'Ivan Ivanovic', 'czy_wykladowca': True}

    >>> out = {wartosc: klucz for klucz, wartosc in osoba.items()}

    >>> print(out)
    {'wykladowca1': 'Ivan Ivanovic', True: 'czy_wykladowca'}

    >>> type(out)
    <class 'dict'>

    >>> out = {wartosc for klucz, wartosc in osoba.items()}

    >>> print(out)
    {'Ivan Ivanovic', True}

    >>> type(out)
    <class 'set'>

Filtrowanie wyników na liście dictów
------------------------------------

.. code-block:: python

    ADDRESS_BOOK = [
        {'imie': 'Ivan',
        'nazwisko': 'Ivanovic',
        'ulica': 'Wochod',
        'miasto': 'Bajkonur',
        'kod_pocztowy': '101503',
        'wojewodztwo': 'Kyzyłordyńskie',
        'panstwo': 'Kazachstan'},

        {'imie': 'José',
        'nazwisko': 'Jiménez',
        'ulica': '2101 E NASA Pkwy',
        'miasto': 'Huston',
        'kod_pocztowy': '77058',
        'wojewodztwo': 'Texas',
        'panstwo': 'USA'},
    ]

    osoby = [{'imie': x['imie'], 'nazwisko': x['nazwisko']} for x in ADDRESS_BOOK]
    print(osoby)


Zaawansowane wykorzystanie `List Comprehension`
-----------------------------------------------

.. code-block:: python

    def parzyste_f1(x):
        if x % 2 == 0:
            return True
        else:
            return False

    def parzyste_f2(x):
        return x % 2 == 0

    parzyste1 = [float(x) for x in range(0, 30) if x % 2 == 0]
    parzyste2 = [float(x) for x in range(0, 30) if parzyste_f1(x)]
    parzyste3 = []

    for x in range(0, 30):
        if x % 2 == 0:
            parzyste3.append(float(x))

    def parzyste_f3():
        parzyste = []

        for x in range(0, 30):
            if x % 2 == 0:
                parzyste.append(float(x))

        return parzyste

    a = range(0, 30)

Zaawansowane wykorzystanie `Generator Expressions`
--------------------------------------------------

.. code-block:: python

    liczby = (x for x in range(0, 30))
    parzyste1 = (x for x in range(0, 30) if x % 2 == 0)

    MAX = 30
    parzyste1 = (x for x in range(0, MAX) if x % 2 == 0)

    p = lambda a: (x for x in range(0, a) if x % 2 == 0)

    def xxx(a):
        return (x for x in range(0, a) if x % 2 == 0)

    p(2)
    xxx(2)

    parzyste2 = (x for x in range(0, a) if x % 2 == 0)

.. code-block:: python

    DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Max', 'last_name': 'Peck'},
        {'first_name': 'Ivan'},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961},
        {'first_name': 'Max', 'last_name': 'Peck', 'born': 1961, 'first_step': 1969},
    ]


    # Wykorzystując listę
    fieldnames = []

    for record in DATA:
        for key in record.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    print('list():', fieldnames)


    # set(), podejście 1
    # Wykorzystując zbiór, który deduplikuje za nas
    fieldnames = set()

    for record in DATA:
        for key in record.keys():
            fieldnames.add(key)

    print('set(), podejście 1:', fieldnames)


    # set(), podejście 2
    # Wykorzystując zbiór, który deduplikuje za nas
    fieldnames = set()

    for key in [record.keys() for record in DATA]:
        fieldnames.update(key)

    print('set(), podejście 2:', fieldnames)


    # set(), podejście 3
    # Wykorzystując zbiór, który deduplikuje za nas
    fieldnames = set()

    for record in DATA:
        fieldnames.update(record.keys())

    print('set(), podejście 3:', fieldnames)


    # set(), podejście 4
    # Wykorzystując zbiór, który deduplikuje za nas
    fieldnames = set()
    fieldnames.update(key for key in record.keys() for record in DATA)
    print('set(), podejście 4:', fieldnames)




Zadania kontrolne
=================

Generatory vs. Przetwarzanie Listy
----------------------------------

Napisz program, który wczyta plik ``/etc/passwd``, a następnie:

* przefiltruje linie, tak aby nie zawierały komentarzy (zaczynające się od ``#``)
* przefiltruje linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
* zwróci listę loginów takich użytkowników

* Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję.
* Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``.

* Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``

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
