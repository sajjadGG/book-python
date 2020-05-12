Pa = 1
hPa = 100 * Pa
ATA = 1013.25 * hPa

o2 = 20.946/100 * ATA
pressure_gradient = -11.3 * Pa
death_altitude = (o2 - ATA) / pressure_gradient

print(f'O2 partial pressure at sea level: {o2/hPa:.2f} hPa')
print(f'International Standard Atmosphere: {ATA/hPa:.2f} hPa')
print(f'Death altitude: {death_altitude:.2f} m')
