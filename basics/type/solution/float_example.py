SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE


M = 1
KM = 1000 * M
FT = 0.3048 * M
MI = 1609.344 * M
KPH = KM / HOUR
MPH = MI / HOUR

LITER = 1
FLOZ = 0.02957344 * LITER

plane_altitude = 10_000 * FT
bottle = 20 * FLOZ
speed_limit = 75 * MI/HOUR


print(f'Plane altitude: {plane_altitude/M} m')
# Plane altitude: 3048.0 m

print(f'Bottle volume: {bottle/LITER} l')
# Bottle volume: 0.5914688 l

print(f'Speed limit: {speed_limit/KPH:.1f} km/h')
# Speed limit: 120.7 km/h
