from datetime import datetime
from sqlalchemy import Interval, Time, create_engine, select
from sqlalchemy import Table, Column
from sqlalchemy import String, Integer, Date, DateTime, Enum, Float, Numeric, Boolean
import pandas as pd
from sqlalchemy.orm import declarative_base


pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)



DATABASE = 'sqlite:///space.db'
engine = create_engine(DATABASE)
DatabaseModel = declarative_base()


class Apollo11(DatabaseModel):
    __tablename__ = 'apollo11'
    datetime = Column(DateTime, index=True),
    date = Column(Date),
    time = Column(Time),
    met = Column(Interval),
    category = Column(Enum('CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG')),
    event = Column(String),

query = (
    select(Apollo11.datetime, Apollo11.category, Apollo11.event).
    where(Apollo11.category == 'CRITICAL')
)


with engine.connect() as db:
    df = pd.read_sql(query, engine)
    print(df)
