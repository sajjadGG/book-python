import datetime

dt1 = datetime.datetime(1961, 4, 12, 6, 7)
dt2 = datetime.datetime(1969, 7, 21, 14, 56, 15)

duration = dt2 - dt1
# datetime.timedelta(3022, 31755)

print(duration)
# 3022 days, 8:49:15

duration.seconds
# 31755

duration.days
# 3022

duration.total_seconds()
# 261132555.0  # bo duration.days * ilosc sekund na dzien + duration.seconds

YEAR = 365
MONTH = 30
years = duration.days / YEAR
# 8.27945205479452

years, days = divmod(duration.days, YEAR)
months, days = divmod(days, MONTH)
roznica = {
    'years': years,
    'months': months,
    'days': days,
}