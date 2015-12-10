import datetime

year = 2015
month = 12
day = 17
hour = 11
minutes = 20
seconds = 10
milliseconds = 0


datetime.datetime.today()

d = datetime.datetime(year, month, day, hour, minutes, seconds)

d = datetime.datetime(year, month, day)
d = datetime.date(year, month, day)

#print(d.strftime('%A, %B %d, %I:%M %p'))


d3 = datetime.date(2015, 12, 18) - datetime.timedelta(days=3)

print(d3)
print(d)


'17.12.2015'
'17/12/2015'
'17 grudnia 2015'
'17 grudzień 2015'


'12/17/15'
'December 17, 2015'


