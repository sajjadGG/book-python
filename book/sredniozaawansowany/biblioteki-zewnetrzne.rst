*********************
Biblioteki zewnętrzne
*********************

Inne
====

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
