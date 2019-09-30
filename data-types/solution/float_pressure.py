Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
ATA = 1013.25 * hPa
PSI = 6894.757 * Pa

emu = 4.3 * PSI
orlan = 400 * hPa
o2 = 20.946/100 * ATA

pressure_gradient = -11.3 * Pa
death_altitude = (o2 - ATA) / pressure_gradient

print(f'EMU operating pressure: {emu / kPa} kPa, {emu / PSI} psi')
print(f'Orlan operating pressure: {orlan / kPa} kPa, {orlan / PSI} psi')
print(f'O2 partial pressure at sea level: {o2 / kPa} kPa, {o2 / PSI} psi')
print(f'International Standard Atmosphere: {ATA / hPa} hPa, {ATA / PSI}')
print(f'Death altitude: {death_altitude}m')
