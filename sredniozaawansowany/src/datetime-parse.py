import datetime


today = 'Tuesday, December 19, 2017. 05:41 PM'

out = datetime.datetime.strptime(today, '%A, %B %d, %Y. %I:%M %p')
print(out)
# 2017-12-19 17:41:00
