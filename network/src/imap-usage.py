import imaplib


HOSTNAME = 'localhost'
USERNAME = 'myusername'
PASSWORD = 'mypassword'


imap = imaplib.IMAP4_SSL(HOSTNAME)
imap.login(USERNAME, PASSWORD)
imap.select('INBOX')

data = imap.search(None, 'ALL')
messages = data[1][0].split()

for msgid in messages:
    data = imap.fetch(msgid, '(RFC822)')[1]
    email = data[0][1].decode()

    print(email)
    print('-' * 30)


imap.close()
imap.logout()
