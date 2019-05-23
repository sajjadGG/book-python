import poplib


HOSTNAME = 'localhost'
USERNAME = 'myusername'
PASSWORD = 'mypassword'


server = poplib.POP3_SSL(host=HOSTNAME, timeout=30)
server.user(USERNAME)
server.pass_(PASSWORD)

status, messages, length = server.list()

for message in messages:
    msgid, length = message.split()
    status, content, length = server.retr(int(msgid))
    email = '\r\n'.join(line.decode() for line in content)

    print(email)
    print('-' * 30)
