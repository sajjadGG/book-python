**********************
Introduction to Django
**********************

Co to jest Django?
==================
Web Framework

Dokumentacja
============
* jedna z najlepszych dokumentacji

Wersjonowanie
=============
* Semantic Versioning
* Bugfix releases
* alpha - feature freeze
* beta - code freeze
* rc - translation freeze
* 1.0
* 1.1
* ...
* 1.10
* 1.11
* 2.0 (new features)
* 2.1 (maturing features)
* 2.2 (LTS)
* 3.0 (new features)
* 3.1 (maturing features)
* 3.2 (LTS)
* 4.0 (new features)
* ...

LTS - Long Time Support
-----------------------

``setup.cfg``
=============
.. code-block:: ini

    [bdist_wheel]
    universal = 1

    [metadata]
    license_file = LICENSE

    [pycodestyle]
    max-line-length = 300
    exclude = */migrations/*

    [mypy]
    strict_optional = True

    [flake8]
    ignore = F403,F401
    max-line-length = 300
    exclude =
        .git,
        __pycache__,
        docs/source/conf.py,
        old,
        build,
        dist,
        */migrations/*

IDE Support
===========

Runserver
---------

Debugging
---------

Database Explorer
-----------------

Mark as Sources Root
--------------------

Podpowiadanie składni
---------------------
* Template
* templatetags
* filters
