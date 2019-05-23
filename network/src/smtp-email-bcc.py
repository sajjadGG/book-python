import smtplib
from email.mime.multipart import MIMEMultipart


SMTP_USER = 'myusername@gmail.com'
SMTP_PASS = 'mypassword'
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

EMAIL_FROM = "myusername@gmail.com"
EMAIL_TO = "someone@gmail.com"
EMAIL_CC = "anotherperson@gmail.com,someone@yahoo.com"
EMAIL_BCC = "bccperson1@gmail.com,bccperson2@yahoo.com"
EMAIL_BODY = 'hello'
EMAIL_SUBJECT = 'my subject'


msg = MIMEMultipart('alternative')
msg['Subject'] = EMAIL_SUBJECT
msg['To'] = EMAIL_TO
msg['Cc'] = EMAIL_CC
msg['Bcc'] = EMAIL_BCC
msg.attach(EMAIL_BODY)


server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
server.login(SMTP_USER, SMTP_PASS)

server.sendmail(
    from_addr=EMAIL_FROM,
    to_addrs=EMAIL_CC.split(',') + EMAIL_BCC.split(',') + [EMAIL_TO],
    msg=msg.as_string())

server.quit()
