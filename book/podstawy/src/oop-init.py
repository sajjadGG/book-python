class Server:
    def __init__(self, host, user, password=None):
        """
        host i user są wymagane
        password jest niewymagany i domyślnie jest None
        """
        self.host = host
        self.user = user
        self.password = password


connection = Server(
    host='localhost',
    user='admin',
    password='admin'
)

connection.__dict__
# {'host': 'localhost', 'user': 'admin', 'password': 'admin'}
