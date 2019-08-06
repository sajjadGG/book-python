"""
    * Słońca: 5778 K
    * Księżyca w dzień: -180 °C
    * Księżyca w nocy: 180 °C
    * Wenus: 737 K
    * Mars średnia: −63 °C
    * Mars najwyższa: 20 °C
    * Mars najniższa: 120 K
"""

OFFSET = 273

sun_kelvin = 5778
sun_celsius = OFFSET+ sun_kelvin

moon_day_celsius = 180
moon_day_kelvin = OFFSET + moon_day_celsius

moon_night_celsius = -180
moon_night_kelvin = OFFSET + moon_night_celsius

venus_kelvin = 734
venus_celsius = venus_kelvin - OFFSET

mars_avg_celsius = -63
mars_avg_kelvin = OFFSET + mars_avg_celsius

mars_high_celsius = 20
mars_high_kelvin = OFFSET + mars_high_celsius

mars_low_kelvin = 120
mars_low_celsius = mars_low_kelvin - OFFSET


print(f'Sun: {sun_kelvin}K, {sun_celsius}°C')
# Sun: 5778K, 6051°C

print(f'Moon day: {moon_day_kelvin}K, {moon_day_celsius}°C')
# Moon day: 453K, 180°C

print(f'Moon night: {moon_night_kelvin}K, {moon_night_celsius}°C')
# Moon night: 93K, -180°C

print(f'Venus: {venus_kelvin}K, {venus_celsius}°C')
# Venus: 734K, 461°C

print(f'Mars avg: {mars_avg_kelvin}K, {mars_avg_celsius}°C')
# Mars avg: 210K, -63°C

print(f'Mars high: {mars_high_kelvin}K, {mars_high_celsius}°C')
# Mars high: 293K, 20°C

print(f'Moon low: {mars_low_kelvin}K, {mars_low_celsius}°C')
# Moon low: 120K, -153°C
