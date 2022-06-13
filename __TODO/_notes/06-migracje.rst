

.. code-block:: console

    cd <twojkatalog>/08-migracje
    alembic init migrations

W pliku alembic.ini modyfikujemy linię:

.. code-block:: ini

    sqlalchemy.url = sqlite:///tmp.db

Zmień nazwę pliku migrations.py na models.py

W pliku migrations/env.py modyfikujemy linię:

.. code-block:: python

    from models import DatabaseModel

    target_metadata = DatabaseModel.metadata
    alembic revision --autogenerate -m 'initial migration'
    alembic upgrade heads

Polecenie poprawnie wyświetla schemat:

.. code-block:: console

    sqlite3 tmp.db .schema

W modelu dodaję dwie kolumny:

.. code-block:: console

    height = Column(Numeric(3,2), nullable=True, default=None)
    weight = Column(Numeric(3,2), nullable=True, default=None)

.. code-block:: console

    alembic revision --autogenerate -m 'add height, weight'
    alembic upgrade head

Polecenie poprawnie wyświetla schemat:

.. code-block:: console

    sqlite3 tmp.db .schema

.. code-block:: console

    alembic downgrade -1

Polecenie poprawnie wyświetla schemat:

.. code-block:: console

    sqlite3 tmp.db .schema

.. code-block:: console

    alembic upgrade head

Polecenie poprawnie wyświetla schemat:

.. code-block:: console

    sqlite3 tmp.db .schema
