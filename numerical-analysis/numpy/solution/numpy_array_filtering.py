import numpy as np
np.random.seed(0)


INPUT = np.random.randint(0, 1025, dtype=int, size=(50, 50))

selection = [2**x for x in range(0, 11)]
mask = np.isin(INPUT, selection)

OUTPUT = INPUT[mask]
OUTPUT = sorted(OUTPUT)
OUTPUT = np.flip(OUTPUT)

print(OUTPUT)
