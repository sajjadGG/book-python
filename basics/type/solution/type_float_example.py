SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

M = 1
KM = 1000 * M
MI = 1609.344 * M

KPH = KM / HOUR
MPH = MI / HOUR

speed_limit = 75 * MPH

print(f'Speed limit: {speed_limit/KPH:.1f} km/h')
# Speed limit: 120.7 km/h
