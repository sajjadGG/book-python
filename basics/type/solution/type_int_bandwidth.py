BIT = 1
KILOBIT = 1024 * BIT
MEGABIT = 1024 * KILOBIT

BYTE = 8 * BIT
KILOBYTE = 1024 * BYTE
MEGABYTE = 1024 * KILOBYTE

file_size = 100 * MEGABYTE
speed = 100 * MEGABIT
time = file_size / speed

print(f'Download time: {time} sec')
