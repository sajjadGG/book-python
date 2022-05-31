from sqlalchemy import create_engine
import pandas as pd

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)


DATABASE = 'sqlite:///space.db'

SQL = """

    SELECT *
    FROM astronauts

"""


engine = create_engine(DATABASE)
df = pd.read_sql(SQL, engine)
print(df)
