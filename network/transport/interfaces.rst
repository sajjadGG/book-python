**********
Interfaces
**********


``netifaces``
=============

Installation
------------
.. code-block:: console

    $ pip install netifaces

Basic operations
----------------
.. code-block:: python

    import netifaces

    dir(netifaces)
    # [ 'address_families', 'gateways', 'ifaddresses', 'interfaces', 'version', ...]

Variables
---------
.. code-block:: python

    netifaces.AF_INET
    # 2

    netifaces.AF_INET6
    # 30

    netifaces.AF_UNIX
    # 1

.. code-block:: python

    netifaces.AF_APPLETALK  # 16
    netifaces.AF_CCITT      # 10
    netifaces.AF_CHAOS      # 5
    netifaces.AF_CNT        # 21
    netifaces.AF_COIP       # 20
    netifaces.AF_DATAKIT    # 9
    netifaces.AF_DECnet     # 12
    netifaces.AF_DLI        # 13
    netifaces.AF_ECMA       # 8
    netifaces.AF_HYLINK     # 15
    netifaces.AF_IMPLINK    # 3
    netifaces.AF_INET       # 2
    netifaces.AF_INET6      # 30
    netifaces.AF_IPX        # 23
    netifaces.AF_ISDN       # 28
    netifaces.AF_ISO        # 7
    netifaces.AF_LAT        # 14
    netifaces.AF_LINK       # 18
    netifaces.AF_NATM       # 31
    netifaces.AF_NDRV       # 27
    netifaces.AF_NETBIOS    # 33
    netifaces.AF_NS         # 6
    netifaces.AF_PPP        # 34
    netifaces.AF_PUP        # 4
    netifaces.AF_ROUTE      # 17
    netifaces.AF_SIP        # 24
    netifaces.AF_SNA        # 11
    netifaces.AF_SYSTEM     # 32
    netifaces.AF_UNIX       # 1
    netifaces.AF_UNSPEC     # 0

List network interfaces
-----------------------
.. code-block:: python

    import netifaces

    netifaces.interfaces()
    # ['lo0', 'gif0', 'stf0', 'XHC1', 'XHC20', 'VHC128',
    #  'XHC0', 'en5', 'ap1', 'en0', 'p2p0', 'awdl0',
    #  'en1', 'en2', 'en3', 'en4', 'bridge0',
    #  'utun0', 'utun1', 'utun2']

Addresses of a interface
------------------------
.. code-block:: python

    import netifaces

    netifaces.ifaddresses('en0')
    # {
    #  18: [{'addr': 'f0:18:98:3a:ca:52'}],
    #  30: [{'addr': 'fe80::813:d8b:d837:541b%en0', 'netmask': 'ffff:ffff:ffff:ffff::/64', 'flags': 1024}],
    #   2: [{'addr': '10.0.3.173', 'netmask': '255.255.255.0', 'broadcast': '10.0.3.255'}]
    # }

List Gateways
-------------
.. code-block:: python

    import netifaces

    netifaces.gateways()
    # {
    #   'default': {2: ('10.0.3.1', 'en0')},
    #   2: [('10.0.3.1', 'en0', True)],
    #   30: [
    #       ('fe80::%utun0', 'utun0', False),
    #       ('fe80::%utun1', 'utun1', False),
    #       ('fe80::%utun2', 'utun2', False),
    # ]}

Getting list of IPv4 addresses excluding loopback
-------------------------------------------------
.. code-block:: python

    import netifaces


    EXCLUDE = ['lo0', 'lo']

    for iface in netifaces.interfaces():
        # ['lo0', 'gif0', 'stf0', 'XHC1', 'XHC20', 'VHC128',
        #  'XHC0', 'en5', 'ap1', 'en0', 'p2p0', 'awdl0',
        #  'en1', 'en2', 'en3', 'en4', 'bridge0',
        #  'utun0', 'utun1', 'utun2']

        if iface in EXCLUDE:
            continue

        details = netifaces.ifaddresses(iface)

        if netifaces.AF_INET in details:
            info = details[netifaces.AF_INET]
            print(info)
            # [{'addr': '10.0.3.173', 'netmask': '255.255.255.0', 'broadcast': '10.0.3.255'}]


More examples
-------------
* https://www.programcreek.com/python/example/81895/netifaces.interfaces
