import ssl
import smtplib


SMTP_HOST = 'localhost'
SMTP_PORT = 465
SMTP_USER = 'myusername'
SMTP_PASS = 'mypassword'


smtp = smtplib.SMTP_SSL(
    host=SMTP_HOST,
    port=SMTP_PORT)

context = ssl.create_default_context()

smtp.starttls(context=context)
# (220, b'2.0.0 Ready to start TLS')
