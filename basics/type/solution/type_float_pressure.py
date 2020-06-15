Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
PSI = 6894.757 * Pa

emu = 4.3 * PSI
orlan = 400 * hPa

print(f'EMU operating pressure: {emu/kPa:.2f} kPa, {emu/PSI:.2f} psi')
print(f'Orlan operating pressure: {orlan/kPa:.2f} kPa, {orlan/PSI:.2f} psi')

