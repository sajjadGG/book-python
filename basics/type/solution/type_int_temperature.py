C = -273
K = +273

moon_day_C = 180
moon_day_K = moon_day_C + K

moon_night_K = 93
moon_night_C = moon_night_K + C

mars_avg_C = -63
mars_avg_K = mars_avg_C + K

mars_high_celsius = 20
mars_high_kelvin = mars_high_celsius +K

mars_low_kelvin = 120
mars_low_celsius = mars_low_kelvin +C


print(f'Moon day: {moon_day_K}K, {moon_day_C}°C')        # Moon day: 453K, 180°C
print(f'Moon night: {moon_night_K}K, {moon_night_C}°C')  # Moon night: 93K, -180°C
print(f'Mars avg: {mars_avg_K}K, {mars_avg_C}°C')        # Mars avg: 210K, -63°C
print(f'Mars high: {mars_high_kelvin}K, {mars_high_celsius}°C')     # Mars high: 293K, 20°C
print(f'Mars low: {mars_low_kelvin}K, {mars_low_celsius}°C')        # Moon low: 120K, -153°C
