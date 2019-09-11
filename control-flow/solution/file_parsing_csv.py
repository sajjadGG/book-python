FILE = r'../data/iris.csv'
features = []
labels = []


with open(FILE) as file:
    file.readline()

    for line in file:
        line = line.strip().split(',')

        features.append(tuple(line[:4]))
        labels.append(line[4])


print(features)
print(labels)
