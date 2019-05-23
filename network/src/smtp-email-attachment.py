import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


SMTP_USER = 'myusername@gmail.com'
SMTP_PASS = 'mypassword'
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

FROM = 'myusername@gmail.com'
RCPT = ['he@example.com', 'she@example.com']


msg = MIMEMultipart()
msg['Subject'] = 'I have a picture'
msg['From'] = FROM
msg['To'] = ', '.join(RCPT)

txt = MIMEText('This is the email body.')
msg.attach(txt)


FILE = '/path/to/image/file.png'

with open(FILE, mode='rb') as file:
    img = MIMEImage(file.read())

img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(FILE))
msg.attach(img)


server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
server.login(SMTP_USER, SMTP_PASS)
server.sendmail(FROM, RCPT, msg.as_string())
server.quit()
