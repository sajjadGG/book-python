HTTP Methods
============
* ``GET`` - Read
* ``POST`` - Create
* ``PUT`` - Update/Replace
* ``PATCH`` - Partial Update/Modify
* ``DELETE`` - Delete
* ``HEAD`` - Show Headers
* ``CONNECT`` - Connect
* ``OPTIONS`` - Show HTTP Methods
* ``TRACE`` - Show Trace


GET
---
* ``GET`` - Read
* Retrieve data
* No other effect

Requests using GET should only retrieve data and should have no other effect.


POST
----
* ``POST`` - Create
* Stores information on the server
* Requires whole object
* Assigns a new URI

The POST method requests that the server accept the entity enclosed in the
request as a new subordinate of the web resource identified by the URI.


PUT
---
* ``PUT`` - Update/Replace
* Stores information on the server
* Requires whole object
* Reuse URI

The PUT method requests that the enclosed entity be stored under the
supplied URI.


PATCH
-----
* ``PATCH`` - Partial Update/Modify
* Stores information on the server
* Requires part of object
* Reuse URI

The PATCH method applies partial modifications to a resource.


DELETE
------
* ``DELETE`` - Delete
* Removes information from the server
* Requires URI
* Discards URI

The DELETE method deletes the specified resource.


HEAD
----
* ``HEAD`` - Show Headers
* Identical to ``GET`` request without the response body

The HEAD method asks for a response identical to that of a GET request,
but without the response body.


CONNECT
-------
* ``CONNECT`` - Connect
* Request connection to a transparent TCP/IP tunnel
* Used for SSL-encryption (HTTPS) through an unencrypted HTTP proxy

The CONNECT method converts the request connection to a transparent TCP/IP
tunnel, usually to facilitate SSL-encrypted communication (HTTPS) through
an unencrypted HTTP proxy.


OPTIONS
-------
* ``OPTIONS`` - Show HTTP Methods
* Returns HTTP methods for the specified URL

The OPTIONS method returns HTTP methods that the server supports for
the specified URL.


TRACE
-----
* ``TRACE`` - Show Trace
* Echoes the received request
* Debug what changes have been made by intermediate servers

The TRACE method echoes the received request so that a client can see
what (if any) changes or additions have been made by intermediate servers.



Match Block
-----------
* HTTP Request
* Match Block
* ``'GET /index.html HTTP/2.0'``

>>> request = 'GET /index.html HTTP/2.0'
>>>
>>> match request.split():
...     case ['GET', uri, version]:     handle_get(uri)
...     case ['POST', uri, version]:    handle_post(uri)
...     case ['PUT', uri, version]:     handle_put(uri)
...     case ['DELETE', uri, version]:  handle_delete(uri)
