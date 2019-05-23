"""
apt install mailutils

# Add following line to file /etc/postfix/master.cf
smtps     inet  n       -       y       -       -       smtpd
"""
import ssl
import smtplib


SMTP_USER = 'myusername'
SMTP_PASS = 'mypassword'
SMTP_HOST = 'localhost'
SMTP_PORT = 465


smtp = smtplib.SMTP_SSL(SMTP_HOST, port=SMTP_PORT)

context = ssl.create_default_context()

smtp.starttls(context=context)
# (220, b'2.0.0 Ready to start TLS')
