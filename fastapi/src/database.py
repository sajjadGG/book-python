from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:////tmp/mydatabase.sqlite3'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Model = declarative_base()
Model.metadata.create_all(engine)


def database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
