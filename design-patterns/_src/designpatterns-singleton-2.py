class DB:
    __connection = None

    @classmethod
    def connect(cls):
        if not cls.__connection:
            print('Establishing connection...')
            cls.__connection = ...
        return cls.__connection


# Connecting for the first time
# Will establish new connection
first = DB.connect()

# Connecting for the second time
# Will use existing connection to the DB
# The same handle as `first`
second = DB.connect()
