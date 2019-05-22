""" /etc/proftpd/proftpd.conf
UseIPv6				off
PassivePorts        1024 1048
MasqueradeAddress	[YOUR PUBLIC IP ADDRESS]
"""

from ftplib import FTP


HOSTNAME = 'YOUR PUBLIC IP ADDRESS'
USERNAME = 'upload'
PASSWORD = '12345678'


with FTP(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, timeout=10) as ftp:

    with open('README.txt', mode='wb') as file:
        ftp.retrbinary('RETR README.txt', file.write)

    with open('Untitled.ipynb', mode='rb') as file:
        ftp.storbinary('STOR Untitled.ipynb', file)
