FILE = r'../data/iris.csv'
X = []
y = []


with open(FILE) as file:
    file.readline()

    for line in file:
        line = line.strip().split(',')
        features = line[:4]
        label = line[4]

        X.append(tuple(features))
        y.append(label)


print(X)
print(y)
