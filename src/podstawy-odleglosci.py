#!/usr/bin/env python3

meters = float(input('Distance [m]: '))

km = int(meters / 1000)
miles = float(meters / 1608)
nm = float(meters / 1852)

print({
    'kilometers': int,
    'miles': float,
    'nautical miles': float,
    'all': [int, float, float]
})
