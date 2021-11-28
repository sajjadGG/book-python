CSV Non-Standard
================


SSHd Config
-----------
* ``/etc/ssh/sshd_config``

.. code-block:: text

    ChrootDirectory none
    ClientAliveCountMax 3
    ClientAliveInterval 0
    Compression delayed
    MaxStartups 10:30:100
    PidFile /var/run/sshd.pid
    X11Forwarding no
    X11UseLocalhost yes

>>> delimiter = ' '
>>> result = [row.split(delimiter) for row in DATA.splitlines()]  # doctest: +SKIP


Config
------
* ``/etc/postgresql/12/main/postgresql.conf``

.. code-block:: text

    listen_addresses = 'localhost'
    port = 5432
    max_connections = 100
    ssl = on
    password_encryption = on
    db_user_namespace = off

>>> delimiter = ' = '
>>> result = [row.split(delimiter) for row in DATA.splitlines()]  # doctest: +SKIP


Properties
----------
* Java properties

.. code-block:: text

    sonar.projectKey=MP
    sonar.projectName=MyProject
    sonar.language=py
    sonar.sourceEncoding=UTF-8
    sonar.verbose=true

>>> delimiter = '='
>>> result = [row.split(delimiter) for row in DATA.splitlines()]  # doctest: +SKIP

.. code-block:: python

    import csv

    FILE = r'_temporary.properties'

    with open(FILE) as file:
        result = csv.DictReader(
            file,
            fieldnames=['property', 'value'],
            delimiter='=',
            lineterminator='\n',
            quoting=csv.QUOTE_NONE)

        for line in result:
            print(line)

    # {'property': 'sonar.projectKey', 'value': 'MP'}
    # {'property': 'sonar.projectName', 'value': 'MyProject'}
    # {'property': 'sonar.language', 'value': 'py'}
    # {'property': 'sonar.sourceEncoding', 'value': 'UTF-8'}
    # {'property': 'sonar.verbose', 'value': 'true'}


Passwd
------
* ``/etc/passwd``

.. code-block:: text

    root:x:0:0:root:/root:/bin/bash
    watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
    lewis:x:1001:1001:José Jiménez:/home/lewis:/bin/bash
    twardowski:x:1002:1002:Jan Twardowski:/home/twardowski:/bin/bash

>>> delimiter = ':'
>>> result = [row.split(delimiter) for row in DATA.splitlines()]  # doctest: +SKIP

.. code-block:: python

    import csv


    FILE = r'_temporary.txt'

    with open(FILE) as file:
        result = csv.DictReader(
            file,
            fieldnames=['username', 'password', 'uid', 'gid', 'fullname', 'home', 'shell'],
            delimiter=':',
            lineterminator='\n',
            quoting=csv.QUOTE_NONE)

        for line in result:
            print(line)

    # {'username': 'root', 'password': 'x', 'uid': '0',...}
    # {'username': 'watney', 'password': 'x', 'uid': '1000',...}
    # {'username': 'lewis', 'password': 'x', 'uid': '1001',...}
    # {'username': 'twardowski', 'password': 'x', 'uid': '1002',...}


Hosts
-----
.. code-block:: text

    ##
    # `/etc/hosts` structure:
    #   - IPv4 or IPv6
    #   - Hostnames
    ##

    127.0.0.1       localhost
    127.0.0.1       astromatt
    10.13.37.1      nasa.gov esa.int roscosmos.ru
    255.255.255.255 broadcasthost
    ::1             localhost


Crontab
-------
* /etc/crontab

.. code-block:: text

    # [Minute] [Hour] [Day_of_the_Month] [Month_of_the_Year] [Day_of_the_Week] [command]
    */5 * * * *          /usr/bin/python3 /home/python/run-5min.py 1>/dev/null
    * * * * *            /usr/bin/python3 /home/python/run-1min.py 1>/dev/null
    00 * * * *           /home/python/run.py 1>/dev/null
    * * * jan,may,aug *  /home/python/run.py
    0 17 * * sun,fri     /home/python/run.py
    0 */4 * * *          /home/python/run.py
    0 4,17 * * sun,mon   /home/python/run.py


Key-Value
---------
* /etc/locate.rc
* ``.env`` from Docker

.. code-block:: text

    TMPDIR="/tmp"
    FCODES="/var/db/locate.database"
    SEARCHPATHS="/"
    PRUNEPATHS="/tmp /var/tmp"

.. code-block:: docker

    DATABASE_ENGINE=postgresql
    DATABASE_SERVER=localhost
    DATABASE_PORT=5432
    DATABASE_NAME=mydatabase
    DATABASE_USERNAME=myusername
    DATABASE_PASSWORD=mypassword

.. code-block:: text

    # temp directory
    TMPDIR="/tmp"

    # the actual database
    #FCODES="/var/db/locate.database"

    # directories to be put in the database
    SEARCHPATHS="/"

    # directories unwanted in output
    #PRUNEPATHS="/tmp /var/tmp"


Sensors
-------
.. code-block:: text

    Name;Long;Lat;ModuleName;ModuleType
    "European Astronaut Centre (EAC) - ESA";50.8524881,7.1315254;;Indoor
    Timestamp;"Timezone : Europe/Berlin";Temperature;Humidity;CO2;Noise;Pressure
    1622498702;"2021/06/01 00:05:02";22.6;46;981;32;1019.1
    1622499004;"2021/06/01 00:10:04";22.6;46;981;31;1019.1
    1622499306;"2021/06/01 00:15:06";22.6;46;968;32;1019.1
    1622499608;"2021/06/01 00:20:08";22.5;46;940;31;1019.1
    1622499912;"2021/06/01 00:25:12";22.5;46;907;32;1019
    1622500214;"2021/06/01 00:30:14";22.5;46;877;31;1019
    1622500517;"2021/06/01 00:35:17";22.4;46;873;32;1019

