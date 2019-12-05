import numpy as np

# array([ 0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20., 22., 24.,
#        26., 28., 30., 32., 34., 36., 38., 40., 42., 44., 46., 48., 50.,
#        52., 54., 56., 58., 60., 62., 64., 66., 68., 70., 72., 74., 76.,
#        78., 80., 82., 84., 86., 88., 90., 92., 94., 96., 98.])


## Results with ``%%timeit``

np.arange(0, 100, step=2, dtype=float)
# 718 ns ± 6.78 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

np.array(range(0, 100, 2), dtype=float)
# 7.89 µs ± 91.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

np.array([x for x in range(0, 100) if x % 2 == 0], dtype=float)
# 9.42 µs ± 129 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

np.array([float(x) for x in range(0, 100) if x % 2 == 0])
# 12.3 µs ± 108 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

np.array([float(x) for x in range(0, 100, 2)])
# 7.61 µs ± 80.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

np.array([x for x in range(0, 100, 2)], dtype=float)
# 5.73 µs ± 104 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
