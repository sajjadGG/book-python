from pathlib import Path

AUTH_SECRET_KEY = '8dd0c72c203f1c63bd67d2089b9f3dd069873ef78688cf840c71a2237ec01d1f'
AUTH_ALGORITHM = 'HS256'
AUTH_ACCESS_TOKEN_EXPIRE_MINUTES = 30

BASE_DIR = Path(__file__).parent
DATABASE_URL = f'sqlite:///{BASE_DIR}/mydatabase.db'
DEBUG_SQL = False
