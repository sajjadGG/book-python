*********************
Biblioteki zewnętrzne
*********************

Inne
====

Wykonywanie poleceń równolegle na wielu maszynach
-------------------------------------------------
https://linux.die.net/man/1/pssh

Wizualizacja danych
-------------------
- https://superset.incubator.apache.org/

.. code-block:: console

    # Install superset
    pip install superset

    # Create an admin user (you will be prompted to set username, first and last name before setting a password)
    fabmanager create-admin --app superset

    # Initialize the database
    superset db upgrade

    # Load some data to play with
    superset load_examples

    # Create default roles and permissions
    superset init

    # Start the web server on port 8088, use -p to bind to another port
    superset runserver

    # To start a development web server, use the -d switch
    # superset runserver -d

:superset_config.py:
    .. code-block:: python

        import os

        #---------------------------------------------------------
        # Superset specific config
        #---------------------------------------------------------
        ROW_LIMIT = 5000
        SUPERSET_WORKERS = 4

        SUPERSET_WEBSERVER_PORT = 8088
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Flask App Builder configuration
        #---------------------------------------------------------
        # Your App secret key
        SECRET_KEY = '\2\1secretkey\1\2\e\y\y\h'

        # The SQLAlchemy connection string to your database backend
        # This connection defines the path to the database that stores your
        # superset metadata (slices, connections, tables, dashboards, ...).
        # Note that the connection information to connect to the datasources
        #you want to explore are managed directly in the web UI
        SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_GREEN_URL', None)

        # Flask-WTF flag for CSRF
        WTF_CSRF_ENABLED = True
        # Add endpoints that need to be exempt from CSRF protection
        WTF_CSRF_EXEMPT_LIST = []

        # Set this API key to enable Mapbox visualizations
        MAPBOX_API_KEY = ''


.. code-block:: console

    gunicorn \
        -w 10 \
        -k gevent \
        --timeout 120 \
        -b  0.0.0.0:6666 \
        --limit-request-line 0 \
        --limit-request-field_size 0 \
        --statsd-host localhost:8125 \
        superset:app

HTML Scrapping
--------------
* BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
* Scrapy https://scrapy.org/

Zastosowania sieciowe
---------------------
* Scapy http://www.secdev.org/projects/scapy/

Python Executable
-----------------
* https://py2app.readthedocs.io/
* http://www.py2exe.org/
* http://www.pyinstaller.org/

Allegro Tipboard
----------------
* http://allegro.tech/tipboard/
* https://github.com/allegro/tipboard

Tipboard is a system for creating dashboards, written in JavaScript and Python. Its widgets ('tiles' in Tipboard's terminology) are completely separated from data sources, which provides great flexibility and relatively high degree of possible customizations.

Because of its intended target (displaying various data and statistics in your office), it is optimized for larger screens.

Similar projects: Geckoboard, Dashing.

.. code-block:: console

    $ pip install tipboard
    $ tipboard create_project my_test_dashboard
    $ tipboard runserver


Allegro Ralph
-------------

* http://allegro.tech/ralph/
* https://github.com/allegro/ralph

Ralph is full-featured Asset Management, DCIM and CMDB system for data center and back office.

Features:

- keep track of assets purchases and their life cycle
- generate flexible and accurate cost reports
- integrate with change management process using JIRA integration

It is an Open Source project provided on Apache v2.0 License.

Live demo:

- http://ralph-demo.allegro.tech/
- login: ralph
- password: ralph

``ldap3``
---------

.. code-block:: python

    import datetime
    import time
    from pprint import pprint
    from ldap3 import Server, Connection, SEARCH_SCOPE_WHOLE_SUBTREE


    USER = 'myusername'
    PASS = 'mypassword'
    BASEDN = 'OU=Users,DC=local'
    SERVER = Server('127.0.0.1', port=389)
    ATTRIBUTES = ['mail', 'pwdLastSet']


    def construct_filter(wintimestamp):
        return """(&
           (objectCategory=Person)
           (objectCategory=User)
           (userAccountControl=512)
           (pwdLastSet<={wintimestamp})
           (mail=*)
        )""".format(wintimestamp=wintimestamp)


    def search(filter):
        with Connection(SERVER, user=USER, password=PASS) as c:
            c.search(BASEDN, filter, SEARCH_SCOPE_WHOLE_SUBTREE, attributes=ATTRIBUTES)
            return [record['attributes'] for record in c.response]


    def datetime_to_mstimestamp(date):
        """
        Active Direcotry has different approach to create timestamp than Unix.
        Here's a function to convert the Unix timestamp to the AD one.

        >>> datetime_to_mstimestamp(datetime.datetime(2000, 1, 1, 0, 0))
        125911548000000000
        """
        timestamp = int(time.mktime(date.timetuple()))
        magic_number = 116444736000000000
        return timestamp * 10000000 + magic_number


    def mstimestamp_to_datetime(mstimestamp):
        """
        Active Direcotry has different approach to create timestamp than Unix.
        Here's a function to convert AD timestamp to the Unix one.

        >>> mstimestamp_to_datetime(130567328471235643)
        datetime.datetime(2014, 10, 2, 16, 14, 7, 123563)
        """
        magic_number = 11644473600
        return datetime.datetime.fromtimestamp(mstimestamp / 10000000 - magic_number)


    def month_ago(date):
        """
        >>> month_ago(datetime.datetime(2000, 1, 31, 0, 0))
        datetime.datetime(2000, 1, 1, 0, 0)
        """
        return date - datetime.timedelta(days=30)


    def print_users_with_expiring_password():
        now = datetime.datetime.now()
        expiration_date = month_ago(now)
        wintimestamp = datetime_to_mstimestamp(expiration_date)
        older_than_month_ago = construct_filter(wintimestamp)

        for user in search(older_than_month_ago):
            user['pwdLastSet'] = mstimestamp_to_datetime(int(user['pwdLastSet'][0]))
            pprint(user)


    if __name__ == '__main__':
        print_users_with_expiring_password()
