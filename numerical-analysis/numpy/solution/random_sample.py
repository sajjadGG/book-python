import numpy as np

np.random.seed(0)


a = np.array([], int)

while a.size <= 6:
    number = np.random.randint(1, 50)

    if number not in a:
        a = np.append(a, number)

print(a)
