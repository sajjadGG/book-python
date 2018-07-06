from sklearn.tree import DecisionTreeClassifier


features = [
    (5.1, 3.5, 1.4, 0.2),  # I. setosa
    (7.0, 3.2, 4.7, 1.4),  # I. versicolor
    (6.3, 3.3, 6.0, 2.5),  # I. virginica
    (4.9, 3.0, 1.4, 0.2),  # I. setosa
    (4.7, 3.2, 1.3, 0.2),  # I. setosa
    (6.4, 3.2, 4.5, 1.5),  # I. versicolor
    (7.1, 3.0, 5.9, 2.1),  # I. virginica
    (6.9, 3.1, 4.9, 1.5),  # I. versicolor
    (5.8, 2.7, 5.1, 1.9),  # I. virginica
]

labels = [
    'I. setosa',
    'I. versicolor',
    'I. virginica',
    'I. setosa',
    'I. setosa',
    'I. versicolor',
    'I. virginica',
    'I. versicolor',
    'I. virginica'
]


model = DecisionTreeClassifier()
model.fit(features, labels)

to_predict = [
    (5.6, 2.3, 4.1, 2.9)
]

output = model.predict(to_predict)
print(output)
# ['I. virginica']
