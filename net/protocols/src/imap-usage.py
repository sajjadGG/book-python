import imaplib


IMAP4_HOST = 'localhost'
IMAP4_PORT = 993
IMAP4_USER = 'myusername'
IMAP4_PASS = 'mypassword'
IMAP4_MAILBOX = 'INBOX'


imap = imaplib.IMAP4_SSL(
    host=IMAP4_HOST,
    port=IMAP4_PORT)

imap.login(
    user=IMAP4_USER,
    password=IMAP4_PASS)

imap.select(
    mailbox=IMAP4_MAILBOX,
    readonly=False)

result = imap.search(None, 'ALL')
messages = result[1][0].split()

for msgid in messages:
    status, data = imap.fetch(msgid, '(RFC822)')
    mail = data[0][1].decode()

    print(mail)
    print('-' * 30)


imap.close()
imap.logout()

# Return-Path: <root@ip-172-31-5-83.eu-central-1.compute.internal>
# X-Original-To: upload@localhost
# Delivered-To: upload@localhost
# Received: by ip-172-31-5-83.eu-central-1.compute.internal (Postfix, from userid 0)
# 	id 2481544BD5; Thu, 23 May 2019 07:36:17 +0000 (UTC)
# Subject: test
# To: <upload@localhost>
# X-Mailer: mail (GNU Mailutils 3.4)
# Message-Id: <20190523073617.2481544BD5@ip-172-31-5-83.eu-central-1.compute.internal>
# Date: Thu, 23 May 2019 07:36:17 +0000 (UTC)
# From: root <root@ip-172-31-5-83.eu-central-1.compute.internal>
#
# hello
# ------------------------------
