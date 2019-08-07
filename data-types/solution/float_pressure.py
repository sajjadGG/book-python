PASCAL = 1
HECTOPASCAL = 100 * PASCAL
KILOPASCAL = 1000 * PASCAL
ATA = 1013.25 * HECTOPASCAL
PSI = 6894.757 * PASCAL

emu = 4.3
orlan = 5.8
o2 = 20.946/100 * ATA
isa = 1 * ATA

emu_kPa = emu*PSI / KILOPASCAL
orlan_kPa = orlan*PSI / KILOPASCAL
o2_psi = o2 / PSI
o2_kPa = o2 / KILOPASCAL
isa_hPa = isa / HECTOPASCAL
isa_psi = isa / PSI


print(f'EMU operating pressure: {round(emu_kPa, 2)} kPa, {emu} psi')
print(f'Orlan operating pressure: {round(orlan_kPa, 2)} kPa, {orlan} psi')
print(f'O2 partial pressure at sea level: {o2_kPa:.2f} kPa, {round(o2_psi, 2)} psi')
print(f'International Standard Atmosphere: {isa_hPa} hPa, {round(isa_psi, 2)}')
