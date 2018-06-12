**********************
Introduction to Django
**********************

Co to jest Django?
==================

Dokumentacja
============
- jedna z najlepszych dokumentacji

Wersjonowanie
=============

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
