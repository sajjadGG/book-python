import numpy as np
import matplotlib.pyplot as plt


greyhounds = 500
labradors = 500

# height in centimeters + around 10cm variation
greyhounds_height = 70 + 10 * np.random.randn(greyhounds)
labradors_height = 60 + 10 * np.random.randn(labradors)

plt.hist(
    [greyhounds_height, labradors_height],
    stacked=True,
    color=['red', 'blue']
)

plt.show()
