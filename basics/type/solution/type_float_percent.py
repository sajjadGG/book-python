Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
ATA = 1013.25 * hPa

o2 = 20.946/100 * ATA

print(f'International Standard Atmosphere: {ATA/kPa:.2f} kPa')
print(f'O2 partial pressure at sea level: {o2/kPa:.2f} kPa')
