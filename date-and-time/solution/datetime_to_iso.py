from datetime import datetime


gagarin = 'April 12, 1961 6:07 local time'  # Asia/Almaty


dt = datetime.strptime(gagarin, '%B %d, %Y %H:%M local time')
format = dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

print(f'{format}')

