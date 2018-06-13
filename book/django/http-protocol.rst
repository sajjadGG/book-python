****
HTTP
****

Narzędzia
=========

Web Inspector
-------------

curl
----

wget
----

DNS
===
- /etc/hosts
- DNS

HTTP Protocol
=============

HTTP and HTTPS
--------------

HTTP/1.1 vs. HTTP/2.0
---------------------

URI vs URL
----------

text protocol
-------------

Methods
-------
['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

GET vs POST
-----------
- przekazywanie parametrów
- ``?zmienna1=wartosc&zmienna2=wartosc``
- przesylanie plikow
- przesylanie tablicy zmiennych

Status Code
-----------
* https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

Header
------
Host

Request
-------
.. code-block:: text

    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9,pl;q=0.8
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: _ga=GA1.2.1711323714.1523218102; csrftoken=CwTmac4VUT7FcyFAEKkIXWCxQurIZVbU
    DNT: 1
    Host: python.astrotech.io
    If-Modified-Since: Wed, 13 Jun 2018 00:15:11 GMT
    If-None-Match: W/"5b20620f-60e2"
    Referer: http://python.astrotech.io/django/django-apps.html
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36

Response
--------
.. code-block:: text

    Connection: keep-alive
    Date: Wed, 13 Jun 2018 07:21:58 GMT
    ETag: "5b20620f-60e2"
    Last-Modified: Wed, 13 Jun 2018 00:15:11 GMT
    Server: nginx/1.10.3 (Ubuntu)
    X-Cname-TryFiles: True
    X-Deity: web01
    X-Served: Nginx

stateless
---------

sessions
--------
- bazy danych
- cache
- pliki
- memory

Cookies
-------
- ustawa o cookies


HTML + JS + CSS
===============
