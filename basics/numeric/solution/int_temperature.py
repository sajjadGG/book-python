OFFSET = 273

moon_day_celsius = 180
moon_day_kelvin = OFFSET + moon_day_celsius
moon_night_kelvin = 93
moon_night_celsius = moon_night_kelvin - OFFSET
mars_avg_celsius = -63
mars_avg_kelvin = OFFSET + mars_avg_celsius
mars_high_celsius = 20
mars_high_kelvin = OFFSET + mars_high_celsius
mars_low_kelvin = 120
mars_low_celsius = mars_low_kelvin - OFFSET

print(f'Moon day: {moon_day_kelvin}K, {moon_day_celsius}°C')        # Moon day: 453K, 180°C
print(f'Moon night: {moon_night_kelvin}K, {moon_night_celsius}°C')  # Moon night: 93K, -180°C
print(f'Mars avg: {mars_avg_kelvin}K, {mars_avg_celsius}°C')        # Mars avg: 210K, -63°C
print(f'Mars high: {mars_high_kelvin}K, {mars_high_celsius}°C')     # Mars high: 293K, 20°C
print(f'Mars low: {mars_low_kelvin}K, {mars_low_celsius}°C')        # Moon low: 120K, -153°C
