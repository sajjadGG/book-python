import smtplib
from email.mime.multipart import MIMEMultipart


SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = 'myusername@gmail.com'
SMTP_PASS = 'mypassword'

EMAIL_FROM = 'myusername@gmail.com'
EMAIL_TO = ['user1@example.com', 'user2@example.com']
EMAIL_CC = ['user3@example.com']
EMAIL_BCC = ['user4@example.com', 'user5@example.com']
EMAIL_SUBJECT = 'My Subject'
EMAIL_BODY = 'My Email Body'


msg = MIMEMultipart('alternative')
msg['Subject'] = EMAIL_SUBJECT
msg['To'] = ', '.join(EMAIL_TO)
msg['Cc'] = ', '.join(EMAIL_CC)
msg['Bcc'] = ', '.join(EMAIL_BCC)
msg.attach(EMAIL_BODY)


server = smtplib.SMTP_SSL(
    host=SMTP_HOST,
    port=SMTP_PORT)

server.login(
    user=SMTP_USER,
    password=SMTP_PASS)

server.sendmail(
    from_addr=EMAIL_FROM,
    to_addrs=EMAIL_CC + EMAIL_BCC + EMAIL_TO,
    msg=msg.as_string())

server.quit()
