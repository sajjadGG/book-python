*********************
Biblioteki zewnętrzne
*********************


Do zastosowań naukowych
=======================

``num.py``
----------

``sci.py``
----------

``pandas``
----------

``pybrain``
-----------


Wspierających programowanie sieciowe
====================================

Standard WSGI
-------------

``requests``
------------

.. code-block:: python

    >>> import requests

    >>> requests.put('http://httpbin.org/put', data = {'key':'value'})
    >>> requests.delete('http://httpbin.org/delete')
    >>> requests.head('http://httpbin.org/get')
    >>> requests.options('http://httpbin.org/get')

.. code-block:: python

    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get('http://httpbin.org/get', params=payload)
    >>> print(r.url)
    http://httpbin.org/get?key2=value2&key1=value1

    >>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    >>> r = requests.get('http://httpbin.org/get', params=payload)
    >>> print(r.url)
    http://httpbin.org/get?key1=value1&key2=value2&key2=value3

.. code-block:: python

    >>> import requests

    >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'private_gists': 419, u'total_private_repos': 77, ...}

.. code-block:: python

    >>> url = 'https://api.github.com/some/endpoint'
    >>> headers = {'user-agent': 'my-app/0.0.1'}

    >>> r = requests.get(url, headers=headers)

.. code-block:: python

    >>> payload = {'key1': 'value1', 'key2': 'value2'}

    >>> r = requests.post("http://httpbin.org/post", data=payload)
    >>> print(r.text)
    {
      ...
      "form": {
        "key2": "value2",
        "key1": "value1"
      },
      ...
    }

.. code-block:: python

    >>> r = requests.head('http://github.com', allow_redirects=True)

    >>> r.url
    'https://github.com/'

    >>> r.history
    [<Response [301]>]

.. code-block:: python

    >>> import json

    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}

    >>> r = requests.post(url, data=json.dumps(payload))

.. code-block:: python

    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}

    >>> r = requests.post(url, json=payload)

* http://docs.python-requests.org/en/master/user/quickstart/#json-response-content
* http://docs.python-requests.org/en/master/dev/contributing/#kenneth-reitz-s-code-style


``suds``
--------

Google App Engine
=================

``django``
----------

``flask``
---------

``webapp2``
-----------

``tornado``
-----------

``atlassian-python-api``
------------------------

``fabric``
----------

``BeautifulSoup``
-----------------

Inne
====

``py2app``
----------

``docopt``
----------

``Jinja2``
----------

``pytz``
--------

``ldap3``
---------

.. code-block:: python

    import datetime
    import time
    from pprint import pprint
    from ldap3 import Server, Connection, SEARCH_SCOPE_WHOLE_SUBTREE


    USER = "myusername"
    PASS = "mypassword"
    BASEDN = "OU=Users,DC=local"
    SERVER = Server("127.0.0.1", port=389)
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


    if __name__ == "__main__":
        print_users_with_expiring_password()
