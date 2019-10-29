SECOND = 1
MIN = 60 * SECOND
HOUR = 60 * MIN
DAY = 8 * HOUR

work_day = 8 * HOUR
work_week = 40 * HOUR
work_month = 22 * work_day

print(f'5 min = {5 * MIN} sec')
print(f'1 h = {HOUR} sec')
print(f'8 h = {work_day} sec')
print(f'22 day = {work_month} sec')
print(f'1 week = {work_week} min')
