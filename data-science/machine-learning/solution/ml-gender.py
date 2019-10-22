# import pandas as pd
# from sklearn import tree
#
# data = pd.read_csv(r'ml-gender.csv')
#
# features = data.iloc[:, 1:5]
# labels = data.iloc[:, 0]
#
# model = tree.DecisionTreeClassifier()
# model.fit(features, labels)
#
# to_predict = [
#     [6, 130, 8]
# ]
#
# output = model.predict(to_predict)
# print(output)


from sklearn.tree import DecisionTreeClassifier

features = [
    (6.00, 180, 12),
    (5.92, 190, 11),
    (5.58, 170, 12),
    (5.92, 165, 10),
    (5.00, 100, 6),
    (5.50, 150, 8),
    (5.42, 130, 7),
    (5.75, 150, 9),
]

labels = [
    "male",
    "male",
    "male",
    "male",
    "female",
    "female",
    "female",
    "female",
]

model = DecisionTreeClassifier()
model.fit(features, labels)

to_predict = [
    (6, 130, 8)
]

output = model.predict(to_predict)
print(output)
# ['female']
