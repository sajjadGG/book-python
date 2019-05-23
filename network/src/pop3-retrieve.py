import poplib


HOSTNAME = 'localhost'
PORT = poplib.POP3_SSL_PORT
USERNAME = 'myusername'
PASSWORD = 'mypassword'


server = poplib.POP3_SSL(host=HOSTNAME, port=PORT, timeout=30)
server.user(USERNAME)
server.pass_(PASSWORD)

for message in server.list()[1]:
    msgid, length = message.split()
    status, content, length = server.retr(int(msgid))
    content = list(line.decode() for line in content)
    print(content)
