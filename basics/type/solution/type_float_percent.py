Pa = 1
hPa = 100 * Pa
ATA = 1013.25 * hPa

o2 = 20.946/100 * ATA

print(f'International Standard Atmosphere: {ATA/hPa:.2f} hPa')
print(f'O2 partial pressure at sea level: {o2/hPa:.2f} hPa')
