class Database:
    connection = None

    @classmethod
    def connect(cls):
        if not cls.connection:
            print('Establishing connection...')
            cls.connection = ...
        return cls.connection


# Connecting for the first time
# Will establish new connection
first = Database.connect()

# Connecting for the second time
# Will use existing connection to the DB
# The same handle as `first`
second = Database.connect()
