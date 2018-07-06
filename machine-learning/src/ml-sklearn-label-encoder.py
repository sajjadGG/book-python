from sklearn import preprocessing


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

labels_names = [
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

label_encoder = preprocessing.LabelEncoder()
labels = label_encoder.fit_transform(labels_names)
# array([0, 1, 2, 0, 0, 1, 2, 1, 2])

list(label_encoder.classes_)
# ['I. setosa', 'I. versicolor', 'I. virginica']

# 0: I. setosa
# 1: I. versicolor
# 2: I. virginica

list(label_encoder.inverse_transform([2, 2, 1]))
# ['I. virginica', 'I. virginica', 'I. setosa']