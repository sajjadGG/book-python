SECOND = 1
MIN = 60 * SECOND
HOUR = 60 * MIN
DAY = 24 * HOUR

workday = 8 * HOUR
workweek = 5 * workday
workmonth = 22 * workday

print(f'5 min = {5*MIN} sec')
print(f'1 h = {HOUR} sec')
print(f'work day = {workday} sec')
print(f'work month = {workmonth / HOUR} h')
print(f'work week = {workweek / MIN} min')
