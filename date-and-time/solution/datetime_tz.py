from datetime import datetime
from pytz import timezone, utc as UTC


WAW = timezone('Europe/Warsaw')


gagarin = 'April 12, 1961 2:07 local time'  # Asia/Almaty
gagarin = datetime.strptime(gagarin, '%B %d, %Y %H:%M local time').replace(tzinfo=UTC)

print('Gagarin [UTC]', gagarin)
print('Gagarin [WAW]', gagarin.astimezone(WAW))


armstrong = '"07/21/69 2:56:15 AM UTC"'
armstrong = datetime.strptime(armstrong, '"%m/%d/%y %I:%M:%S %p %Z"')
armstrong = UTC.localize(armstrong)

print('Armstrong [UTC]', armstrong)
print('Armstrong [WAW]', armstrong.astimezone(WAW))
