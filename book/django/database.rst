********
Database
********


Database schema migration
=========================

Makemigrations
--------------
.. code-block:: console

    $ python manage.py makemigrations
    Migrations for 'contact':
      addressbook/contact/migrations/0001_initial.py
        - Create model Contact

Migrate
-------
.. code-block:: console

    $ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, contact, sessions
    Running migrations:
      Applying contact.0001_initial... OK

Management commands
===================

dbshell
-------

dumpdata
--------
dumpdata --format json  --exclude=auth --exclude=contenttypes

loaddata
--------

inspectdb
---------

makemigrations
--------------
- ``--squash``

migrate
-------

Database settings
=================

Sqlite3
-------
.. code-block:: python

    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'HabitatOS.sqlite3'),
        }
    }

Heroku
------
.. code-block:: python

    if os.environ.get('DATABASE_URL'):
        import dj_database_url
        DATABASES['default'] = dj_database_url.config()

Fixtures
========
fixtures directory of every installed application

Multiple DB and db routing
==========================
