from ftplib import FTP


FTP_HOST = 'ftp.us.debian.org'
FTP_USER = 'anonymous'
FTP_PASS = ''


with FTP(host=FTP_HOST, user=FTP_USER, passwd=FTP_PASS, timeout=30) as ftp:
    ftp.cwd('debian')  # change into "debian" directory

    ftp.dir()  # list directory contents
    # drwxr-xr-x    9 ftp      ftp          4096 Nov 06 21:00 debian
    # drwxr-xr-x    9 ftp      ftp          4096 Nov 06 13:57 debian-archive
    # drwxr-sr-x    5 ftp      ftp          4096 Mar 13  2016 debian-backports
    # drwxr-xr-x    2 ftp      ftp          4096 Jun 22  2015 stats

    with open('README', mode='wb') as file:
        ftp.retrbinary('RETR README', file.write)
        # '226 Transfer complete.'
