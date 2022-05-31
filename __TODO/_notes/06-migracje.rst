


cd <twojkatalog>/08-migracje
alembic init migrations
"W pliku alembic.ini modyfikujemy linię:
sqlalchemy.url = sqlite:///tmp.db"
Zmień nazwę pliku migrations.py na models.py
"W pliku migrations/env.py modyfikujemy linię:

from models import DatabaseModel
target_metadata = DatabaseModel.metadata"
alembic revision --autogenerate -m 'initial migration'
alembic upgrade heads
"../sqlite3-macos tmp.db .schema
lub
../sqlite3-windows tmp.db .schema

Polecenie poprawnie wyświetla schemat"
"W modelu dodaję dwie kolumny

height = Column(Numeric(3,2), nullable=True, default=None)
weight = Column(Numeric(3,2), nullable=True, default=None)"
alembic revision --autogenerate -m 'add height, weight'
alembic upgrade head
"../sqlite3-macos tmp.db .schema
lub
../sqlite3-windows tmp.db .schema

Polecenie poprawnie wyświetla schemat"
alembic downgrade -1
"../sqlite3-macos tmp.db .schema
lub
../sqlite3-windows tmp.db .schema

Polecenie poprawnie wyświetla schemat"
alembic upgrade head
"../sqlite3-macos tmp.db .schema
lub
../sqlite3-windows tmp.db .schema

Polecenie poprawnie wyświetla schemat"
