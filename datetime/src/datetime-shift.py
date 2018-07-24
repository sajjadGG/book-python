import datetime

dt1 = datetime.datetime(1961, 4, 12, 6, 7)
dt2 = datetime.datetime(1969, 7, 21, 14, 56, 15)

duration = dt2 - dt1            # datetime.timedelta(3022, 31755)
print(duration)                 # 3022 days, 8:49:15
duration.seconds                # 31755
duration.days                   # 3022
duration.total_seconds()        # 261132555.0 (days * seconds per day + seconds)


SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR
MONTH = 30.436875               # Average days a month in solar calendar
YEAR = 365.2425                 # Solar calendar

years = duration.days / YEAR    # 8.27395497511927

years, days = divmod(duration.days, YEAR)
months, days = divmod(days, MONTH)
hours, minutes = divmod(duration.seconds, HOUR)
minutes, seconds = divmod(minutes, MINUTE)

difference = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}

print(difference)
# {'years': 8, 'months': 3, 'days': 8, 'hours': 8, 'minutes': 49, 'seconds': 15}
