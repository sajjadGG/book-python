import numpy as np
np.random.seed(0)


INPUT = np.random.randint(0, 1025, size=(50, 50))

selection = [2**x for x in range(0, 11)]
mask = np.isin(INPUT, selection)

OUTPUT = sorted(INPUT[mask])
OUTPUT = np.flip(OUTPUT)

print(OUTPUT)
