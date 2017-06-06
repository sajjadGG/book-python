******************
Programowanie HTTP
******************

Biblioteki standardowe
======================

``httplib``
-----------

``urllib``
----------


Standard WSGI
=============

Biblioteki zewnętrzne
=====================

``suds``
--------

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


HTML Scrapping i ``BeautifulSoup``
----------------------------------

* ``pip install beautifulsoup4``

.. code-block:: python
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """

.. code-block:: python

    soup.title
    # <title>The Dormouse's story</title>

    soup.title.name
    # u'title'

    soup.title.string
    # u'The Dormouse's story'

    soup.title.parent.name
    # u'head'

    soup.p
    # <p class="title"><b>The Dormouse's story</b></p>

    soup.p['class']
    # u'title'

    soup.a
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    soup.find_all('a')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    soup.find(id="link3")
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


.. code-block:: python

    for link in soup.find_all('a'):
        print(link.get('href'))

    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

.. code-block:: python

    print(soup.get_text())
    # The Dormouse's story
    #
    # The Dormouse's story
    #
    # Once upon a time there were three little sisters; and their names were
    # Elsie,
    # Lacie and
    # Tillie;
    # and they lived at the bottom of a well.
    #
    # ...


Frameworki webowe
=================

Google App Engine
-----------------

``django``
----------

``flask``
---------

.. code-block:: python

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()


``webapp2``
-----------

``tornado``
-----------

Utils
=====

``atlassian-python-api``
------------------------

* https://github.com/AstroTech/atlassian-python-api

.. code-block:: python

    from atlassian import Confluence
    from atlassian import Jira


    jira = Jira(
        url='http://localhost:8080',
        username='admin',
        password='admin')

    confluence = Confluence(
        url='http://localhost:8090',
        username='admin',
        password='admin')


    JQL = 'project = DEMO AND status NOT IN (Closed, Resolved) ORDER BY issuekey'
    data = jira.jql(JQL)

    status = confluence.create_page(
        space='DEMO',
        title='This is the title',
        body=f'This is the body. You can use <strong>HTML tags</strong>!<div>{data}</div>')

    print(status)


Template
========

``Jinja2``
----------

.. code-block:: html

    <title>{% block title %}{% endblock %}</title>
    <ul>
    {% for user in users %}
      <li><a href="{{ user.url }}">{{ user.username }}</a></li>
    {% endfor %}
    </ul>

Przykłady praktyczne
====================

Prosty serwer HTTP
------------------


Zadania kontrolne
=================


REST API
--------

Używając biblioteki standardowej w Pythonie zaciągnij informacje o repozytoriach użytkownika Django na https://github.com

* w przeglądarce internetowej wygeneruj w swoim profilu token https://github.com/settings/tokens

* Następnie z przeglądnij listę z poziomu Pythona i znajdź URL dla repozytorium ``django``.

.. code-block:: python

    "name": "django",
    "full_name": "django/django",

    # wyszukaj "commits_url": ???

* Przeglądnij to repozytorium i jego listę commitów.
* Podaj datę i opis ostatniego commita
* Znajdź numery ID ticketów (``Fixed #...``) z issue trackera, które zostały rozwiązane w ostatnim miesiącu
* Spróbuj skorzystać zamiast biblioteki standardowej z pakietu ``requests``

.. code:: REST

    https://api.github.com/

    GET /orgs/django/repos
    GET /repos/dajngo/django/commits


.. code:: shell

    curl https://api.github.com/orgs/django/repos


.. code-block:: python

    >>> auth = b'username:token'
    >>> headers={
    ...     'Authorization': 'Basic {}'.format(base64.b64encode(auth).decode('ascii')),
    ...     'User-Agent': 'Python HTTP',
    ...}

    # ...

    >>> body = resp.read().decode()
    >>> data = json.loads(body)
