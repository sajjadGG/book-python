import numpy as np

np.random.seed(0)


a = np.random.random_sample(6) * 49
print(a.astype(int))
# array([14, 22, 32, 41,  0,  2])


## Alternative
a = np.array([], int)

while a.size <= 6:
    number = np.random.randint(1, 50)
    if number not in a:
        a = np.append(a, number)

print(a)
