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

print(f'EMU operating pressure: {emu / kPa:.2f} kPa, {emu / PSI:.2f} psi')
print(f'Orlan operating pressure: {orlan / kPa:.2f} kPa, {orlan / PSI:.2f} psi')
print(f'O2 partial pressure at sea level: {o2 / kPa:.2f} kPa, {o2 / PSI:.2f} psi')
print(f'International Standard Atmosphere: {ATA / kPa:.2f} hPa, {ATA / PSI:.2f}')
print(f'Death altitude: {death_altitude:.2f} m')
