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
    mail = '\r\n'.join(line.decode() for line in content)

    print(mail)
    print('-' * 30)

"""
Return-Path: <root@ip-172-31-5-83.eu-central-1.compute.internal>
X-Original-To: upload@localhost
Delivered-To: upload@localhost
Received: by ip-172-31-5-83.eu-central-1.compute.internal (Postfix, from userid 0)
	id 2481544BD5; Thu, 23 May 2019 07:36:17 +0000 (UTC)
Subject: test
To: <upload@localhost>
X-Mailer: mail (GNU Mailutils 3.4)
Message-Id: <20190523073617.2481544BD5@ip-172-31-5-83.eu-central-1.compute.internal>
Date: Thu, 23 May 2019 07:36:17 +0000 (UTC)
From: root <root@ip-172-31-5-83.eu-central-1.compute.internal>

hello
------------------------------
"""
