import datetime

YEAR = 365
MONTH = 30

input1 = 'April 12, 1961 2:07 local time'
input2 = '07/21/69 2:56:15 AM UTC'

gagarin = datetime.datetime.strptime(input1, '%B %d, %Y %H:%M local time')
# 1961-04-12 02:07:00

armstrong = datetime.datetime.strptime(input2, '%x %X %p %Z')
# 1969-07-21 02:56:15

armstrong = datetime.datetime.strptime(input2, '%m/%d/%y %I:%M:%S %p %Z')
# 1969-07-21 02:56:15

roznica = armstrong - gagarin
# 3022 days, 0:49:15

years, days = divmod(roznica.days, YEAR)
months, days = divmod(days, MONTH)
print(f'Uplynelo: {years}y {months}m {days}d')
# Uplynelo: 8y 3m 12d

delta = datetime.timedelta(seconds=roznica.total_seconds())
# 3022 days, 0:49:15

now = datetime.datetime.now()

future = now + delta
print(future.date())
# 2026-07-20

birthday = datetime.datetime(1970, 1, 1, 0, 0, 0)

ile_czasu = future - birthday
print(ile_czasu)
# 20654 days, 12:03:09.805525


years, days = divmod(data.days, YEAR)
months, days = divmod(days, MONTH)
print(f'Bede mial: {years}y {months}m {days}d')
# Bede mial: 56y 7m 4d