********
Database
********

Sygnały
=======

dbshell
dumpdata --format json  --exclude=auth --exclude=contenttypes
loaddata
inspectdb
fixture (fixtures directory of every installed application)
makemigrations
migrate

.. code-block:: python

    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'HabitatOS.sqlite3'),
        }
    }

    if os.environ.get('DATABASE_URL'):
        import dj_database_url
        DATABASES['default'] = dj_database_url.config()


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

Multiple DB and db routing
==========================