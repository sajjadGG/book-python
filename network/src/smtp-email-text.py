import smtplib
from email.mime.text import MIMEText


USER = 'myusername@gmail.com'
PASS = 'mypassword'
HOST = 'smtp.gmail.com'
PORT = 465

FROM = 'ME@EXAMPLE.COM'
RCPT = ['HE@EXAMPLE.COM', 'SHE@EXAMPLE.COM']

msg = MIMEText('This is my email body.')
msg['Subject'] = 'Hello'
msg['From'] = FROM
msg['To'] = ', '.join(RCPT)

server = smtplib.SMTP_SSL(HOST, PORT)
server.login(USER, PASS)
server.sendmail(FROM, RCPT, msg.as_string())
server.quit()
