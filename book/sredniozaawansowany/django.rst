******
Django
******

Instalacja i uruchamianie
=========================

Instalacja
----------
.. code-block:: console

    $ pip install django

Tworzenie nowego projektu
-------------------------
.. code-block:: console

    $ django-admin startproject botnet

    $ python manage.py migrate

    $ python manage.py createsuperuser
    Username (leave blank to use 'matt'): admin
    Email address: jose.jimenez@nasa.gov
    Password:
    Password (again):
    Superuser created successfully.

    $ python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    June 12, 2018 - 13:37:00
    Django version 2.1.0, using settings 'botnet.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

    $ cd botnet

    $ django-admin startapp heartbeat

Sprawdź w przeglądarce strony:

* ``http://127.0.0.1:8000/``
* ``http://localhost:8000/admin/``

Co to jest Django?
==================

Architektura aplikacji Django
=============================

Modele
======

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

INSTALLED_APPS.append('import_export')


:admin.py:
    .. code-block:: python

        from import_export.admin import ImportExportModelAdmin

        @admin.register(Command)
        class CommandAdmin(ImportExportModelAdmin):
            pass

``django-grappelli``
--------------------

INSTALLED_APPS.insert(0, 'grappelli')
