BIT = 1
KILOBIT = 1024 * BIT
MEGABIT = 1024 * KILOBIT

BYTE = 8 * BIT
KILOBYTE = 1024 * BYTE
MEGABYTE = 1024 * KILOBYTE

size = 1 * MEGABYTE
ratio = (MEGABYTE - MEGABIT)

print(f'1 MB in bit = {size / BIT} bits')
print(f'1 MB in Mb = {size / MEGABIT} Mb')
print(f'MB - Mb = {ratio / BIT}')
