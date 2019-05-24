******
Socket
******


``socket``
==========
.. figure:: img/socket-flow.jpg
    :scale: 50%
    :align: center

    Socket Flow

Protocols
---------
* IPv4 - ``socket.AF_INET``
* IPv6 - ``socket.AF_INET6``
* UDP - ``socket.SOCK_DGRAM``
* TCP - ``socket.SOCK_STREAM``



* Broadcast - ``socket.SO_BROADCAST``

API
---
* The ``bufsize`` argument of 1024 used above is the maximum amount of data to be received at once
* ``accept()``, ``connect()``, ``send()``, and ``recv()`` are blocking
* Blocking calls have to wait on system calls (I/O) to complete before they can return a value

.. csv-table:: API
    :header-rows: 1

    "Method", "Description"
    "``socket()``", ""
    "``bind()``", ""
    "``listen()``", ""
    "``accept()``", ""
    "``connect()``", ""
    "``connect_ex()``", ""
    "``send()``", ""
    "``recv()``", ""
    "``close()``", ""

TCP
---

Server
^^^^^^
.. literalinclude:: src/socket-tcp-server.py
    :language: python
    :caption: ``socket`` TCP Server

Client
^^^^^^
.. literalinclude:: src/socket-tcp-client.py
    :language: python
    :caption: ``socket`` TCP Client

UDP
---

Server
^^^^^^
.. literalinclude:: src/socket-udp-server.py
    :language: python
    :caption: ``socket`` UDP Server

Client
^^^^^^
.. literalinclude:: src/socket-udp-client.py
    :language: python
    :caption: ``socket`` UDP Client

Multicast
---------
.. literalinclude:: src/socket-multicast.py
    :language: python
    :caption: ``socket`` Multicast Client


``socketserver``
================

TCP
---

Server
^^^^^^
.. literalinclude:: src/socketserver-tcp-server.py
    :language: python
    :caption: ``socketserver`` TCP Server

Client
^^^^^^
.. literalinclude:: src/socket-tcp-client.py
    :language: python
    :caption: ``socket`` TCP Client

Asynchronous
------------

Threaded
^^^^^^^^
* ``socketserver.ThreadingTCPServer``
* ``socketserver.ThreadingUDPServer``

.. literalinclude:: src/socketserver-tcp-threaded.py
    :language: python
    :caption: ``socketserver`` TCP Threaded Client

Forking
^^^^^^^
* ``socketserver.ForkingTCPServer``
* ``socketserver.ForkingUDPServer``

.. literalinclude:: src/socketserver-tcp-forking.py
    :language: python
    :caption: ``socketserver`` TCP Forking Client


References
==========
* https://realpython.com/python-sockets/


Assignments
===========

Heartbeat
---------
* Filename: ``socket_heartbeat_client.py`` and ``socket_heartbeat_server.py``
* Lines of code to write: 20 lines
* Estimated time of completion: 20 min

#. Stwórz klienta i serwer Heart Beat
#. Zarówno klient jak i serwer ma być uruchamiany w wątkach
#. Serwer ma przyjmować komunikaty UDP na porcie 1337
#. Komunikacja ma odbywać się za pomocą protokołu JSON
#. Klient ma mieć informację o swoim adresie IP i PORT
#. Klient ma co 5 sekund wysyłać informację do serwera o swoim IP i PORT
#. Wyświetl na ekranie:

    - datę UTC przyjścia pakietu,
    - IP i PORT przesłany przez klienta

:Hints:
    * ``threading.Timer(frequency: int, fn: Callable).start()``
    * ``socketserver.UDPServer``
