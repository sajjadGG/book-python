******
Django
******

Co to jest Django?
==================

Instalacja i uruchamianie
=========================

Instalacja
----------
.. code-block:: console

    $ pip install django

Starting new project
--------------------
.. code-block:: console

    $ django-admin startproject apollo

    $ python manage.py migrate

    $ python manage.py createsuperuser
    Username (leave blank to use 'admin'): jose.jimenez
    Email address: jose.jimenez@nasa.gov
    Password:
    Password (again):
    Superuser created successfully.

    $ python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    July 21, 1969 - 14:56:15
    Django version 2.1.0, using settings 'apollo.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Sprawdź w przeglądarce strony:

* ``http://127.0.0.1:8000/``
* ``http://localhost:8000/admin/``

Starting new app
----------------
.. code-block:: console

    $ cd apollo

    $ django-admin startapp lem

Architektura aplikacji Django
=============================

Modele
======
- ``CharField``
- ``DateField``
- ``DateTimeField``
- ``DecimalField``
- ``DurationField``
- ``FileField``
- ``ImageField``
- ``IntegerField``
- ``ManyToManyField``
- ``BooleanField``
- ``PositiveIntegerField``
- ``PositiveSmallIntegerField``
- ``SlugField``
- ``TextField``
- ``TimeField``
- ``URLField``


Widoki
======

Panel admina
============

Dokumentacja
============

Widoki generyczne
=================

Localization
============
.. code-block:: console

    $ cd botnet/heartbeat
    $ mkdir locale

    $ django-admin makemessages -l en
    processing locale en

    $ django-admin makemessages -l pl
    processing locale pl

    $ django-admin compilemessages
    processing file django.po in /private/tmp/botnet/botnet/heartbeat/locale/en/LC_MESSAGES
    processing file django.po in /private/tmp/botnet/botnet/heartbeat/locale/pl/LC_MESSAGES

Sygnały
=======

Migracje schematów bazy danych
==============================

.. code-block:: console

    $ python manage.py makemigrations
    Migrations for 'heartbeat':
      botnet/heartbeat/migrations/0001_initial.py
        - Create model Heartbeat

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, heartbeat, sessions
    Running migrations:
      Applying heartbeat.0001_initial... OK

Management Commands
===================

ORM
===

Skrypty z Django
================

Przydatne Biblioteki
====================

``django-import-export``
------------------------
* ``INSTALLED_APPS.append('import_export')``


:admin.py:
    .. code-block:: python

        from import_export.admin import ImportExportModelAdmin

        @admin.register(Command)
        class CommandAdmin(ImportExportModelAdmin):
            pass

``django-grappelli``
--------------------
* ``INSTALLED_APPS.insert(0, 'grappelli')``

``django-rest-framework``
-------------------------

``transifex``
-------------
