sepal_length = (5.8, 5.1, 5.7, 6.3, 6.4, 4.7, 7.0, 7.6, 4.9, 4.9, 7.1)
sepal_width = (2.7, 3.5, 2.8, 2.9, 3.2, 3.2, 3.2, 3.0, 3.0, 2.5, 3.0)
petal_length = (5.1, 1.4, 4.1, 5.6, 4.5, 1.3, 4.7, 6.6, 1.4, 4.5, 5.9)
petal_width = (1.9, 0.2, 1.3, 1.8, 1.5, 0.2, 1.4, 2.1, 0.2, 1.7, 2.1)
species = ("virginica", "setosa", "versicolor", "virginica", "versicolor", "setosa", "versicolor", "virginica", "setosa", "virginica", "virginica")

avg = sum(sepal_length) / len(sepal_length)
print(avg)

avg = sum(sepal_width) / len(sepal_width)
print(avg)

avg = sum(petal_length) / len(petal_length)
print(avg)

avg = sum(petal_width) / len(petal_width)
print(avg)
