class DB:
    connection = None

    def __init__(self):
        pass

    @staticmethod
    def connect():
        if not DB.connection:
            print('Nawiazujemy nowe polaczenie')
            DB.connection = ...

        return DB.connection


# Bedzie sie laczyl do bazy danych
conn = DB().connect()

# uzyje juz istniejacego polaczenia
conn = DB().connect()
