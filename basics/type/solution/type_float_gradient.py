m = 1
Pa = 1
hPa = 100 * Pa
ATA = 1013.25 * hPa

o2 = 20.946/100 * ATA
pressure_gradient = 11.3 * Pa / m
death_altitude = (ATA - o2) / pressure_gradient

print(f'Death altitude: {death_altitude:.2f} m')
