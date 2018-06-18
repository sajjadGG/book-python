# Further indentation required as indentation is not distinguishable.
def Server(
    host='localhost', port=1337,
    username='admin', password='admin'):
    return host, port, username, password


# Arguments on first line forbidden when not using vertical alignment.
server = Server(host='localhost', port=1337,
    username='admin', password='admin')
