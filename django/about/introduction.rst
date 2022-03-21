Introduction to Django
======================


Important
---------
* Why use Django?
* What problems Django solves?
* What is Django?
* Web Framework


Documentation
-------------
* One of the best in Open Source


Versioning
----------
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


Release Notes
-------------
* List of releases: https://docs.djangoproject.com/en/dev/releases/
* 1.11 - https://docs.djangoproject.com/en/dev/releases/1.11/
* 2.0 - https://docs.djangoproject.com/en/dev/releases/2.0/
* 2.1 - https://docs.djangoproject.com/en/dev/releases/2.1/
* 2.2 - https://docs.djangoproject.com/en/dev/releases/2.2/
* 3.1 - https://docs.djangoproject.com/en/dev/releases/3.1/
* 3.2 - https://docs.djangoproject.com/en/dev/releases/3.2/
* 4.0 - https://docs.djangoproject.com/en/dev/releases/4.0/


LTS - Long Time Support
-----------------------
* What is LTS?
* How long support last?

.. figure:: img/django-roadmap.png

Source: https://static.djangoproject.com/img/release-roadmap.688d8d65db0b.png


``setup.cfg``
-------------
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
-----------
* Runserver
* Debugging
* Profiling
* Docker
* Database Explorer
* Mark as Sources Root
* Syntax Autocompletion (Template, Templatetags, Filters)
