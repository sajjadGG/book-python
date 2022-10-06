class Database:
    _connection = None

    @classmethod
    def connect(cls):
        if not cls._connection:
            print('Establishing connection...')
            cls._connection = ...
        return cls._connection


# Connecting for the first time
# Will establish new connection
first = Database.connect()

# Connecting for the second time
# Will use existing connection to the DB
# The same handle as `first`
second = Database.connect()
